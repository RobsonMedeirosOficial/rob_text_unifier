import os

# =============================================================================
# CONFIGURAÇÕES GERAIS
# =============================================================================

# Diretório raiz onde o script será executado
pasta_raiz = "."  

# Nome do arquivo de saída que será gerado
arquivo_saida = "Rob_Text_Unifier_Result.txt"

# =============================================================================
# LISTAS DE FILTROS E EXCEÇÕES
# =============================================================================

# 1. Arquivos específicos a ignorar (comparação exata pelo nome + extensão)
arquivos_ignorados = {
    "rob_text_unifier.py",
    "README.md",
}

# 2. Pastas completas a ignorar (o script não entra nelas nem em suas subpastas)
pastas_ignoradas = {
    "__pycache__",
    ".git",
    "node_modules",

}

# 3. Pastas com regra parcial: 
# Ignora arquivos que estão DIRETAMENTE nelas, mas PERMITE entrar nas subpastas.
# Ex: Se "./src" está aqui, ignora "./src/arquivo.py" mas lê "./src/lib/util.py"
ignora_arquivos_das_pastas = {
    ".",      # Ignora arquivos na raiz do projeto
    "rob_text_unifier-web"
    # Adicione outras pastas conforme necessário, ex: "logs", "temp"
}

# 4. EXTENSÕES DE ARQUIVOS A IGNORAR (comparação case-insensitive)
# Adicione as extensões SEM o ponto inicial
extensoes_ignoradas = {
    "log",
    "tmp",
    "temp",
    "bak",
    "swp",
    "pyc",
    # Adicione mais extensões conforme necessário, ex: "md", "txt", "exe"
}

# =============================================================================
# FUNÇÃO AUXILIAR: VERIFICA EXTENSÃO DO ARQUIVO
# =============================================================================

def deve_ignorar_por_extensao(nome_arquivo, extensoes):
    """
    Verifica se a extensão do arquivo está na lista de extensões ignoradas.
    Retorna True se a extensão estiver na lista (deve ignorar).
    Retorna False se a extensão não estiver na lista (pode processar).
    
    Args:
        nome_arquivo: Nome completo do arquivo (ex: "script.py")
        extensoes: Set com extensões a ignorar (ex: {"log", "tmp"})
    """
    # Extrai a extensão do arquivo (tudo depois do último ponto)
    _, extensao = os.path.splitext(nome_arquivo)
    
    # Remove o ponto inicial e converte para minúsculas para comparação
    extensao_limpa = extensao.lstrip(".").lower()
    
    # Verifica se a extensão está na lista de ignorados
    return extensao_limpa in extensoes

# =============================================================================
# FUNÇÃO AUXILIAR: VERIFICA SE ARQUIVO ESTÁ EM PASTA DE REGRA PARCIAL
# =============================================================================

def deve_ignorar_por_pasta_parcial(caminho_relativo, pastas_parciais):
    """
    Verifica se o arquivo está diretamente dentro de uma das pastas listadas.
    Retorna True se o arquivo deve ser ignorado por estar 'solto' na pasta.
    Retorna False se o arquivo estiver em uma subpasta (permitido).
    """
    # Normaliza separadores para garantir comparação correta (Windows/Linux)
    caminho_normalizado = caminho_relativo.replace("\\", "/")
    
    # Remove o './' inicial se existir para facilitar a lógica
    if caminho_normalizado.startswith("./"):
        caminho_normalizado = caminho_normalizado[2:]
    
    # Um arquivo está 'diretamente' na pasta se tiver apenas 1 nível de profundidade
    # Ex: "pasta/arquivo.txt" (1 barra) vs "pasta/sub/arquivo.txt" (2 barras)
    partes = caminho_normalizado.split("/")
    
    if len(partes) == 2:
        # Significa que é pasta/arquivo (sem subpastas no meio)
        nome_pasta = partes[0]
        if nome_pasta in pastas_parciais:
            return True
            
    return False

# =============================================================================
# PROCESSO PRINCIPAL DE GERAÇÃO DO ARQUIVO
# =============================================================================

with open(arquivo_saida, "w", encoding="utf-8") as saida:
    
    # os.walk navega recursivamente por todas as pastas
    # diretorio_raiz: caminho da pasta atual
    # subdirs: lista de subpastas (podemos modificar para pular pastas)
    # arquivos: lista de arquivos na pasta atual
    for diretorio_raiz, subdirs, arquivos in os.walk(pasta_raiz):
        
        # ETAPA 1: Filtragem de Pastas Completas
        # Remove da lista 'subdirs' as pastas que estão em 'pastas_ignoradas'.
        # Isso impede que o os.walk entre nelas (economia de performance).
        subdirs[:] = [d for d in subdirs if d not in pastas_ignoradas]

        # ETAPA 2: Processamento dos Arquivos
        for nome_arquivo in sorted(arquivos):
            
            # 2.1: Verifica se o nome do arquivo está na lista de ignoro exato
            if nome_arquivo in arquivos_ignorados:
                continue

            # 2.2: Verifica se a EXTENSÃO do arquivo está na lista de ignorados
            # Ex: ignora todos os .log, .tmp, .bak independentemente do nome
            if deve_ignorar_por_extensao(nome_arquivo, extensoes_ignoradas):
                continue

            # Constrói os caminhos absoluto e relativo
            caminho_absoluto = os.path.join(diretorio_raiz, nome_arquivo)
            caminho_relativo = os.path.relpath(caminho_absoluto, pasta_raiz)
            
            # Padroniza o caminho relativo começando com "./"
            if not caminho_relativo.startswith("."):
                caminho_relativo = "./" + caminho_relativo

            # 2.3: Verifica a regra de pastas parciais
            # Se retornar True, pula este arquivo mas continua lendo subpastas depois
            if deve_ignorar_por_pasta_parcial(caminho_relativo, ignora_arquivos_das_pastas):
                continue

            # ETAPA 3: Leitura do Conteúdo
            try:
                with open(caminho_absoluto, "r", encoding="utf-8") as f:
                    conteudo = f.read()
            except Exception as e:
                # Caso o arquivo esteja bloqueado, seja binário ou tenha erro de encoding
                conteudo = f"[Erro ao ler o arquivo: {e}]"

            # ETAPA 4: Escrita no Arquivo de Saída
            # Formato: Nome do arquivo, caminho relativo e conteúdo completo
            saida.write(f"{nome_arquivo}\n")
            saida.write(f"caminho: {caminho_relativo}\n")
            saida.write(f"\n{conteudo}\n\n")

print(f"Arquivo consolidado gerado: '{arquivo_saida}'")
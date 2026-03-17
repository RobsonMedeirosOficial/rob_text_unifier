import os

# =============================================================================
# CONFIGURAÇÕES GERAIS
# =============================================================================

pasta_raiz = r"."  
arquivo_saida = "Rob_Text_Unifier_Result.txt"

# =============================================================================
# VALIDAÇÃO INICIAL
# =============================================================================

if not os.path.exists(pasta_raiz):
    print(f"❌ ERRO: O caminho não existe: {pasta_raiz}")
    exit(1)

if not os.path.isdir(pasta_raiz):
    print(f"❌ ERRO: O caminho não é uma pasta: {pasta_raiz}")
    exit(1)

print(f"🔍 Processando: {pasta_raiz}")

# =============================================================================
# LISTAS DE FILTROS E EXCEÇÕES
# =============================================================================

arquivos_ignorados = {
    "Rob_Text_Unifier_Result.txt",
    "rob_text_unifier.py",
    "README.md",
}

pastas_ignoradas = {
    "__pycache__",
    ".git",
    "node_modules",
    "Textos",
}

ignora_arquivos_das_pastas = {
    ".",      # Ignora arquivos na raiz do projeto
}

extensoes_ignoradas = {
    "log", "tmp", "temp", "bak", "swp", "pyc",
}

# =============================================================================
# FUNÇÃO AUXILIAR: LÊ ARQUIVO COM FALLBACK DE ENCODING
# =============================================================================

def ler_arquivo_com_fallback(caminho_absoluto):
    encodings = ['utf-8', 'utf-8-sig', 'latin-1', 'cp1252', 'iso-8859-1']
    
    for encoding in encodings:
        try:
            with open(caminho_absoluto, "r", encoding=encoding) as f:
                return f.read()
        except UnicodeDecodeError:
            continue
        except Exception as e:
            return f"[Erro ao ler ({encoding}): {e}]"
    
    try:
        with open(caminho_absoluto, "r", encoding='utf-8', errors='replace') as f:
            return f.read()
    except Exception as e:
        return f"[Erro crítico: {e}]"

# =============================================================================
# FUNÇÃO AUXILIAR: VERIFICA EXTENSÃO (CASE-INSENSITIVE)
# =============================================================================

def deve_ignorar_por_extensao(nome_arquivo, extensoes):
    _, extensao = os.path.splitext(nome_arquivo)
    extensao_limpa = extensao.lstrip(".").lower()
    extensoes_lower = {ext.lower() for ext in extensoes}
    return extensao_limpa in extensoes_lower

# =============================================================================
# FUNÇÃO AUXILIAR: VERIFICA REGRA PARCIAL DE PASTAS
# =============================================================================

def deve_ignorar_por_pasta_parcial(caminho_relativo, pastas_parciais):
    caminho_normalizado = caminho_relativo.replace("\\", "/")
    
    if caminho_normalizado.startswith("./"):
        caminho_normalizado = caminho_normalizado[2:]
    
    partes = caminho_normalizado.split("/")
    
    if len(partes) == 1:
        if "." in pastas_parciais:
            return True
    elif len(partes) == 2:
        nome_pasta = partes[0]
        if nome_pasta in pastas_parciais:
            return True
    
    return False

# =============================================================================
# FUNÇÃO AUXILIAR: FORMATA SEÇÃO COM SEPARADORES VISUAIS
# =============================================================================

def formatar_secao(numero, nome_arquivo, caminho_relativo):
    """
    Formata o cabeçalho de cada arquivo com separadores visuais para facilitar busca humana.
    
    Exemplo de saída:
    # ==================================================================
    SECTION: 1
    ------------
    Arquivo.txt
    caminho: ./Arquivo.txt
    # ==================================================================
    """
    separador = "=" * 66
    sub_separador = "-" * 12
    
    # Padroniza caminho com barras normais para melhor leitura
    caminho_limpo = caminho_relativo.replace("\\", "/")
    
    return f"""# {separador}
SECTION: {numero}
{sub_separador}
{nome_arquivo}
caminho: {caminho_limpo}
# {separador}
"""

# =============================================================================
# PROCESSO PRINCIPAL
# =============================================================================

with open(arquivo_saida, "w", encoding="utf-8") as saida:
    
    # Cabeçalho inicial do arquivo consolidado
    saida.write(f"""# {'='*66}
# ROB_TEXT_UNIFIER - ARQUIVO CONSOLIDADO
# {'='*66}
# Pasta origem: {pasta_raiz}
# Gerado automaticamente - Não edite manualmente
# {'='*66}

""")
    
    contador_arquivos = 0
    contador_ignorados = 0
    numero_secao = 1  # Contador para as seções numeradas
    
    for diretorio_raiz, subdirs, arquivos in os.walk(pasta_raiz):
        
        subdirs[:] = [d for d in subdirs if d not in pastas_ignoradas]

        for nome_arquivo in sorted(arquivos):
            
            if nome_arquivo in arquivos_ignorados:
                contador_ignorados += 1
                continue

            if deve_ignorar_por_extensao(nome_arquivo, extensoes_ignoradas):
                contador_ignorados += 1
                continue

            caminho_absoluto = os.path.join(diretorio_raiz, nome_arquivo)
            caminho_relativo = os.path.relpath(caminho_absoluto, pasta_raiz)
            
            if not caminho_relativo.startswith("."):
                caminho_relativo = "./" + caminho_relativo

            if deve_ignorar_por_pasta_parcial(caminho_relativo, ignora_arquivos_das_pastas):
                contador_ignorados += 1
                continue

            conteudo = ler_arquivo_com_fallback(caminho_absoluto)
            contador_arquivos += 1

            # ✅ Escreve a seção formatada com número e separadores
            saida.write(formatar_secao(numero_secao, nome_arquivo, caminho_relativo))
            saida.write(f"\n{conteudo}\n\n")
            
            numero_secao += 1  # Incrementa para o próximo arquivo

print(f"\n✅ Arquivo consolidado gerado: '{arquivo_saida}'")
print(f"📊 Estatísticas:")
print(f"   • Arquivos processados: {contador_arquivos}")
print(f"   • Arquivos ignorados: {contador_ignorados}")
print(f"\n💡 Dica: Use Ctrl+F no editor para buscar por 'SECTION: X' ou pelo nome do arquivo!")
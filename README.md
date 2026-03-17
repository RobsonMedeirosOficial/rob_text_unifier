# 🤖 rob_text_unifier

[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**Junte todos os arquivos do seu projeto em um único arquivo de texto para compartilhar contexto com IAs.**

---

## 🎯 Objetivo

Este script foi criado para **facilitar o compartilhamento de contexto de projetos com IAs** (ChatGPT, Claude, GitHub Copilot, etc.). 

Em vez de copiar e colar arquivos individualmente, o `rob_text_unifier` consolida todo o código-fonte em um único arquivo `.txt`, mantendo a estrutura de pastas e nomes de arquivos. Isso permite que a IA tenha uma visão completa do seu projeto para:

- ✅ Analisar a arquitetura do código
- ✅ Sugerir melhorias e refatorações
- ✅ Debugar problemas com contexto completo
- ✅ Documentar o projeto automaticamente
- ✅ Migrar ou reescrever código com entendimento total

---

## 🚀 Funcionalidades

| Funcionalidade | Descrição |
|----------------|-----------|
| 🔍 **Filtro por Nome** | Ignore arquivos específicos pelo nome exato (ex: `package-lock.json`) |
| 📁 **Filtro por Pasta** | Pule pastas completas (ex: `node_modules`, `.git`, `__pycache__`) |
| 📄 **Filtro por Extensão** | Ignore todas as arquivos de uma extensão (ex: `.log`, `.tmp`, `.bak`) |
| 🎯 **Regra Parcial** | Ignore arquivos soltos em uma pasta, mas leia suas subpastas |
| 📊 **Caminhos Relativos** | Mantém a estrutura de pastas no arquivo de saída |
| 🛡️ **Tratamento de Erros** | Continua mesmo se algum arquivo não puder ser lido |

---

## 📦 Instalação

Não requer instalação de dependências externas! Apenas Python 3.6+.

```bash
# Clone o repositório
git clone https://github.com/RobsonMedeirosOficial/rob_text_unifier.git

# Entre na pasta
cd rob_text_unifier

# Execute o script
python rob_text_unifier.py

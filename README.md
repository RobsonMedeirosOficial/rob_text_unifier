# 🤖 rob_text_unifier

[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Stable-green.svg)]()

> **Consolide todo o código do seu projeto em um único arquivo de texto, com seções numeradas e formatação amigável para humanos e IAs.**

---

## 📋 Índice

- [🎯 Objetivo](#-objetivo)
- [🚀 Funcionalidades](#-funcionalidades)
- [📦 Instalação](#-instalação)
- [⚙️ Configuração](#️-configuração)
- [📤 Formato da Saída](#-formato-da-saída)
- [💡 Casos de Uso](#-casos-de-uso)
- [🔍 Dicas de Busca](#-dicas-de-busca)
- [🧪 Exemplo com IA](#-exemplo-com-ia)
- [🔒 Segurança](#-segurança)
- [🛠️ Troubleshooting](#️-troubleshooting)
- [📁 Estrutura do Projeto](#-estrutura-do-projeto)
- [🤝 Contribuindo](#-contribuindo)
- [📄 Licença](#-licença)

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
| 📄 **Filtro por Extensão** | Ignore arquivos por extensão, com comparação **case-insensitive** (`.LOG`, `.log`, `.Log`) |
| 🎯 **Regra Parcial** | Ignore arquivos soltos em uma pasta, mas continue lendo suas subpastas |
| 🔣 **Encoding Inteligente** | Lê arquivos com múltiplos encodings (UTF-8, Latin-1, CP1252) automaticamente |
| 📑 **Seções Numeradas** | Cada arquivo no output ganha um cabeçalho visual com `SECTION: X` para fácil busca |
| 📊 **Estatísticas em Tempo Real** | Veja quantos arquivos foram processados e ignorados ao final da execução |
| 🛡️ **Validação de Caminho** | Verifica se o diretório existe antes de iniciar o processamento |
| 🔧 **Caminhos Windows Amigáveis** | Suporte nativo a caminhos com backslashes usando raw strings |

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

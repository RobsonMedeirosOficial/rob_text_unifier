/**
 * =============================================================================
 * 🤖 rob_text_unifier - Servidor Web
 * =============================================================================
 * Servidor Node.js para apresentar a landing page do rob_text_unifier
 * 
 * Funcionalidades:
 * - Serve arquivos estáticos da pasta public/
 * - Rota de health check para monitoramento
 * - Logs formatados no console
 * - Suporte a PORT dinâmica (para deploy em nuvem)
 * 
 * @author Robson Medeiros
 * @license MIT
 * =============================================================================
 */

const express = require('express');
const path = require('path');

// Inicializa o app Express
const app = express();

// Porta do servidor (usa variável de ambiente ou padrão 3000)
const PORT = process.env.PORT || 3000;

// =============================================================================
// MIDDLEWARES
// =============================================================================

// Serve arquivos estáticos da pasta 'public'
// Isso permite que CSS, JS, imagens, etc. sejam carregados pelo navegador
app.use(express.static(path.join(__dirname, 'public')));

// Parse de JSON para futuras APIs (preparação para expansão)
app.use(express.json());

// Parse de URL encoded para formulários (preparação para expansão)
app.use(express.urlencoded({ extended: true }));

// =============================================================================
// ROTAS PRINCIPAIS
// =============================================================================

/**
 * Rota raiz - Serve a página principal (index.html)
 * @route GET /
 */
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

/**
 * Rota de health check - Para monitoramento e deploy
 * @route GET /health
 * @returns {Object} Status do servidor
 */
app.get('/health', (req, res) => {
    res.json({
        status: 'ok',
        message: 'rob_text_unifier server is running! 🚀',
        timestamp: new Date().toISOString(),
        version: '1.1.0'
    });
});

/**
 * Rota de informações da API (futuro)
 * @route GET /api/info
 */
app.get('/api/info', (req, res) => {
    res.json({
        name: 'rob_text_unifier',
        description: 'Consolida arquivos de projeto em um único texto para IAs',
        features: [
            'Filtro por nome de arquivo',
            'Filtro por pasta',
            'Filtro por extensão (case-insensitive)',
            'Regra parcial de pastas',
            'Encoding inteligente com fallback',
            'Seções numeradas para busca humana'
        ],
        github: 'https://github.com/RobsonMedeirosOficial/rob_text_unifier'
    });
});

/**
 * Rota 404 - Página não encontrada
 * @route * (qualquer rota não definida)
 */
app.use((req, res) => {
    res.status(404).sendFile(path.join(__dirname, 'public', 'index.html'));
    // Alternativa: criar uma página 404.html personalizada
});

// =============================================================================
// TRATAMENTO DE ERROS GLOBAL
// =============================================================================

app.use((err, req, res, next) => {
    console.error('❌ Erro não tratado:', err);
    res.status(500).json({
        error: 'Internal Server Error',
        message: process.env.NODE_ENV === 'development' ? err.message : 'Algo deu errado'
    });
});

// =============================================================================
// INICIALIZAÇÃO DO SERVIDOR
// =============================================================================

const server = app.listen(PORT, () => {
    // Limpa o console para uma apresentação mais limpa
    console.clear();
    
    // Mensagem de inicialização formatada
    console.log(`
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║   🤖  rob_text_unifier - Servidor Web                    ║
║                                                           ║
║   🚀  Status: ONLINE                                     ║
║   🌐  URL: http://localhost:${PORT}                         ║
║   📁  Public: ./public/                                  ║
║   🔧  Node: ${process.version}                                  ║
║                                                           ║
║   💡  Comandos úteis:                                    ║
║   • Health:  curl http://localhost:${PORT}/health           ║
║   • API:     curl http://localhost:${PORT}/api/info         ║
║   • Dev:     npm run dev (com auto-reload)                ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
    `);
});

// =============================================================================
// TRATAMENTO DE ENCERRAMENTO GRACIOSO
// =============================================================================

// Captura sinais de interrupção para fechar o servidor corretamente
process.on('SIGINT', () => {
    console.log('\n🛑 Recebido SIGINT - Fechando servidor...');
    server.close(() => {
        console.log('✅ Servidor encerrado com sucesso');
        process.exit(0);
    });
});

process.on('SIGTERM', () => {
    console.log('\n🛑 Recebido SIGTERM - Fechando servidor...');
    server.close(() => {
        console.log('✅ Servidor encerrado com sucesso');
        process.exit(0);
    });
});

// Log de erros não capturados
process.on('uncaughtException', (err) => {
    console.error('❌ Uncaught Exception:', err);
    server.close(() => process.exit(1));
});

process.on('unhandledRejection', (reason, promise) => {
    console.error('❌ Unhandled Rejection at:', promise, 'reason:', reason);
});
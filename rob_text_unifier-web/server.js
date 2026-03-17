const express = require('express');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000;

// Servir arquivos estáticos da pasta public
app.use(express.static(path.join(__dirname, 'public')));

// Rota principal
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// Rota de saúde (health check)
app.get('/health', (req, res) => {
    res.json({ status: 'ok', message: 'Server is running!' });
});

// Iniciar servidor
app.listen(PORT, () => {
    console.log(`
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║   🚀  rob_text_unifier - Servidor rodando!               ║
║                                                           ║
║   🌐  Acesse: http://localhost:${PORT}                      ║
║   📁  Arquivos: ./public/                                ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
    `);
});
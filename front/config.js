// ============================================
// CONFIGURAÇÃO DA API
// ============================================

// Detectar URL da API automaticamente
// Em desenvolvimento: usa localhost
// Em produção: usa a URL do backend deployado


const CONFIG = {
    // Localmente: http://localhost:8000
    // Em produção: https://seu-backend.render.com
    API_BASE_URL: window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1'
        ? `http://${window.location.hostname}:8000`
        : 'https://beck-end-do-site-de-receitas-2.onrender.com', // MUDE ISTO QUANDO FIZER DEPLOY

    API_ENDPOINTS: {
        RECEITAS: '/1receita/receber',
        RECEITA_ESPECIFICA: '/1receita/especifico',
        CRIAR_RECEITA: '/1receita_auth/enviar',
        UPLOAD_FOTO: '/1foto/enviar',
        DELETAR_FOTO: '/1foto/deletar',
        OBTER_FOTO: '/1foto/receber',
        REGISTRAR: '/1registro/registro',
        LOGIN: '/1login/login',
    }
};

// Função auxiliar para construir URLs
function getApiUrl(endpoint, id = null) {
    const url = CONFIG.API_BASE_URL + CONFIG.API_ENDPOINTS[endpoint];
    return id ? `${url}/${id}` : url;
}



// ============================================
// CONFIGURAÇÃO DA API
// ============================================

// Detectar URL da API automaticamente
// Em desenvolvimento: usa localhost
// Em produção: usa a URL do backend deployado no Render
/*
const CONFIG = {
    API_BASE_URL: window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1'
        ? `http://${window.location.hostname}:8000`
        : 'https://beck-end-do-site-de-receitas-2.onrender.com',

    API_ENDPOINTS: {
        RECEITAS: '/1receita/receber',
        RECEITA_ESPECIFICA: '/1receita/especifico',
        CRIAR_RECEITA: '/1receita_auth/criar',
        UPLOAD_FOTO: '/1foto/enviar',
        DELETAR_FOTO: '/1foto/deletar',
        OBTER_FOTO: '/1foto/receber',
        REGISTRAR: '/1registro/registrar',
        LOGIN: '/1login/login',
    }
};

// Função auxiliar para construir URLs da API
function getApiUrl(endpoint, id = null) {
    const url = CONFIG.API_BASE_URL + CONFIG.API_ENDPOINTS[endpoint];
    return id ? `${url}/${id}` : url;
}

// Função auxiliar para montar URL de fotos
function getFotoUrl(nomeArquivo) {
    return `${CONFIG.API_BASE_URL}/uploads/${nomeArquivo}`;
}
*/




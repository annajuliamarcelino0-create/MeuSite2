// 1. Seleciona o elemento diretamente pela tag 'h1'
const titulo = document.querySelector('h1');

// 2. Adiciona o Event Listener para o evento de clique duplo ('dblclick')
titulo.addEventListener('dblclick', function () {
    // 3. Altera a cor de fundo do body para azul
    document.body.style.backgroundColor = 'royalblue';
    alert('O fundo da página foi alterado para azul!');
});

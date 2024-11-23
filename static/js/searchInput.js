document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('searchForm');
    const input = document.getElementById('searchInput');

    form.addEventListener('submit', function (event) {
        if (!input.value.trim()) {
            event.preventDefault(); // Previne o envio do formulário
        }
    });
});
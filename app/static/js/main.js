document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');
    const loadingMessage = document.getElementById('loading-message');

    form.addEventListener('submit', function () {
        loadingMessage.classList.remove('hidden');
    });
});
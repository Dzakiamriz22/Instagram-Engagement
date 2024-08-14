document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');
    const loadingMessage = document.getElementById('loading-message');
    const userMenuButton = document.getElementById('user-menu-button');
    const userMenu = document.getElementById('user-menu');

    form.addEventListener('submit', function () {
        loadingMessage.classList.remove('hidden');
    });

    userMenuButton.addEventListener('click', function () {
        // Toggle the visibility of the dropdown menu
        if (userMenu.classList.contains('hidden')) {
            userMenu.classList.remove('hidden');
        } else {
            userMenu.classList.add('hidden');
        }
    });

    // Close the dropdown menu if the user clicks outside of it
    document.addEventListener('click', function (event) {
        if (!userMenuButton.contains(event.target) && !userMenu.contains(event.target)) {
            userMenu.classList.add('hidden');
        }
    });
});

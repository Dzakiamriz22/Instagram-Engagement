document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');
    const loadingMessage = document.getElementById('loading-message');
    const userMenuButton = document.getElementById('user-menu-button');
    const userMenu = document.getElementById('user-menu');
    const popup = document.getElementById('success-popup');

    // Show loading message on form submit
    if (form) {
        form.addEventListener('submit', function () {
            loadingMessage.classList.remove('hidden');
        });
    }

    // Toggle the visibility of the dropdown menu
    if (userMenuButton && userMenu) {
        userMenuButton.addEventListener('click', function (event) {
            event.preventDefault();
            userMenu.classList.toggle('hidden');
        });

        // Close the dropdown menu if the user clicks outside of it
        document.addEventListener('click', function (event) {
            if (!userMenuButton.contains(event.target) && !userMenu.contains(event.target)) {
                userMenu.classList.add('hidden');
            }
        });
    }

    // Show and hide the success popup
    if (popup) {
        console.log('Popup found, attempting to show.');
        popup.classList.remove('hidden');
        setTimeout(function () {
            console.log('Hiding popup.');
            popup.classList.add('hidden');
        }, 2000); // 2000ms = 2 seconds
    } else {
        console.log('Popup not found.');
    }
});
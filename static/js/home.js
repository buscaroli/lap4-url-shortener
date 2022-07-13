const form = document.getElementById('url-shortener');
const shortURLParagraph = document.getElementById('short-url-output');
const refreshButton = document.getElementById('refresh');
const URLInput = document.getElementById('url-input');

form.addEventListener('submit', (e) => {
    console.log(URLInput.value);
    localStorage.setItem('showUrl', true);
    localStorage.setItem('input', URLInput.value);
});

refreshButton.addEventListener('click', (e) => {
    shortURLParagraph.classList.add('short-url');
    URLInput.value = '';
    if (localStorage.getItem('showUrl')) {
        localStorage.removeItem('showUrl');
    }
    if (localStorage.getItem('input')) {
        localStorage.removeItem('input');
    }
});

window.onload = function () {
    if (localStorage.getItem('showUrl')) {
        shortURLParagraph.classList.remove('short-url');
    }
    if (localStorage.getItem('input')) {
        URLInput.value = localStorage.getItem('input');
    }
};

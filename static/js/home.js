const form = document.getElementById('url-shortener');
const shortURLParagraph = document.getElementById('short-url-output');
const refreshButton = document.getElementById('refresh');
const URLInput = document.getElementById('url-input');

form.addEventListener('submit', (e) => {
    e.preventDefault();
    shortURLParagraph.classList.remove('short-url');
});

refreshButton.addEventListener('click', (e) => {
    console.log('I am being clicked');
    shortURLParagraph.classList.add('short-url');
    URLInput.value = '';
});

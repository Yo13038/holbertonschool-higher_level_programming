
const redHeaderButton = document.querySelector('#red_header');
const headerElement = document.querySelector('header');

redHeaderButton.addEventListener('click', () => {

  headerElement.classList.add('red');
});

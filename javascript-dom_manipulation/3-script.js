
const toggleButton = document.querySelector('#toggle_header');
const headerElement = document.querySelector('header');

toggleButton.addEventListener('click', () => {

  headerElement.classList.toggle('red');
  headerElement.classList.toggle('green');
});

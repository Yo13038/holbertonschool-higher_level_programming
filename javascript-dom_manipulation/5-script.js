
const updateHeader = document.querySelector('#update_header');
const headerElement = document.querySelector('header');

updateHeader.addEventListener('click', () => {

  headerElement.textContent = 'New Header!!!';
});

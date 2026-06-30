
function changeColor() {
  const header = document.querySelector('header');
  header.style.color = '#FF0000';
}

const triggerElement = document.getElementById('red_header');

triggerElement.addEventListener('click', () => {
  changeColor();
});

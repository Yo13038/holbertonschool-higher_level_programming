
const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';


const characterElement = document.querySelector('#character');


fetch(url)
  .then((response) => {

    return response.json();
  })
  .then((data) => {

    characterElement.textContent = data.name;
  })
  .catch((error) => {

    console.error('Erreur lors de la récupération :', error);
  });
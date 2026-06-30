
const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

const listMoviesElement = document.querySelector('#list_movies');


fetch(url)
  .then((response) => {

    return response.json();
  })
  .then((data) => {

    const movies = data.results;

    movies.forEach((movie) => {
      const li = document.createElement('li');
      
      li.textContent = movie.title;
      
      listMoviesElement.appendChild(li);
    });
  })
  .catch((error) => {
    console.error('Erreur lors de la récupération des films :', error);
  });

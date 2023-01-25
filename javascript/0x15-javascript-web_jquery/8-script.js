const endpoint = "https://swapi-api.alx-tools.com/api/films/?format=json";

$.get(endpoint, function(data) {
	data.results.forEach(movie => {
		$('UL#list_movies').append(`<li>${movie.title}</li>`);
	});
});
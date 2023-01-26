const endpoint = "https://swapi-api.alx-tools.com/api/people/5/?format=json"

$.get(endpoint, function(data) {
  $("#character").text(data.name);
});


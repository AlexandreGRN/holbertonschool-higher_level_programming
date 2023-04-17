$.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  const items = [];
  $.each(data.results, function (key, val) {
    items.push("<li id='" + key + "'>" + val.title + '</li>');
  });
  $('<ul/>', {
    class: 'my-new-list',
    html: items.join('')
  }).appendTo('body');
});

$(document).ready(init);

const HOST = '0.0.0.0';

function init () {
  const artsObj = {};
  $('.artts .popover input').change(function () {
    if ($(this).is(':checked')) {
      artsObj[$(this).attr('data-name')] = $(this).attr('data-id');
    } else if ($(this).is(':not(:checked)')) {
      delete artsObj[$(this).attr('data-name')];
    }
    const names = Object.keys(artsObj);
    $('.artts h4').text(names.sort().join(', '));
  });

  apiStatus();
  fetchArtists();
}

function apiStatus () {
  const API_URL = `http://${HOST}:5001/api/v1/status/`;
  $.get(API_URL, (data, textStatus) => {
    if (textStatus === 'success' && data.status === 'OK') {
      $('#api_status').addClass('available');
    } else {
      $('#api_status').removeClass('available');
    }
  });
}

function fetchPlaces () {
  const PLACES_URL = `http://${HOST}:5001/api/v1/artists_search/`;
  $.ajax({
    url: PLACES_URL,
    type: 'POST',
    headers: { 'Content-Type': 'application/json' },
    data: JSON.stringify({}),
    success: function (response) {
      for (const r of response) {
        const article = ['<article>',
          '<div class="title_box">',
        `<h2>${r.name}</h2>`,
        `<div class="price_by_hour">$${r.price_by_hour}</div>`,
        '</div>',
        '<div class="information">',
        '</div>',
        '<div class="description">',
        `${r.description}`,
        '</div>',
        '</article>'];
        $('SECTION.artists').append(article.join(''));
      }
    },
    error: function (error) {
      console.log(error);
    }
  });
}

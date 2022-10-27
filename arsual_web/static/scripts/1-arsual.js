$(document).ready(init);

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
}

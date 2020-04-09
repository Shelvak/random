// TraktTV
$('.huckster-vip-square, .selected .trakt-icon-check-thick').each(function(i, element) {
  $(element).parents('.grid-item:first').remove()
});
$('.huckster-vip-info').parent().remove();

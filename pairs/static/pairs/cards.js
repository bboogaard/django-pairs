var current = null;

$('.grid-view li').click(function(event) {
    if (!$(this).hasClass('turn') && !$(this).hasClass('open') && !$(this).hasClass('hold')) {
        $(this).addClass('turn');
        if (!current) {
            current = $(this).data('card-id');
        }
        else if ($(this).data('card-id') == current) {
            $('li[data-card-id="' + current + '"]').removeClass('turn').addClass('open');
            current = null;
        }
        else {
            $('li:not(.turn)').addClass('hold');
            setTimeout(function() {
                $('li.turn').removeClass('turn');
                $('li:not(.turn)').removeClass('hold');
                current = null;
            }, 2000);
        }
    }
});

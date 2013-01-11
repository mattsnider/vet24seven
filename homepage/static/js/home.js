var isAnimating = false;

$('form').submit(function(e) {
    var elForm = $(e.target);
    e.preventDefault();
    $.ajax(elForm.attr('action'), {
        data: elForm.serialize(),
        type: elForm.attr('method')
    });
    elForm.find('button').removeClass('on').addClass('off');
    elForm.find('input[type=text]').val('').focus();
});

$('a.link-back').click(function(e) {
    e.preventDefault();

    if (!isAnimating) {
        var elTarget = $(e.target),
            elScrollTarget = $('.scroll_target'),
            iStepSize = Math.round((elScrollTarget.offset().top - elTarget.offset().top) / 25),
            iStepIndex = 0,
            iIntervalId = setInterval(function() {
                if (5 > iStepIndex) {
                    window.scrollTo(0, iStepSize * iStepIndex * iStepIndex);
                    iStepIndex += 1;
                }
                else {
                    window.scrollTo(0, elScrollTarget.offset().top);
                    clearInterval(iIntervalId);
                    isAnimating = false;
                }
            }, 100);

        isAnimating = true;
    }
});
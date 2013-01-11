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
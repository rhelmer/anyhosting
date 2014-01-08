$(document).ready(function() {
    $('#upload-button').click(function() {
        $('html,body').css('background-color', 'grey');
        $('#newfolder').hide();
        $('#upload').fadeToggle();
    });
    $('#newfolder-button').click(function() {
        $('html,body').css('background-color', 'grey');
        $('#upload').hide();
        $('#newfolder').fadeToggle();
    });
    $('.close-button').click(function() {
        $('html,body').css('background-color', '#8ab5a2');
        $('#upload').fadeOut();
        $('#newfolder').fadeOut();
    })
    $('#upload-ok').click(function(event) {
        $('html,body').css('background-color', '#8ab5a2');
        event.preventDefault();
        $('#upload').fadeOut();
    });
    $('#newfolder-ok').click(function(event) {
        $('html,body').css('background-color', '#8ab5a2');
        event.preventDefault();
        $('#newfolder').fadeOut();
    });
});

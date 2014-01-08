$(document).ready(function() {
    $('#upload-button').click(function() {
        $('#newfolder').hide();
        $('#upload').fadeToggle();
    });
    $('#newfolder-button').click(function() {
        $('#upload').hide();
        $('#newfolder').fadeToggle();
    });
    $('.close-button').click(function() {
        $('#upload').fadeOut();
        $('#newfolder').fadeOut();
    })
    $('#upload-ok').click(function(event) {
        event.preventDefault();
        $('#upload').fadeOut();
    });
    $('#newfolder-ok').click(function(event) {
        event.preventDefault();
        $('#newfolder').fadeOut();
    });
});

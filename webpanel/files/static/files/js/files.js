$(document).ready(function() {
    $('#upload-button').click(function() {
        $('#newfolder').hide();
        $('#upload').fadeToggle();
    });
    $('#newfolder-button').click(function() {
        $('#upload').hide();
        $('#newfolder').fadeToggle();
    });
    $('#upload-ok').click(function(event) {
        event.preventDefault();
        $('#upload').fadeOut();
    });
    $('#newfolder-ok').click(function(event) {
        event.preventDefault();
        $('#newfolder').fadeOut();
    });
});

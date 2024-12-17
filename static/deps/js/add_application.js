('$application-form').submit(function(e) {
    $.post('/create_application/', $(this).serialize(), function(data) {
        $('.posts').html(data);
    });
    e.preventDefault();
});
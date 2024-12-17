('$search-application').submit(function(e) {
    $.post('/search_application/', $(this).serialize(), function(data) {
        $('.posts').html(data);
    });
    e.preventDefault();
});
$('.head_search').on('keyup', function() {
    $('div.nav-search').show();
    $.ajax({
        url : '/search/isearch/head/',
        method : 'GET',
        data:{'key':$(this).val()},
        success : function(data) {
            $('div.nav-search').empty().append(data);
        },
    });
});

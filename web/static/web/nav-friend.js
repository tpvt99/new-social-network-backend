$('button#nav-friend').on('click', function() {
    $('div.nav-friend').show();
    $('div.nav-stat').hide();
    $('div.nav-search').hide();
    $('div.nav-mess').hide();
    $.ajax({
        url : '/friend/friendajax/',
        method : 'GET',
        data:{'page':'0'},
        success: function(data) {
            $('div.nav-friend').empty().append(data);
        }
    });
});

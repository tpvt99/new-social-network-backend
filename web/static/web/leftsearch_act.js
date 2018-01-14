$.ajax({
    url : "/leftsearch/activity/",
    method : 'GET',
    success : function(data) {
        $('div#l_s_act_show').append(data);
    }
});
$('a#l_search_act').on('click', function() {
    if ($('div#l_s_act_show').html().trim() === '') {
        $.ajax({
            url : "/leftsearch/activity/",
            method : 'GET',
            success : function(data) {
                $('div#l_s_act_show').append(data).show();
            }
        });
    }
    else {
        $('div#l_s_act_show').show();
    }
});

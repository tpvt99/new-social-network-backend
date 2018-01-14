$('button#nav-stat').on('click', function() {
    $('div.nav-stat').show();
    $('div.nav-friend').hide();
    $('div.nav-mess').hide();
    $('div.nav-search').hide();
    if($('p.more')[0]) {} else {
    $.ajax({
        url : '/noti/notiajax/',
        method : 'GET',
        data:{'page':'0'},
        success: function(data) {
            $('div.nav-stat').empty().append(data);
            $('div.nav-stat').find('p.more').remove();
            $('div.nav-stat').append('<p class="more" style="text-align:center"; data-page="1"><a href="javascript:void(0);">Xem thêm</a></p>');
            NotiTime();
        }
    });
    }
});
$('div.nav-stat').on('click','.more', function(e) {
    e.stopPropagation();
    x = $(this)[0].dataset.page;
    $.ajax({
        url : '/noti/notiajax/',
        method : 'GET',
        data:{'page':x},
        success: function(data) {
            if($(data).find('p.nope').prevObject[0].textContent.trim() === 'Không có thông báo nào') {
            } else {
            $('div.nav-stat').append(data);
            $('div.nav-stat').find('p.more').remove();
            $('div.nav-stat').append(['<p class="more" style="text-align:center" data-page="',parseInt(x)+1,'"><a href="javascript:void(0);">Xem thêm</a></p>'].join(''));
            NotiTime();
            }
        }
    });
});

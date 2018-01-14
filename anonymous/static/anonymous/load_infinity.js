var curr_page = 0;
var hasmoreload = true;
function getDocHeight() {
    var D = document;
    return Math.max(
        D.body.scrollHeight, D.documentElement.scrollHeight,
        D.body.offsetHeight, D.documentElement.offsetHeight,
        D.body.clientHeight, D.documentElement.clientHeight);
}

var loadScroll = function(e) {
    var page = e.data.page;
    if ( $(window).scrollTop() + $(window).height() > getDocHeight() - 50) {
        $(window).off('scroll');
        callAjax(page);
    }
}

function LoadAjax(page) {
    $.ajax({
        url : "/anonymous/content/",
        method : 'GET',
        data: {'page' :page},
        success : function(data) {
            if (data !== 'error') {
                $('.middle_sta').append(data);
                $(window).on('scroll', {'page':page+1}, loadScroll);
            }
            else {
                hasmoreload = false;
            }
       },
    });
}

function callAjax(page) {
    LoadAjax(page);
}
callAjax(curr_page);


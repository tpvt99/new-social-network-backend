$(document).on('keydown','.comment-text', function(e) {
    var z = $(this).find('br[data-text="true"]');
    var br = $("<br data-text='true' />");
    var t = $(this).find('span.data-top-text');
    var ph = $(this).find('.comment-placeholder');
    console.log(e);
    if(e.keyCode === 8 || e.keyCode === 46) { //delete
    }
    else if(e.keyCode == 13 ) { //Enter
    }
    else if(e.keyCode == 9) {
        e.preventDefault();
    } else {
    }
});
$(document).on('click','.comment-text', function(e) {
    console.log(e);
});

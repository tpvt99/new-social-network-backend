$('.m1').on('mouseover', function() {
    $(this).css('opacity','0.7');
    var x = $('<span class="m1 ion ion-plus-round"></span>');
    $(this).append(x);
}).on('mouseleave', function() {
    $(this).css('opacity','1');
    $(this).children('span').remove();
});
$('.sp1').on('click',function() {window.location.href='/activity/create/?type=sport'});
$('.es1').on('click',function() {window.location.href='/activity/create/?type=esport'});
$('.vl1').on('click',function() {window.location.href='/activity/create/?type=volunteer'});
$('.bp1').on('click',function() {window.location.href='/activity/create/?type=backpacking'});
$('.ca1').on('click',function() {window.location.href='/activity/create/?type=camp'});
$('.si1').on('click',function() {window.location.href='/activity/create/?type=sing'});
$('.en1').on('click',function() {window.location.href='/activity/create/?type=entertainment'});
$('.cl1').on('click',function() {window.location.href='/activity/create/?type=clb'});
$('.ex1').on('click',function() {window.location.href='/activity/create/?type=exchange'});

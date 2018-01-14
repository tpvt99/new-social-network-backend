function ImageX(x) {
    $('.modal').find('.modal-content').empty().append('<p style="padding:10px 20px;text-align:center;"><span class="fa fa-circle-o-notch fa-spin fa-3x fa-fw"></span><p>');
    $('.modal').modal({
        keyborad : false,
        show : true,
    });
    $.ajax({
        method:'GET',
        url:'/group/edit/',
        data : {'which':'background', 'group':x.data('group')},
        success:function(data) {
            $('.modal').find('.modal-content').empty().append(data);
        }
    });
}
$('.background-edit').on('click', function() {
    ImageX($(this));
});

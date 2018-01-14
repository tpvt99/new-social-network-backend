$('#content').on('click','.w_op_img', function() {
    var idx = $(this).parents('.usrcont').data('id');
    $('#addimgModal').find('.addimgact').val(idx);
    $('#addimgModal').modal('show');
});
$('#addimgModal').on('change','#addimgMo', function() {
    var x = $('.addimgact').val();
    var form = new FormData($('.aiform')[0]);
    form.append('x', x);
    if (x) {
    var csrftoken = getCookie('csrftoken');
    $.ajaxSetup({beforeSend: function(xhr, settings) { if (!csrfSafeMethod(settings.type) && !this.crossDomain) { xhr.setRequestHeader('X-CSRFToken', csrftoken);}} });
        $.ajax({
            method : 'POST',
            url : '/addimg/activity/',
            processData : false,
            contentType : false,
            cache : false,
            data : form,
            success : function(data) {
                if (data !== 'error') {
                    var idx = data.id;
                    var url = data.url;
                    var a = data.act;
                    var ap = $('.d_img_1');
                    var x = $( ['<div class="d_img" data-img-id="',idx,'" data-act-id="',a,'"><img src="',url,'"class="d_img_e"><span class="d_img_co">&times;</span></div>'].join(''));
                    $('.ren_addimg').append(x);
                    $('.d_img_1').remove();
                    ap.appendTo( $('.ren_addimg'));
                }
                else {
                    alert('Đã xảy ra lỗi. Xin thực hiện lại');
                }
            },
        });
    }
});
$('#addimgModal').on('click', '.d_img_co', function() {
    var $this = $(this);
    var datax = {};
    datax.i_i = $this.parent('div.d_img').data('img-id');
    datax.a_i = $this.parent('div.d_img').data('act-id');
    var csrftoken = getCookie('csrftoken');
    $.ajaxSetup({beforeSend: function(xhr, settings) { if (!csrfSafeMethod(settings.type) && !this.crossDomain) { xhr.setRequestHeader('X-CSRFToken', csrftoken);}} });
    $.ajax({
        method : 'POST',
        url :'/delimg/',
        data : {'data': JSON.stringify(datax)},
        success: function(data) {
            if (data === 'error') {
                alert('Error happended. Please try again');
            }
            else {
                $this.parent('div.d_img').remove();
            }
        },
    });
});

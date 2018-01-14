$(document).on('submit','.mess-form', function(e) {
    e.preventDefault();
    var $this = $(this);
    var val = $this.find('input.mess-in').val();
    if(val.trim() === '') {
        alert('Tin nhắn còn trống');
        return false;
    }
    $this.find('input.mess-in').val('');
    var csrftoken = $this.find('input[name="csrfmiddlewaretoken"]').val();
    $.ajaxSetup({beforeSend: function(xhr, settings) {if (!csrfSafeMethod(settings.type) && !this.crossDomain) {xhr.setRequestHeader('X-CSRFToken', csrftoken);}}});
    $.ajax({
        method : 'POST',
        url : '/message/ajax/sendmess/',
        data : {'mess':val,'mu':$this.data('b')},
        success : function(data) {
            if(data ==='error') {alert('Có lỗi xảy ra. Xin vui lòng thử lại');}
            else {
                var x= $this.parents('.div-chat').find('.chat-body');
                x.append(data);
                x[0].scrollTop = x[0].scrollHeight;
            }
        }
    });
});
$(document).on('click','.chat-close', function() {
    clearInterval(parseInt($(this).data('ti')));
    $(this).parents('div.div-chat').remove();
});
$(document).on('click','.chat-title', function() {
    var x = $(this)[0];
    if(x.dataset.min == 'false' ) {
        $(this).siblings('div').css('display','none');
        x.dataset.min = 'true';
    } else {
        $(this).siblings('div').css('display','');
        x.dataset.min = 'false';
    }
});

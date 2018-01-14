$('.ev-add').on('click', function(e) {
    e.stopPropagation();
    var $this = $(this);
    var t = $this[0].dataset.action;
    var csrftoken = $(this).parents('.friend-div-info').find('input[name="csrfmiddlewaretoken"]').val();
    $.ajaxSetup({beforeSend: function(xhr, settings) {if (!csrfSafeMethod(settings.type) && !this.crossDomain) {xhr.setRequestHeader('X-CSRFToken', csrftoken);}}});
    $.ajax({
        method : 'POST',
        url : '/friend/add/',
        data : {'key':$this[0].dataset.who,'action':t},
        success: function(data) {
            if (data === 'ok') {
                if(t==='connect') {
                    $this.removeClass('btn-primary').addClass('btn-default');
                    $this.text('Hủy kết bạn');
                    $this[0].dataset.action = 'decline';
                    $this.siblings('.ev-add').remove();
                } else if(t=== 'decline') {
                    $this.removeClass('btn-default').addClass('btn-primary');
                    $this[0].dataset.action = 'connect';
                    $this.text('Kết bạn');
                    $this.siblings('.ev-add').remove();
                } else if(t=== 'accept') {
                    $this.removeClass('btn-default').addClass('btn-success');
                    $this.text('Đã là bạn bè');
                    $this.attr('disabled','disabled');
                    $this.siblings('.ev-add').remove();
                } else if (t=== 'refuse') {
                    $this.removeClass('btn-danger').addClass('btn-primary');
                    $this.text('Kết bạn');
                    $this[0].dataset.action = 'connect';
                    $this.siblings('.ev-add').remove();
                }
            }
            else {
                alert('Có lỗi xảy ra. Xin vui lòng thử lại');
            }
        }
    });
});

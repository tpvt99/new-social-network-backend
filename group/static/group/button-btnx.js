$('.btnx').on('click', function() {
    var $this = $(this);
    if($this.data('send') === true) {
    var csrftoken =$this.siblings('input[name="csrfmiddlewaretoken"]').val();$.ajaxSetup({beforeSend: function(xhr, settings) {if (!csrfSafeMethod(settings.type) && !this.crossDomain) {xhr.setRequestHeader('X-CSRFToken', csrftoken);}}});
    $.ajax({
        url : '/group/join/',
        method : 'POST',
        data:{'action':$this.data('action'),'group':$this.data('group'),'who':$this.data('who')},
        success : function(data) {
            if(data === 'ok') {
                if($this.data('action') === 'join') {
                    $this[0].dataset.send = false;
                    $this.text('Đã gửi lời mời');
                } else if($this.data('action') === 'back') {
                    $this[0].dataset.send = false;
                    $this.text('Đã rút lại lời mời');
                } else if($this.data('action') === 'refuse') {
                    $this[0].dataset.send = false;
                    $this.text('Đã từ chối');
                    $this.siblings('button').remove();
                } else if($this.data('action') === 'accept') {
                    $this[0].dataset.send = false;
                    $this.text('Đã chấp nhận');
                    $this.siblings('button').remove();
                }
            } else {
                alert('Có lỗi xảy ra. Xin vui lòng tải lại trang');
            }
        }
    });
    }
});

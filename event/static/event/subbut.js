$('.subbut').on('click', function() {
    var $this = $(this);
    if($this[0].dataset.send == 'false') return false;
    var csrftoken = $(this).siblings('input').val();
    $.ajaxSetup({beforeSend: function(xhr, settings) {if (!csrfSafeMethod(settings.type) && !this.crossDomain) {xhr.setRequestHeader('X-CSRFToken', csrftoken);}}});
    $.ajax({
        url :'/event/join/',
        method : 'POST',
        data: {'event':$this[0].dataset.event, 'action':$this[0].dataset.action,'who':$this[0].dataset.who},
        success: function(data) {
            if(data === 'ok' && $this[0].dataset.action === 'join') {
                $this[0].dataset.action = 'decline';
                $this.removeClass('btn-primary').addClass('btn-default').text('Hủy tham gia');
            }
            else if(data === 'ok' && $this[0].dataset.action === 'decline') {
                $this[0].dataset.send = "false";
                $this.text('Đã hủy');
            }
            else if(data === 'ok' && $this[0].dataset.action === 'accept') {
                $this[0].dataset.send="false";
                $this.text('Đã chấp nhận');
                $this.siblings('button').remove();
                $this.removeClass('btn-info').addClass('btn-success');
            }
            else if(data === 'ok' && $this[0].dataset.action === 'invite') {
                $this.text('Hủy lời mời');
                $this[0].dataset.action = "decline";
                $this.removeClass('btn-primary').addClass('btn-default');
            }
            else if(data === 'ok' && $this[0].dataset.action === 'refuse') {
                $this.text('Đã từ chối');
                $this[0].dataset.send = "false";
                $this.attr('disabled','disabled');
                $this.removeClass('btn-warning').addClass('btn-default');
                $this.siblings('button').remove();
            }
            else if(data === 'ok' && $this[0].dataset.action === 'report') {
                $this.text('Bạn đã báo cáo vi phạm sự kiện này');
                $this.prop('disabled','disabled');
            }
            else if(data !== 'ok') {
                alert('Có lỗi xảy ra. Vui lòng thử lại');
            }
        }
    }); 
});

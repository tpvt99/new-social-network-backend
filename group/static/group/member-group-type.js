$('button.but').on('click', function() {
    var $this = $(this);
    var csrftoken =$this.siblings('input[name="csrfmiddlewaretoken"]').val();$.ajaxSetup({beforeSend: function(xhr, settings) {if (!csrfSafeMethod(settings.type) && !this.crossDomain) {xhr.setRequestHeader('X-CSRFToken', csrftoken);}}});
    $.ajax({
        url : '/group/member/',
        method : 'POST',
        data:{'action':'group-type','group':$this.data('group'),'x':$this.data('x')},
        success : function(data) {
            if(data === 'ok') {
                $this.siblings('button').removeClass('but-active');
                $this.addClass('but-active');
            } else {
                alert('Có lỗi xảy ra. Xin vui lòng thử lại');
            }
        }
    });
});

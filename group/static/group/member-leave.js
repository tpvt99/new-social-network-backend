$('a.leave-remove').on('click', function() {
    var $this = $(this);
    var csrftoken =$this.siblings('input[name="csrfmiddlewaretoken"]').val();$.ajaxSetup({beforeSend: function(xhr, settings) {if (!csrfSafeMethod(settings.type) && !this.crossDomain) {xhr.setRequestHeader('X-CSRFToken', csrftoken);}}});
    $.ajax({
        url : '/group/member/',
        method : 'POST',
        data:{'action':'leave','group':$this.data('group')},
        success : function(data) {
            if(data === 'ok') {
                window.location = "/group/group/"+$this.data('group')+'/';
            }
             else{
                alert('Có lỗi xảy ra. Xin vui lòng thử lại');
            }
        }
    });
});

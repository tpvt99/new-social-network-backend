$('a.follow-edit').on('click', function() {
    var $this = $(this);
    var csrftoken =$this.siblings('input[name="csrfmiddlewaretoken"]').val();$.ajaxSetup({beforeSend: function(xhr, settings) {if (!csrfSafeMethod(settings.type) && !this.crossDomain) {xhr.setRequestHeader('X-CSRFToken', csrftoken);}}});
    $.ajax({
        url : '/group/member/',
        method : 'POST',
        data:{'action':'follow-edit','group':$this.data('group')},
        success : function(data) {
            if(data === 'True') {
                $this.empty().append('<span class="ion-eye-disabled"></span><span style="margin-left:5px;">Bỏ theo dõi nhóm</span>');
            } else if(data === 'False') {
                $this.empty().append('<span class="ion-eye"></span><span style="margin-left:5px;">Theo dõi nhóm</span>');
            }
             else{
                alert('Có lỗi xảy ra. Xin vui lòng thử lại');
            }
        }
    });
});

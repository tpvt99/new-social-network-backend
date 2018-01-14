$('.edit-privacy').on('click', function() {
    var $this = $(this);
    var csrftoken =$this.siblings('input[name="csrfmiddlewaretoken"]').val();$.ajaxSetup({beforeSend: function(xhr, settings) {if (!csrfSafeMethod(settings.type) && !this.crossDomain) {xhr.setRequestHeader('X-CSRFToken', csrftoken);}}});
    $.ajax({
        url : '/group/edit/',
        method : 'POST',
        data:{'which':'privacy','group':$this.data('group'),'privacy':$this.data('privacy')},
        success : function(data) {
            if(data === 'ok') {
                if($this.data('privacy') ==='public') {
                    $('.a-pr').empty().append('<span class="fa fa-unlock-alt"></span><span style="margin-left:10px;">Nhóm công khai</span>');
                } else {
                    $('.a-pr').empty().append('<span class="fa fa-lock"></span><span style="margin-left:10px;">Nhóm riêng tư</span>');
                }
            }
        }
    });
});

$(document).on('submit','.comment-form-moment', function(e) {
    e.preventDefault();
    var $this = $(this);
    var i = $this.find('.comment-text');
    if(i.val().trim() === '') {
        alert('Bạn phải điền bình luận');
    }
    var csrftoken = $this.find('input[name="csrfmiddlewaretoken"]').val();
    $.ajaxSetup({beforeSend: function(xhr, settings) {if (!csrfSafeMethod(settings.type) && !this.crossDomain) {xhr.setRequestHeader('X-CSRFToken', csrftoken);}}});
    $.ajax({
        method : 'POST',
        url :'/moment/comment/',
        data: {'text':i.val(),'m':i.data('m')},
        success :function(data) {
            $this.parent('.moment-comment').siblings('.moment-index').append(data);
            i.val('');
        }
    });
});

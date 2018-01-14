$('.post-form-x').on('submit', function(e) {
    e.preventDefault();
    var text = $(this).find('.st-text').val();
    if(text === '') {
        alert('Bài đăng còn trống');
        return false;
    }
    var form = new FormData($(this)[0]);
    var csrftoken = getCookie('csrftoken');$.ajaxSetup({beforeSend: function(xhr, settings) {if (!csrfSafeMethod(settings.type) && !this.crossDomain) {xhr.setRequestHeader('X-CSRFToken', csrftoken);}}});
    $.ajax({
        method : 'POST',
        url : '/group/grouppost/',
        data : form,
        processData : false,
        contentType : false,
        success : function(data) {
            if(data !== 'error') {
                $('.st-text').val('');
                $('.c_img_div').empty();
                $('.status-index').prepend(data);
                $('#st-image').val('');
            }
        }
    }); 
});

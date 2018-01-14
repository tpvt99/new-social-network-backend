$('.actf').on('submit', function(e) {
    e.preventDefault();
    var form = new FormData($(this)[0]);
    if (form.get('actin').trim() === '' && form.get('desin').trim() === '') 
    {
        alert('Bạn phải điền suy nghĩ hoặc hoạt đông mới đăng được bài');
        return false;
    }
    var csrftoken = getCookie('csrftoken');$.ajaxSetup({beforeSend: function(xhr, settings) {if (!csrfSafeMethod(settings.type) && !this.crossDomain) {xhr.setRequestHeader('X-CSRFToken', csrftoken);}}});
    $.ajax({
        method : 'POST',
        url : '/status/create/',
        data : form,
        processData: false,
        contentType : false,
        success: function(data) {
            $('.content').prepend(data);
            $('.actin').val('');
            $('.desin').val('');
            $('.desin')[0].style.height = $('.desin').data('h');
            $('.act-image').val('');
            $('.c_img_div').remove();
            $('.fr-c').remove();
        }
    });
});

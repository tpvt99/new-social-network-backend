$('#content').on('focusin', '.w_com_t', function() {
    $(this).addClass('w_text_pholder');
}).on('focusout', '.w_com_t', function() {
    $(this).removeClass('w_text_pholder');
});

$('#content').on('keyup', 'textarea.w_com_t', function(e) {
    var $this = $(this);
    var old_size = this.scrollHeight;
    var pa = $this.parents('form.f_wcom');
    if (e.which == 13 && !e.shiftKey) {
        var val = $this.val();
        var img = pa.find('input:file')[0].files.length;
        if (val.trim() === '' && img === 0) {
            return false; 
        }
        var csrftoken = getCookie('csrftoken');
        $.ajaxSetup({
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader('X-CSRFToken', csrftoken);
                }
            }
        });
        var formData = new FormData(pa[0]);
        $this.val('');
        $this.get(0).style.height = '37' + 'px';
        pa.find('input:file').val('');
        pa.find('.w_com_div').empty().hide(); 
        $.ajax({
            url : "/comment/",
            method : 'POST',
            data : formData,
            processData : false,
            contentType : false,
            success : function(data) {
                if (data !== 'error') {
                    var com = $this.parents('.w_post');
                    com.before(data);
                } else {
                    alert('Loi xay ra. Xin vui long thu lai');
                }
            },
        });
    }
});

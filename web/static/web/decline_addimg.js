$('#addimgModal').on('click', '.d_i_b2', function() {
    var $this = $(this);
    var x = $('.ren_addimg').find('.d_img');
    var obj = {};
    obj.list = [];
    x.each( function() {
        obj.list.push($(this).data('img-id'));
    });
    if (x.length !== 0) {
        var csrftoken = getCookie('csrftoken');
        $.ajaxSetup({beforeSend: function(xhr, settings) { if (!csrfSafeMethod(settings.type) && !this.crossDomain) { xhr.setRequestHeader('X-CSRFToken', csrftoken);}} });
        $.ajax({
            url : '/si/decline/',
            method : 'POST',
            data : {'data' : JSON.stringify(obj)},
            success: function(data) {
                if (data === 'success') {
                    $this.parents('#addimgModal').modal('hide');
                    var e = $('.d_img'); 
                    e.each(function() {
                        $(this).remove();
                    });
                    $('#addimgMo').val('');
                }
                else {
                    alert('Da xay ra loi. Xin vui long thu lai sau');
                }
            }
        });
    }
    else {
        $this.parents('#addimgModal').modal('hide');
    }
});

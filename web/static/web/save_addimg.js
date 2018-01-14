$('#addimgModal').on('click', '.d_i_b1', function() {
    var $this = $(this);
    var x = $('.ren_addimg').find('.d_img');
    var obj = {};
    obj.list = [];
    x.each( function() {
        obj.list.push($(this).data('img-id'));
    });
    obj.actid = $('.addimgact').val();
    var cont = $( ['div.usrcont[data-id="',obj.actid,'"]'].join('')).find('.w_image');
    if (x.length !== 0) {
        var csrftoken = getCookie('csrftoken');
        $.ajaxSetup({beforeSend: function(xhr, settings) { if (!csrfSafeMethod(settings.type) && !this.crossDomain) { xhr.setRequestHeader('X-CSRFToken', csrftoken);}} });
        $.ajax({
            url : '/si/save/',
            method : 'POST',
            data : {'data' : JSON.stringify(obj)},
            success: function(data) {
                if (data.log === 'success') {
                    $this.parents('#addimgModal').modal('hide');
                    if ((parseInt(data.len) + x.length) >= 6)
                    {
                        var cla = "w_imge";
                    }
                    else {
                        var cla = "w_img" +(parseInt(data.len) + parseInt(x.length) );
                    }
                    var t = cont.find('img');
                    t.each(function() {
                        $(this).removeClass().addClass(cla);
                    });
                    x.each(function() {
                        $(this).find('img').removeClass('d_img_e').addClass(cla).appendTo(cont);
                        $(this).remove();
                    });
                    $('#addimgMo').val('');
                }
                else {
                    alert('Da xay ra loi. Xin vui long thu lai sau');
                }
            },
        });
    }
});


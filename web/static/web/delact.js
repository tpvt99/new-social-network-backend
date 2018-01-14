$('#content').on('click','.w_op_del', function() {
    var idx = $(this).parents('.usrcont').data('id');
    $('#deleteModal').find('button').val(idx);
    $('#deleteModal').modal('show');
});
$('#deleteModal').on('click', '#delact', function() {
    var x = $(this).val();
    var csrftoken = getCookie('csrftoken');
    $.ajaxSetup({beforeSend: function(xhr, settings) { if (!csrfSafeMethod(settings.type) && !this.crossDomain) { xhr.setRequestHeader('X-CSRFToken', csrftoken);}} });
    $.ajax({
        url : '/delete_act/',
        method : 'POST',
        data : {'id' : x},
        success : function(data) {
            if (data === 'ok') {
                $( ['div.usrcont[data-id="',x,'"]'].join('')).remove();
                $('#deleteModal').modal('hide');
            }
            else {
                alert('Error happended. Please try again');
            }
        },
    });
});

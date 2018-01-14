$('.member-search').on('keyup', function() {
    var $this = $(this);
    var x = $this.val();
    $.ajax({
        method : 'GET',
        url : '/group/member/',
        data : {'name':x,'group':$this.data('group'), 'action':'add'},
        success : function(data) {
            if(x.trim() === '') {
                $('.fr-div').empty().hide();
            } else {
                $('.fr-div').empty().append(data).show();
                $('.member-add-a').on('click', function() {
    var $this = $(this);
    if($this.data('send') == true) {
    var csrftoken =$this.siblings('input[name="csrfmiddlewaretoken"]').val();$.ajaxSetup({beforeSend: function(xhr, settings) {if (!csrfSafeMethod(settings.type) && !this.crossDomain) {xhr.setRequestHeader('X-CSRFToken', csrftoken);}}});
    $.ajax({
        url : '/group/join/',
        method : 'POST',
        data:{'action':$this.data('action'),'group':$this.data('group'),'who':$this.data('who')},
        success : function(data) {
            if(data === 'ok') {
                $this[0].dataset.send = false;
                $this.empty().append('Đã thêm thành công');
            }
        }
    });
    }
});
            }
        }
    });
});

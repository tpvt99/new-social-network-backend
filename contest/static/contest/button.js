$(document).on('click', '.but-fol', function() {
    var $this = $(this);
    var sub = $this.data('submit');
    if(sub) {
        $.ajax({
            url : '/contest/follow/',
            method : 'GET',
            data : {'action':$this.data('action'), contest:$this.data('id')},
            success : function(data) {
                console.log(data);
                if(data === 'ok') {
                    $this.removeClass('but-fol1').addClass('but-fol2');
                    $this[0].dataset.submit = false;
                    $this.text("Đã theo dõi");
                }
                else {
                    alert('Có lỗi xảy ra. Xin vui lòng thử lại');
                }
            }
        });
    }
});

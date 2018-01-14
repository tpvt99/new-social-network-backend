(function() {
    var x = $('.p_image');
    x.each( function() {
        var $this = $(this);
        if( $this.html().trim() === '' && $this.data('isload') === false) {
            $this.data('isload',true);
            $.ajax({
                url : $this.data('load'),
                method : 'GET',
                success : function(data) {
                    var z = $(['<img src="',data,'" class="p_img_img" />'].join(''));
                    $this.append(z);
                }
            });
        }
    });
})();

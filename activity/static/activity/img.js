function readURL(input) {
    var $this = input;
    input = input.get(0);
    var pa = $this.parents('.c_img');
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function(e) {
            var div = $( ['<div class="c_img_div"><img src="',e.target.result,'" /></div>'].join(''));
            div.find('img').css({'width':'100px','height':'100px'});
            div.append( $("<span class='ld_cl'>&times;</span>").on('click', function() {
                $this.val('');
                pa.find('.c_img_div').remove();
            })
            );
            pa.find('.c_img_div').remove();
            pa.append(div);
        }
        reader.readAsDataURL(input.files[0]);
    }
}

$('.c_img_in').on('change', function() {
    readURL($(this));
});

$('input[name="image"]').on('change', function() {
    input = $(this);
    var $this = input;
    input = input.get(0);
    var pa = $('.ac-image');
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function(e) {
            var div = $( ['<div class="c_img_div"><img src="',e.target.result,'" class="cimg" style="z-index:-1" /></div>'].join(''));
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
});

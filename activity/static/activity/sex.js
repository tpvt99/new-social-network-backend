(function() {
    var x = $('.c_si').children('select');
    x.on('change', function() {
        var z = $(this).val();
        if (z === 'd') {
            $('<input type="text" name="c_sex_in" class="c_sex_in" autocomplete="off" autocorrect="off" placeholder="Giới tính">').appendTo($('.c_si'));
        }
        else {
            $('.c_si').find('input').remove();
        }
    });
})();

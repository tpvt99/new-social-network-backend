$('select[name="money"]').on('change', function() {
    var z = $(this).val();
    if (z === 'no') {
        $('<input type="number" name="c_mi_in" class="c_mi_in" placeholder="Kinh phí cho 1 người tham gia (VND)">').appendTo($('.c_mi'));
    }
    else {
        $('.c_mi').children('input').remove();
    }
});
$('select[name="quantity"]').on('change', function() {
    var z = $(this).val();
    if (z === 'limited') {
        $('<input type="number" name="c_qi_i" class="c_qi_i" placeholder="Số lượng người tham gia tối đa">').appendTo($('.c_qi'));
    }
    else {
        $('.c_qi').children('input').remove();
    }
});

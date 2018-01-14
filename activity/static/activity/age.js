(function() {
var b_a = $('.c_ai').children('select:nth-child(1)');
var e_a = $('.c_ai').children('select:nth-child(2)');
var i;
for(i=10;i<=100;i++) {
    b_a.append( ['<option value="',i,'">',i,'</option>'].join(''));
}
b_a.on('change', function() {
    var i = parseInt($(this).val());
    if(i) {
        e_a.empty();
        e_a.append('<option value="">Tuổi kết thúc</option>');
        for(;i<=100;i++) {
            e_a.append( ['<option value="',i,'">',i,'</option>'].join(''));
        }
    }
});
})();

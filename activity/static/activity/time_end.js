(function() {
    var today = new Date();
    var dayx = today.getDate();
    var yearx = today.getFullYear();
    var monthx = today.getMonth() + 1;
    var hourx = today.getHours();
    var ren_yearx =  $('#c_ti1').find('select');
    var ren_monthx = $('#c_ti2').find('select');
    var ren_dayx =   $('#c_ti3').find('select');
    var ren_hourx =  $('#c_ti4').find('select');
    var ren_minutex =$('#c_ti5').find('select');
    var year_choosed, month_choosed, day_choosed;
    var ren_yearx_e =  $('#c_tie1').find('select');
    var ren_monthx_e = $('#c_tie2').find('select');
    var ren_dayx_e =   $('#c_tie3').find('select');
    var ren_hourx_e =  $('#c_tie4').find('select');
    var ren_minutex_e =$('#c_tie5').find('select');
    var year_choosed_e;

    for (var i =yearx; i <= yearx + 1; i++) {
        var l = $(['<option value="',i,'">',i,'</option>'].join(''));
        ren_yearx.append(l);
    }

    ren_yearx.on('change', function() {
        var $this = $(this);
        year_choosed = parseInt($this.val());
        if (year_choosed) {
            if (year_choosed == yearx) {
                hideDayBelow();
                ren_monthx.empty();
                ren_monthx.append( $('<option value="">Tháng</option>'));
                for (i = monthx; i <= 12; i++) {
                    var l = $(['<option value="',i,'">',i,'</option>'].join(''));
                    ren_monthx.append(l);
                }
            }
            else {
                hideDayBelow();
                ren_monthx.empty();
                ren_monthx.append( $('<option value="">Tháng</option>'));
                for (i = 1; i <= 12; i++) {
                    var l = $(['<option value="',i,'">',i,'</option>'].join(''));
                    ren_monthx.append(l);
                }
            }
            $('#c_ti2').show();
            ren_yearx_e.empty();
            ren_yearx_e.append($('<option value="">Năm</option>'));
            for (i = year_choosed; i <= year_choosed + 1; i++) {
                var l = $(['<option value="',i,'">',i,'</option>'].join(''));
                ren_yearx_e.append(l);
            }
        }
        else {
            $('#c_ti2').hide();
            ren_monthx.empty();
            hideDayBelow();
            ren_yearx_e.empty();
            ren_yearx_e.append($('<option value="">Năm</option>'));
        }

    });

    ren_yearx_e.on('change', function() {
        var $this = $(this);
        year_choosed_e = parseInt($this.val());
        if (year_choosed_e) {
            if (year_choosed == year_choosed_e && month_choosed) {
                hideDayBelowE();
                ren_monthx_e.empty();
                ren_monthx_e.append( $('<option value="">Tháng</option>'));
                for (i = month_choosed; i <= 12; i++) {
                    var l = $(['<option value="',i,'">',i,'</option>'].join(''));
                    ren_monthx_e.append(l);
                }
            }
            else if(year_choosed_e > year_choosed && month_choosed) {
                hideDayBelowE();
                ren_monthx_e.empty();
                ren_monthx_e.append( $('<option value="">Tháng</option>'));
                for (i = 1; i <= 12; i++) {
                    var l = $(['<option value="',i,'">',i,'</option>'].join(''));
                    ren_monthx_e.append(l);
                }
            }
            else {
                ren_monthx_e.empty();
                ren_monthx_e.append( $('<option value="">Tháng</option>'));
            }
            $('#c_tie2').show();
        }
        else {
            $('#c_ti2').hide();
            ren_monthx_e.empty();
            hideDayBelowE();
        }
    });

    ren_monthx.on('change', function() {
        var $this = $(this);
        month_choosed = parseInt($this.val());
        if (month_choosed) {
            if (month_choosed == 1 || month_choosed == 3 || month_choosed == 5 || month_choosed == 7 || month_choosed == 8 || month_choosed == 10 || month_choosed == 12) {
                if(month_choosed == monthx && year_choosed == yearx) {
                $('#c_ti4').hide();
                ren_hourx.empty();
                $('#c_ti5').hide();
                ren_minutex.empty();
                    ren_dayx.empty();
                    ren_dayx.append( $('<option value="">Ngày</option>'));
                    for (i = dayx; i <= 31; i++) {
                        var l = $(['<option value="',i,'">',i,'</option>'].join(''));
                        ren_dayx.append(l);
                    }
                    $('#c_ti3').show();
                }
                else {
                    $('#c_ti4').hide();
                    ren_hourx.empty();
                    $('#c_ti5').hide();
                    ren_minutex.empty();
                    ren_dayx.empty();
                    ren_dayx.append( $('<option value="">Ngày</option>'));
                    for (i = 1; i <= 31; i++) {
                        var l = $(['<option value="',i,'">',i,'</option>'].join(''));
                        ren_dayx.append(l);
                    }
                    $('#c_ti3').show();
                }
            }
            else if(month_choosed == 2) {
                var isLeap = isLeapYear(year_choosed);
                if (month_choosed == monthx && year_choosed == yearx) {
                    if (isLeap) {
                        $('#c_ti4').hide();
                        ren_hourx.empty();
                        $('#c_ti5').hide();
                        ren_minutex.empty();
                        ren_dayx.empty();
                        ren_dayx.append( $('<option value="">Ngày</option>'));
                        for (i = dayx; i <= 29; i++) {
                            var l = $(['<option value="',i,'">',i,'</option>'].join(''));
                            ren_dayx.append(l);
                        }
                        $('#c_ti3').show();
                    }
                    else {
                        $('#c_ti4').hide();
                        ren_hourx.empty();
                        $('#c_ti5').hide();
                        ren_minutex.empty();
                        ren_dayx.empty();
                        ren_dayx.append( $('<option value="">Ngày</option>'));
                        for (i =dayx; i <= 28; i++) {
                            var l = $(['<option value="',i,'">',i,'</option>'].join(''));
                            ren_dayx.append(l);
                        }
                        $('#c_ti3').show();
                    }
                }
                else {
                    if (isLeap) {
                        $('#c_ti4').hide();
                        ren_hourx.empty();
                        $('#c_ti5').hide();
                        ren_minutex.empty();
                        ren_dayx.empty();
                        ren_dayx.append( $('<option value="">Ngày</option>'));
                        for (i = 1; i <= 29; i++) {
                            var l = $(['<option value="',i,'">',i,'</option>'].join(''));
                            ren_dayx.append(l);
                        }
                        $('#c_ti3').show();
                    }
                    else {
                        $('#c_ti4').hide();
                        ren_hourx.empty();
                        $('#c_ti5').hide();
                        ren_minutex.empty();
                        ren_dayx.empty();
                        ren_dayx.append( $('<option value="">Ngày</option>'));
                        for (i = 1; i <= 28; i++) {
                            var l = $(['<option value="',i,'">',i,'</option>'].join(''));
                            ren_dayx.append(l);
                        }
                        $('#c_ti3').show();
                    }
                }
            }
            else {
                if(month_choosed == monthx && year_choosed == yearx) {
                    $('#c_ti4').hide();
                    ren_hourx.empty();
                    $('#c_ti5').hide();
                    ren_minutex.empty();
                    ren_dayx.empty();
                    ren_dayx.append( $('<option value="">Ngày</option>'));
                    for (i = dayx; i <= 30; i++) {
                        var l = $(['<option value="',i,'">',i,'</option>'].join(''));
                        ren_dayx.append(l);
                    }
                    $('#c_ti3').show();
                }
                else {
                    $('#c_ti4').hide();
                    ren_hourx.empty();
                    $('#c_ti5').hide();
                    ren_minutex.empty();
                    ren_dayx.empty();
                    ren_dayx.append( $('<option value="">Ngày</option>'));
                    for (i = 1; i <= 30; i++) {
                        var l = $(['<option value="',i,'">',i,'</option>'].join(''));
                        ren_dayx.append(l);
                    }
                    $('#c_ti3').show();
                }

            }

        }
        else {
            $('#c_ti3').hide();
            $('#c_ti4').hide();
            ren_hourx.empty();
            $('#c_ti5').hide();
            ren_minutex.empty();
        }

    });

    ren_dayx.on('change', function() {
        var $this = $(this);
        day_choosed = parseInt($this.val());
        if (day_choosed) {
            if (day_choosed == dayx) {
                $('#c_ti5').hide();
                ren_minutex.empty();
                ren_hourx.empty();
                ren_hourx.append( $('<option value="">Giờ</option>'));
                for (i = hourx + 1; i <= 23; i++) {
                    l = $(['<option value="',i,'">',i,'</option>'].join(''));
                    ren_hourx.append(l);
                }
            }
            else {
                $('#c_ti5').hide();
                ren_minutex.empty();
                ren_hourx.empty();
                ren_hourx.append( $('<option value="">Giờ</option>'));
                for (i = 0; i <= 23; i++) {
                    var l = $(['<option value="',i,'">',i,'</option>'].join(''));
                    ren_hourx.append(l);
                }
            }
            $('#c_ti4').show();
        }
        else {
            $('#c_ti4').hide();
            ren_hourx.empty();
            $('#c_ti5').hide();
            ren_minutex.empty();
        }

    });
    ren_hourx.on('change', function() {
        ren_minutex.append( $('<option value="">Phút</option>'));
        for(i = 0; i < 60; i+= 5) {
            l = $(['<option value="',i,'">',i,'</option>'].join(''));
            ren_minutex.append(l);
        }
        $('#c_ti5').show();
    });

    function isLeapYear(year) {
        if (year % 4 != 0) {
            return false;
        }
        else if (year %100 != 0) {
            return true;
        }
        else if (year % 400 != 0) {
            return false;
        }
        else {
            return true;
        }
    }
    function hideDayBelow() {
        $('#c_ti3').hide();
        ren_dayx.empty();
        $('#c_ti4').hide();
        ren_hourx.empty();
        $('#c_ti5').hide();
        ren_minutex.empty();
    }
    function hideDayBelowE() {
        $('#c_tie3').hide();
        ren_dayx.empty();
        $('#c_tie4').hide();
        ren_hourx.empty();
        $('#c_tie5').hide();
        ren_minutex.empty();
    }

})();

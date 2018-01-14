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

    for (var i =yearx; i <= yearx + 1; i++) {
        var l = $(['<option value="',i,'">',i,'</option>'].join(''));
        ren_yearx.append(l);
    }

    ren_yearx.on('change', function() {
        var $this = $(this);
        year_choosed = parseInt($this.val());
        if (year_choosed) {
            if (year_choosed == yearx) {
                ren_monthx.empty();
                ren_monthx.append( $('<option value="">Tháng</option>'));
            hideDayBelow();
                for (i = monthx; i <= 12; i++) {
                    var l = $(['<option value="',i,'">',i,'</option>'].join(''));
                    ren_monthx.append(l);
                }
            }
            else {
                ren_monthx.empty();
                ren_monthx.append( $('<option value="">Tháng</option>'));
            hideDayBelow();
                for (i = 1; i <= 12; i++) {
                    var l = $(['<option value="',i,'">',i,'</option>'].join(''));
                    ren_monthx.append(l);
                }
            }
        }
        else {
            ren_monthx.empty();
            ren_monthx.append( $('<option value="">Tháng</option>'));
            hideDayBelow();
        }

    });
    ren_monthx.on('change', function() {
        var $this = $(this);
        month_choosed = parseInt($this.val());
        if (month_choosed) {
            if (month_choosed == 1 || month_choosed == 3 || month_choosed == 5 || month_choosed == 7 || month_choosed == 8 || month_choosed == 10 || month_choosed == 12) {
                if(month_choosed == monthx && year_choosed == yearx) {
                    hideDayBelow();
                    for (i = dayx; i <= 31; i++) {
                        var l = $(['<option value="',i,'">',i,'</option>'].join(''));
                        ren_dayx.append(l);
                    }
                    $('#c_ti3').show();
                }
                else {
                    hideDayBelow();
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
                        hideDayBelow();
                        for (i = dayx; i <= 29; i++) {
                            var l = $(['<option value="',i,'">',i,'</option>'].join(''));
                            ren_dayx.append(l);
                        }
                    }
                    else {
                        hideDayBelow();
                        for (i =dayx; i <= 28; i++) {
                            var l = $(['<option value="',i,'">',i,'</option>'].join(''));
                            ren_dayx.append(l);
                        }
                    }
                }
                else {
                    if (isLeap) {
                        hideDayBelow();
                        for (i = 1; i <= 29; i++) {
                            var l = $(['<option value="',i,'">',i,'</option>'].join(''));
                            ren_dayx.append(l);
                        }
                    }
                    else {
                        hideDayBelow();
                        for (i = 1; i <= 28; i++) {
                            var l = $(['<option value="',i,'">',i,'</option>'].join(''));
                            ren_dayx.append(l);
                        }
                    }
                }
            }
            else {
                if(month_choosed == monthx && year_choosed == yearx) {
                    hideDayBelow();
                    for (i = dayx; i <= 30; i++) {
                        var l = $(['<option value="',i,'">',i,'</option>'].join(''));
                        ren_dayx.append(l);
                    }
                }
                else {
                    hideDayBelow();
                    for (i = 1; i <= 30; i++) {
                        var l = $(['<option value="',i,'">',i,'</option>'].join(''));
                        ren_dayx.append(l);
                    }
                }

            }

        }
        else {
            hideDayBelow();
        }

    });

    ren_dayx.on('change', function() {
        var $this = $(this);
        day_choosed = parseInt($this.val());
        if (day_choosed) {
            if (day_choosed == dayx) {
                hideHourBelow();
                for (i = hourx + 1; i <= 23; i++) {
                    l = $(['<option value="',i,'">',i,'</option>'].join(''));
                    ren_hourx.append(l);
                }
            }
            else {
                hideHourBelow();
                for (i = 0; i <= 23; i++) {
                    var l = $(['<option value="',i,'">',i,'</option>'].join(''));
                    ren_hourx.append(l);
                }
            }
        }
        else {
            hideHourBelow();
        }

    });
    ren_hourx.on('change', function() {
        ren_minutex.append( $('<option value="">Phút</option>'));
        for(i = 0; i < 60; i+= 5) {
            l = $(['<option value="',i,'">',i,'</option>'].join(''));
            ren_minutex.append(l);
        }
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
        ren_dayx.empty();
        ren_dayx.append( $('<option value="">Ngày</option>'));
        ren_hourx.empty();
        ren_hourx.append( $('<option value="">Giờ</option>'));
        ren_minutex.empty();
        ren_minutex.append( $('<option value="">Phút</option>'));
    }
    function hideHourBelow() {
        ren_hourx.empty();
        ren_hourx.append( $('<option value="">Giờ</option>'));
        ren_minutex.empty();
        ren_minutex.append( $('<option value="">Phút</option>'));
    }

})();

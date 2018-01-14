var year_choosed_e, month_choosed_e, day_choosed_e, hour_choosed_e;
var year_choosed, month_choosed, day_choosed, hour_choosed, minute_choosed;
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
    var ren_yearx_e =  $('#c_ti1_e').find('select');
    var ren_monthx_e = $('#c_ti2_e').find('select');
    var ren_dayx_e =   $('#c_ti3_e').find('select');
    var ren_hourx_e =  $('#c_ti4_e').find('select');
    var ren_minutex_e =$('#c_ti5_e').find('select');

    for (var i =yearx; i <= yearx + 1; i++) {
        var l = $(['<option value="',i,'">',i,'</option>'].join(''));
        ren_yearx.append(l);
    }

    ren_yearx.on('change', function() {
        var $this = $(this);
        year_choosed = parseInt($this.val());
        if (year_choosed) {
            hideBegin(y=0,m=1,d=0,h=0,mi=0);
            if (year_choosed == yearx) {
                for (i = monthx; i <= 12; i++) {
                    var l = $(['<option value="',i,'">',i,'</option>'].join(''));
                    ren_monthx.append(l);
                }
            }
            else {
                for (i = 1; i <= 12; i++) {
                    var l = $(['<option value="',i,'">',i,'</option>'].join(''));
                    ren_monthx.append(l);
                }
            }
            hideEnd(y=1,m=0,d=0,h=0,mi=0);
            ren_yearx_e.empty();
            for(i = year_choosed;i<=year_choosed+1; i++) {
                ren_yearx_e.append( $(['<option value="',i,'">',i,'</option>'].join('')));
            }
            year_choosed_e = year_choosed;
        }
        else {
            hideBegin(y=0,m=1,d=0,h=0,mi=0);
            hideEnd(y=1,m=0,d=0,h=0,mi=0);
        }

    });
    ren_yearx_e.on('change', function() {
        var $this = $(this);
        hideEnd(y=0,m=1,d=0,h=0,mi=0);
        year_choosed_e = parseInt($this.val());
        if (month_choosed) {
            if (year_choosed_e == year_choosed) {
                ren_monthx_e.empty();
                for(i=month_choosed;i<=12;i++) {
                    ren_monthx_e.append( $(['<option value="',i,'">',i,'</option>'].join('')));
                }
                month_choosed_e = month_choosed;
            }
            else {
                ren_monthx_e.empty();
                for(i=1;i<=12;i++) {
                    ren_monthx_e.append( $(['<option value="',i,'">',i,'</option>'].join('')));
                }
                month_choosed_e = 1;
            }
        }
        if (day_choosed) {
            RenderDayEnd();
        }
        if (hour_choosed || hour_choosed === 0) {
            if(year_choosed_e == year_choosed && month_choosed_e == month_choosed && day_choosed == day_choosed_e) {
                ren_hourx_e.empty();
                for(i = hour_choosed+1;i<=23;i++) {
                    ren_hourx_e.append( $(['<option value="',i,'">',i,'</option>'].join('')));  
                }
                hour_choosed_e = hour_choosed+1;
            }
            else {
                ren_hourx_e.empty();
                for(i = 0;i<=23;i++) {
                    ren_hourx_e.append( $(['<option value="',i,'">',i,'</option>'].join('')));  
                }
                hour_choosed_e = 0;
            }
        }
        if (minute_choosed || minute_choosed === 0) {
            ren_minutex_e.empty();
            for(i = 0;i<60;i+=5) {
                ren_minutex_e.append( $(['<option value="',i,'">',i,'</option>'].join('')));  
            }
        }
    });
    ren_monthx.on('change', function() {
        var $this = $(this);
        month_choosed = parseInt($this.val());
        if (month_choosed) {
            hideBegin(y=0,m=0,d=1,h=0,mi=0);
            if (month_choosed == 1 || month_choosed == 3 || month_choosed == 5 || month_choosed == 7 || month_choosed == 8 || month_choosed == 10 || month_choosed == 12) {
                if(month_choosed == monthx && year_choosed == yearx) {
                    ren_dayx.empty();
                    ren_dayx.append( $('<option value="">Ngày</option>'));
                    for (i = dayx; i <= 31; i++) {
                        var l = $(['<option value="',i,'">',i,'</option>'].join(''));
                        ren_dayx.append(l);
                    }
                }
                else {
                    ren_dayx.empty();
                    ren_dayx.append( $('<option value="">Ngày</option>'));
                    for (i = 1; i <= 31; i++) {
                        var l = $(['<option value="',i,'">',i,'</option>'].join(''));
                        ren_dayx.append(l);
                    }
                }
            }
            else if(month_choosed == 2) {
                var isLeap = isLeapYear(year_choosed);
                if (month_choosed == monthx && year_choosed == yearx) {
                    if (isLeap) {
                        ren_dayx.empty();
                        ren_dayx.append( $('<option value="">Ngày</option>'));
                        for (i = dayx; i <= 29; i++) {
                            var l = $(['<option value="',i,'">',i,'</option>'].join(''));
                            ren_dayx.append(l);
                        }
                    }
                    else {
                        ren_dayx.empty();
                        ren_dayx.append( $('<option value="">Ngày</option>'));
                        for (i =dayx; i <= 28; i++) {
                            var l = $(['<option value="',i,'">',i,'</option>'].join(''));
                            ren_dayx.append(l);
                        }
                    }
                }
                else {
                    if (isLeap) {
                        ren_dayx.empty();
                        ren_dayx.append( $('<option value="">Ngày</option>'));
                        for (i = 1; i <= 29; i++) {
                            var l = $(['<option value="',i,'">',i,'</option>'].join(''));
                            ren_dayx.append(l);
                        }
                    }
                    else {
                        ren_dayx.empty();
                        ren_dayx.append( $('<option value="">Ngày</option>'));
                        for (i = 1; i <= 28; i++) {
                            var l = $(['<option value="',i,'">',i,'</option>'].join(''));
                            ren_dayx.append(l);
                        }
                    }
                }
            }
            else {
                if(month_choosed == monthx && year_choosed == yearx) {
                    ren_dayx.empty();
                    ren_dayx.append( $('<option value="">Ngày</option>'));
                    for (i = dayx; i <= 30; i++) {
                        var l = $(['<option value="',i,'">',i,'</option>'].join(''));
                        ren_dayx.append(l);
                    }
                }
                else {
                    ren_dayx.empty();
                    ren_dayx.append( $('<option value="">Ngày</option>'));
                    for (i = 1; i <= 30; i++) {
                        var l = $(['<option value="',i,'">',i,'</option>'].join(''));
                        ren_dayx.append(l);
                    }
                }

            }
            hideEnd(y=0,m=1,d=0,h=0,mi=0);
            if (year_choosed == year_choosed_e) {
                ren_monthx_e.empty();
                for(i = month_choosed; i <= 12; i++) {
                    ren_monthx_e.append( $(['<option value="',i,'">',i,'</option>'].join('')));
                }
                month_choosed_e = month_choosed;
            } 
            else {
                ren_monthx_e.empty();
                for(i = 1; i <=12; i++) {
                    ren_monthx_e.append( $(['<option value="',i,'">',i,'</option>'].join('')));
                }
                month_choosed_e = 1;
            }
        }
        else {
            hideBegin(y=0,m=0,d=1,h=0,mi=0);
            hideEnd(y=0,m=1,d=0,h=0,mi=0);
        }

    });
    ren_monthx_e.on('change', function() {
        var $this = $(this);
        month_choosed_e = $this.val();
        RenderDayEnd();
    });
    ren_dayx.on('change', function() {
        var $this = $(this);
        day_choosed = parseInt($this.val());
        if (day_choosed) {
            hideBegin(y=0,m=0,d=0,h=1,mi=0);
            hideEnd(y=0,m=0,d=0,h=1,mi=0);
            if (day_choosed == dayx && month_choosed == monthx && year_choosed == yearx) {
                ren_hourx.empty();
                ren_hourx.append( $('<option value="">Giờ</option>'));
                for (i = hourx + 1; i <= 23; i++) {
                    l = $(['<option value="',i,'">',i,'</option>'].join(''));
                    ren_hourx.append(l);
                }
            }
            else {
                ren_hourx.empty();
                ren_hourx.append( $('<option value="">Giờ</option>'));
                for (i = 0; i <= 23; i++) {
                    var l = $(['<option value="',i,'">',i,'</option>'].join(''));
                    ren_hourx.append(l);
                }
            }
            RenderDayEnd();
        }
        else {
            hideBegin(y=0,m=0,d=0,h=1,mi=0);
            hideEnd(y=0,m=0,d=1,h=0,mi=0);
        }

    });
    ren_hourx.on('change', function() {
        hour_choosed = parseInt($(this).val());
        if(hour_choosed || hour_choosed === 0) {
            hideBegin(y=0,m=0,d=0,h=0,mi=1);
            hideEnd(y=0,m=0,d=0,h=0,mi=1);
            for(i = 0; i < 60; i+= 5) {
                l = $(['<option value="',i,'">',i,'</option>'].join(''));
                ren_minutex.append(l);
            }
            if (day_choosed_e == day_choosed && year_choosed == year_choosed_e && month_choosed == month_choosed_e) {
                ren_hourx_e.empty();
                for(i = hour_choosed+1; i <= 23; i++) {
                    l = $(['<option value="',i,'">',i,'</option>'].join(''));
                    ren_hourx_e.append(l);
                }
                hour_choosed_e = hour_choosed+1;
            }
            else {
                ren_hourx_e.empty();
                for(i = 0 ; i <= 23; i++) {
                    l = $(['<option value="',i,'">',i,'</option>'].join(''));
                    ren_hourx_e.append(l);
                }
                hour_choosed_e = 0;
            }
        }
        else {
            hideBegin(y=0,m=0,d=0,h=0,mi=1);
            hideEnd(y=0,m=0,d=0,h=1,mi=0);
        }
    });
    ren_dayx_e.on('change', function() {
        day_choosed_e = $(this).val();
        if (day_choosed_e == day_choosed && year_choosed_e == year_choosed && month_choosed == month_choosed_e) {
            ren_hourx_e.empty();
            for(i = hour_choosed+1; i <= 23; i++) {
                l = $(['<option value="',i,'">',i,'</option>'].join(''));
                ren_hourx_e.append(l);
            }
            hour_choosed_e = hour_choosed+1;
        }
        else {
            ren_hourx_e.empty();
            for(i = 0 ; i <= 23; i++) {
                l = $(['<option value="',i,'">',i,'</option>'].join(''));
                ren_hourx_e.append(l);
            }
            hour_choosed_e = 0;
        }
    });
    ren_minutex.on('change', function() {
        minute_choosed = parseInt($(this).val());
        if(minute_choosed || minute_choosed == 0) {
            ren_minutex_e.empty();
            for(i = 0; i < 60; i+= 5) {
                l = $(['<option value="',i,'">',i,'</option>'].join(''));
                ren_minutex_e.append(l);
            }
        }
        else {
            hideEnd(y=0,m=0,d=0,h=0,mi=1);
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

    function RenderDayEnd() {
        if (month_choosed_e == 1 || month_choosed_e == 3 || month_choosed_e == 5 || month_choosed_e == 7 || month_choosed_e == 8 || month_choosed_e == 10 || month_choosed_e == 12) {
           if(month_choosed_e == month_choosed && year_choosed_e == year_choosed) {
               ren_dayx_e.empty();
               for(var i = day_choosed; i <= 31; i++) {
                   ren_dayx_e.append( $(['<option value="',i,'">',i,'</option>'].join('')));
               }
               day_choosed_e = day_choosed;
           } 
           else {
               ren_dayx_e.empty();
               for(i = 1; i <= 31; i++) {
                   ren_dayx_e.append( $(['<option value="',i,'">',i,'</option>'].join('')));
               }
               day_choosed_e = 1;
           }
       }
        else if (month_choosed_e == 2) {
            var isLeap = isLeapYear(year_choosed_e);
            if (month_choosed_e == month_choosed && year_choosed_e == year_choosed) {
                if(isLeap) {
                    ren_dayx_e.empty();
                    for(i=day_choosed;i<=29;i++) {
                       ren_dayx_e.append( $(['<option value="',i,'">',i,'</option>'].join('')));
                    }
                    day_choosed_e = day_choosed;
                }
                else {
                    ren_dayx_e.empty();
                    for(i=day_choosed;i<=28;i++) {
                       ren_dayx_e.append( $(['<option value="',i,'">',i,'</option>'].join('')));
                    }
                    day_choosed_e = day_choosed;
                }
            }
            else {
                if(isLeap) {
                    ren_dayx_e.empty();
                    for(i=1;i<=29;i++) {
                       ren_dayx_e.append( $(['<option value="',i,'">',i,'</option>'].join('')));
                    }
                    day_choosed_e = 1;
                }
                else {
                    ren_dayx_e.empty();
                    for(i=1;i<=28;i++) {
                       ren_dayx_e.append( $(['<option value="',i,'">',i,'</option>'].join('')));
                    }
                    day_choosed_e = 1;
                }
            }
        }
        else {
           if(month_choosed_e == month_choosed && year_choosed_e == year_choosed) {
               ren_dayx_e.empty();
               for(i = day_choosed; i <= 30; i++) {
                   ren_dayx_e.append( $(['<option value="',i,'">',i,'</option>'].join('')));
               }
               day_choosed_e = day_choosed;
           } 
           else {
               ren_dayx_e.empty();
               for(i = 1; i <= 30; i++) {
                   ren_dayx_e.append( $(['<option value="',i,'">',i,'</option>'].join('')));
               }
               day_choosed_e = 1;
           }
        }
    }
    function hideBegin(y,m,d,h,mi) {
        if (y ==1) {
        ren_yearx.empty();
        ren_yearx.append( $('<option value="">Năm</option>'));
        ren_dayx.empty();
        ren_dayx.append( $('<option value="">Ngày</option>'));
        ren_hourx.empty();
        ren_hourx.append( $('<option value="">Giờ</option>'));
        ren_minutex.empty();
        ren_minutex.append( $('<option value="">Phút</option>'));
        ren_monthx.empty();
        ren_monthx.append( $('<option value="">Tháng</option>'));
        day_choosed = undefined;
        month_choosed = undefined;
        hour_choosed = undefined;
        minute_choosed = undefined;
        year_choosed = undefined;
        }
        if ( m == 1) {
        ren_dayx.empty();
        ren_dayx.append( $('<option value="">Ngày</option>'));
        ren_hourx.empty();
        ren_hourx.append( $('<option value="">Giờ</option>'));
        ren_minutex.empty();
        ren_minutex.append( $('<option value="">Phút</option>'));
        ren_monthx.empty();
        ren_monthx.append( $('<option value="">Tháng</option>'));
        day_choosed = undefined;
        month_choosed = undefined;
        hour_choosed = undefined;
        minute_choosed = undefined;
        }
        else if ( d == 1) {
        ren_dayx.empty();
        ren_dayx.append( $('<option value="">Ngày</option>'));
        ren_hourx.empty();
        ren_hourx.append( $('<option value="">Giờ</option>'));
        ren_minutex.empty();
        ren_minutex.append( $('<option value="">Phút</option>'));
        day_choosed = undefined;
        hour_choosed = undefined;
        minute_choosed = undefined;
        }
        else if ( h == 1) {
        ren_hourx.empty();
        ren_hourx.append( $('<option value="">Giờ</option>'));
        ren_minutex.empty();
        ren_minutex.append( $('<option value="">Phút</option>'));
        hour_choosed = undefined;
        minute_choosed = undefined;
        }
        else if (mi == 1) {
        ren_minutex.empty();
        ren_minutex.append( $('<option value="">Phút</option>'));
        minute_choosed = undefined;
        }
    }
    function hideEnd( y, m, d, h ,mi) {
        if ( y === 1) {
        ren_yearx_e.empty();
        ren_yearx_e.append( $('<option value="">Năm</option>'));
        year_choosed_e = undefined;
        ren_dayx_e.empty();
        ren_dayx_e.append( $('<option value="">Ngày</option>'));
        day_choosed_e = undefined;
        ren_hourx_e.empty();
        ren_hourx_e.append( $('<option value="">Giờ</option>'));
        hour_choosed_e = undefined;
        ren_minutex_e.empty();
        ren_minutex_e.append( $('<option value="">Phút</option>'));
        minute_choosed_e = undefined;
        ren_monthx_e.empty();
        ren_monthx_e.append( $('<option value="">Tháng</option>'));
        month_choosed_e = undefined;
        }
        else if ( m == 1) {
            ren_dayx_e.empty();
            ren_dayx_e.append( $('<option value="">Ngày</option>'));
            day_choosed_e = undefined;
            ren_hourx_e.empty();
            ren_hourx_e.append( $('<option value="">Giờ</option>'));
            hour_choosed_e = undefined;
            ren_minutex_e.empty();
            ren_minutex_e.append( $('<option value="">Phút</option>'));
            minute_choosed_e = undefined;
            ren_monthx_e.empty();
            ren_monthx_e.append( $('<option value="">Tháng</option>'));
            month_choosed_e = undefined;
        }
        else if ( d == 1) {
            ren_dayx_e.empty();
            ren_dayx_e.append( $('<option value="">Ngày</option>'));
            day_choosed_e = undefined;
            ren_hourx_e.empty();
            ren_hourx_e.append( $('<option value="">Giờ</option>'));
            hour_choosed_e = undefined;
            ren_minutex_e.empty();
            ren_minutex_e.append( $('<option value="">Phút</option>'));
            minute_choosed_e = undefined;
        }
        else if ( h == 1) {
            ren_hourx_e.empty();
            ren_hourx_e.append( $('<option value="">Giờ</option>'));
            hour_choosed_e = undefined;
            ren_minutex_e.empty();
            ren_minutex_e.append( $('<option value="">Phút</option>'));
            minute_choosed_e = undefined;
        }
        else if (mi == 1) {
            ren_minutex_e.empty();
            ren_minutex_e.append( $('<option value="">Phút</option>'));
            minute_choosed_e = undefined;
        }
    }

})();

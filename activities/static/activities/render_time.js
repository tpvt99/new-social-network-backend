(function() {var x = $('.render_time');var tz = -new Date().getTimezoneOffset()/60;x.each(function() {var hour=$(this).find('.hour');var day=$(this).find('.day');var month=$(this).find('.month');var year=$(this).find('.year');var t = new Date(Date.UTC(parseInt(year.text()),parseInt(month.text())-1,parseInt(day.text()),parseInt(hour.text())));t.setHours(t.getHours()+tz);hour.text(t.getUTCHours());day.text(t.getUTCDate());month.text(t.getUTCMonth()+1);year.text(t.getUTCFullYear());});})();
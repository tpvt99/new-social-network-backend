$('.middle_sta').on('click','.w-open', function(e) {e.preventDefault();$(this).parents('.s-co').find('.who-comm').show();$(this).remove();});$('.middle_sta').on('click','.c-choose', function() {var is_ano = $(this).data('ano');var ht = $(this).html();var pa = $(this).parents('.dropdown').find('.will-ex');pa.empty().html(ht);pa.parents('a#dLabel')[0].dataset.ano = is_ano;});$('.middle_sta').on('click', '.stat-comm', function() {$(this).parents('.stat').find('.com-in').focus();});

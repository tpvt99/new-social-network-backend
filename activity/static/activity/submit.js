$('.c_f').on('submit', function(e) {
    e.preventDefault();
    var submit = true;
    var $this = $(this);
    var form = new FormData($this[0]);
    form.append('privacy',$this.find('.c_pr1').find('span').data('pri'));
    if(form.get('c_img_in') && form.get('c_img_in').name.length > 0 ) {
        if (form.get('c_img_in').type.split('/')[0] !== 'image') {
            $('.c_img_err').html('File của bạn không đúng định dạng ảnh. Xin tải lại').show();
            submit = false;
        }
        else {
            $('.c_img_err').html('').hide();
        }
    }
    else {
        $('.c_img_err').html('Xin tải ảnh chủ đề của hoạt động').show();
        submit = false;
    }
    if(form.get('c_main_in').trim() === '') {
        $('.c_main_err').html('Chủ đề hoạt động còn trống').show();
        submit = false;
    }
    else {
        $('.c_main_err').html('').hide();
    }
    if(form.get('c_d_t').trim() === '') {
        $('.c_des_err').html('Xin nhập vào nội dung hoạt động').show();
        submit = false;
    }
    else {
        $('.c_des_err').html('').hide();
    }
    if(form.get('beg_a').trim() == '' || form.get('end_a').trim() === '') {
        $('.c_age_err').html('Bạn chưa chọn tuổi phù hợp cho người tham gia').show();
        submit = false;
    }
    else {
        $('.c_age_err').html('').hide();
    }
    if(form.get('money').trim() === 'no') {
        if(form.get('c_mi_in') && form.get('c_mi_in').trim() !== '') {
            if(parseInt(form.get('c_mi_in')) === 0) {
                $('.c_money_err').html('Xin nhập vào số tiền lớn hơn 0').show();
                submit = false;
            }
            else {
                $('.c_money_err').html('').hide();
            }
        }
        else {
            $('.c_money_err').html('Xin hãy nhập vào số tiền').show();
            submit = false;
        }
    }
    else {
            $('.c_money_err').html('').hide();
    }
    if(form.get('quantity').trim() === 'limited') {
        if(form.get('c_qi_i') && form.get('c_qi_i').trim() !== '') {
            if (parseInt(form.get('c_qi_i')) === 0) {
                $('.c_quantity_err').html('Xin hãy nhập vào số lượng lớn hơn 0').show();
                submit = false;
            } else {
                $('.c_quantity_err').html('').hide();
            }
        }
        else {
            $('.c_quantity_err').html('Xin hãy nhập và số lương người tham gia').show();
            submit = false;
        }
    }
    else {
            $('.c_quantity_err').html('').hide();
    }
    if(form.get('province').trim() !== '' && form.get('c_p_in2').trim() !== '') {
        $('.c_place_err').html('').hide();
    } else {
        $('.c_place_err').html('Xin hãy chọn và ghi địa chỉ cụ thể của hoạt động').show();
        submit = false;
    }
    if(form.get('year') && form.get('month') && form.get('day') && form.get('hour') && form.get('minute')) {
        $('.c_begin_time').html('').hide();
    } else {
        $('.c_begin_time').html('Xin hãy chọn thời gian bắt đầu hoạt động').show();
        submit = false;
    }
    if(form.get('year_e') && form.get('month_e') && form.get('day_e') && form.get('hour_e') && form.get('minute_e')) {
        $('.c_end_time').html('').hide();
    } else {
        $('.c_end_time').html('Xin hãy chọn thời gian kết thúc hoạt động').show();
        submit = false;
    }
    if($('select[name="c_sport"]')[0]) {
        if(form.get('c_sport').trim() === '') {
            $('.c_type_err').html('Xin hãy chọn môn thể thao bạn tổ chức').show();
            submit = false;
        }
        else {
            $('.c_type_err').html('').hide();
            form.append('type_of_sport_unicode', getContext('c_sport'));
        }
    }
    else if($('select[name="c_esport"]')[0]) {
        if(form.get('c_esport').trim() === '') {
            $('.c_type_err').html('Xin hãy chọn môn thể thao bạn tổ chức').show();
            submit = false;
        }
        else {
            $('.c_type_err').html('').hide();
            form.append('type_of_esport_unicode', getContext('c_esport'));
        }
    }
    else if($('select[name="c_music"]')[0]) {
        if(form.get('c_music').trim() === '') {
            $('.c_type_err').html('Xin hãy chọn 1 thể loại âm nhạc cho hoạt động ca hát của bạn');
            submit = false;
        }
        else {
            $('.c_type_err').html('').hide();
            form.append('type_of_music_unicode', getContext('c_music'));
        }
    }
    form.append('timezone', -new Date().getTimezoneOffset()/60);
    form.append('type', $('.main')[0].dataset.type);
    form.append('province_unicode',getContext('province'));
    form.append('city_unicode',getContext('city'));
    form.append('who-organize',$('input[name="who-organize"]').val());
    form.append('group-id',$('input[name="group-id"]').val());
    if(!submit) return false;
    var csrftoken = getCookie('csrftoken');$.ajaxSetup({beforeSend: function(xhr, settings) {if (!csrfSafeMethod(settings.type) && !this.crossDomain) {xhr.setRequestHeader('X-CSRFToken', csrftoken);}}});
    $.ajax({
        method : 'POST',
        url: '/activity/create/',
        processData: false,
        contentType : false,
        dataType : 'json',
        data : form,
        success : function(data) {
            if(data.a === 'ok') window.location.href = ["/activity/activity/",data.id,"/",data.head].join('');
            else alert('Có lỗi xảy ra. Xin vui lòng thử lại');
        },
    });
});

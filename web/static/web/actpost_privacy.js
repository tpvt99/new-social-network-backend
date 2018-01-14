$('.div-pri').on('click', function() {
    $(this).parents('form.actf').find('input[name="privacy"]').val($(this)[0].dataset.privacy);
    if($(this)[0].dataset.privacy === 'public') {
        $(this).parents('div.dropdown').find('.ren-pri').empty().append('<span class="fa fa-globe"></span><span style="margin-left:3px;">Công khai</span></span>');
    } else if($(this)[0].dataset.privacy == 'friend') {
        $(this).parents('div.dropdown').find('.ren-pri').empty().append('<span class="ion ion-person-stalker"></span><span style="margin-left:3px;">Bạn bè</span></span>');
    }
    else {
        $(this).parents('div.dropdown').find('.ren-pri').empty().append('<span class="fa fa-lock"></span><span style="margin-left:3px;">Riêng tư</span></span>');
    }
});

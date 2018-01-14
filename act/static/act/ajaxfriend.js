var re = [];
function AjaxFriend(x, key, except) {
    var t = $.ajax({
            method : 'GET',
            data: {'key':key, 'except':JSON.stringify(except)},
            url : '/act/ajax/friend/',
            success : function(data) {
                if(data.trim() !== ''){
                    x.empty().append(data).show();
                }else {
                    x.empty().hide();
                }
                re = [];
            }
        });
    re.push(t);
}
$('.ac-frin').on('keyup', function() {
    var $this = $(this);
    var key = $this.val();
    var x = $this.parents('.ac-friend').find('.fr-div');
    $this.attr('value',key);
    if (key) {
        for(var i =0;i<re.length;i++) {
            re[i].abort();
        }
        except = []
        $('.hiddenin').find('input[type="hidden"]').each(function() {
            except.push($(this).val());
        });
        x.empty().append("<p style='text-align:center;'><span class='fa fa-circle-o-notch fa-spin fa-fw'></span></p>").show();
        AjaxFriend(x, key, except);
    } else {
        for(var i =0;i<re.length;i++) {
            re[i].abort();
        }
        x.empty().hide();
        re = [];
    }
});
$('.fr-div').on('click', '.fr-c', function(e) {
    e.stopPropagation();
    $('.ac-frlist').append($(this).css({'border':'none','display':'inline-block','margin':'5px','padding':'2px 4px','border':'1px solid #e1e1e1'}));
    if(!$('.fr-div').find('.fr-c')[0]) $('.fr-div').hide();
    $('.hiddenin').append($(['<input type="hidden" name="hiddenfr" value="',$(this)[0].dataset.f,'">'].join('')));
});
$(document).click(function() {
    $('.fr-div').hide();
});

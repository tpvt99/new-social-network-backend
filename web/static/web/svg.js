$('img.svg').each(function() {var $img = $(this);var imgId = $img.attr('id');var imgClass = $img.attr('class');var imgURL = $img.attr('src');jQuery.get(imgURL, function(data) {var $svg = $(data).find('svg');if(typeof imgId !== 'undefined') {$svg = $svg.attr('id',imgID);}if(typeof imgClass !== 'undefined') {$svg = $svg.attr('class', imgClass + ' replaced-svg');}$svg = $svg.removeAttr('xmlns:a');$img.replaceWith($svg);}, 'xml');});
(function() {
    function e(div) {
        div.forEach(function(e) {
            document.getElementsByClassName(e)[0].style.display = "";
        });
    }
    var t = document.getElementById('nav-mess');
    var div = document.getElementsByClassName('nav-mess')[0];
    t.addEventListener('click', function() {
        document.getElementsByClassName('nav-mess')[0].style.display = "";
        e(['nav-stat','nav-search','nav-friend']);
        $.ajax({
            method : 'GET',
            url : '/message/ajax/',
            success : function(data) {
                div.innerHTML = "";
                $(div).append(data);
            }
        });
    });
})();

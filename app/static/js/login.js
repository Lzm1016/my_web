$(function () {
    $('body').particleground({
        dotColor: '#E8DFE8',
        lineColor: '#1b3273'
    });

    $('body').keydown(function () {
        if (event.keyCode == 13) {
            $('#login_button').click()
        }
    })


    $('#login_button').click(function () {
        var username = $('.username').val()
        var password = $('.passwordNumder').val()
        if (username != '' && password != '') {
            start_animation()
            var data = {"username": username, "password": password}
            $.post('/login/', data, function (data) {
                data_js = $.parseJSON(data)
                if (data_js.status) {
                    window.location.href = '/index'
                } else {
                    end_animation(data_js)
                }
            })
        } else {
            alert("用户名和密码不能为空")
        }
    })


});

var start_animation = function () {
    $('.username').attr('disabled', 'disabled')
    $('.passwordNumder').attr('disabled', 'disabled')
    $('.authent > p ').text('登录中……')
    setTimeout(function () {
        setTimeout(function () {
            $('.login').addClass('testtwo');
        }, 300);

        $('.authent').show().animate({right: -320}, {
            easing: 'easeOutQuint',
            duration: 600,
            queue: false
        });
        $('.authent').animate({opacity: 1}, {
            duration: 200,
            queue: false
        }).addClass('visible');
    }, 500);
}


var end_animation = function (data_js) {
    setTimeout(function () {
        $('.authent').show().animate({right: 90}, {
            easing: 'easeOutQuint',
            duration: 600,
            queue: false
        });
        $('.authent').animate({opacity: 0}, {
            duration: 200,
            queue: false
        }).addClass('visible');
        $('.login').removeClass('testtwo');
    }, 2000);
    setTimeout(function () {
        if (!data_js.status) {
            $('.authent > p ').text(data_js.error)
        }
    },1000)
    setTimeout(function () {
        $('.authent').css('display', 'none');
        $('.username').val('')
        $('.passwordNumder').val('')
        $('.username').removeAttr('disabled')
        $('.passwordNumder').removeAttr('disabled')
    }, 2500)
}



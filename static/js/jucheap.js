//�Զ���js
$(document).ready(function () {
    // MetsiMenu
    $('#side-menu').metisMenu();

    // �Ҳ����ʹ��slimscroll
    $('.sidebar-container').slimScroll({
        height: '100%',
        railOpacity: 0.4,
        wheelStep: 10
    });

    // Small todo handler
    $('.check-link').click(function () {
        var button = $(this).find('i');
        var label = $(this).next('span');
        button.toggleClass('fa-check-square').toggleClass('fa-square-o');
        label.toggleClass('todo-completed');
        return false;
    });

    //�̶��˵���
    $(function () {
        $('.sidebar-collapse').slimScroll({
            height: '100%',
            railOpacity: 0.9,
            alwaysVisible: false
        });
    });

    // �˵��л�
    $('#btnChangeMenu').click(function () {
        $("body").toggleClass("mini-navbar");
        SmoothlyMenu();
    });


    // ������߶�
    function fixHeight() {
        var heightWithoutNavbar = $("body > #wrapper").height() - 61;
        $(".sidebard-panel").css("min-height", heightWithoutNavbar + "px");
    }
    fixHeight();

    $(window).bind("load resize click scroll", function () {
        if (!$("body").hasClass('body-small')) {
            fixHeight();
        }
    });

    //���������
    $(window).scroll(function () {
        if ($(window).scrollTop() > 0 && !$('body').hasClass('fixed-nav')) {
            $('#right-sidebar').addClass('sidebar-top');
        } else {
            $('#right-sidebar').removeClass('sidebar-top');
        }
    });

    $('.full-height-scroll').slimScroll({
        height: '100%'
    });

    $('#side-menu>li').click(function () {
        if ($('body').hasClass('mini-navbar')) {
            NavToggle();
        }
    });
    $('#side-menu>li li a').click(function () {
        if ($(window).width() < 769) {
            NavToggle();
        }
    });

    $('.nav-close').click(NavToggle);

    //ios����������Դ���
    if (/(iPhone|iPad|iPod|iOS)/i.test(navigator.userAgent)) {
        $('#content-main').css('overflow-y', 'auto');
    }

});

$(window).bind("load resize", function () {
    if ($(this).width() < 769) {
        $('body').addClass('mini-navbar');
        $('.navbar-static-side').fadeIn();
    }
});

function NavToggle() {
    $('#btnChangeMenu').trigger('click');
}

function SmoothlyMenu() {
    if (!$('body').hasClass('mini-navbar')) {
        $('#side-menu').hide();
        setTimeout(
            function () {
                $('#side-menu').fadeIn(500);
            }, 100);
    } else if ($('body').hasClass('fixed-sidebar')) {
        $('#side-menu').hide();
        setTimeout(
            function () {
                $('#side-menu').fadeIn(500);
            }, 300);
    } else {
        $('#side-menu').removeAttr('style');
    }
}


//��������
$(function () {

    // �����˵��̶�
    $('#fixednavbar').click(function () {
        if ($('#fixednavbar').is(':checked')) {
            $(".navbar-static-top").removeClass('navbar-static-top').addClass('navbar-fixed-top');
            $("body").removeClass('boxed-layout');
            $("body").addClass('fixed-nav');
            $('#boxedlayout').prop('checked', false);

            if (localStorageSupport) {
                localStorage.setItem("boxedlayout", 'off');
            }

            if (localStorageSupport) {
                localStorage.setItem("fixednavbar", 'on');
            }
        } else {
            $(".navbar-fixed-top").removeClass('navbar-fixed-top').addClass('navbar-static-top');
            $("body").removeClass('fixed-nav');

            if (localStorageSupport) {
                localStorage.setItem("fixednavbar", 'off');
            }
        }
    });


    // �������˵�
    $('#collapsemenu').click(function () {
        if ($('#collapsemenu').is(':checked')) {
            $("body").addClass('mini-navbar');
            SmoothlyMenu();

            if (localStorageSupport) {
                localStorage.setItem("collapse_menu", 'on');
            }

        } else {
            $("body").removeClass('mini-navbar');
            SmoothlyMenu();

            if (localStorageSupport) {
                localStorage.setItem("collapse_menu", 'off');
            }
        }
    });

    // �̶�����
    $('#boxedlayout').click(function () {
        if ($('#boxedlayout').is(':checked')) {
            $("body").addClass('boxed-layout');
            $('#fixednavbar').prop('checked', false);
            $(".navbar-fixed-top").removeClass('navbar-fixed-top').addClass('navbar-static-top');
            $("body").removeClass('fixed-nav');
            if (localStorageSupport) {
                localStorage.setItem("fixednavbar", 'off');
            }


            if (localStorageSupport) {
                localStorage.setItem("boxedlayout", 'on');
            }
        } else {
            $("body").removeClass('boxed-layout');

            if (localStorageSupport) {
                localStorage.setItem("boxedlayout", 'off');
            }
        }
    });

    if (localStorageSupport) {
        var collapse = localStorage.getItem("collapse_menu");
        var fixednavbar = localStorage.getItem("fixednavbar");
        var boxedlayout = localStorage.getItem("boxedlayout");

        if (collapse == 'on') {
            $('#collapsemenu').prop('checked', 'checked')
        }
        if (fixednavbar == 'on') {
            $('#fixednavbar').prop('checked', 'checked')
        }
        if (boxedlayout == 'on') {
            $('#boxedlayout').prop('checked', 'checked')
        }
    }

    if (localStorageSupport) {

        var collapse = localStorage.getItem("collapse_menu");
        var fixednavbar = localStorage.getItem("fixednavbar");
        var boxedlayout = localStorage.getItem("boxedlayout");

        var body = $('body');

        if (collapse == 'on') {
            if (!body.hasClass('body-small')) {
                body.addClass('mini-navbar');
            }
        }

        if (fixednavbar == 'on') {
            $(".navbar-static-top").removeClass('navbar-static-top').addClass('navbar-fixed-top');
            body.addClass('fixed-nav');
        }

        if (boxedlayout == 'on') {
            body.addClass('boxed-layout');
        }
    }
});

//�ж�������Ƿ�֧��html5���ش洢
function localStorageSupport() {
    return (('localStorage' in window) && window['localStorage'] !== null)
}

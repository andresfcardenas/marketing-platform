/*jshint strict:true, browser:true, jquery:true */
// Django CSRF Handling

$.ajaxSetup({
    crossDomain: false,
    beforeSend: function(xhr, settings) {
        'use strict';

        if (!((/^(GET|HEAD|OPTIONS|TRACE)$/.test(settings.type)))) {
            xhr.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));
        }
    }
});

/**
* cookie cart
**/

function save_cart(cart_list) {
    // Actualizamos el numero en el listado de productos del carrito
    if ($.isArray(cart_list)) {
        // Almacenamos la cookie
        $.cookie('ligucart', cart_list.join(','), { path: '/', expires: 7 });
        subtotal = 0;
        quantity = 0;

        $.each(cart_list, function(index, value) {
            var element = value.split('_');
            subtotal += parseInt(element[0]) * parseInt(element[2])
            quantity += parseInt(element[0])
        });
        $('#cart_count').html(quantity);
        $('#cart_cash').html(subtotal);
    } else {
        $.cookie('ligucart', null, { path: '/', expires: -1 });
    }
}


function add_to_cart(product_code, price, num) {
    var cart_list = [];
    if ($.cookie('ligucart') === null || $.cookie('ligucart') === '' ) {
        // Crear un nuevo carrito
        $.cookie('ligucart', null, { path: '/', expires: -1 });
    } else {
        // Agregar productos al carrito actual
        cart_list = $.cookie('ligucart').split(',');
    }

    var is_added = false;
    $.each(cart_list, function(index, value) {
        var element = value.split('_');
        if (Number(element[1]) === product_code && num === undefined) {
            var cant = Number(element[0]) + 1;
            cart_list[index] = cant + '_' + product_code + '_' + price;
            is_added = true;
        }

         if(Number(element[1]) === product_code && !isNaN(num)){
            cart_list[index] = num + '_' + product_code + '_' + price;
            is_added = true;
        }
    });
    if (!is_added) {
        cart_list.push('1_' + product_code + '_' + price);
    }

    save_cart(cart_list);
}

$(function() {
    // Mostramos la cantidad de productos del carrito
    if ($.cookie('ligucart') !== null && $.cookie('ligucart') !== '' ) {
        cart_list = $.cookie('ligucart').split(',');
        subtotal = 0;
        quantity = 0;

        $.each(cart_list, function(index, value) {
            var element = value.split('_');
            subtotal += parseInt(element[0]) * parseInt(element[2])
            quantity += parseInt(element[0])
        });

        $('#cart_count').html(quantity);
        $('#cart_cash').html(subtotal);
    }

    // Agregar al carrito
    $('#add_to_cart').click(function(e) {
        e.preventDefault();
        if ($(this).data('code') !== undefined && $(this).data('price') !== undefined) {
            $(this).hide();
            $(this).find('span').text('Agregado').end().removeAttr('data-code').removeAttr('data-price').show('slow');
            add_to_cart($(this).data('code'), $(this).data('price'));
        }
    });
});

// Open the login colorbox
$('.cbox_login').colorbox();

// Open the register colorbox
$('.cbox_register').colorbox();

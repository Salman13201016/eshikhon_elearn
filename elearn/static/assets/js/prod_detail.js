



$(document).ready(function () {
    value_quant = 0
    price = parseFloat($('.price').text())
    main_price = parseFloat($('.price-strike').text())
    $('.count').text($('.quant-input input').val())
    $('.total-price .value').text(price)

    // alert(price)
    $('.plus').click(function () {
        value_quant = $('.quant-input input').val()
        console.log(value_quant)
        value_quant = parseInt(value_quant) + 1
        if (value_quant > 5) {
            value_quant = 5
            $('.quant-input input').val(5)
            // $('.count').text(5)
        }
        else {
            $('.quant-input input').val(value_quant)
            // $('.count').text(value_quant)
        }
        // price1 = price * value_quant
        // price2 = main_price * value_quant
        // // // alert(price1)
        // $('.total-price .value').text(price1)
        // $('.price-strike').text(price2)


    });

    $('.minus').click(function () {

        value_quant = $('.quant-input input').val()
        value_quant = parseInt(value_quant) - 1
        if (value_quant < 1) {
            value_quant = 1
            $('.quant-input input').val(1)
            // $('.count').text(1)
        }
        else {
            $('.quant-input input').val(value_quant)
            // $('.count').text(value_quant)
        }
        // price1 = price * value_quant
        // price2 = main_price * value_quant
        // // // alert(price1)
        // $('.total-price .value').text(price1)
        // $('.price-strike').text(price2)

    });

    $('body').on('click', '.add_to_cart', function () {
        console.log("yes")
        value_quant = $('.quant-input input').val()
        $('.count').text(value_quant)
        price1 = price * value_quant
        price2 = main_price * value_quant
        // // alert(price1)
        $('.total-price .value').text(price1)
        // $('.price-strike').text(price2)


    });
});
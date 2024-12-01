



function operation(num,productId) {

    var itemquantity = document.getElementById("quantity-"+productId)

    itemquantity.value = num + parseInt(itemquantity.value)

    if (itemquantity.value < 1) {

        itemquantity.value = 1
    }

    if (itemquantity.value > 12) {

        itemquantity.value = 12
    }
}


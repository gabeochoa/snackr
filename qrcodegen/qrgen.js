var body = null, itemlist = null, shoppingcart = [];

window.onload = function() {
    body = document.getElementsByTagName('body');
    if (body == null) { alert('body is null'); }
    var itemlist = document.getElementById('itemlist');
    if (itemlist == null) { alert('itemlist is null'); }
    document.getElementById('genQRCode').onclick = function(e) {
        e.preventDefault();
        var urlToEncode = JSON.stringify(shoppingcart);
        var finalURLforGET =
            "https://chart.googleapis.com/chart?cht=qr&chs=64x64&chl=" + urlToEncode;
        console.log(finalURLforGET);
        window.location = finalURLforGET;
    }
    document.getElementById('addItem').onclick = function(e) {
        e.preventDefault();
        var itemname = document.getElementById('itemname').value;
        var dateofpurchase = document.getElementById('dateofpurchase').value;
        var dateofexpiration = document.getElementById('dateofexpiration').value;
        var quantity = document.getElementById('quantity').value;
        if (itemname == '' ||
            dateofpurchase == '' ||
            dateofexpiration == '' ||
            quantity == '') {
            alert("All fields required.");
            return;
        }
        shoppingcart.push({name:itemname, purchased:dateofpurchase,
                           expired:dateofexpiration, amount:quantity});
        var node = document.createElement("LI");
        var newInputCheckBox = document.createElement('input');
        newInputCheckBox.type = 'checkbox';
        newInputCheckBox.setAttribute('checked', 'checked');
        var nameOfItem = itemname;
        newInputCheckBox.id = 'id' + nameOfItem;
        var newInputLabel = document.createElement('label');
        newInputLabel.innerHTML = nameOfItem + "<br>bought: " 
                                  + dateofpurchase + "<br>expiring: " +
                                  dateofexpiration + "<br>amount: " +
                                  quantity;
        node.appendChild(newInputCheckBox);
        node.appendChild(newInputLabel);
        itemlist.appendChild(node);
    }
}

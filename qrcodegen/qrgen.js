var body = null, itemlist = null, shoppingcart = [];

window.onload = function() {
    body = document.getElementsByTagName('body');
    if (body == null) { alert('body is null'); }
    var itemlist = document.getElementById('itemlist');
    if (itemlist == null) { alert('itemlist is null'); }
    document.getElementById('genQRCode').onclick = function(e) {
        e.preventDefault();
        var urlToEncode = "https://snackr.herokuapp.com/add/" + btoa(JSON.stringify(shoppingcart));
        var finalURLforGET =
            "https://chart.googleapis.com/chart?cht=qr&chs=64x64&chl=" + urlToEncode;
        console.log(finalURLforGET);
        window.location = finalURLforGET;
    }
    document.getElementById('addItem').onclick = function(e) {
        e.preventDefault();
        var itemname = document.getElementById('itemname').value;
        var quantity = document.getElementById('quantity').value;
        if (itemname == '' ||
            quantity == '') {
            alert("All fields required.");
            return;
        }
        shoppingcart.push({name:itemname, amount:quantity});
        var node = document.createElement("LI");
        var nameOfItem = itemname;
        var newInputLabel = document.createElement('label');
        newInputLabel.innerHTML = nameOfItem + "<br>amount: " + quantity;
        node.appendChild(newInputLabel);
        itemlist.appendChild(node);
    }
}

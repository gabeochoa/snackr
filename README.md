# snackr

Have you ever wanted to keep track of what goes in and out of your fridge and
pantry? Snackr will keep track of it all for you so food won't get forgotten
or spoiled, especially if your fridge is full or shared with friends.

Snackr requires a grocery store to output a QR code on the customer receipt
representing the information about the items purchased.
Using a QR scanner, a client can use our web app to update a live inventory of
their digital pantry online, see what they have left (instead of digging
through the freezer), and update what they've eaten.

Features:
* none

Todo: 

* [x] QR Code Generation
* [x] Create Sample Inv
* [ ] Read Codes
* [ ] Codes call API
* [x] Database I/O
* [ ] Add / Delete Items
* [ ] Logged out UI
* [ ] Logged in UI
* [ ] Inv UI

Stretch Goals:

* [ ] Notifications (upcoming expirations)
* [ ] Shared Accounts (Items have owners)
* [ ] Fix URL Length problem (QR codes only support ~4k alphabetic/numeric
      characters. A solution would be for the grocery distributor to maintain
      a service that logs customer purchases. Instead of encoding information
      about the purchase inside the QR code, the QR code contains a purchase ID
      that when scanned will ping the grocer to find the purchase from the ID
      and forward the items to our web service.)

Food
* Name
* Image
* Date of Purchase
* Expiration
* Number of Items

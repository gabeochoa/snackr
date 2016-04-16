import urllib

# Input JSON to generate qr code

qrdata = "12345"
qrfilename = qrdata + ".png"

urllib.urlretrieve("https://api.qrserver.com/v1/create-qr-code/?data=" + qrdata + "&size=320x320", qrfilename)

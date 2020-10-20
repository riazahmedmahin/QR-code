import pyqrcode
import png
from pyqrcode import QRCode
mystring="riazahmedmahin@gmail.com"
qr= pyqrcode.create(mystring)
qr.png("qrcode.png",scale=7)
qr.svg("qrcode.svg",scale=10)




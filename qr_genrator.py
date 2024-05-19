import pyqrcode 
from pyqrcode import QRCode 
  
# String which represent the QR code 
s = "https://web.telegram.org/k/"
  
# Generate QR code 
url = pyqrcode.create(s) 
  
# Create and save the png file naming "myqr.png" 
url.svg("telegram.svg", scale = 8)
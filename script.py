import pyqrcode
from PIL import Image

#variable definitions
logoWidth=100       #change this to enlarge/reduce logo size
string='https://www.facebook.com/HolyFamilyKajang/'         #url to be embedded
logoString='logo.png'       #path to intended logo location
out='qrcode.jpg'        #save name and format as jpg


#generate qr code, open, obtain width and height of qrcode
url=pyqrcode.QRCode(string)
url.png('test.png',scale=10) #save qrcode as test.png
im=Image.open('test.png') #open saved qrcode
im=im.convert("RGBA")
width,height = im.size


#open logo image, crop and paste logo
logo=Image.open(logoString)
leftUpBorder = int((width-logoWidth)/2)
rightBottomBorder = int((width+logoWidth)/2)
box=(leftUpBorder,leftUpBorder,rightBottomBorder,rightBottomBorder) #logo placement. take (qrcode size-logo size)/2 , (qrcode size+logo size)/2
im.crop(box)
logo= logo.resize((logoWidth,logoWidth)) #set logo size
im.paste(logo,box) #place logo
#im.show()
im.save(out)

import qrcode
s=input("Enter the link:")
img1=qrcode.make(s)
img1.show()
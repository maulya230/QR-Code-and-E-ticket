import qrcode
import png
# img=qrcode.make("https://www.google.com/")
# img.save("images/1.jpg")

# img=qrcode.make("7777047796")
# img.save("images/visitor1.jpg")

a=["ABZ","BQR","CZS","XYZ"]
for i in a:
    img=qrcode.make(i)
    name="images/"+str(i)+".png"

    img.save(name,"png")
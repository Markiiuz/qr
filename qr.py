import qrcode
import io

def startText():
    print("QR Code creator")
    print("By Markiiuz - https://github.com/Markiiuz")

def inputReader():
    global name
    global age
    global city

    print("Name?: ")
    name = input()

    print("Age?: ")
    age = input()

    print("City?:")
    city = input()

def qrCreate():
    global qr
    qr = qrcode.QRCode()
    qr.add_data("Name: " + name)
    qr.add_data(" Age: " + age)
    qr.add_data(" City: " + city)


def qrPrint():

    f = io.StringIO()
    qr.print_ascii(out=f)
    f.seek(0)
    print(f.read())

startText()
inputReader()
qrCreate()
qrPrint()
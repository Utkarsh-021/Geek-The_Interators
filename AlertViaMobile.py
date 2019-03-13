import serial
import time
import pymysql
import geocoder

class PhoneLib:
    def ConnectDevice(self, port):                   #function called for establishing the connection
        self.sp = serial.Serial(port, 9600, timeout=5)       #re-Establishment of connection after 5s of in activity

    def Dial(self, phoneno):                                 #Calling done from the server side to the patient
        self.sp.write("AT\r".encode())
        time.sleep(2)
        cmd = "ATD{};\r".format(phoneno).encode()
        print(cmd)
        self.sp.write(cmd)
        time.sleep(5)

    def HangUp(self):                                           #Breeaaking the Connection
        self.sp.write("ATH\r".encode())

    def SendSmsOTP(self, ph, msg):                               #Sending the message for OTP Purposes...
        cmd = "AT+CMGF=1\r".encode();
        self.sp.write(cmd)
        time.sleep(1)
        cmd = "AT+CMGS=\"{}\"\r".format(ph).encode()
        self.sp.write(cmd)
        time.sleep(2)
        m = "Your One-Time-Password for the given transition is" + msg + ".It is valid for 5 minutes..."
        cmd = "{}{}\r".format(m, chr(26)).encode()
        self.sp.write(cmd)
        time.sleep(5)

    def SendSmsHELP(self, ph, msg):                               #For help sending the message...
        cmd = "AT+CMGF=1\r".encode();
        self.sp.write(cmd)
        time.sleep(1)
        cmd = "AT+CMGS=\"{}\"\r".format(ph).encode()
        self.sp.write(cmd)
        time.sleep(2)
        if (ph in """Directory"""):
            m="I need Help.. My Location is:-"+g.latlng+"Come As soon as possible..."
            cmd = "{}{}\r".format(m, chr(26)).encode()
            self.sp.write(cmd)
        else:
            print("You are not registered....")
        time.sleep(5)


    def InitReadSms(self):                                    #Method for encoding the recieved message
        self.sp.write("AT+CNMI=1,2,0,0,0\r".encode())
        time.sleep(1)

    def ReadSms(self):                                           #Message Sent is Readed at server side
        data = self.sp.readline()
        info = data.decode()
        if (info.startswith("+CMT")):
            d = info.split("\"")
            print(d[1], d[5])
            data = self.sp.readline()
            print(data.decode())
        time.sleep(1)

    def CloseDevice(self):
        self.sp.close()


P = PhoneLib()
P.ConnectDevice("COM5")                            #For Establishing connectiong with specified driver
ph = input("Enter Phone No:")                      #Number to which alert is to be sent
P.Dial(ph)                                         #calling the specified number
v = ""                                             #Generating OTP for verification purposes
for i in range(5):
    t = random.randint(0, 9)
    v = v + str(t)

g = geocoder.ip('me')
P.SendSmsHELP("--Your Number--",g)

P.SendSmsOTP("--Your Number--", v)
P.InitReadSms()
while (True):
    P.ReadSms()
input()

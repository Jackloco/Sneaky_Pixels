from PIL import Image
import os
import math

enPic = ("C:/Users/iD Student/Desktop/Jackson M/encodedPic.png")
enPic = Image.open("C:/Users/iD Student/Desktop/Jackson M/encodedPic.png")
width, height = enPic.size
enPixels = enPic.getdata()

enBacon = { '00000' : 'A' ,'00001' : 'B','00010' : 'C', '00011' : 'D' , '00100' : 'E' , '00101' : 'F', '00110' : 'G', '00111' : 'H', '01000':'I','01001':'J','01010':'K','01011':'L','01100':'M','01101':'N','01110':'O','01111':'P','10000':'Q','10001':'R','10010':'S','10011':'T','10100':'U','10101':'V','10110':'W','10111':'X','11000':'Y','11001':'Z','11011':' '}
decrypted = ""
conglom = ""

print("Decrypting...")
for index, px in enumerate(enPixels):##looking at current pixel to change the last several set of digits
    try:##keeps doing this until the program crashes
        if conglom == '11111':
            print(decrypted)
            print("Decryption complete with no artifacts")
            break

        if len(conglom) == 5:
            decrypted+=(enBacon[conglom]) ##adds the ones and zeroes from the dict to decrypted
            conglom = ""
            
        if px[2] %2 == 0:#even
            conglom += "1"
        else:
            conglom += "0"

    except:##now, yes, i could've used an if statement looking for 11111 but i have not used this method before and i wanted to use it :D
        print (decrypted)
        print("Decryption complete with some artifacts")
        break

from PIL import Image
import os
import math

pictureName = input("Please put the name of the png that is within the same folder of this script: ")

pic = ("C:/Users/iD Student/Desktop/Jackson M/"+ pictureName +".png")
pic = Image.open("C:/Users/iD Student/Desktop/Jackson M/"+pictureName+".png")
width, height = pic.size
pixels = pic.getdata()


bacon = { 'A' : '00000' , 'B' : '00001' , 'C' : '00010' , 'D' : '00011' , 'E' : '00100' , 'F' : '00101', 'G' : '00110', 'H' : '00111', 'I':'01000','J':'01001','K':'01010','L':'01011','M':'01100','N':'01101','O':'01110','P':'01111','Q':'10000','R':'10001','S':'10010','T':'10011','U':'10100','V':'10101','W':'10110','X':'10111','Y':'11000','Z':'11001',' ':'11011'}
baconed = ""

print("With the current image, the amount of characters available for use is:" , math.floor(height * width / 5) )
message = input("What is your message?: ")
message = message.upper()##upper case, very important

print (message)
for eachLetter in message:
    baconed+=(bacon[eachLetter]) ##adds the ones and zeroes from the dict to baconed

##print(baconed)

i=0
a=0
c=0
counter = 0
for b in baconed:

    a+=1
    x=i%width
    y=math.floor(i/width)
    px=pixels[i]    

    if b == '0': ##if the baconed is zero, so it needs to be turned odd px[2] needs to be odd
        if px[2] %2 == 0: ##checks to see if the blue pixel is even
            if px[2]!=0:
                upPx= (px[0],px[1],(px[2]-1))##reduces the blue pixel by 1
                pic.putpixel((x,y),upPx)##places the pixel
            else:
                upPx= (px[0],px[1],(px[2]+1))##Increases the blue pixel by 1
                pic.putpixel((x,y),upPx)##places the pixe
                         
    else: #if the baconed is 1, so px[2] needs  to be even
        if px[2] %2 ==1: ##checks if it is odd
            upPx= (px[0],px[1],(px[2]-1))##reduces the blue pixel by 1
            pic.putpixel((x,y),upPx)##places the pixel

    while a >=len(baconed) and c<=5:##a is another counter because i wouldnt work because it would never trigger. c is set to stop at 5
        i+=1##was editing the last actual baconed, so needs to be first to change it one plus. Also, is here because i dont think it can talk to the other bunch on the top of the for loop because it's technically done
        x=i%width
        y=math.floor(i/width)
        px=pixels[i]##from top  
        if px[2] %2 ==1: ##checks if it is odd
                upPx= (px[0],px[1],(px[2]-1))##reduces the blue pixel by 1
                pic.putpixel((x,y),upPx)##places the pixel
        c+=1##localized counter to make sure it only runs 5 times. this is not a hard code because it needs 5 because this is the designated end combonation
        
    i+=1

        
print("Saving")
pic.save("encodedPic.png")
print("Picture saved into this file directory")


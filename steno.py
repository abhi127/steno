
from PIL import Image

def getkey(img):
    key = (input("Enter the 4 digit key code for encoding Or Enter for default\n> "))
    if(1<len(key)>4):
        raise ValueError('key is out of specified lenth')
    if (key == ''):
        key = gcd(img.size)
    return key
    
def gcd(ig):
        x,y = ig
        while(y):
            x, y = y, x % y
        return(x)

def gen(dt):
    newdata = []
    for i in dt:
        newdata.append(format(ord(i),'08b'))
    return newdata

def enc(img,DT):
    data=gen(DT)
    dlen = len(data)
    
    pix=[]
    imdata = iter(img.getdata())
    
    key =str(getkey(img))
    
    z = 0
    while z<dlen:
        for i in key:
            if(z>=dlen):break;
            for _ in range(int(i)):
                if(z>=dlen):break;
                pix.append(imdata.__next__())
                
            
            temp = [value for value in imdata.__next__()[:3] + imdata.__next__()[:3] + imdata.__next__()[:3]]
            
            for j in range(0,8):
                if (data[z][j] == '0' and temp[j]% 2 != 0):
                    temp[j] -= 1

                elif(data[z][j] == '1') and (temp[j]%2 == 0):
                    if(temp[j] != 0):
                        temp[j] -= 1
                    else:
                        temp[j] += 1
            z += 1
            temp = tuple(temp)
            
            pix.append(tuple(temp[0:3]))
            pix.append(tuple(temp[3:6]))
            pix.append(tuple(temp[6:9]))
            
        
    
    w = img.size[0]
    (x, y) =(0, 0)
    for pixel in pix:
        img.putpixel((x, y),pixel)
        if (x == w-1):
            x = 0
            y += 1
        else:
            x += 1
    new_img_name = input("Enter the name of new image(with extension) : ")
    try:
        img.save(new_img_name, str(new_img_name.split(".")[1].upper()))
    except:
        print(">ERROR !!Please check for supported format!! ")

    
def decode():
    m = input("Enter the path for decoding of image(Realative or absolute with extension)\n>")
    try:
        im = Image.open(m,'r')
    except IOError:
        print("Please check the path !!try again!!\n>")
        decode()
    img = im.getdata()
    imdata = iter(img)
    key = getkey(im)
    data = ''
    while True:
        for i in key:
            for _ in range(int(i)):
                imdata.__next__()
            temp = [value for value in imdata.__next__()[:3] + imdata.__next__()[:3] + imdata.__next__()[:3]]
            
            bstr =''
            for b in temp[0:8]:
                if(b % 2 == 0):
                    bstr +='0'
                else:
                    bstr +='1'
            data+= chr(int(bstr,2))
            if (len(data)>4):
                if data[len(data)-4:len(data)]=='*#*#':
                    return data[4:len(data)-4]


            
def encode():
    m = input("Enter the path for image(Realative or absolute with extension)\n>")
    try:
        im = Image.open('image.jpg','r')
    except IOError:
        print("Please check the path !!try again!!\n>")
        encode()
    data = input("Enter the data\n>")
    if (len(data)==0):
            raise ValueError('data is empty')
    data = "#*#*" + data + "*#*#"        
    newimg = im.copy()
    enc(newimg,data)
    
        
        
        

def main(): 
	a = int(input(":: Welcome to Steganography ::\n"
						"1. Encode\n2. Decode\n>")) 
	if (a == 1): 
		encode() 
		
	elif (a == 2): 
		print("Decoded word- " + decode()) 
	else: 
		raise Exception("Enter correct input")
    
if __name__=='__main__':
    main()

   

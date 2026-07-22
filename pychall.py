import urllib.request
from icecream import ic
from functools import reduce
from collections import Counter
import urllib


def zero():
    print(pow(2,38))


def helperOne(a):
    a = chr(ord(a)+2)
    return a

def one():
    with open('text1.txt', 'r') as f:
        data = f.read()
        #newData = list(map(helperOne, data))
        x="abcdefghijklmnopqrstuvwxyz"
        y="cdefghijklmnopqrstuvwxyzab"
        text = data.translate(str.maketrans(x,y))
        #ic(text)
        data = 'map'
        text = data.translate(str.maketrans(x,y))
        ic(text)



def two():
    with open('text2.txt', 'r') as f:
        data = Counter(f.read())
        ic(data.most_common())


def helperThree(x, i, counter):
    try:
        x[i]
    except:
        return False
    if(counter==0):
        #find ascii characters with values between 97 - 122 for lower case
        if (ord(x[i])<122 and ord(x[i])>97):
            return helperThree(x,i+1,counter+1)
        else: return False
    if(counter==8):
        if (ord(x[i])<122 and ord(x[i])>97):
            return True
        else: return False
    if (counter == 4):
        if (ord(x[i])<122 and ord(x[i])>97):
            return helperThree(x,i+1,counter+1)
        else: return False
    #find ascii characters with values between 65 - 90 for upper case
    if (ord(x[i])<90 and ord(x[i])>65):
        return helperThree(x,i+1,counter+1)
    
    return False

def three():
    with open('text3.txt', 'r') as f:
        data = f.read()
        text = ''
        for i, v in enumerate(data):
            if(helperThree(data,i,0)):
                text = text+data[i+4]
                print(data[i+0] + data[i+1] + data[i+2] + data[i+3] + data[i+4] + data[i+5] +\
                   data[i+6] + data[i+7] + data[i+8] + '--\n')

        ic(text)


def four():
    ic(urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php'))



def main():
    zero()

if __name__ == "__main__":
    main()

#Password generator using python
#Code By Vasant
import string
import random

s1=string.ascii_lowercase
s2=string.ascii_uppercase
s3=string.digits
s4=string.punctuation
s=[]
s.extend(list(s1))
s.extend(list(s2))
s.extend(list(s3))
s.extend(list(s4))
random.shuffle(s)
psw=int(input('Enter length of your password \n'))
if(psw<8):
    print('For strong password length should be greater than 8')
else:
    print("Your Newly Generated Password is :")
    print((''.join(s[0:psw])))

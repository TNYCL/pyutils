import random
import string

class Password:
    def __init__(self, length, r1=[], r2=[], r3=[]):
        chars = '{}{}'.format(string.ascii_letters, 
        string.digits)
        for i in range(length):
            if(len(r1) < length/4):
                r1.append(random.choice(chars))
                r2.append(random.choice(chars))
                r3.append(random.choice(chars))
            if(i == length-1):
                output = 'TNYCL-{}{}-{}.'.format(''.join(r1), ''.join(r2), ''.join(r3))
        self.password = ''.join(output)

try:
    length = int(input('Length: '))
except Exception:
    exit('You can use only digits chars.')
password = Password(length).password
print('\nCreated password is: {}'.format(password))
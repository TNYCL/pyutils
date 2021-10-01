class Encrypt:
    def __init__(self, text, value, output=''):
        for char in text:
            output = '{}{}'.format(output, chr(ord(char) + value))
        self.output = output

incrementLevel = 25

text = input('Text: ')
print('Encrypting...')
exit(Encrypt(text, incrementLevel).output)
class Decrypt:
    def __init__(self, text, value, output=''):
        for char in text:
            output = '{}{}'.format(output, chr(ord(char) - value))
        self.output = output

increment_level = 25

text = input('Decrypt olacak metin: ')
print('Decrypting...')
exit(Decrypt(text, increment_level).output)
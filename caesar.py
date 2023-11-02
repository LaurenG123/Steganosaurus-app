import string
class Caesar:
    def __init__(self, shift):
        self.shift = shift
        
    # takes message and returns encrypted message using shift defined above
    def encrypt(self,msg):
        if msg.isalpha() and int(self.shift) >= 0 and int(self.shift) < 26:
            alphabet = string.ascii_lowercase
            shifted_alphabet = alphabet[int(self.shift):] + alphabet[:int(self.shift)]
            table = str.maketrans(alphabet, shifted_alphabet)
            return msg.translate(table)
        else:
            return "invalid input"

    # takes encrypted message and returns plaintext using shift defined above
    def decrypt(self,msg):
        if msg.isalpha() and int(self.shift) >= 0 and int(self.shift) < 26:
            alphabet = string.ascii_lowercase
            shifted_alphabet = alphabet[26-int(self.shift):] + alphabet[:26-int(self.shift)]
            table = str.maketrans(alphabet, shifted_alphabet)
            return msg.translate(table)
        else:
            return "invalid input"
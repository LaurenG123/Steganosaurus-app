class Caesar:
    def __init__(self, shift):
        self.shift = shift
        
    # takes message and returns encrypted message using shift defined above
    def encrypt(self,msg):
        alphabet = string.ascii_lowercase
        shifted_alphabet = alphabet[self.shift:] + alphabet[:self.shift]
        table = string.maketrans(alphabet, shifted_alphabet)
        return msg.translate(table)

    # takes encrypted message and returns plaintext using shift defined above
    def decrypt(self,msg):
        alphabet = string.ascii_lowercase
        shifted_alphabet = alphabet[26-self.shift:] + alphabet[:26-self.shift]
        table = string.maketrans(alphabet, shifted_alphabet)
        return msg.translate(table)

from PIL import Image
import stepic
import requests
from bs4 import BeautifulSoup
class bookCipher:
    def __init__(self, book):
        with open(book, 'r',encoding='utf-8') as book_doc:
            self.book_to_encode = book_doc.read().lower().split()
    def encrypt(self, message):
        encryption = ''
        words = message.lower().split()
        for word in words:
            try:
                word_index = self.book_to_encode.index(word)
                encryption += str(word_index) + ' '
            except:
                print(f"('{word}' not in text)")
                for letter in words:
                        encryption += "* "

        return encryption
    def decrypt(self, encrypted):
        decrypted = ''
        code = encrypted.split()
        for number in code:
            if number == ' ':
                decrypted += ' '
            else:
                try:
                    int(number) == self.book_to_encode[int(number)]
                    decrypted += self.book_to_encode[int(number)] + ' '
                except:
                    print(f"('{number}' not in text)")
                    decrypted += number + ' '

        return decrypted
class steganography:
    def __init__(self, image_path='saved_image.png'):
        self.image_path = image_path

    def steg_encrypt(self, message):
        try:

            image = Image.open(self.image_path)
            message_bytes = message.encode('utf-8')
            encoded_img = stepic.encode(image, message_bytes)
            encoded_img.save("saved_image.png")

        except Exception as e:
            print(f"Error during steg_encrypt: {e}")

    def steg_decrypt(self):
        try:
            image = Image.open(self.image_path)
            decoded_msg = stepic.decode(image)
            return decoded_msg
        except Exception as e:
            print(f"Error during steg_decrypt: {e}")
def enter_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')
        text_content = ' '.join(soup.stripped_strings)
        words = text_content.split()[:500]
        extracted_text = ' '.join(words)

        with open('downloaded_content.txt', 'w', encoding='utf-8') as file:
            file.write(extracted_text)
        print('Content saved to downloaded_content.txt')
    except requests.exceptions.RequestException as e:
        print(f'Error fetching content: {e}')
    except Exception as e:
        print(f'Error saving content: {e}')
def goo(secret_message):
    try:
        book = 'downloaded_content.txt'
        book_cipher_key = bookCipher(book)
        encrypted_message = book_cipher_key.encrypt(secret_message)
        steg = steganography()
        steg.steg_encrypt(encrypted_message)
        print("Image successfully encrypted")

    except Exception as e:
        print(f"Error in goo function: {e}")
def goop():
    try:
        book = 'downloaded_content.txt'
        uncode_message = steganography(image_path='saved_image.png').steg_decrypt()
        decrypted_message = bookCipher(book).decrypt(uncode_message)

        return decrypted_message

    except Exception as e:
        print(f"Error in goop function: {e}")
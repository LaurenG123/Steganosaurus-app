from imports import *
from steg_funcs import *
from caesar import *
from android.permissions import request_permissions, Permission
request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE, Permission.INTERNET])
class LoadingScreen(Screen):
    pass
class CaesarMultiplex(Screen):
    pass
class WelcomeScreen(MDScreen):
    pass
class EncryptType(MDScreen):
    pass
class CaesarEncrypt(MDScreen):
    def encrypt(self):
        shifter = Caesar(self.ids.shift.text)
        self.ids.output.text = "Your Result: " + shifter.encrypt(self.ids.plaintext.text)
class CaesarDecrypt(MDScreen):
    def decrypt(self):
        shifter = Caesar(self.ids.shift.text)
        self.ids.output.text = "Your Result: " + shifter.decrypt(self.ids.plaintext.text)
class ChooseMethod(MDScreen):
    pass
class Uploader(MDScreen):
    def open(self, path, filename):
        if filename:
            selected_image_path = os.path.join(path, filename[0])
            self.ids.image_view.source = selected_image_path
        else:
            self.ids.image_view.source = ''

    def save_image(self, filename):
        if not filename:
            print("No file selected to save.")
            return

        selected_image_path = filename[0]
        destination_path = os.path.join(os.getcwd(), 'saved_image.png')

        try:
            shutil.copy(selected_image_path, destination_path)
            print(f"Image saved to: {destination_path}")
        except Exception as e:
            print(f"Error saving image: {str(e)}")

    def selected(self, filename):
        if filename:
            print("Selected: %s" % filename[0])
        else:
            print("No file selected")
class Downloader(MDScreen):

    def selectedpath(self, selection):
        if not selection:
            return

        selected_path = selection[0]
        if os.path.isdir(selected_path):

            print("Selected directory:", selected_path)
        else:

            print("Selected file:", selected_path)

    def download_image(self, instance):

        source_image_path = "saved_image.png"

        if not self.ids.file_chooser_download.selection:
            print("Please select a destination directory.")
            return

        destination_directory = self.ids.file_chooser_download.selection[0]
        destination_image_path = os.path.join(destination_directory, "HERE.png")

        try:
            shutil.copy(source_image_path, destination_image_path)
            print(f"Image copied to: {destination_image_path}")
        except Exception as e:
            print("Error copying image:", e)
class Encrypter(MDScreen):

    def download_and_save(self):
        url = self.ids.url_input.text
        enter_url(url)
    def enter_message(self):
        secret_message = self.ids.secret_message.text
        goo(secret_message)
class Decrypter(MDScreen):

    def enter_url_key(self):
        url = self.ids.url_decrypt.text
        enter_url(url)
class SecretsScreen(MDScreen):

    def discovery(self):
        decryptedmessage = goop()
        if decryptedmessage:
            self.ids.decrypted_label.text = decryptedmessage
        else:
            self.ids.decrypted_label.text = "Please upload an image"

class Stegmain(MDApp):

    def build(self):
        #Window.size = (400, 600) # Change if necessary

        sm = ScreenManager(transition=FadeTransition())
        screens = [
            LoadingScreen(name='loading'),
            CaesarMultiplex(name='caesarm'),
            CaesarEncrypt(name='caesare'),
            CaesarDecrypt(name='caesard'),
            WelcomeScreen(name='welcome'),
            ChooseMethod(name='choose_method'),
            Encrypter(name='encryption'),
            Decrypter(name='decryption'),
            Uploader(name='uploadimage'),
            Downloader(name='downloadimage'),
            SecretsScreen(name='secretscreen'),
            EncryptType(name='encrypttype')
        ]

        for screen in screens:
            sm.add_widget(screen)

        # Example opening screen
        Clock.schedule_once(self.switch_to_main, 5)

        return sm

    def switch_to_main(self, *args):
        self.root.current = 'welcome'


if __name__ == '__main__':
    Stegmain().run()





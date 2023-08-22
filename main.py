from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import wikipedia
import requests

Builder.load_file("frontend.kv")


class FirstScreen(Screen):
    def search_image(self):
        query = self.manager.current_screen.ids.user_query.text
        print(query)
        content = self._search_query(query)
        self._download_image(query, content)
        self.manager.current_screen.ids.img.source = f'files/{query}.jpg'

    @staticmethod
    def _download_image(filename, image):
        with open(f"files/{filename}.jpg", "wb") as file:
            file.write(image)

    def _search_query(self, text_input):
        page = wikipedia.page(text_input)
        url = page.images[0]
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) '
                                 'AppleWebKit/537.36 (KHTML, like Gecko) '
                                 'Chrome/56.0.2924.76 Safari/537.36'}
        response = requests.get(url=url, headers=headers)
        if response.status_code == 200:
            return response.content
        else:
            print("bad response code for wikipedia GET request")


class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


MainApp().run()

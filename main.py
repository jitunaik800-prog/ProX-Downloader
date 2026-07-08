from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

Window.size = (360, 640)

class ProXDownloader(App):
    def build(self):
        main_layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        Window.clearcolor = get_color_from_hex('#121212')
        
        title = Label(
            text="ProX Downloader", 
            font_size='28sp', 
            bold=True, 
            color=get_color_from_hex('#00E5FF'),
            size_hint_y=None, 
            height=60
        )
        main_layout.add_widget(title)
        
        format_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)
        
        self.btn_music = ToggleButton(
            text="🎵 MP3 (Music)", 
            group='format', 
            state='down',
            background_normal='',
            background_color=get_color_from_hex('#1F1F1F'),
            color=get_color_from_hex('#FFFFFF')
        )
        
        self.btn_video = ToggleButton(
            text="🎥 MP4 (Video)", 
            group='format',
            background_normal='',
            background_color=get_color_from_hex('#1F1F1F'),
            color=get_color_from_hex('#FFFFFF')
        )
        
        format_layout.add_widget(self.btn_music)
        format_layout.add_widget(self.btn_video)
        main_layout.add_widget(format_layout)
        
        self.url_input = TextInput(
            hint_text="Paste Video or Music Link Here...",
            multiline=False,
            padding=[10, 15, 10, 15],
            font_size='16sp',
            background_normal='',
            background_color=get_color_from_hex('#1E1E1E'),
            foreground_color=get_color_from_hex('#FFFFFF'),
            hint_text_color=get_color_from_hex('#757575'),
            size_hint_y=None,
            height=55
        )
        main_layout.add_widget(self.url_input)
        
        main_layout.add_widget(Label())
        
        download_btn = Button(
            text="🪄 DOWNLOAD (Auto Quality)",
            font_size='18sp',
            bold=True,
            background_normal='',
            background_color=get_color_from_hex('#00E5FF'),
            color=get_color_from_hex('#121212'),
            size_hint_y=None,
            height=60
        )
        download_btn.bind(on_press=self.start_download)
        main_layout.add_widget(download_btn)
        
        return main_layout

    def start_download(self, instance):
        url = self.url_input.text
        if url:
            self.url_input.text = "Processing Magic Download..."

if __name__ == '__main__':
    ProXDownloader().run()

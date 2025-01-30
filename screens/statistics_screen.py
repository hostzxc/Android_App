from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
import json

class StatisticsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10)
        
        header = Label(text="Статистика", font_size=32, size_hint=(1, None), height=50)
        layout.add_widget(header)

        back_button = Button(text="Назад", size_hint=(None, None), size=(100, 50), pos_hint={'right': 1, 'top': 1})
        back_button.bind(on_press=self.go_back)
        layout.add_widget(back_button)
        
        self.stats_layout = BoxLayout(orientation='vertical', size_hint=(1, None))
        self.stats_layout.bind(minimum_height=self.stats_layout.setter('height'))

        scroll_view = ScrollView(size_hint=(1, 1))
        scroll_view.add_widget(self.stats_layout)
        layout.add_widget(scroll_view)

        self.add_widget(layout)

        self.load_statistics()

    def load_statistics(self):
        try:
            with open('statistics.json', 'r') as file:
                stats = json.load(file)

            for entry in stats:
                date = entry['date']
                status = entry['status']
                self.stats_layout.add_widget(Label(text=f"{date} - {status}", font_size=18))
        except FileNotFoundError:

            self.stats_layout.add_widget(Label(text="Статистика не найдена", font_size=18))
            
    def go_back(self, instance):
        self.manager.current = 'daily'
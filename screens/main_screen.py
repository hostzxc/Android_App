from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = FloatLayout()

        # Фон
        self.background = Image(source="icons/Cena.png", allow_stretch=True, keep_ratio=False)
        layout.add_widget(self.background)

        # Основной контейнер для кнопок
        outer_layout = BoxLayout(orientation='vertical', size_hint=(0.8, 0.5))
        outer_layout.pos_hint = {'center_x': 0.5, 'center_y': 0.5}

        # Сетка для кнопок
        self.layout = GridLayout(
            cols=2, rows=2, spacing=20, size_hint=(1, 1)
        )

        # Стили для кнопок
        button_style = {
            "size_hint": (0.4, 0.3),  # Каждая кнопка занимает 45% ширины и 40% высоты сетки
            "background_color": (0.2, 0.6, 1, 1),  # Синий цвет
            "color": (1, 1, 1, 1),  # Белый текст
            "bold": True
        }

        self.button_daily = Button(text="Дейлики", **button_style)
        self.button_daily.bind(on_press=self.go_to_daily)
        self.layout.add_widget(self.button_daily)

        self.button_workout = Button(text="Тренировки", **button_style)
        self.button_workout.bind(on_press=self.go_to_workout)
        self.layout.add_widget(self.button_workout)

        self.button_gallery = Button(text="Галерея", **button_style)
        self.button_gallery.bind(on_press=self.go_to_gallery)
        self.layout.add_widget(self.button_gallery)

        self.button_calendar = Button(text="Календарь", **button_style)
        self.button_calendar.bind(on_press=self.go_to_calendar)
        self.layout.add_widget(self.button_calendar)

        outer_layout.add_widget(self.layout)
        layout.add_widget(outer_layout)
        
        self.add_widget(layout)

    def go_to_gallery(self, instance):
        self.manager.current = 'gallery'

    def go_to_calendar(self, instance):
        self.manager.current = 'calendar'

    def go_to_daily(self, instance):
        self.manager.current = 'daily'

    def go_to_workout(self, instance):
        self.manager.current = 'workout'


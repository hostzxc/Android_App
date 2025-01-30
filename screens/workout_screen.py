from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.scrollview import ScrollView
import json
import random
from datetime import datetime, timedelta

class WorkoutScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Основной вертикальный контейнер
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Кнопка "Назад"
        back_button = Button(text="Назад", size_hint=(None, None), size=(100, 50))
        back_button.bind(on_press=self.go_back)
        self.layout.add_widget(back_button)

        # Заголовок
        self.header = Label(text="Программа тренировок на неделю", font_size=20, bold=True, size_hint=(1, None), height=50)
        self.layout.add_widget(self.header)

        # Прокручиваемая область для упражнений
        self.scroll_view = ScrollView(size_hint=(1, 1))
        self.workout_layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        self.workout_layout.bind(minimum_height=self.workout_layout.setter('height'))

        self.scroll_view.add_widget(self.workout_layout)
        self.layout.add_widget(self.scroll_view)

        self.add_widget(self.layout)

        self.load_workout_plan()

    def go_back(self, instance):
        self.manager.current = 'main'

    def generate_workout_plan(self):
        exercises = {
            "Понедельник": ["Жим лёжа - 4x8", "Подтягивания - 4x10", "Пресс - 3x15"],
            "Вторник": ["Приседания - 4x12", "Выпады - 3x10", "Планка - 3x60 сек"],
            "Среда": ["Отжимания - 4x15", "Тяга гантели - 3x12", "Скручивания - 3x20"],
            "Четверг": ["Мёртвая тяга - 4x10", "Подъём на носки - 3x15", "Боковая планка - 3x45 сек"],
            "Пятница": ["Жим гантелей - 4x8", "Тяга блока - 4x12", "Пресс - 3x20"],
            "Суббота": ["Кардио - 30 минут", "Берпи - 3x12", "Растяжка - 10 минут"],
            "Воскресенье": ["Отдых / Лёгкое кардио"]
        }
        return exercises

    def load_workout_plan(self):
        try:
            with open('workout_plan.json', 'r') as file:
                data = json.load(file)
            last_update = datetime.strptime(data['last_update'], "%Y-%m-%d").date()
            if (datetime.now().date() - last_update) >= timedelta(days=7):
                raise FileNotFoundError
        except (FileNotFoundError, json.JSONDecodeError, KeyError):
            data = {
                "last_update": datetime.now().strftime("%Y-%m-%d"),
                "workout_plan": self.generate_workout_plan()
            }
            with open('workout_plan.json', 'w') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
        
        self.display_workout_plan(data["workout_plan"])

    def display_workout_plan(self, workout_plan):
        self.workout_layout.clear_widgets()

        for day, exercises in workout_plan.items():
            day_box = BoxLayout(orientation='vertical', padding=10, spacing=5, size_hint_y=None)
            day_box.height = 60 + (len(exercises) * 40)  # Высота блока зависит от количества упражнений
            day_box.add_widget(Label(text=f"{day}", font_size=24, bold=True, size_hint_y=None, height=40))

            for exercise in exercises:
                day_box.add_widget(Label(text=f" • {exercise}", font_size=20, size_hint_y=None, height=40))

            # Добавляем рамку вокруг блока
            container = BoxLayout(orientation='vertical', padding=5, size_hint_y=None)
            container.height = day_box.height + 10
            container.add_widget(day_box)

            self.workout_layout.add_widget(container)

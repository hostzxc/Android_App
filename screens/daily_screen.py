import os
import json
from datetime import datetime
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock
from kivy.uix.anchorlayout import AnchorLayout 

class DailyScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10)

        # Путь к файлу JSON в корневой папке проекта
        self.json_path = os.path.join(os.path.dirname(__file__), '..', 'daily_data.json')

        # Кнопка назад
        # Обёртка для кнопки "Назад"
        back_button_layout = AnchorLayout(anchor_x='right', anchor_y='top')
        back_button = Button(text="Назад", size_hint=(0.3, 0.7))
        back_button.bind(on_press=self.go_back)
        back_button_layout.add_widget(back_button)

        layout.add_widget(back_button_layout)  # Добавляем обёртку с кнопкой

        # Заголовок
        header = Label(text="Ежедневные упражнения", font_size=26, size_hint=(1, None), height=50)
        layout.add_widget(header)

        # Сетка с упражнениями
        grid = GridLayout(cols=3, size_hint=(1, None), height=400, padding=20)

        # Заголовки
        grid.add_widget(Label(text="Упражнения", font_size=14))
        grid.add_widget(Label(text="Повторения", font_size=14))
        grid.add_widget(Label(text="Выполненность", font_size=14))

        # Отжимания
        self.pushups_checkbox = CheckBox()
        self.pushups_reps = Label(text="20")
        grid.add_widget(Label(text="Отжимания"))
        grid.add_widget(self.pushups_reps)
        grid.add_widget(self.pushups_checkbox)

        # Приседания
        self.squats_checkbox = CheckBox()
        self.squats_reps = Label(text="20")
        grid.add_widget(Label(text="Приседания"))
        grid.add_widget(self.squats_reps)
        grid.add_widget(self.squats_checkbox)

        # Пресс
        self.abs_checkbox = CheckBox()
        self.abs_reps = Label(text="20")
        grid.add_widget(Label(text="Пресс"))
        grid.add_widget(self.abs_reps)
        grid.add_widget(self.abs_checkbox)

        # Подтягивания
        self.pullups_checkbox = CheckBox()
        self.pullups_reps = Label(text="20")
        grid.add_widget(Label(text="Подтягивания"))
        grid.add_widget(self.pullups_reps)
        grid.add_widget(self.pullups_checkbox)

        layout.add_widget(grid)

        # Кнопка статистики
        stats_button = Button(text="Статистика", size_hint=(None, None), size=(200, 50), pos_hint={"center_x": 0.5})
        stats_button.bind(on_press=self.show_stats)
        layout.add_widget(stats_button)

        self.add_widget(layout)

        # Загружаем состояние чекбоксов
        self.load_checkboxes_state()

        # Запускаем обновление каждый день в 00:00
        Clock.schedule_interval(self.check_daily_update, 1)

        # Начальная установка даты для сравнения
        self.last_check_date = datetime.now().date()

    def go_back(self, instance):
        self.manager.current = 'main'

    def show_stats(self, instance):
        self.manager.current = 'statistics'

    def check_daily_update(self, dt):
        """Проверяем каждый день обновление в 00:00"""
        current_date = datetime.now().date()
        if current_date > self.last_check_date:
            self.last_check_date = current_date
            self.update_reps()
            self.save_checkboxes_state()
            print(f"Обновление: {current_date}")

    def update_reps(self):
        """Обновляем количество повторений для упражнений"""
        if not self.pushups_checkbox.active:
            self.pushups_reps.text = str(int(self.pushups_reps.text) + 1)

        if not self.squats_checkbox.active:
            self.squats_reps.text = str(int(self.squats_reps.text) + 1)

        if not self.abs_checkbox.active:
            self.abs_reps.text = str(int(self.abs_reps.text) + 1)

        if not self.pullups_checkbox.active:
            self.pullups_reps.text = str(int(self.pullups_reps.text) + 1)

        # Еженедельное увеличение на 5
        if datetime.now().weekday() == 0:
            self.pushups_reps.text = str(int(self.pushups_reps.text) + 5)
            self.squats_reps.text = str(int(self.squats_reps.text) + 5)
            self.abs_reps.text = str(int(self.abs_reps.text) + 5)
            self.pullups_reps.text = str(int(self.pullups_reps.text) + 5)

    def save_checkboxes_state(self):
        """Сохраняем состояние чекбоксов и количество повторений в JSON"""
        data = {
            "pushups": {"checked": self.pushups_checkbox.active, "reps": self.pushups_reps.text},
            "squats": {"checked": self.squats_checkbox.active, "reps": self.squats_reps.text},
            "abs": {"checked": self.abs_checkbox.active, "reps": self.abs_reps.text},
            "pullups": {"checked": self.pullups_checkbox.active, "reps": self.pullups_reps.text},
        }
        try:
            with open(self.json_path, "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Ошибка при сохранении JSON: {e}")

    def load_checkboxes_state(self):
        """Загружаем состояние чекбоксов и количество повторений из JSON"""
        if os.path.exists(self.json_path):
            try:
                with open(self.json_path, "r", encoding="utf-8") as file:
                    data = json.load(file)

                self.pushups_checkbox.active = data["pushups"]["checked"]
                self.pushups_reps.text = data["pushups"]["reps"]

                self.squats_checkbox.active = data["squats"]["checked"]
                self.squats_reps.text = data["squats"]["reps"]

                self.abs_checkbox.active = data["abs"]["checked"]
                self.abs_reps.text = data["abs"]["reps"]

                self.pullups_checkbox.active = data["pullups"]["checked"]
                self.pullups_reps.text = data["pullups"]["reps"]

                print(f"Данные загружены из {self.json_path}")
            except Exception as e:
                print(f"Ошибка при загрузке JSON: {e}")
        else:
            print("Файл с данными не найден, создаем новый при первом сохранении.")

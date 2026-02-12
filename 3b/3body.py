import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
from scipy.integrate import solve_ivp

class ThreeBodySimulation:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Симуляция задачи трёх тел")
        self.root.geometry("1000x700")
        
        # Настройка параметров
        self.canvas_width = 600
        self.canvas_height = 600
        
        # Параметры симуляции
        self.G = 1.0  # Гравитационная постоянная (в условных единицах)
        self.simulation_time = 20  # Время моделирования
        self.time_step = 0.05
        
        # Переменные для UI
        self.selected_scenario = tk.StringVar(value="lagrange")
        
        # Создание интерфейса
        self.create_widgets()
        
    def create_widgets(self):
        # Фрейм для ввода параметров
        input_frame = ttk.LabelFrame(self.root, text="Настройки сценария", padding=10)
        input_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)
        
        # Выбор сценария
        ttk.Label(input_frame, text="Сценарий:").grid(row=0, column=0, sticky="w")
        
        # Карта соответствия отображаемых названий и кодовых имен
        self.scenarios = {
            "lagrange": "Стабильная орбита (Треугольник Лагранжа)",
            "chaotic": "Хаотичное движение",
            "collision": "Столкновение двух тел",
            "escape": "Улетание в космос"
        }
        
        # Создаем выпадающее меню с отображаемыми названиями
        self.scenario_var = tk.StringVar(value=self.scenarios["lagrange"])
        scenario_menu = ttk.OptionMenu(
            input_frame, 
            self.scenario_var,
            self.scenarios["lagrange"],  # Значение по умолчанию
            *self.scenarios.values(),
            command=self.update_inputs  # Теперь передается отображаемое название
        )
        scenario_menu.grid(row=1, column=0, columnspan=2, sticky="ew", pady=(5, 15))
        
        # Поля ввода для параметров (создаем один раз и обновляем)
        self.entry_fields = {}
        self.create_input_fields(input_frame)
        
        # Кнопки управления
        ttk.Button(
            input_frame,
            text="Запустить симуляцию",
            command=self.run_simulation
        ).grid(row=15, column=0, columnspan=2, sticky="ew", pady=(10, 5))
        
        ttk.Button(
            input_frame,
            text="Остановить",
            command=self.stop_simulation
        ).grid(row=16, column=0, columnspan=2, sticky="ew")
        
        ttk.Button(
            input_frame,
            text="Очистить",
            command=self.clear_canvas
        ).grid(row=17, column=0, columnspan=2, sticky="ew")
        
        # Канвас для отрисовки
        self.canvas = tk.Canvas(self.root, width=self.canvas_width, height=self.canvas_height, bg="black")
        self.canvas.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Отображаем текущие поля ввода при запуске
        self.update_inputs(self.scenarios["lagrange"])
    
    def create_input_fields(self, parent):
        # Создаем поля для разных параметров
        parameters = [
            ("Масса тела 1 (m1):", "m1"),
            ("Масса тела 2 (m2):", "m2"),
            ("Масса тела 3 (m3):", "m3"),
            ("Начальная позиция X1:", "x1"),
            ("Начальная позиция Y1:", "y1"),
            ("Начальная скорость X1:", "vx1"),
            ("Начальная скорость Y1:", "vy1"),
            ("Начальная позиция X2:", "x2"),
            ("Начальная позиция Y2:", "y2"),
            ("Начальная скорость X2:", "vx2"),
            ("Начальная скорость Y2:", "vy2"),
            ("Начальная позиция X3:", "x3"),
            ("Начальная позиция Y3:", "y3"),
            ("Начальная скорость X3:", "vx3"),
            ("Начальная скорость Y3:", "vy3"),
        ]
        
        for i, (label, var_name) in enumerate(parameters):
            ttk.Label(parent, text=label).grid(row=i+2, column=0, sticky="w", pady=2)
            entry = ttk.Entry(parent)
            entry.grid(row=i+2, column=1, sticky="ew", pady=2)
            self.entry_fields[var_name] = entry
    
    def update_inputs(self, scenario_display_name):
        # Карта соответствия отображаемых названий и кодовых имен
        display_to_code = {
            "Стабильная орбита (Треугольник Лагранжа)": "lagrange",
            "Хаотичное движение": "chaotic",
            "Столкновение двух тел": "collision",
            "Улетание в космос": "escape"
        }
        
        scenario_code = display_to_code.get(scenario_display_name, "lagrange")
        
        defaults = {
            "lagrange": {
                "m1": "50", "m2": "50", "m3": "1",
                "x1": "100", "y1": "259.8", "vx1": "-0.52", "vy1": "0.9",
                "x2": "-200", "y2": "0", "vx2": "0.52", "vy2": "0.9",
                "x3": "100", "y3": "-259.8", "vx3": "0", "vy3": "-1.8"
            },
            "chaotic": {
                "m1": "100", "m2": "100", "m3": "100",
                "x1": "50", "y1": "50", "vx1": "-5", "vy1": "3",
                "x2": "-80", "y2": "-60", "vx2": "4", "vy2": "-2",
                "x3": "70", "y3": "-30", "vx3": "-1", "vy3": "5"
            },
            "collision": {
                "m1": "100", "m2": "100", "m3": "50",
                "x1": "0", "y1": "100", "vx1": "-4", "vy1": "0",
                "x2": "0", "y2": "-100", "vx2": "4", "vy2": "0",
                "x3": "50", "y3": "0", "vx3": "0", "vy3": "-2"
            },
            "escape": {
                "m1": "100", "m2": "100", "m3": "200",
                "x1": "50", "y1": "0", "vx1": "2", "vy1": "-3",
                "x2": "-50", "y2": "0", "vx2": "-2", "vy2": "-3",
                "x3": "0", "y3": "100", "vx3": "0", "vy3": "4"
            }
        }
        
        # Заполняем поля значениями по умолчанию
        for var_name, value in defaults[scenario_code].items():
            self.entry_fields[var_name].delete(0, tk.END)
            self.entry_fields[var_name].insert(0, value)
    
    def get_parameters(self):
        try:
            params = {}
            for key, entry in self.entry_fields.items():
                value = float(entry.get())
                if "m" in key and value <= 0:  # Проверка массы
                    raise ValueError(f"Масса должна быть положительной: {key}")
                params[key] = value
            return params
        except ValueError as e:
            messagebox.showerror("Ошибка ввода", f"Некорректные данные: {e}")
            return None
    
    def three_body_system(self, t, y):
        # Дифференциальные уравнения для задачи трёх тел
        G = self.G
        
        # Извлекаем координаты и скорости
        x1, y1, vx1, vy1, x2, y2, vx2, vy2, x3, y3, vx3, vy3 = y
        
        # Расстояния между телами (с учетом защиты от деления на ноль)
        r12_sq = (x2-x1)**2 + (y2-y1)**2
        r13_sq = (x3-x1)**2 + (y3-y1)**2
        r23_sq = (x3-x2)**2 + (y3-y2)**2
        
        # Минимальное расстояние для защиты от деления на ноль
        min_dist_sq = 1.0
        
        r12 = np.sqrt(max(r12_sq, min_dist_sq))
        r13 = np.sqrt(max(r13_sq, min_dist_sq))
        r23 = np.sqrt(max(r23_sq, min_dist_sq))
        
        # Ускорения по второму закону Ньютона
        ax1 = -G * self.m2 * (x1-x2) / (r12_sq * r12) - G * self.m3 * (x1-x3) / (r13_sq * r13)
        ay1 = -G * self.m2 * (y1-y2) / (r12_sq * r12) - G * self.m3 * (y1-y3) / (r13_sq * r13)
        ax2 = -G * self.m1 * (x2-x1) / (r12_sq * r12) - G * self.m3 * (x2-x3) / (r23_sq * r23)
        ay2 = -G * self.m1 * (y2-y1) / (r12_sq * r12) - G * self.m3 * (y2-y3) / (r23_sq * r23)
        ax3 = -G * self.m1 * (x3-x1) / (r13_sq * r13) - G * self.m2 * (x3-x2) / (r23_sq * r23)
        ay3 = -G * self.m1 * (y3-y1) / (r13_sq * r13) - G * self.m2 * (y3-y2) / (r23_sq * r23)
        
        return [vx1, vy1, ax1, ay1,
                vx2, vy2, ax2, ay2,
                vx3, vy3, ax3, ay3]
    
    def run_simulation(self):
        params = self.get_parameters()
        if params is None:
            return
        
        # Обновляем массы для системы
        self.m1 = float(params["m1"])
        self.m2 = float(params["m2"])
        self.m3 = float(params["m3"])
        
        # Начальные условия: x1, y1, vx1, vy1, x2, y2, vx2, vy2, x3, y3, vx3, vy3
        y0 = [
            float(params["x1"]), float(params["y1"]),
            float(params["vx1"]), float(params["vy1"]),
            float(params["x2"]), float(params["y2"]),
            float(params["vx2"]), float(params["vy2"]),
            float(params["x3"]), float(params["y3"]),
            float(params["vx3"]), float(params["vy3"])
        ]
        
        # Создаем временной массив
        t_eval = np.arange(0, self.simulation_time, self.time_step)
        
        try:
            # Решаем дифференциальные уравнения
            sol = solve_ivp(
                self.three_body_system,
                [0, self.simulation_time],
                y0,
                t_eval=t_eval,
                method='RK45',
                vectorized=False
            )
            
            if not sol.success:
                messagebox.showerror("Ошибка", "Не удалось решить систему дифференциальных уравнений")
                return
            
            # Очистка канваса перед новой отрисовкой
            self.clear_canvas()
            
            # Инициализируем переменные для анимации
            self.current_step = 0
            self.max_points = len(sol.t)
            
            # Рассчитываем масштаб и центр
            all_x = np.concatenate([
                sol.y[0],
                sol.y[4],
                sol.y[8]
            ])
            all_y = np.concatenate([
                sol.y[1],
                sol.y[5],
                sol.y[9]
            ])
            
            # Находим минимальный и максимальный координаты
            x_min, x_max = np.min(all_x), np.max(all_x)
            y_min, y_max = np.min(all_y), np.max(all_y)
            
            # Добавляем отступы
            padding = 0.2 * max(x_max - x_min, y_max - y_min)
            if padding == 0:  # Если все точки совпадают (редкий случай)
                padding = 50
            
            self.x_range = x_max - x_min + 2 * padding
            self.y_range = y_max - y_min + 2 * padding
            
            # Центр сцены в мировых координатах
            self.center_x = (x_min + x_max) / 2.0
            self.center_y = (y_min + y_max) / 2.0
            
            # Масштаб: сколько мировых единиц приходится на один пиксель
            scale_x = (self.canvas_width - 40) / self.x_range if self.x_range > 0 else 1
            scale_y = (self.canvas_height - 40) / self.y_range if self.y_range > 0 else 1
            self.scale = min(scale_x, scale_y) * 0.8  # 0.8 для запаса
            
            # Рисуем траектории и начальные положения
            self.colors = ["red", "green", "blue"]
            
            # Вычисляем количество шагов для отрисовки (для производительности)
            step_size = max(1, len(sol.t) // 300)  # Ограничиваем до ~300 точек
            
            self.x1_vals = sol.y[0][::step_size]
            self.y1_vals = sol.y[1][::step_size]
            self.x2_vals = sol.y[4][::step_size]
            self.y2_vals = sol.y[5][::step_size]
            self.x3_vals = sol.y[8][::step_size]
            self.y3_vals = sol.y[9][::step_size]
            
            # Рисуем траектории
            for i in range(1, len(self.x1_vals)):
                # Преобразуем координаты для отображения на канвасе
                cx1 = self.canvas_width/2 + (self.x1_vals[i] - self.center_x)*self.scale
                cy1 = self.canvas_height/2 - (self.y1_vals[i] - self.center_y)*self.scale
                cx2 = self.canvas_width/2 + (self.x2_vals[i] - self.center_x)*self.scale
                cy2 = self.canvas_height/2 - (self.y2_vals[i] - self.center_y)*self.scale
                cx3 = self.canvas_width/2 + (self.x3_vals[i] - self.center_x)*self.scale
                cy3 = self.canvas_height/2 - (self.y3_vals[i] - self.center_y)*self.scale
                
                if i > 0:
                    self.canvas.create_line(
                        self.canvas_width/2 + (self.x1_vals[i-1] - self.center_x)*self.scale,
                        self.canvas_height/2 - (self.y1_vals[i-1] - self.center_y)*self.scale,
                        cx1, cy1,
                        fill=self.colors[0], width=2
                    )
                    self.canvas.create_line(
                        self.canvas_width/2 + (self.x2_vals[i-1] - self.center_x)*self.scale,
                        self.canvas_height/2 - (self.y2_vals[i-1] - self.center_y)*self.scale,
                        cx2, cy2,
                        fill=self.colors[1], width=2
                    )
                    self.canvas.create_line(
                        self.canvas_width/2 + (self.x3_vals[i-1] - self.center_x)*self.scale,
                        self.canvas_height/2 - (self.y3_vals[i-1] - self.center_y)*self.scale,
                        cx3, cy3,
                        fill=self.colors[2], width=2
                    )
            
            # Рисуем тела в начальных позициях
            self.body_items = []
            for i in range(3):
                if i == 0:
                    x_vals, y_vals = self.x1_vals, self.y1_vals
                    color = self.colors[0]
                elif i == 1:
                    x_vals, y_vals = self.x2_vals, self.y2_vals
                    color = self.colors[1]
                else:
                    x_vals, y_vals = self.x3_vals, self.y3_vals
                    color = self.colors[2]
                
                # Рисуем тело в начальной позиции (индекс 0)
                cx = self.canvas_width/2 + (x_vals[0] - self.center_x)*self.scale
                cy = self.canvas_height/2 - (y_vals[0] - self.center_y)*self.scale
                
                # Размер тела зависит от его массы
                radius = max(3, 5 * np.log10(max(getattr(self, f"m{i+1}"), 1)))
                
                body = self.canvas.create_oval(
                    cx-radius, cy-radius, cx+radius, cy+radius,
                    fill=color, outline="white", width=2
                )
                self.body_items.append(body)
            
            # Запускаем анимацию
            self.animation_id = None
            self.animate()
        
        except Exception as e:
            messagebox.showerror("Ошибка симуляции", f"Произошла ошибка при запуске симуляции: {str(e)}")
    
    def animate(self):
        if hasattr(self, 'body_items') and len(self.body_items) > 0:
            # Обновляем позиции тел
            for i in range(len(self.body_items)):
                if i == 0:
                    x_vals, y_vals = self.x1_vals, self.y1_vals
                    color = self.colors[0]
                elif i == 1:
                    x_vals, y_vals = self.x2_vals, self.y2_vals
                    color = self.colors[1]
                else:
                    x_vals, y_vals = self.x3_vals, self.y3_vals
                    color = self.colors[2]
                
                # Получаем текущую позицию (если анимация не дошла до конца)
                idx = min(self.current_step, len(x_vals)-1)
                cx = self.canvas_width/2 + (x_vals[idx] - self.center_x)*self.scale
                cy = self.canvas_height/2 - (y_vals[idx] - self.center_y)*self.scale
                
                # Размер тела зависит от его массы
                radius = max(3, 5 * np.log10(max(getattr(self, f"m{i+1}"), 1)))
                
                # Обновляем позицию тела
                self.canvas.coords(
                    self.body_items[i],
                    cx-radius, cy-radius, cx+radius, cy+radius
                )
            
            # Увеличиваем индекс текущего кадра
            self.current_step += 1
            
            # Если достигли конца анимации, останавливаемся (или можно зациклить)
            if self.current_step >= len(self.x1_vals):
                # Можно раскомментировать следующую строку для зацикливания
                # self.current_step = 0
                pass
            else:
                # Запускаем следующий кадр через 30 мс (примерно 33 FPS)
                self.animation_id = self.root.after(30, self.animate)
    
    def stop_simulation(self):
        if hasattr(self, 'animation_id') and self.animation_id is not None:
            self.root.after_cancel(self.animation_id)
            self.animation_id = None
    
    def clear_canvas(self):
        self.canvas.delete("all")
    
    def on_closing(self):
        # Останавливаем анимацию при закрытии окна
        if hasattr(self, 'animation_id') and self.animation_id is not None:
            self.root.after_cancel(self.animation_id)
        self.root.destroy()

if __name__ == "__main__":
    sim = ThreeBodySimulation()
    sim.root.protocol("WM_DELETE_WINDOW", sim.on_closing)
    sim.root.mainloop()

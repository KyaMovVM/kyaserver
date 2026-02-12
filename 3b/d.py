import tkinter as tk
from functools import wraps

# --- Декораторы событий ---
class EventApp:
    def __init__(self):
        self.bindings = {}

    def event(self, *keys):
        """Декоратор для регистрации обработчиков событий (аналог @app.event('button1'))"""
        def decorator(func):
            @wraps(func)
            def wrapper(event=None):
                return func(event)
            for key in keys:
                self.bindings[key] = wrapper
            return wrapper
        return decorator

# --- Приложение ---
class E8DiagramApp(EventApp):
    def __init__(self, root):
        super().__init__()
        self.root = root
        root.title("E₈ Root System (Dynkin Diagram)")

        # Canvas
        self.canvas = tk.Canvas(root, width=600, height=400, bg='white')
        self.canvas.pack()

        # Регистрация событий
        self.event('Draw')(self.draw_e8)
        self.event('Clear')(self.clear_canvas)
        self.event('Exit')(root.quit)

        # Привязка к кнопкам/меню (для удобства — через bind, но можно и через меню)
        root.bind('<Control-d>', lambda e: self.bindings['Draw'](e))
        root.bind('<Control-c>', lambda e: self.bindings['Clear'](e))
        root.bind('<Control-q>', lambda e: self.bindings['Exit'](e))

        # Отрисовать при запуске
        self.draw_e8(None)

    def draw_e8(self, event=None):
        """Отрисовка диаграммы Эдинктона для E8"""
        self.canvas.delete("all")

        # Координаты узлов (упрощённо)
        # Строкой: 6 узлов
        row_nodes = [(50 + i*70, 100) for i in range(6)]  # ● — ● — ● — ● — ● — ●

        # Ответвление: 2 узла вниз от 3-го узла (индекс 2)
        branch_nodes = [
            (50 + 2*70, 180),
            (50 + 2*70, 260)
        ]

        # Рисуем вертикальную ось ответвления
        for i in range(len(branch_nodes) - 1):
            x1, y1 = branch_nodes[i]
            x2, y2 = branch_nodes[i+1]
            self.canvas.create_line(x1, y1, x2, y2, fill="black", width=2)

        # Рисуем ответвление от строки
        self.canvas.create_line(
            row_nodes[2][0], row_nodes[2][1],
            branch_nodes[0][0], branch_nodes[0][1],
            fill="black", width=2
        )

        # Рисуем горизонтальную цепь
        for i in range(len(row_nodes) - 1):
            x1, y1 = row_nodes[i]
            x2, y2 = row_nodes[i+1]
            self.canvas.create_line(x1, y1, x2, y2, fill="black", width=2)

        # Рисуем узлы (точки)
        all_nodes = row_nodes + branch_nodes
        for x, y in all_nodes:
            self.canvas.create_oval(x-8, y-8, x+8, y+8, fill="blue")

        # Подписи: 1..8 (для простых корней)
        labels = ["α₁", "α₂", "α₃", "α₄", "α₅", "α₆", "α₇", "α₈"]  # не по порядку на диаграмме, но просто для примера
        for i, (x, y) in enumerate(all_nodes):
            self.canvas.create_text(x, y+25, text=f"α{i+1}", font=("Arial", 10), fill="black")

        self.canvas.create_text(300, 350, text="E₈ Dynkin Diagram", font=("Arial", 14, "bold"), fill="darkblue")

    def clear_canvas(self, event=None):
        self.canvas.delete("all")

# Запуск
if __name__ == "__main__":
    root = tk.Tk()
    app = E8DiagramApp(root)
    root.mainloop()

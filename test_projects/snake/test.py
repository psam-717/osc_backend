import tkinter as tk
import random

CELL = 20
COLS = 25
ROWS = 20
WIDTH = CELL * COLS
HEIGHT = CELL * ROWS
SPEED = 120  # ms between frames

COLORS = {
    "bg": "#1a1a2e",
    "snake": "#00ff88",
    "snake_head": "#00ffcc",
    "food": "#ff4757",
    "text": "#ffffff",
    "grid": "#16213e",
}

class SnakeGame:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("🐍 Snake")
        self.root.resizable(False, False)

        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg=COLORS["bg"], highlightthickness=0)
        self.canvas.pack()

        self.root.bind("<KeyPress>", self.on_key)

        self.high_score = 0
        self.reset()
        self.draw()

    def reset(self):
        mid_col = COLS // 2
        mid_row = ROWS // 2
        self.snake = [(mid_col, mid_row), (mid_col - 1, mid_row), (mid_col - 2, mid_row)]
        self.direction = (1, 0)
        self.next_dir = (1, 0)
        self.score = 0
        self.alive = True
        self.place_food()
        if hasattr(self, "_after_id"):
            self.root.after_cancel(self._after_id)
        self._after_id = self.root.after(SPEED, self.tick)

    def place_food(self):
        occupied = set(self.snake)
        while True:
            pos = (random.randint(0, COLS - 1), random.randint(0, ROWS - 1))
            if pos not in occupied:
                self.food = pos
                break

    def on_key(self, event: tk.Event):
        key = event.keysym
        moves = {"Up": (0, -1), "Down": (0, 1), "Left": (-1, 0), "Right": (1, 0),
                 "w": (0, -1), "s": (0, 1), "a": (-1, 0), "d": (1, 0)}
        if key in moves:
            dx, dy = moves[key]
            # Prevent reversing
            if (dx, dy) != (-self.direction[0], -self.direction[1]):
                self.next_dir = (dx, dy)
        elif key == "r" and not self.alive:
            self.reset()

    def tick(self):
        if not self.alive:
            return
        self.direction = self.next_dir
        hx, hy = self.snake[0]
        nx, ny = hx + self.direction[0], hy + self.direction[1]

        # Wall collision
        if not (0 <= nx < COLS and 0 <= ny < ROWS):
            self.game_over()
            return

        # Self collision
        if (nx, ny) in self.snake[:-1]:
            self.game_over()
            return

        self.snake.insert(0, (nx, ny))

        if (nx, ny) == self.food:
            self.score += 10
            self.place_food()
        else:
            self.snake.pop()

        self.draw()
        self._after_id = self.root.after(SPEED, self.tick)

    def game_over(self):
        self.alive = False
        if self.score > self.high_score:
            self.high_score = self.score
        self.draw()

    def draw(self):
        c = self.canvas
        c.delete("all")

        # Grid lines
        for col in range(COLS):
            c.create_line(col * CELL, 0, col * CELL, HEIGHT, fill=COLORS["grid"], width=1)
        for row in range(ROWS):
            c.create_line(0, row * CELL, WIDTH, row * CELL, fill=COLORS["grid"], width=1)

        # Food
        fx, fy = self.food
        c.create_oval(fx * CELL + 3, fy * CELL + 3,
                      fx * CELL + CELL - 3, fy * CELL + CELL - 3,
                      fill=COLORS["food"], outline="")

        # Snake
        for i, (sx, sy) in enumerate(self.snake):
            color = COLORS["snake_head"] if i == 0 else COLORS["snake"]
            pad = 1 if i == 0 else 2
            c.create_rectangle(sx * CELL + pad, sy * CELL + pad,
                                sx * CELL + CELL - pad, sy * CELL + CELL - pad,
                                fill=color, outline="")

        # Score HUD
        c.create_text(8, 8, anchor="nw", text=f"Score: {self.score}",
                      fill=COLORS["text"], font=("Consolas", 11, "bold"))
        c.create_text(WIDTH - 8, 8, anchor="ne", text=f"Best: {self.high_score}",
                      fill=COLORS["text"], font=("Consolas", 11, "bold"))

        # Game over overlay
        if not self.alive:
            c.create_rectangle(0, HEIGHT // 2 - 55, WIDTH, HEIGHT // 2 + 55,
                                fill="#000000", stipple="gray50", outline="")
            c.create_text(WIDTH // 2, HEIGHT // 2 - 20,
                          text="GAME OVER", fill="#ff4757",
                          font=("Consolas", 28, "bold"))
            c.create_text(WIDTH // 2, HEIGHT // 2 + 18,
                          text=f"Score: {self.score}", fill=COLORS["text"],
                          font=("Consolas", 14))
            c.create_text(WIDTH // 2, HEIGHT // 2 + 42,
                          text="Press R to restart", fill="#aaaaaa",
                          font=("Consolas", 11))


if __name__ == "__main__":
    root = tk.Tk()
    SnakeGame(root)
    root.mainloop()

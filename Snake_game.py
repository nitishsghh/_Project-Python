import tkinter as tk
import random
import time

class SnakeGame:
    def __init__(self, master):
        self.master = master
        self.master.title('Snake Game')
        self.master.resizable(False, False)
        self.canvas = tk.Canvas(self.master, width=300, height=300, bg='black')
        self.canvas.pack()
        self.snake = [(100, 100), (90, 100), (80, 100)]
        self.food = self.generate_food()
        self.direction = 'Right'
        self.score = 0
        self.speed = 100
        self.game_over = False
        self.draw_board()
        self.master.bind('<KeyPress>', self.change_direction)
        self.move()

    def draw_board(self):
        self.canvas.delete('all')
        for segment in self.snake:
            self.canvas.create_rectangle(segment[0], segment[1], segment[0] + 10, segment[1] + 10, fill='white')
        self.canvas.create_oval(self.food[0], self.food[1], self.food[0] + 10, self.food[1] + 10, fill='red')
        self.canvas.create_text(50, 10, text=f"Score: {self.score}", fill='white')

    def generate_food(self):
        x = random.randint(0, 29) * 10
        y = random.randint(0, 29) * 10
        return x, y

    def move(self):
        if not self.game_over:
            self.check_collision()
            self.check_food_collision()
            self.move_snake()
            self.draw_board()
            self.master.after(self.speed, self.move)
        else:
            self.canvas.create_text(150, 150, text="Game Over!", fill='white', font=('Helvetica', 24, 'bold'))

    def move_snake(self):
        head = self.snake[0]
        if self.direction == 'Right':
            new_head = (head[0] + 10, head[1])
        elif self.direction == 'Left':
            new_head = (head[0] - 10, head[1])
        elif self.direction == 'Up':
            new_head = (head[0], head[1] - 10)
        else:
            new_head = (head[0], head[1] + 10)
        self.snake.insert(0, new_head)
        if not self.check_food_collision():
            self.snake.pop()

    def change_direction(self, event):
        key = event.keysym
        if key == 'Right' and self.direction != 'Left':
            self.direction = 'Right'
        elif key == 'Left' and self.direction != 'Right':
            self.direction = 'Left'
        elif key == 'Up' and self.direction != 'Down':
            self.direction = 'Up'
        elif key == 'Down' and self.direction != 'Up':
            self.direction = 'Down'

    def check_collision(self):
        head = self.snake[0]
        if head[0] < 0 or head[0] >= 300 or head[1] < 0 or head[1] >= 300:
            self.game_over = True
        for segment in self.snake[1:]:
            if head == segment:
                self.game_over = True

    def check_food_collision(self):
        if self.snake[0] == self.food:
            self.score += 1
            self.food = self.generate_food()
            return True
        return False

def main():
    root = tk.Tk()
    snake_game = SnakeGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()

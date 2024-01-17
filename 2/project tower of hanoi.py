import tkinter as tk
from tkinter import simpledialog, messagebox

class TowerOfHanoi:
    def __init__(self, master, num_discs):
        self.master = master
        self.num_discs = num_discs
        self.towers = [[i for i in range(self.num_discs, 0, -1)], [], []]

        self.canvas = tk.Canvas(master, width=400, height=300, bg="white")
        self.canvas.pack()

        self.initialize_towers()
        self.draw_towers()

    def initialize_towers(self):
        self.towers = [[i for i in range(self.num_discs, 0, -1)], [], []]

    def draw_towers(self):
        self.canvas.delete("all")
        
        self.canvas.create_rectangle(50, 50, 60, 260, fill="black") 
        self.canvas.create_rectangle(200, 50, 210, 260, fill="black") 
        self.canvas.create_rectangle(350, 50, 360, 260, fill="black") 

        
        for i in range(3):
            for j, disc in enumerate(self.towers[i]):
                width = 20 + disc * 20
                height = 10
                x = 55 + i * 150 - width // 2 
                y = 250 - j * 20
                self.canvas.create_rectangle(x, y, x + width, y + height, fill="red")

    def move_disc(self, from_tower, to_tower):
        if self.is_valid_move(from_tower, to_tower):
            disc = self.towers[from_tower].pop()
            self.towers[to_tower].append(disc)
            self.draw_towers()
            if self.is_game_complete():
                self.show_congratulations()

    def is_valid_move(self, from_tower, to_tower):
        if not self.towers[from_tower]:
            return False
        if not self.towers[to_tower] or self.towers[to_tower][-1] > self.towers[from_tower][-1]:
            return True
        return False

    def is_game_complete(self):
        return len(self.towers[0]) == self.num_discs or len(self.towers[1]) == self.num_discs or len(self.towers[2]) == self.num_discs


    def show_congratulations(self):
        messagebox.showinfo("Congratulations!", "You have successfully completed the Tower of Hanoi!")

def run_game():
    while True:
        num_discs = simpledialog.askinteger("Number of Discs", "Enter the number of discs:", initialvalue=3)
        
        if num_discs is None:
            return 
        root = tk.Tk()
        root.title("Tower of Hanoi")

        game = TowerOfHanoi(root, num_discs)

        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)

        for i in range(3):
            for j in range(3):
                if i != j:
                    button = tk.Button(button_frame, text=f"{i + 1} -> {j + 1}",
                                       command=lambda i=i, j=j: game.move_disc(i, j))
                    button.grid(row=i, column=j, padx=10)

        root.protocol("WM_DELETE_WINDOW", root.destroy)
        root.mainloop()

        play_again = messagebox.askyesno("Play Again?", "Do you want to play again?")

        if not play_again:
            break

if __name__ == "__main__":
    run_game()

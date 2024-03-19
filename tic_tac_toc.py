import tkinter as tk
from tkinter import messagebox

class TicTacToeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")

        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]

        self.buttons = [[tk.Button(root, text="", width=10, height=5, command=lambda row=row, col=col: self.click(row, col)) 
                         for col in range(3)] for row in range(3)]

        for row in range(3):
            for col in range(3):
                self.buttons[row][col].grid(row=row, column=col)

    def click(self, row, col):
        if self.board[row][col] == "":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if self.check_winner(row, col):
                messagebox.showinfo("Winner", f"Player {self.current_player} wins!")
                self.reset_game()
            elif self.check_draw():
                messagebox.showinfo("Draw", "It's a draw!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self, row, col):
        # Check row
        if self.board[row][0] == self.board[row][1] == self.board[row][2] != "":
            return True
        # Check column
        if self.board[0][col] == self.board[1][col] == self.board[2][col] != "":
            return True
        # Check diagonal
        if (self.board[0][0] == self.board[1][1] == self.board[2][2] != "") or \
           (self.board[0][2] == self.board[1][1] == self.board[2][0] != ""):
            return True
        return False

    def check_draw(self):
        for row in self.board:
            for cell in row:
                if cell == "":
                    return False
        return True

    def reset_game(self):
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text="")
                self.board[row][col] = ""
        self.current_player = "X"

if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeApp(root)
    root.mainloop()

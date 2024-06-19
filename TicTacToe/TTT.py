import tkinter as tk
from tkinter import messagebox

def gameboard(board):
    for i in range(3):
        for j in range(3):
            button = tk.Button(board_frame, text=board[i][j], font=('Helvetica', 24, 'bold'), width=6, height=3,
                               command=lambda row=i, col=j: on_click(row, col), bg="black", fg="white")
            button.grid(row=i, column=j, padx=5, pady=5, sticky="nsew")

def check_winner(board, player):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player: 
            return True
        if board[0][i] == board[1][i] == board[2][i] == player:  
            return True
    if board[0][0] == board[1][1] == board[2][2] == player or \
       board[0][2] == board[1][1] == board[2][0] == player:  
        return True
    return False

def get_players():
    player1 = player1_entry.get()
    player2 = player2_entry.get()
    return {'X': player1, 'O': player2}

def show_top_players():
    try:
        with open("gamescores2.txt", "r") as file:
            scores = [line.strip().split(": ") for line in file]
            if scores:
                sorted_scores = sorted(scores, key=lambda x: int(x[1]), reverse=True)
                top_players = "\n".join([f"{player}: {score} points" for player, score in sorted_scores[:3]])
                messagebox.showinfo("Top Players", f"Top 3 players:\n{top_players}")
            else:
                messagebox.showinfo("Top Players", "No scores available.")
    except FileNotFoundError:
        messagebox.showinfo("Top Players", "No scores available.")

def update_score(player):
    try:
        with open("gamescores2.txt", "r+") as file:
            lines = file.readlines()
            file.seek(0)
            updated = False
            for line in lines:
                name, score = line.strip().split(": ")
                if name == player:
                    score = str(int(score) + 1)
                    updated = True
                file.write(f"{name}: {score}\n")
            if not updated:
                file.write(f"{player}: 1\n")
            file.truncate()
    except FileNotFoundError:
        with open("gamescores2.txt", "w") as file:
            file.write(f"{player}: 1\n")

def on_click(row, col):
    global board, current_player
    if board[row][col] == " ":
        board[row][col] = current_player
        gameboard(board)
        if check_winner(board, current_player):
            messagebox.showinfo("Game Over", f"{players[current_player]} wins!")
            update_score(players[current_player])
            show_top_players()
            reset_game()
        elif all(cell != " " for row in board for cell in row):
            messagebox.showinfo("Game Over/DRAW", "All cells filled! Game Over!")
            reset_game()
        else:
            current_player = 'O' if current_player == 'X' else 'X'

def reset_game():
    global board, current_player
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    gameboard(board)

root = tk.Tk()
root.title("Tic Tac Toe")

root.columnconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

label_frame = tk.LabelFrame(root, text="Players", font=('Helvetica', 14, 'bold'))
label_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

player1_label = tk.Label(label_frame, text="Player 1 (X):", font=('Helvetica', 12, 'bold'))
player1_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
player1_entry = tk.Entry(label_frame, font=('Helvetica', 12, 'bold'))
player1_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

player2_label = tk.Label(label_frame, text="Player 2 (O):", font=('Helvetica', 12, 'bold'))
player2_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
player2_entry = tk.Entry(label_frame, font=('Helvetica', 12, 'bold'))
player2_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

start_button = tk.Button(label_frame, text="Start Game", command=lambda: start_game(), font=('Helvetica', 12, 'bold'))
start_button.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

board_frame = tk.Frame(root)
board_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

board = [[" " for _ in range(3)] for _ in range(3)]
current_player = 'X'
players = {}

def start_game():
    global players
    players = get_players()
    show_top_players()
    reset_game()

root.mainloop()
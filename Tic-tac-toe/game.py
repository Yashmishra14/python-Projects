import tkinter as tk
from tkinter import messagebox

# Winner check karne ke liye function
def check_winner():
    # Sare winning combinations check karte hain
    for combo in [[0,1,2], [3,4,5], [6,7,8], [0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]:
        if buttons[combo[0]]['text'] == buttons[combo[1]]['text'] == buttons[combo[2]]['text'] != '':
            return True
    return False

# Draw check karne ke liye function
def check_draw():
    # Agar koi button khali hai to draw nahi hai
    for button in buttons:
        if button['text'] == '':
            return False
    return True

# Button click hone par ye function chalega
def button_click(index):
    global current_player
    # Agar button pehle se click nahi hua hai aur game jeet nahi chuki
    if buttons[index]['text'] == '' and not winner:
        buttons[index]['text'] = current_player
        # Jeet check karo
        if check_winner():
            messagebox.showinfo("Tic-Tac-Toe", f"Player {current_player} wins!")
            disable_buttons()
        # Draw check karo
        elif check_draw():
            messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
            disable_buttons()
        else:
            # Player change karo
            current_player = 'O' if current_player == 'X' else 'X'
            label.config(text=f"Player {current_player}'s turn")

# Sare buttons disable karne ke liye function
def disable_buttons():
    for button in buttons:
        button.config(state=tk.DISABLED)

# Game reset karne ke liye function
def reset_game():
    global current_player, winner
    current_player = 'X'
    winner = False
    label.config(text="Player X's turn")
    for button in buttons:
        button.config(text='', state=tk.NORMAL)

# Tkinter window create karte hain
root = tk.Tk()
root.title("Tic-Tac-Toe")

current_player = 'X'
winner = False

buttons = []
# 3x3 grid ke liye buttons create karte hain
for i in range(9):
    button = tk.Button(root, text='', font=('normal', 20), width=5, height=2, command=lambda i=i: button_click(i))
    button.grid(row=i//3, column=i%3)
    buttons.append(button)

# Player turn dikhane ke liye label
label = tk.Label(root, text="Player X's turn", font=('normal', 16))
label.grid(row=3, column=0, columnspan=3)

# Reset button
reset_button = tk.Button(root, text='Reset', font=('normal', 16), command=reset_game)
reset_button.grid(row=4, column=0, columnspan=3)

# Window ko chalate hain
root.mainloop()

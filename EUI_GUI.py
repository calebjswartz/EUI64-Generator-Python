import tkinter as tk
import uuid

def generate():
    hex_characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    test = ['0', '1', '4', '5', '8', '9', 'c', 'd']
    MAC = hex(uuid.getnode())
    MAC = str(MAC.strip("0x"))
    EUI_bits = "fffe"
    first_half = MAC[:6]
    char = first_half[1]
    index = hex_characters.index(char)
    if char in test:
        index = index + 2
    else: 
        index = index - 2
    new_char = hex_characters[index]
    first_half_new = first_half[:1] + new_char + first_half[2:6]
    EUI = first_half_new + EUI_bits + MAC[6:]
    output.insert(1.0, EUI)
    output.configure(state="disabled")



window = tk.Tk()
window.title("EUI Generator")
button = tk.Button(window, text="Generate", command=generate)
output = tk.Text(window, height=1, borderwidth=0, width=25)
output.configure(inactiveselectbackground=output.cget("selectbackground"))
button.pack()
output.pack()

tk.mainloop()
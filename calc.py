import tkinter as tk

class BasicCalculator:
    def __init__(self, master):
        self.master = master
        master.title("Basic Calculator")
        master.geometry("350x500")
        master.configure(bg="black")

        self.expression = ""
        self.input_text = tk.StringVar()

        # Entry display
        self.input_frame = tk.Frame(master, bg="black")
        self.input_frame.pack()

        self.input_field = tk.Entry(self.input_frame, font=('Arial', 24), textvariable=self.input_text,
                                    width=20, bd=5, relief="flat", justify='right', bg="white")
        self.input_field.grid(row=0, column=0, ipady=20)
        self.input_field.pack(pady=10)

        # Buttons
        self.create_buttons()

    def create_buttons(self):
        buttons = [
            ['C', 'DEL', '/', '*'],
            ['7', '8', '9', '-'],
            ['4', '5', '6', '+'],
            ['1', '2', '3', '='],
            ['0', '.', '', '']
        ]

        btn_frame = tk.Frame(self.master, bg="black")
        btn_frame.pack()

        for row_index, row in enumerate(buttons):
            for col_index, item in enumerate(row):
                if item == '':
                    continue  # Skip empty slots
                button = tk.Button(
                    btn_frame,
                    text=item,
                    width=6,
                    height=3,
                    font=("Arial", 18),
                    fg="white",
                    bg="gray20",
                    bd=1,
                    command=lambda x=item: self.on_button_click(x)
                )
                button.grid(row=row_index, column=col_index, padx=5, pady=5)

    def on_button_click(self, char):
        if char == "C":
            self.expression = ""
            self.input_text.set("")
        elif char == "DEL":
            self.expression = self.expression[:-1]
            self.input_text.set(self.expression)
        elif char == "=":
            try:
                result = str(eval(self.expression))
                self.input_text.set(result)
                self.expression = result
            except:
                self.input_text.set("Error")
                self.expression = ""
        else:
            self.expression += str(char)
            self.input_text.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = BasicCalculator(root)
    root.mainloop()

import tkinter as tk
import random


class MemoryGame():

    def __init__(self, root):
        self.root = root 
        self.root.config(bg="#f0f0f0")
        
        self.root.title("Memory Matcher")
        self.symbols = list("AABBCCDDEEFFGGHH")
        random.shuffle(self.symbols)
        self.buttons = []
        self.build_ui()
        self.flipped = []
        self.matched = set()
        self.clicks = 0

    def build_ui(self):

        self.click_label = tk.Label(
            self.root,
            text = "Clicks : 0",
            font=("Arial", 14),
            bg="#f0f0f0",
            fg="#333"
            )
        self.click_label.grid(row=0, column=0, columnspan=4, pady = (10,5))
        # self.click_label.configure(font=("Arial", 14), bg="#f0f0f0",fg="#333") can change the bg by this also
       
        

        for i in range(4):
             for j in range(4):

                
                idx = 4 * i + j
                self.btn = tk.Button(
                    self.root,
                    text = "",
                    width = 5,
                    height = 2,
                    command = lambda  b = idx : self.flip(b),
                    font=("Arial", 16, "bold"),
                    bg="#e0e0e0",
                    activebackground="#d0d0d0",
                    relief="flat"
                    )
            

                # command = lambda  current_idx =idx : self.flip(current_idx) it choose one letter and store it and flip it

                self.btn.grid(row = i+1, column = j,padx = 4, pady = 4, ipadx = 4, ipady = 4)
                self.buttons.append(self.btn)

    

    def flip(self, idx):

        if idx in self.flipped or len(self.flipped) == 2 or idx in self.matched:
            return

        # self.btn.config(text = self.symbols[0])  
        # self.buttons[idx].config(text=self.symbols[idx]) passing the 16 symbol to empty buttons
        # (self.buttons[idx]['text'] = self.symbols[idx]) shorter version
        
        self.reveal_tile(idx)
        self.flipped.append(idx)
        self.clicks += 1
        self.click_label.config(text = f"Click: {self.clicks}")
        
        if len(self.flipped) == 2:
            self.root.after(500, self.check_match)

        
    def reveal_tile(self, idx):
        self.buttons[idx]["text"] = self.symbols[idx]




    def check_match(self): 
        a, b = self.flipped

        if self.symbols[a] != self.symbols[b]:
            self.buttons[a]["text"] = ""
            self.buttons[b]["text"] = ""
            
        else:
            self.matched.update(self.flipped)
            for i in (a, b):
                self.buttons[i]['bg'] = "#90ee90"
                self.buttons[i]['activebackground'] = "#90ee90"
        
        self.flipped = []

      


if __name__ == "__main__":
    root = tk.Tk()
    game = MemoryGame(root)
    root.mainloop()





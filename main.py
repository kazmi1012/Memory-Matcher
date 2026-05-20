import tkinter as tk
import random


class MemoryGame():

    def __init__(self, root):
        self.root = root 
        self.root.title("Memory Matcher")
        self.symbols = list("AABBCCDDEEFFGGHH")
        random.shuffle(self.symbols)
        self.buttons = []
        self.build_ui()
        self.flipped = []

    def build_ui(self):
        for i in range(4):

            for j in range(4):

                idx = 4 * i + j
                self.btn = tk.Button(self.root, text = "", width = 5, height = 2, command = lambda  b = idx : self.flip(b))
                # command = lambda  current_idx =idx : self.flip(current_idx) it choose one letter and store it and flip it
                self.btn.grid(row = i, column = j)
                self.buttons.append(self.btn)

    

    def flip(self, idx):

        if idx in self.flipped or len(self.flipped) == 2:
            return

        # self.btn.config(text = self.symbols[0])  
        # self.buttons[idx].config(text=self.symbols[idx]) passing the 16 symbol to empty buttons
        # (self.buttons[idx]['text'] = self.symbols[idx]) shorter version
        
        self.buttons[idx]["text"] = self.symbols[idx]
        self.flipped.append(idx)

      
        



if __name__ == "__main__":
    root = tk.Tk()
    game = MemoryGame(root)
    root.mainloop()





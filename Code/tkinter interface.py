import tkinter as tk
from tkinter import filedialog
root2 = tk.Tk()
root2.withdraw()
path =filedialog.askopenfilename()
count =0
root = tk.Tk()
root.geometry("850x550")
label_search= tk.Label(root,text = "Enter keywords")
label_search.grid(row = 0, column = 1, pady = 2)
entry = tk.Entry(root )
entry.grid(row = 2, column = 2, pady = 2)
text = tk.Text(root)
text.grid(row = 5, column = 2, pady = 2)

def get_vals():
    text.delete('1.0', tk.END)
    string = entry.get()
    text.insert(tk.END, path)
    
      

    return count
label_search= tk.Label(root,text = "Results:")
label_search.grid(row = 4, column = 1, pady = 2)

button= tk.Button(root, text ="search", command = get_vals,height=2, width=10)
button.grid(row = 3, column = 3, pady = 2)


root.mainloop()

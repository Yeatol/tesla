import tkinter as tk
from tkinter import filedialog

def browse_file(text):
    text.config(state=tk.NORMAL)
    files = filedialog.askopenfilenames(filetypes=[("图片文件", "*.png;*.jpg;*.jpeg;*.bmp;*.tiff;*.webp")])
    if files:
        try:
            for file in files:
                text.insert(tk.END, file + "\n")

        except Exception as e:
            text.insert(tk.END, f"{e}\n")
            text.config(state=tk.DISABLED)

    text.config(state=tk.DISABLED)

def main():
    root = tk.Tk()
    root.title("法线贴图生成工具")
    root.geometry("600x400")

    frame = tk.Frame(root)
    frame.pack(pady=10, padx=10, fill=tk.BOTH)

    text = tk.Text(frame, width=40, height=100)
    text.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)
    text.config(state=tk.DISABLED)

    button = tk.Button(frame, text="选择文件", command=lambda: browse_file(text))
    button.pack(side=tk.TOP, padx=10, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()

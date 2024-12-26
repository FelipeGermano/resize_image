import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageOps, ImageDraw
import os

def process_image(input_file, new_width, new_height, margin_size, output_file):
    try:
        # Abre a imagem
        img = Image.open(input_file)

        # Redimensiona a imagem
        img = img.resize((new_width, new_height))

        # Adiciona a margem
        img_with_margin = ImageOps.expand(img, border=margin_size, fill="white")

        # Adiciona a linha na margem
        draw = ImageDraw.Draw(img_with_margin)
        draw.rectangle([
            margin_size, margin_size,
            img_with_margin.width - margin_size - 1, img_with_margin.height - margin_size - 1
        ], outline="black", width=1)

        # Salva a imagem
        img_with_margin.save(output_file)
        messagebox.showinfo("Sucesso", f"Imagem salva com sucesso em {output_file}")

    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

def select_input_file():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
    input_file_var.set(file_path)

def select_output_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg")])
    output_file_var.set(file_path)

def run():
    input_file = input_file_var.get()
    output_file = output_file_var.get()

    if not input_file or not output_file:
        messagebox.showwarning("Atenção", "Você deve selecionar os arquivos de entrada e saída.")
        return

    try:
        new_width = int(width_var.get())
        new_height = int(height_var.get())
        margin_size = int(margin_var.get())
    except ValueError:
        messagebox.showerror("Erro", "Largura, altura e margem devem ser números inteiros.")
        return

    process_image(input_file, new_width, new_height, margin_size, output_file)

# Interface gráfica
root = tk.Tk()
root.title("Editor de Imagens")

# Variáveis
input_file_var = tk.StringVar()
output_file_var = tk.StringVar()
width_var = tk.StringVar()
height_var = tk.StringVar()
margin_var = tk.StringVar()

# Layout
frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

# Input file
tk.Label(frame, text="Arquivo de entrada:").grid(row=0, column=0, sticky="w")
tk.Entry(frame, textvariable=input_file_var, width=40).grid(row=0, column=1)
tk.Button(frame, text="Selecionar", command=select_input_file).grid(row=0, column=2)

# Width
tk.Label(frame, text="Largura:").grid(row=1, column=0, sticky="w")
tk.Entry(frame, textvariable=width_var).grid(row=1, column=1, sticky="w")

# Height
tk.Label(frame, text="Altura:").grid(row=2, column=0, sticky="w")
tk.Entry(frame, textvariable=height_var).grid(row=2, column=1, sticky="w")

# Margin
tk.Label(frame, text="Margem:").grid(row=3, column=0, sticky="w")
tk.Entry(frame, textvariable=margin_var).grid(row=3, column=1, sticky="w")

# Output file
tk.Label(frame, text="Arquivo de saída:").grid(row=4, column=0, sticky="w")
tk.Entry(frame, textvariable=output_file_var, width=40).grid(row=4, column=1)
tk.Button(frame, text="Selecionar", command=select_output_file).grid(row=4, column=2)

# Run button
tk.Button(frame, text="Executar", command=run, bg="green", fg="white").grid(row=5, column=0, columnspan=3, pady=10)

root.mainloop()

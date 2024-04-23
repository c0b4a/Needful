import customtkinter
import sys

#custom GUI framework
customtkinter.set_appearance_mode('system')
customtkinter.set_default_color_theme('dark-blue')

root = customtkinter.CTk()
root.title('Basic')
root.geometry('500x350')

def quit() -> None:
    sys.exit()

frame = customtkinter.CTkFrame(master = root)
frame.pack(pady = 20, padx = 60, fill = 'both', expand = True)

label = customtkinter.CTkLabel(master = frame, text = 'Hello World', font = ('Roboto', 24))
label.pack(pady = 12, padx = 10)

entry = customtkinter.CTkEntry(master = frame, placeholder_text = 'Text Box')
entry.pack(pady = 12, padx = 10)

button = customtkinter.CTkButton(master = frame, text = 'quit', command = quit)
button.pack(pady = 12, padx = 10)

checkbox = customtkinter.CTkCheckBox(master = frame, text = 'A checkbox')
checkbox.pack(pady = 12, padx = 10)

#get text from box
text = entry.get()

root.mainloop()
from customtkinter import CTk, CTkEntry, CTkButton, CTkLabel
import threading
import asyncio
from main import main

app = CTk()
app.geometry("600x400")

#def get_city():
#    city = entry.get()
#    loop.run_until_complete())

def run_async_task(city):
    result = asyncio.run(main(f'https://sinoptik.ua/pohoda/{city}'))
    label.configure(text = f"{city}:{result}")

def get_city():
    city = entry.get()
    threading.Thread(target=run_async_task, args=(city,)).start()

entry = CTkEntry(app, placeholder_text="CTkEntry")
entry.pack(padx=1, pady=1)

btn = CTkButton(app, text ="Choose City", command=get_city)
btn.pack(padx=1, pady=1)

label = CTkLabel(app, text = '')
label.pack(padx=1, pady=1)
app.mainloop()
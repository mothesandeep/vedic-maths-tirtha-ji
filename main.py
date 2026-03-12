import customtkinter as ctk
from PIL import Image

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("950x600")
app.title("VEDIC MATHS")


# ---------- Helper ----------
def clear():
    for widget in app.winfo_children():
        widget.destroy()


# ---------- Welcome Screen ----------
def welcome_screen():
    clear()

    frame = ctk.CTkFrame(app)
    frame.pack(expand=True)

    title = ctk.CTkLabel(
        frame,
        text="WELCOME TO\nVEDIC MATHS\nPOSTER SUBMISSION",
        font=("Arial", 40, "bold"),
        justify="center"
    )
    title.pack(pady=60)

    next_btn = ctk.CTkButton(frame, text="NEXT", width=200, command=menu_screen)
    next_btn.pack(pady=20)


# ---------- Menu ----------
def menu_screen():
    clear()

    frame = ctk.CTkFrame(app)
    frame.pack(expand=True)

    title = ctk.CTkLabel(frame, text="MENU", font=("Arial", 35, "bold"))
    title.pack(pady=30)

    btn1 = ctk.CTkButton(frame, text="ABOUT TEAM", width=250, command=about_team)
    btn1.pack(pady=10)

    btn2 = ctk.CTkButton(frame, text="ABOUT TIRTHA JI", width=250, command=about_tirtha)
    btn2.pack(pady=10)

    btn3 = ctk.CTkButton(frame, text="SUTRA EXPLAINATION", width=250, command=sutra_page)
    btn3.pack(pady=10)

    btn4 = ctk.CTkButton(frame, text="EXIT", width=250, command=app.destroy)
    btn4.pack(pady=10)


# ---------- About Team ----------
def about_team():
    clear()

    frame = ctk.CTkFrame(app)
    frame.pack(expand=True)

    title = ctk.CTkLabel(frame, text="GROUP 7", font=("Arial", 35, "bold"))
    title.pack(pady=20)

    member = ctk.CTkLabel(frame, text="Mothe Sandeep", font=("Arial", 25))
    member.pack(pady=10)

    back = ctk.CTkButton(frame, text="BACK", command=menu_screen)
    back.pack(pady=30)


# ---------- About Tirtha Ji ----------
def about_tirtha():
    clear()

    frame = ctk.CTkScrollableFrame(app, width=900, height=500)
    frame.pack(pady=20)

    title = ctk.CTkLabel(
        frame,
        text="Bharati Krishna Tirtha Ji",
        font=("Arial", 30, "bold")
    )
    title.pack(pady=10)

    text = """
Bharati Krishna Tirtha Ji (1884–1960) was an Indian mathematician
and scholar who rediscovered the ancient system of Vedic Mathematics.

He was a Shankaracharya of Govardhan Math, Puri.
He studied the Vedas deeply and derived 16 mathematical sutras
that make calculations very fast and simple.

His famous book 'Vedic Mathematics' explains these sutras and
their applications in arithmetic, algebra, and geometry.

These techniques help solve complex problems quickly
using mental calculations.
"""
    label = ctk.CTkLabel(frame, text=text, wraplength=800, justify="left")
    label.pack(pady=20)

    # Image
    try:
        img = Image.open("tirtha.jpg")
        img = ctk.CTkImage(img, size=(200, 250))
        img_label = ctk.CTkLabel(frame, image=img, text="")
        img_label.pack(pady=10)
    except:
        pass

    back = ctk.CTkButton(frame, text="BACK", command=menu_screen)
    back.pack(pady=20)


# ---------- Sutra Explanation ----------
def sutra_page():
    clear()

    frame = ctk.CTkFrame(app)
    frame.pack(expand=True)

    title = ctk.CTkLabel(frame, text="SUTRA: Nikhilam Navatashcaramam Dashatah",
                         font=("Arial", 28, "bold"))
    title.pack(pady=20)

    text = """
Meaning: "All from 9 and the last from 10"

This sutra is used to multiply numbers close to 10, 100, 1000 etc.

Example: 98 × 97

Step 1: Base = 100
Step 2: Find deficiency
98 → -2
97 → -3

Step 3: Cross subtract
98 - 3 = 95

Step 4: Multiply deficiencies
(-2 × -3) = 06

Step 5: Combine
Answer = 9506
"""

    label = ctk.CTkLabel(frame, text=text, wraplength=800, justify="left")
    label.pack(pady=20)

    back = ctk.CTkButton(frame, text="BACK", command=menu_screen)
    back.pack(pady=20)


# Start program
welcome_screen()

app.mainloop()
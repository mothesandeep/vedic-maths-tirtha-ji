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

    btn4 = ctk.CTkButton(frame, text="VEDIC CALCULATOR", width=250, command=vedic_calc)
    btn4.pack(pady=10)

    btn5 = ctk.CTkButton(frame, text="EXIT", width=250, command=app.destroy)
    btn5.pack(pady=10)


# ---------- About Team ----------
def about_team():
    clear()

    frame = ctk.CTkFrame(app)
    frame.pack(expand=True)

    title = ctk.CTkLabel(frame, text="GROUP 7", font=("Arial", 35, "bold"))
    title.pack(pady=20)

    member1 = ctk.CTkLabel(frame, text="Mothe Sandeep", font=("Arial", 25))
    member1.pack(pady=10)

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

    try:
        img = Image.open("tirtha.jpg")
        img = ctk.CTkImage(img, size=(200, 250))
        img_label = ctk.CTkLabel(frame, image=img, text="")
        img_label.pack(pady=10)
    except:
        pass

    text = """
•Bharati Krishna Tirtha (1884–1960) was a famous Indian mathematician, scholar, and spiritual leader.

•He was born on 14 March 1884 in Tamil Nadu, India. His original name was Venkatraman Shastri.

•From childhood, he was known for his extraordinary intelligence and excellent academic performance.

•He studied many subjects such as mathematics, Sanskrit, philosophy, history, and science.

•During his student life, he achieved very high marks and was considered one of the most brilliant students of his time.

•Later, he chose a spiritual path and became the Shankaracharya of Govardhan Math in Puri, an important spiritual position in India.

•While serving as Shankaracharya, he studied the ancient Indian scriptures, especially the Vedas.

•Through his research, he rediscovered a mathematical system called Vedic Mathematics.

•This system is based on 16 mathematical sutras (formulas) and 13 sub-sutras, which help solve mathematical problems quickly.

•His famous book Vedic Mathematics explains these formulas and their applications in arithmetic, algebra, and geometry.

•The book became popular worldwide and helped many students learn faster calculation techniques.

•Bharati Krishna Tirtha was also a great teacher, philosopher, and spiritual guide.

•His work helped revive and promote the ancient Indian knowledge system of mathematics.
"""

    label = ctk.CTkLabel(frame, text=text, wraplength=800, justify="left")
    label.pack(pady=20)


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
Meaning: All from 9 and the last from 10

This sutra is used to multiply numbers close to 100.

Example: 98 × 97

Step 1: Base = 100
Step 2: Deficiency
98 → -2
97 → -3

Step 3: Cross Subtract
98 - 3 = 95

Step 4: Multiply deficiency
(-2 × -3) = 06

Final Answer = 9506
"""

    label = ctk.CTkLabel(frame, text=text, wraplength=800, justify="left")
    label.pack(pady=20)

    back = ctk.CTkButton(frame, text="BACK", command=menu_screen)
    back.pack(pady=20)


# ---------- Vedic Calculator ----------
# ---------- Vedic Calculator ----------
def vedic_calc():
    clear()

    frame = ctk.CTkFrame(app)
    frame.pack(expand=True)

    title = ctk.CTkLabel(frame, text="VEDIC MULTIPLICATION", font=("Arial", 30, "bold"))
    title.pack(pady=20)

    num1 = ctk.CTkEntry(frame, placeholder_text="Enter First Number")
    num1.pack(pady=10)

    num2 = ctk.CTkEntry(frame, placeholder_text="Enter Second Number")
    num2.pack(pady=10)

    result_label = ctk.CTkLabel(frame, text="", font=("Arial", 20))
    result_label.pack(pady=20)

    def calculate():
        try:
            a = int(num1.get())
            b = int(num2.get())

            # automatic base detection
            max_num = max(a, b)
            base = 10 ** len(str(max_num))

            d1 = a - base
            d2 = b - base

            # left part
            left = a + d2

            # right part
            right = d1 * d2

            # digits according to base
            digits = len(str(base)) - 1
            right_part = str(abs(right)).zfill(digits)

            answer = a * b

            result_label.configure(
                text=f"""
Base = {base}

Deficiency = {d1} , {d2}

Left Part = {left}
Right Part = {right_part}

Answer = {answer}
"""
            )

        except:
            result_label.configure(text="Please enter valid numbers")

    calc_btn = ctk.CTkButton(frame, text="CALCULATE", command=calculate)
    calc_btn.pack(pady=10)

    back = ctk.CTkButton(frame, text="BACK", command=menu_screen)
    back.pack(pady=20)


# ---------- Start Program ----------
welcome_screen()

app.mainloop()


import tkinter as tk
from tkinter import PhotoImage
import webbrowser
    
def open_motivational_quote(feeling):
        quotes = {
            "really great": "Believe you can and you're halfway there. - Theodore Roosevelt",
            "great": "“A good teacher can inspire hope, ignite the imagination, and instill a love of learning.” – Brad Henry" ,
            "really good": "“You may not always have a comfortable life and you will not always be able to solve all of the world’s problems at once but don’t ever underestimate the importance you can have because history has shown us that courage can be contagious and hope can take on a life of its own.” – Michelle Obama",
            "good": "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
            "okay": "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle. - Christian D. Larson",
            "not bad" : "“Hope lies in dreams, in imagination, and in the courage of those who dare to make dreams into reality.” – Jonas Salk" ,
            "not so good": "The only way to do great work is to love what you do. - Steve Jobs",
            "Like shit":"Now I can’t stop thinking that I can’t stop thinking.-Sting",
            "bad": "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
            "terrible": "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
            "been worse":"Even tough you-re fed up, you gotta keep your head up. – Tupac",
            "never been worse": "A normal life is a boring life. -Eminem"
        }
    
        if feeling.lower() in quotes:
            quote = quotes[feeling.lower()]
        else:
            quote = "Keep going! Your future is brighter than you think."
    
        html_content = f"""
        <html>
        <head>
            <title>Motivational Quote</title>
        </head>
        <body>
            <h1 style="text-align: center;">Motivational Quote</h1>
            <p style="font-size: 44px; text-align: center;">{quote}</p>
        </body>
        </html>
        """
    
       
        with open("motivational_quote.html", "w") as file:
            file.write(html_content)
    
        
        webbrowser.open_new_tab("motivational_quote.html")
    
def create_button(feeling, row, column):
        button = tk.Button(
            text=feeling,
            width=15,
            height=3,
            bg="black",
            fg="red",
            font=("Arial", 24),
            command=lambda: open_motivational_quote(feeling)
        )
        button.grid(row=row, column=column, padx=7, pady=7)
    
    
window = tk.Tk()
window.title("Motivational Quotes")
window.configure(bg="black")
    
    
gif_image = PhotoImage(file="C:/Users/cansu/OneDrive/Masaüstü/furkan ben aka your bro/giphy.gif")
    
    
gif_label = tk.Label(image=gif_image)
gif_label.grid(row=2, columnspan=4)
    
feelings = ["Really Great", "Great", "Really Good", "Good", "Okay", "Not Bad",
                "Not so good","Like Shit", "Bad", "Terrible","Been worse", 
                "Never been worse"]
    
    
num_columns = 4
num_rows = (len(feelings) + 1) // num_columns 
button_row = num_rows + 1

for index, feeling in enumerate(feelings):
        row = button_row + index // num_columns
        column = index % num_columns
        create_button(feeling, row, column)
    
window.mainloop()
    
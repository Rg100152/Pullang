import tkinter as tk
from tkinter import messagebox
import math

# Colors (Hex se RGB)
BG_COLOR = (11, 27, 54)
CARD_COLOR = (16, 26, 48)
TEAL_COLOR = (78, 205, 196)
TEXT_GREY = (174, 181, 194)

class PullangApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Customer Login")
        self.geometry("400x650")
        self.configure(bg='#0b1b36')
        self.resizable(False, False)

        # Canvas for whole UI
        self.canvas = tk.Canvas(self, width=400, height=650, bg='#0b1b36', highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        # Draw Geometric Background
        self.draw_background()

        # Animations Y-offset
        self.anim_offset = 150
        self.target_offset = 0
        self.anim_speed = 5

        # Draw UI elements
        self.draw_ui()

        # Start Animation
        self.animate_card()

    def draw_background(self):
        # Draw abstract triangles and dots to mimic the image
        self.canvas.create_polygon(0, 500, 150, 300, 50, 650, fill="#1a3b5c", outline="")
        self.canvas.create_polygon(350, 0, 400, 50, 300, 100, fill="#1a3b5c", outline="")
        self.canvas.create_line(0, 500, 150, 300, fill="#4ecdc4", width=1)
        self.canvas.create_line(150, 300, 50, 650, fill="#4ecdc4", width=1)
        
        # Dots
        self.canvas.create_oval(148, 298, 152, 302, fill="#4ecdc4", outline="")
        self.canvas.create_oval(398, 48, 402, 52, fill="#4ecdc4", outline="")

    def draw_ui(self):
        # Card Dimensions
        card_w, card_h = 320, 430
        x1 = (400 - card_w) // 2
        y1 = 100
        x2 = x1 + card_w
        y2 = y1 + card_h

        # Draw Card (Rounded Rectangle) using smooth polygon
        self.card_id = self.create_round_rect(x1, y1 + self.anim_offset, x2, y2 + self.anim_offset, 20, fill=self.rgb(CARD_COLOR), outline="")

        # Draw Header
        self.header_id = self.create_round_rect(x1, y1 + self.anim_offset, x2, y1 + 80 + self.anim_offset, 20, fill=self.rgb(TEAL_COLOR), outline="")
        self.canvas.create_rectangle(x1, y1 + 60 + self.anim_offset, x2, y1 + 80 + self.anim_offset, fill=self.rgb(TEAL_COLOR), outline="")
        
        # Header Text
        self.canvas.create_text(x1 + card_w//2, y1 + 40 + self.anim_offset, text="CUSTOMER LOGIN", 
                                fill="#101a30", font=("Helvetica", 16, "bold"))

        # Input Fields
        input_font = ("Helvetica", 12)
        
        # Email
        self.email_var = tk.StringVar()
        self.email_entry = tk.Entry(self, textvariable=self.email_var, bg=self.rgb(CARD_COLOR), fg="white", 
                                    insertbackground="white", bd=0, font=input_font)
        self.email_entry.place(x=x1 + 60, y=y1 + 120 + self.anim_offset, width=200, height=25)
        
        self.canvas.create_text(x1 + 35, y1 + 132 + self.anim_offset, text="✉", fill="white", font=("Helvetica", 12))
        self.canvas.create_line(x1 + 30, y1 + 160 + self.anim_offset, x2 - 30, y1 + 160 + self.anim_offset, fill=self.rgb(TEXT_GREY), width=1)

        # Password
        self.pass_var = tk.StringVar()
        self.pass_entry = tk.Entry(self, textvariable=self.pass_var, bg=self.rgb(CARD_COLOR), fg="white", 
                                   insertbackground="white", bd=0, show="•", font=input_font)
        self.pass_entry.place(x=x1 + 60, y=y1 + 210 + self.anim_offset, width=200, height=25)
        
        self.canvas.create_text(x1 + 35, y1 + 222 + self.anim_offset, text="🔒", fill="white", font=("Helvetica", 12))
        self.canvas.create_line(x1 + 30, y1 + 250 + self.anim_offset, x2 - 30, y1 + 250 + self.anim_offset, fill=self.rgb(TEXT_GREY), width=1)

        # Remember Me & Forgot Password
        self.checkbox_var = tk.IntVar()
        self.check = tk.Checkbutton(self, text="Remember me", variable=self.checkbox_var, 
                                    bg=self.rgb(CARD_COLOR), fg=self.rgb(TEXT_GREY), activebackground=self.rgb(CARD_COLOR),
                                    activeforeground="white", selectcolor=self.rgb(CARD_COLOR), bd=0, font=("Helvetica", 10))
        self.check.place(x=x1 + 30, y=y1 + 270 + self.anim_offset)

        self.forgot_btn = tk.Label(self, text="Forgot Password?", bg=self.rgb(CARD_COLOR), fg=self.rgb(TEXT_GREY), font=("Helvetica", 10, "underline"))
        self.forgot_btn.place(x=x2 - 130, y=y1 + 270 + self.anim_offset)
        self.forgot_btn.bind("<Button-1>", lambda e: messagebox.showinfo("Info", "Password reset link sent!"))

        # Login Button (Custom)
        self.btn_rect = self.create_round_rect(x1 + 50, y1 + 320 + self.anim_offset, x2 - 50, y1 + 370 + self.anim_offset, 10, fill=self.rgb(TEAL_COLOR), outline="")
        self.btn_text = self.canvas.create_text(x1 + 160, y1 + 345 + self.anim_offset, text="LOGIN", fill="white", font=("Helvetica", 13, "bold"))

        # Bind Hover and Click events
        self.canvas.tag_bind(self.btn_rect, "<Enter>", self.on_hover)
        self.canvas.tag_bind(self.btn_rect, "<Leave>", self.on_leave)
        self.canvas.tag_bind(self.btn_rect, "<Button-1>", self.do_login)

    def animate_card(self):
        if self.anim_offset > self.target_offset:
            self.anim_offset -= self.anim_speed
            # Redraw everything at new position (This is a simple way to animate in Tkinter)
            self.canvas.delete("all")
            self.draw_background()
            self.draw_ui()
            self.after(16, self.animate_card)

    def on_hover(self, event):
        # Smooth color transition effect
        self.canvas.itemconfig(self.btn_rect, fill="#45bdb5")

    def on_leave(self, event):
        self.canvas.itemconfig(self.btn_rect, fill=self.rgb(TEAL_COLOR))

    def do_login(self, event):
        # Simulate a working login
        email = self.email_var.get()
        pwd = self.pass_var.get()
        
        if not email or not pwd:
            messagebox.showerror("Error", "Please fill all fields!")
        else:
            messagebox.showinfo("Success", f"Welcome {email}!\nLogin Successful!")
            # Clear fields
            self.email_var.set("")
            self.pass_var.set("")

    # Helper to convert Hex to Tkinter compatible color
    def rgb(self, rgb):
        return "#%02x%02x%02x" % rgb

    # Helper for creating a Rounded Rectangle using Canvas
    def create_round_rect(self, x1, y1, x2, y2, radius=25, **kwargs):
        points = [x1+radius, y1,
                  x1+radius, y1,
                  x2-radius, y1,
                  x2-radius, y1,
                  x2, y1,
                  x2, y1+radius,
                  x2, y1+radius,
                  x2, y2-radius,
                  x2, y2-radius,
                  x2, y2,
                  x2-radius, y2,
                  x2-radius, y2,
                  x1+radius, y2,
                  x1+radius, y2,
                  x1, y2,
                  x1, y2-radius,
                  x1, y2-radius,
                  x1, y1+radius,
                  x1, y1+radius,
                  x1, y1]
        return self.canvas.create_polygon(points, **kwargs, smooth=True)

if __name__ == "__main__":
    app = PullangApp()
    app.mainloop()

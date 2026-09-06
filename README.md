🔐 Pullang

<p align="center">
  <strong>Modern Customer Login GUI</strong>
</p><p align="center">
  A lightweight desktop authentication interface built with Python & Tkinter.
</p><p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Tkinter-GUI-4ecdc4?style=for-the-badge" alt="Tkinter">
  <img src="https://img.shields.io/badge/Desktop-Application-101a30?style=for-the-badge" alt="Desktop Application">
  <img src="https://img.shields.io/github/license/Rg100152/Pullang?style=for-the-badge" alt="License">
</p>---

⚡ About

Pullang is a lightweight desktop Customer Login GUI developed with Python's built-in Tkinter framework.

The project focuses on creating a clean and modern authentication interface with a dark navy background, teal accents, geometric graphics and a simple card entrance animation.

It is designed as a foundation for learning and building Python desktop GUI applications.

---

✨ Features

- 🔐 Customer Login interface
- 📧 Email input
- 🔑 Password input with masking
- ☑️ Remember Me checkbox
- 🔄 Forgot Password interaction
- 🎬 Login-card entrance animation
- 🎨 Dark modern interface
- 💎 Teal accent design
- 🔺 Geometric background graphics
- 🖱️ Interactive login button
- ✅ Empty-field validation
- 💬 Success/error dialogs
- 🧹 Automatic input clearing
- 🪶 Lightweight implementation
- 📦 Minimal dependencies

---

🖥️ UI Layout

┌──────────────────────────────────────┐
│                                      │
│       ┌────────────────────────┐     │
│       │    CUSTOMER LOGIN      │     │
│       ├────────────────────────┤     │
│       │                        │     │
│       │   ✉  Email             │     │
│       │  ────────────────────  │     │
│       │                        │     │
│       │   🔒 Password          │     │
│       │  ────────────────────  │     │
│       │                        │     │
│       │ ☑ Remember me          │     │
│       │              Forgot?   │     │
│       │                        │     │
│       │      ┌──────────┐      │     │
│       │      │  LOGIN   │      │     │
│       │      └──────────┘      │     │
│       │                        │     │
│       └────────────────────────┘     │
│                                      │
└──────────────────────────────────────┘

---

🛠️ Tech Stack

Technology| Purpose
Python 3| Application logic
Tkinter| Desktop GUI
Canvas| Custom graphics and UI
messagebox| Dialog messages
StringVar / IntVar| Form state management

No external GUI framework is required.

---

📂 Project Structure

Pullang/
│
├── Python source file
├── README.md
└── LICENSE

The application is designed to remain lightweight and easy to understand.

---

⚙️ Requirements

- Python 3.x
- Tkinter
- Windows / Linux / macOS desktop environment

Check Python:

python3 --version

Check Tkinter:

python3 -m tkinter

---

🚀 Installation

Clone the repository

git clone https://github.com/Rg100152/Pullang.git

Enter the project directory

cd Pullang

Run the application

python3 main.py

On Windows:

python main.py

«Replace "main.py" with the actual Python filename if your repository uses a different filename.»

---

🎬 Animation

Pullang includes a simple card entrance animation.

The login card starts below its final position and gradually moves upward using Tkinter's event scheduler.

self.after(16, self.animate_card)

This keeps the application dependency-free while providing a smoother UI experience.

---

🎨 Color System

Pullang uses a dark navy + teal visual identity.

Element| Value
Background| "#0b1b36"
Card| "#101a30"
Primary Accent| "#4ecdc4"
Secondary Text| "#aeb5c2"
Header Text| "#101a30"

The colors are defined near the beginning of the Python source and can be customized easily.

---

🔐 Login Flow

The current login functionality is intended for demonstration purposes.

Workflow

User enters email
       ↓
User enters password
       ↓
     LOGIN
       ↓
Check empty fields
   ↙          ↘
Empty       Filled
 ↓             ↓
Error       Success
Dialog      Dialog
               ↓
        Clear input fields

The application does not currently connect to a real authentication server or database.

---

🔑 Forgot Password

The Forgot Password? option currently displays an informational dialog.

It is a simulated UI interaction and does not send an actual password-reset email.

---

🧩 Customization

The primary visual settings can be changed through the color constants:

BG_COLOR = (11, 27, 54)
CARD_COLOR = (16, 26, 48)
TEAL_COLOR = (78, 205, 196)
TEXT_GREY = (174, 181, 194)

You can customize:

- Window size
- Card size
- Colors
- Fonts
- Animation speed
- Button design
- Background geometry
- Dialog messages
- Input behaviour

---

🔮 Roadmap

- [ ] Real authentication system
- [ ] SQLite database
- [ ] User registration
- [ ] Secure password hashing
- [ ] Real password-reset system
- [ ] Email verification
- [ ] Password visibility toggle
- [ ] Login attempt protection
- [ ] Persistent Remember Me
- [ ] User dashboard
- [ ] Application settings
- [ ] Custom application icon
- [ ] Windows executable
- [ ] Linux package

---

🔒 Security Notes

Pullang is currently a frontend-style desktop authentication demonstration.

For production authentication:

- Never store plaintext passwords.
- Use secure password hashing such as Argon2id or bcrypt.
- Validate credentials through a trusted backend.
- Use secure session handling.
- Implement rate limiting.
- Protect authentication APIs.
- Never hard-code secrets into the application.

---

🤝 Contributing

Contributions, bug fixes and UI improvements are welcome.

Basic workflow

git clone https://github.com/Rg100152/Pullang.git
cd Pullang

Make your changes, test the application and submit a pull request.

---

📜 License

Pullang is distributed under the license included in this repository.

See the "LICENSE" file for the complete license terms.

---

👨‍💻 Author

Raj Gautam

BCA Student · Frontend Developer · Cybersecurity Enthusiast

GitHub: "@Rg100152" (https://github.com/Rg100152)

---

⭐ Support

If you like Pullang, consider giving the repository a ⭐ on GitHub.

<p align="center">🔐 PULLANG

Python • Tkinter • Desktop GUI

</p><p align="center">
  <sub>© 2026 Raj Gautam</sub>
</p><img width="525" height="394" alt="image" src="https://github.com/user-attachments/assets/c7785feb-fb4f-4c15-9302-cd5a12b321a5" />

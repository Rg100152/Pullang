🔐 Pullang

<p align="center">
  <strong>Modern Customer Login GUI</strong>
</p><p align="center">
  A lightweight desktop authentication interface built with Python & Tkinter.
</p><p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Tkinter-GUI-00A86B?style=for-the-badge">
  <img src="https://img.shields.io/badge/Desktop-App-4ecdc4?style=for-the-badge">
  <img src="https://img.shields.io/github/license/Rg100152/Pullang?style=for-the-badge">
</p>---

✦ Overview

Pullang is a lightweight desktop Customer Login GUI developed using Python's built-in Tkinter library.

The application combines a dark modern interface with teal accents, geometric background elements, an animated login card and interactive form controls.

It is designed as a simple foundation for experimenting with desktop authentication interfaces and Tkinter GUI development.

«Pullang — Clean desktop UI with a modern login experience.»

---

✨ Features

- 🔐 Customer login interface
- 📧 Email input field
- 🔑 Password input with masking
- ☑️ Remember Me checkbox
- 🔄 Forgot Password interaction
- 🚀 Animated login-card entrance
- 🎨 Dark navy UI
- 💎 Teal/cyan accent color system
- 🔺 Geometric background artwork
- 🖱️ Login button hover effect
- ✅ Basic empty-field validation
- 💬 Success and error message dialogs
- 🧹 Automatic form clearing after successful login
- 🪶 Lightweight Tkinter implementation
- 📦 No external Python GUI framework required

---

🖥️ Interface

The application opens as a compact 400 × 650 desktop window.

┌──────────────────────────────────────┐
│                                      │
│       ╔════════════════════════╗     │
│       ║    CUSTOMER LOGIN      ║     │
│       ╠════════════════════════╣     │
│       ║                        ║     │
│       ║   ✉  Email             ║     │
│       ║  ────────────────────  ║     │
│       ║                        ║     │
│       ║   🔒 Password          ║     │
│       ║  ────────────────────  ║     │
│       ║                        ║     │
│       ║ ☑ Remember me          ║     │
│       ║              Forgot?   ║     │
│       ║                        ║     │
│       ║      ┌──────────┐      ║     │
│       ║      │   LOGIN  │      ║     │
│       ║      └──────────┘      ║     │
│       ╚════════════════════════╝     │
│                                      │
└──────────────────────────────────────┘

---

🛠️ Technology Stack

Technology| Purpose
Python 3| Application logic
Tkinter| Desktop GUI
Canvas| Custom UI graphics
messagebox| Login/error dialogs
math| Supporting Python functionality

Tkinter is included with standard Python installations on most desktop platforms, so the project has minimal dependencies.

---

📂 Project Structure

Pullang/
│
├── main.py
└── README.md

«Rename "main.py" in this section if your Python source file has a different filename in the repository.»

---

⚙️ Requirements

- Python 3.x
- Tkinter
- Desktop operating system

Check Python

python3 --version

Check Tkinter

python3 -m tkinter

If a small Tkinter test window appears, Tkinter is available.

---

🚀 Installation

1. Clone the repository

git clone https://github.com/Rg100152/Pullang.git

2. Enter the project

cd Pullang

3. Run the application

python3 main.py

On Windows:

python main.py

---

🎬 Animation

Pullang includes a simple entrance animation for the login card.

The card initially starts below its final position and progressively moves upward until it reaches its target position.

The animation is implemented using Tkinter's:

after()

method, avoiding external animation libraries.

---

🎨 Color Palette

The interface uses a dark navy and teal visual system.

Component| Color
Background| "#0b1b36"
Card| "#101a30"
Primary Accent| "#4ecdc4"
Secondary Text| "#aeb5c2"
Header Text| "#101a30"

The colors can be customized from the constants near the beginning of the Python source.

---

🔐 Login Behaviour

The current application demonstrates frontend-style login behaviour inside a desktop GUI.

When the user presses LOGIN:

1. Email and password values are collected.
2. Empty fields are checked.
3. An error dialog appears if required fields are missing.
4. Otherwise, a success dialog is displayed.
5. The input fields are cleared.

Important

This project does not currently authenticate against a real server or database.

The login is a UI/demo implementation.

---

🔑 Forgot Password

The Forgot Password? control currently displays an informational dialog:

Password reset link sent!

It is a simulated interaction and does not send an actual email or reset a real account password.

---

🧩 Customization

You can modify the application's visual identity by changing:

BG_COLOR = (11, 27, 54)
CARD_COLOR = (16, 26, 48)
TEAL_COLOR = (78, 205, 196)
TEXT_GREY = (174, 181, 194)

You can also customize:

- Window dimensions
- Card dimensions
- Animation speed
- Fonts
- Button appearance
- Background geometry
- Input fields
- Dialog messages

---

🔮 Roadmap

Possible future improvements:

- [ ] Real authentication backend
- [ ] SQLite database integration
- [ ] User registration
- [ ] Password hashing
- [ ] Real password-reset workflow
- [ ] Email verification
- [ ] Password visibility toggle
- [ ] Login attempt rate limiting
- [ ] Remember-me persistence
- [ ] User dashboard
- [ ] Settings panel
- [ ] Custom application icon
- [ ] Windows executable build
- [ ] Linux package
- [ ] Improved accessibility

---

🔒 Security

Pullang is currently a GUI demonstration project.

For a production authentication application:

- Never store plaintext passwords.
- Use strong password hashing such as Argon2id or bcrypt.
- Validate credentials on the server/backend.
- Use secure session management.
- Protect authentication APIs.
- Implement rate limiting.
- Avoid placing secrets directly inside the client application.

---

📸 Screenshots

Add screenshots to the repository and display them here:

![Pullang Login](assets/pullang-login.png)

Recommended structure:

Pullang/
│
├── assets/
│   └── pullang-login.png
│
├── main.py
├── README.md
└── LICENSE

---

🤝 Contributing

Contributions and UI improvements are welcome.

Contribution workflow

git clone https://github.com/Rg100152/Pullang.git
cd Pullang

Create your changes, test the application and submit a pull request.

---

📄 License

Pullang is distributed under the license included in this repository.

See the "LICENSE" file for the complete terms.

---

👨‍💻 Author

Raj Gautam

BCA Student · Frontend Developer · Cybersecurity Enthusiast

GitHub: "@Rg100152" (https://github.com/Rg100152)

---

⭐ Support

If you find Pullang useful or like the interface, consider giving the repository a ⭐.

<p align="center">🔐 Pullang

Python • Tkinter • Desktop GUI • Modern UI

</p><p align="center">
  <sub>© 2026 Raj Gautam</sub>
</p><img width="525" height="394" alt="image" src="https://github.com/user-attachments/assets/e257c732-945e-494a-946b-1688db1fd1a0" />

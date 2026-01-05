# 🔐 Cryptography CLI Tool

A Python **command-line cryptography application** that I built as an **educational project** to better understand **classical encryption, decryption, and basic cryptanalysis**, while also learning how to design a clean and structured CLI application.

## ✨ Features

### 🔒 Encryption
I implemented several classical ciphers:
- **Caesar Cipher**
- **ROT family**
  - ROT13
  - ROT18 (letters + digits)
  - ROT47 (printable ASCII)
- **Affine Caesar Cipher**
  - Manual keys
  - Automatic key generation
- **Polyalphabetic Caesar Cipher**
- **Vigenère Cipher**
- **One-Time Pad (OTP)**
  - XOR-based encryption
  - Random key generation
  - Symmetric encryption/decryption

---

### 🔓 Decryption
Decryption is implemented progressively, from the simplest case to the hardest:

1. **Method + key known**
2. **Method known, key unknown** *(in progress)*
3. **Key known, method unknown** *(in progress)*
4. **No information at all (full brute-force & cryptanalysis)** *(in progress)*

---

### 📁 File Export System
I implemented a dynamic file creation system:
- Timestamp-based filenames
- Interactive menu to choose what gets written:
  - ASCII header
  - Cipher method
  - Original text
  - Key
  - Encrypted / decrypted text
  - Date & time
- Only selected information is saved (no useless data)

---

### 🧭 User Interface
- Arrow-based menus (↑ ↓)
- Keyboard navigation (Enter / Escape)
- Dynamic menus with live state updates
- Colored output using **Colorama**
- ASCII titles using **pyfiglet**
- Intro animation (ASCII art)
- English / French language support
- Result preview before saving to file

---

### 🧠 Architecture Highlights
- Dispatch-based menus (dynamic function routing)
- Clear separation between:
  - menus
  - ciphers
  - UI components
  - file handling
- Modular folder structure

---

## ▶️ How to Run

```bash 
python main.py
```
---

## 🎯 My Approacht

This is an educational project built to learn Python fundamentals, modular code, and basic cryptography. I intentionally chose **not to use Object-Oriented Programming** in this project I focused on **functional and procedural logic**, clarity, and readability

### 🤖 How I Use AI (and how I don’t)

I didn’t use AI to generate code.

My workflow is:
1. I **think and struggle first**
2. If I’m blocked, I **search documentation or online resources**
3. Only then do I ask an AI for:
   - detailed explanations
   - conceptual help
   - understanding mistakes or alternative approaches

⚠️ No copy-paste from AI  
Every line of code is written by me, understood, and adapted.

---
### Video and resource that inspired this project
  (French 🇫🇷)
1. https://youtu.be/iy4egJKTKtE?si=1bso1Rhrr243sUay
2. https://youtu.be/0JnC1jJa8C8?si=zRNn1OkSzV_yE8VK
3. https://youtu.be/-gJuGFFTsgo?si=7nvwjWRtHGbvSnib
4. https://youtu.be/f7VBEserHxs?si=TBPUmiPwxEvGXBpR
5. https://youtu.be/mHkTzO6U_Ag?si=8gCDuJsg5jAkgjZ1
  (English 🇬🇧)
6. https://youtu.be/QYng_rXg5OQ?si=3wnI6d3UlI4p2KPr
7. https://youtu.be/a64NnBSq8oA?si=awDKOspuVZBUnqve
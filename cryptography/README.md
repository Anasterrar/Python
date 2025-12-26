# 🔐 Cryptography CLI Tool

A Python **command-line cryptography application** designed to explore and understand **classical encryption, decryption, and cryptanalysis techniques**.

This project is **educational** and focuses on learning:
- how classical ciphers work
- how to design a clean CLI application
- how to approach brute-force attacks and scoring systems

---

## ✨ Features

### 🔒 Encryption
Implemented classical ciphers:
- Caesar Cipher
- ROT13
- ROT18 (letters + digits)
- ROT47 (printable ASCII)
- Affine Caesar Cipher
- Polyalphabetic Caesar Cipher
- Vigenère Cipher

---

### 🔓 Decryption (Work in Progress)
Decryption is implemented progressively, from simplest to most complex cases:

1. **Method + key known**
2. **Method known, key unknown**
3. **Key known, method unknown**
4. **No information (full brute-force & cryptanalysis)**

---

### 📊 Cryptanalysis (Planned)
- Dictionary-based word detection
- Letter frequency analysis
- Bigram / trigram scoring
- Language-based scoring (EN / FR)
- Automatic best-candidate selection

---

### 📁 File Encryption & Decryption (Planned)
- Encrypt full text files
- Decrypt files using known keys or brute-force
- UTF-8 safe processing
- Automatic output file generation

---

### 🧭 User Interface
- Arrow-based menus (↑ ↓)
- Keyboard navigation (Enter / Escape)
- Colorized output using **Colorama**
- ASCII titles using **pyfiglet**
- Multi-language support (English / French)
- Result preview and export to files

---

## 🛠 Technologies
- Python 3
- colorama
- pyfiglet
- msvcrt (Windows keyboard input)

---

## ▶️ Usage

Run the main script:
```bash
python main.py
```
This is an educational project built to learn Python fundamentals, modular code, and basic cryptography.

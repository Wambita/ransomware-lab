
# Ransomware-lab (Educational Project)

> **Strictly for educational and cybersecurity learning purposes only.**
> This project is designed to help understand file encryption, key derivation, and secure file handling in a controlled lab environment.

---

##  Project Overview

`ransomware-lab` is a cybersecurity learning project that demonstrates:

* Symmetric encryption using AES-256 (CBC mode)
* Key derivation using Scrypt
* File and directory traversal in Python
* Secure random token generation
* Encryption and decryption workflows
* Cross-platform path handling (Windows, Linux, macOS)

The goal of this project is to understand **how file encryption works**, so that students can better defend against real-world ransomware threats.

---

##  Learning Objectives

By working on this project, you will learn:

* How encryption transforms plaintext into ciphertext
* How salts and IVs improve cryptographic security
* How passwords/tokens are converted into encryption keys
* How to safely handle files in binary mode
* How to recursively process directories
* Why proper key management is critical for recovery

---

##  Important Disclaimer

This project:

*  Must NOT be used on systems you do not own.
*  Must NOT be used to harm, extort, or damage data.
*  Must NOT be executed on important personal or production files.

Always test inside:

* A virtual machine (VM)
* A controlled lab environment
* A dedicated test folder with dummy files

The author assumes no responsibility for misuse.

---

## 🛠 Requirements

* Python 3.8+
* `cryptography` library

Install dependencies:

```bash
pip install cryptography
```


#  Usage (Safe Educational Testing Only)

>  **This project must only be used inside a controlled lab environment.**
>
> Do NOT run this on your main operating system.
> Do NOT use real personal or important files.

---

## 1. Use a Virtual Machine (Required)

For safety, test this project inside a virtual machine (VM).

Recommended tools:

* VirtualBox
* VMware
* Any Linux VM environment

Steps:

1. Install a VM.
2. Create a fresh Linux virtual machine.
3. Clone this repository inside the VM.
4. Use only dummy test files.

This ensures:

* Your real files are protected.
* Any mistakes remain isolated.
* You can reset the VM if needed.

---

##  2. Clone the Repository

Inside your virtual machine:

```bash
git clone https://learn.zone01kisumu.ke/git/shfana/ransomware-lab.git
cd ransomware-lab
```

---

## 3. Create a virtual environment (Recommended) 

```bash
python3 -m venv venv
source venv/bin/activate # linux/mac os
```

- On windows
```bash
venv\Scripts\activate
```
---

## 4. Install Dependencies
```bash
pip install -r requirements.txt
```
This will install everything the project needs

## 5. Create a Test Folder

Create a safe folder with dummy files:

```bash
mkdir ~/Desktop/test
```

Add some sample `.txt` files inside the `test` folder.

 Do NOT use important data.

---

## 5. Encrypt the Folder

Run:

```bash
python3 Ransomware_Encrypt.py
```

The program will:

* Encrypt files inside `~/Desktop/test`
* Generate the  recovery token
* Create a ransomware page informing user that their files have been encrypted and instructions to recover their account (ransomware simulation - educational purposes only)

---

## 6. Save the Generated Token

- Open the generated file containing the token.

- Copy the token. For simulation purposes, you send the  token to the given email

---

### Decryption( Recovering the files (Attacker pov))

## 7. Decrypt the Files

Run:

```bash
python decrypt.py

Enter recovery token: (Enter the token that was generated when the  files  were encrypted / code sent to you)
```

The program will:

* Locate `.enc` files
* Use the provided token
* Restore original files

---

#  Safety Guidelines

* Only test inside a virtual machine.
* Only use dummy test files.
* Never execute on production systems.
* Never execute on systems you do not own.
* Do not modify system directories.
* Always maintain backups in real-world scenarios.

---

#  Why Use a VM?

This project intentionally modifies files to simulate encryption behavior.

Using a VM ensures:

* You can revert to a clean snapshot.
* You avoid accidental data loss.
* You practice responsible security research.

---

#  Educational Purpose

This lab is designed to help students understand:

* How encryption works in practice
* Why key management is critical
* How ransomware technically operates
* Why defensive strategies (backups, isolation, monitoring) matter

Understanding attack mechanics helps build stronger defenses.

---

##  How It Works

### Encryption Flow

1. A secure random token is generated.
2. A random salt is created.
3. A key is derived using Scrypt.
4. A random IV is generated.
5. Data is padded (PKCS7).
6. Data is encrypted using AES-256-CBC.
7. The encrypted file is saved as `.enc`.

Encrypted file structure:

```
[salt (16 bytes)] + [IV (16 bytes)] + [ciphertext]
```

---

### Decryption Flow

1. The salt and IV are extracted.
2. The same token is used to derive the key.
3. Ciphertext is decrypted.
4. Padding is removed.
5. Original file is restored.

If the token is incorrect, decryption fails.


## Security Concepts Demonstrated

* AES-256 symmetric encryption
* Scrypt key derivation function (KDF)
* Secure random generation with `secrets`
* Salted password-based encryption
* Cross-platform filesystem handling



## Educational Value

This lab helps learners:

* Understand how ransomware technically operates
* Appreciate the importance of backups
* Learn secure cryptographic design
* Practice defensive cybersecurity thinking

Understanding the attack mechanism is essential for building strong defenses.

---

##  Future Improvements (Educational Ideas)

* Add logging
* Add file integrity verification
* Add backup simulation
* Add audit mode (dry run without encryption)
* Add GUI interface for demonstration

---

##  Author
### Wambita Sheila Fana
Cybersecurity & systems learning project focused on cryptography and secure software engineering.

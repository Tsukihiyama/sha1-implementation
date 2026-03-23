# SHA-1 Hash Implementation

A from-scratch implementation of the SHA-1 (Secure Hash Algorithm 1) cryptographic hash function.
This project focuses on understanding how hashing works internally — including padding, message scheduling, and bitwise operations.

---
##  What is SHA-1?

SHA-1 is a cryptographic hash function that takes an input of arbitrary length and produces a fixed 160-bit (20-byte) hash.
Example:
```
input:  "hello"
output: "aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d"
```
---
##  Implementation

1. **Padding the Message**
   - Append a `1` bit followed by `0`s
   - Add original message length at the end

2. **Divide into 512-bit Blocks**

3. **Initialize Hash Values**
   - Five 32-bit constants (H0–H4)

4. **Message Schedule Expansion**
   - Extend 16 words → 80 words using bitwise operations

5. **Main Loop (80 rounds)**
   - Uses logical functions and left rotations

6. **Final Hash**
   - Combine results into a 160-bit output
---
## How to Run

### Python
```bash
python sha1.py
```
## SHA-1 Weaknesses

You can also check the `shattered.py` file included in this repository.

It demonstrates how SHA-1 can be broken using known collision attacks, inspired by the SHAttered attack — the first practical collision for SHA-1.

This highlights why SHA-1 is no longer considered secure for cryptographic use.
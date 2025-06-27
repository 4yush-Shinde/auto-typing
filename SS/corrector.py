# corrector.py

# Read the original
with open("data.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Replace digit 1 with lowercase l
corrected_text = text.replace("1", "l").replace("0", "O")

# Overwrite data.txt
with open("data.txt", "w", encoding="utf-8") as f:
    f.write(corrected_text)

print("✅ Corrections applied and saved to data.txt")

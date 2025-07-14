import os
import time
import sys
import pyautogui
from pdfminer.high_level import extract_text
from tkinter import Tk, messagebox

# === Paths ===
downloads = os.path.join(os.path.expanduser("~"), "Downloads")
pdf_name = "Key Fusion Page Typing.pdf"
pdf_path = os.path.join(downloads, pdf_name)

output_dir = r"C:\Users\shind\Desktop\Python Script\SS\Final"
data_txt = os.path.join(output_dir, "data.txt")

# === Simulate Ctrl+P Save PDF ===
time.sleep(0.8)  # slight delay before starting
pyautogui.hotkey('ctrl', 'p')    # open print dialog
time.sleep(1)
pyautogui.press('enter')         # confirm 'Save as PDF'
time.sleep(1)
pyautogui.press('enter')         # confirm default save
print("📄 PDF Save triggered...")

# === Wait for PDF to appear ===
for _ in range(20):  # up to 10 seconds
    if os.path.exists(pdf_path):
        break
    time.sleep(0.5)
else:
    Tk().withdraw()
    messagebox.showerror("❌ Error", f"PDF not found:\n{pdf_path}")
    sys.exit(1)

# === Extract Text (Preserving Double Spaces) ===
text = extract_text(pdf_path)

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

with open(data_txt, "w", encoding="utf-8") as f:
    f.write(text)

# === Delete PDF After Extraction ===
try:
    os.remove(pdf_path)
except Exception as e:
    print(f"⚠️ Could not delete PDF: {e}")

# === Success Popup ===
Tk().withdraw()
messagebox.showinfo("✅ Done", f"Text extracted and saved to:\n{data_txt}")

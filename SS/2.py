import pyautogui
import time

# Load fields from file
with open("data.txt", "r", encoding="utf-8") as f:
    fields = [line.strip() for line in f if line.strip()]

# Check for exactly 9 fields
if len(fields) != 9:
    print(f"⚠️ Expected 9 fields but found {len(fields)}")
    exit()

print("⌛ You have 1.5 seconds to click in the first input field...")
time.sleep(1.5)

# Type each field, then press Tab to switch
for i, field in enumerate(fields):
    print(f"⌨️ Typing Field {i + 1}")
    pyautogui.write(field, interval=0.00001)  # Fast typing
    pyautogui.press("tab")                 # Move to next field
    time.sleep(0.2)

print("✅ Done typing all 9 fields!")

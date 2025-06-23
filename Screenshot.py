import pyautogui
import time
from PIL import ImageGrab
from datetime import datetime
import os

# Create output folder if it doesn't exist
save_dir = "SavedScreenshots"
os.makedirs(save_dir, exist_ok=True)

# Trigger Windows Snipping Tool (Win + Shift + S)
print("📸 Launching Snipping Tool (Win + Shift + S)...")
pyautogui.hotkey('win', 'shift', 's')

# Wait for screenshot to complete
print("⌛ Waiting for you to take the screenshot...")
time.sleep(3)  # Wait for user to snip

# Grab image from clipboard
img = ImageGrab.grabclipboard()

if img:
    # Use timestamp for unique file name
    filename = f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    full_path = os.path.join(save_dir, filename)

    img.save(full_path)
    print(f"✅ Screenshot saved to {full_path}")
else:
    print("❌ No image found in clipboard. Try again.")

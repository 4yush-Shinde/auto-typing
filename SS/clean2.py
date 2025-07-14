import re

# Read the raw PDF-extracted text
with open("data.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

cleaned_lines = []

for line in lines:
    line = line.strip()

    # Only keep lines that start with "Field X:" (case insensitive)
    if re.match(r"^Field\s*\d+\s*:", line, re.IGNORECASE):
        # Remove the label (e.g., "Field 3: ")
        cleaned_line = re.sub(r"^Field\s*\d+\s*:\s*", "", line)
        cleaned_lines.append(cleaned_line)

# Save cleaned output back to the same file
with open("data.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(cleaned_lines))

print("✅ Cleaned: only field text preserved, everything else removed.")

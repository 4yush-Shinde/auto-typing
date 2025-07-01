import re

# read the data
with open("data.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

cleaned_lines = []
for line in lines:
    # remove patterns like "Field 1: ", "Field 2: ", etc.
    cleaned_line = re.sub(r"^Field\s*\d+\s*:\s*", "", line.strip())
    cleaned_lines.append(cleaned_line)

# overwrite data.txt with cleaned data
with open("data.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(cleaned_lines))

print("✅ Field labels removed from data.txt successfully.")

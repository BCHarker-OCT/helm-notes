import sys
import re

def generate_toc(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    toc = []
    in_code_block = False

    for line in lines:
        # Detect the start or end of a multi-line code block (```)
        if line.strip().startswith('```'):
            in_code_block = not in_code_block
            continue

        # Skip processing if inside a multi-line code block
        if in_code_block:
            continue

        # Ignore lines containing inline code marked by backticks (`something`)
        if re.search(r'`.*`', line):
            continue

        # Match headings (from # to ######)
        header_match = re.match(r'^(#+)\s+(.*)', line)
        if header_match:
            header_level = len(header_match.group(1))  # Count the number of '#' to get the header level
            header_text = header_match.group(2).strip()

            # Create the anchor link (convert text to lowercase, replace spaces with hyphens, remove special characters)
            anchor = re.sub(r'[^\w\s-]', '', header_text).strip().lower().replace(' ', '-')

            # Build markdown list with link
            indent = '   ' * (header_level - 1)  # Adjust indentation based on header level (starting from #)
            if header_level == 1:
                toc.append(f"{indent}- [{header_text}](./{filename})")
            else:
                toc.append(f"{indent}- [{header_text}](./{filename}#{anchor})")

    return toc


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python generate_toc.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    toc = generate_toc(filename)

    # Output the TOC
    for item in toc:
        print(item)

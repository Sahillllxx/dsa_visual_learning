
# Read file as latin-1 (which is how the browser sees the bytes)
with open('leetcode_constraints.html', 'rb') as f:
    raw = f.read()

# Try decoding as latin-1 to see what the browser sees
try:
    latin = raw.decode('latin-1')
    # Check for mojibake patterns (UTF-8 bytes misread as latin-1)
    if 'â€' in latin or 'â‰' in latin or 'â†' in latin:
        print("File is UTF-8 but browser reads as latin-1 - fixing...")
        # Decode as latin-1, re-encode as raw bytes, then decode as UTF-8
        fixed = raw.decode('utf-8')
        # Now replace all non-ASCII with HTML entities
        result = []
        for ch in fixed:
            cp = ord(ch)
            if cp > 127:
                result.append(f'&#{cp};')
            else:
                result.append(ch)
        fixed_content = ''.join(result)
        with open('leetcode_constraints.html', 'w', encoding='ascii') as f:
            f.write(fixed_content)
        print("Fixed! All non-ASCII chars replaced with HTML entities.")
    else:
        print("No mojibake found")
except Exception as e:
    print(f"Error: {e}")


from pathlib import Path
import re
file = Path("android/app/src/main/AndroidManifest.xml")
if not file.exists():
    raise SystemExit("AndroidManifest.xml not found")
text = file.read_text(encoding="utf-8")
pattern = r'<activity\b(?=[^>]*android:name="\.MainActivity")[^>]*>'
m = re.search(pattern, text, re.DOTALL)
if not m:
    raise SystemExit("MainActivity not found")
a = m.group(0)
if 'android:screenOrientation=' in a:
    a = re.sub(r'android:screenOrientation="[^"]*"', 'android:screenOrientation="portrait"', a)
else:
    a = a[:-1] + ' android:screenOrientation="portrait">'
file.write_text(text[:m.start()] + a + text[m.end():], encoding="utf-8")
print("OK: portrait enforced")

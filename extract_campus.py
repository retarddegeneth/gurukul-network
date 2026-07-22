import re
with open('/data/data/com.termux/files/home/gurukul-network/vercel_campus.html') as f:
    vercel = f.read()
m = re.search(r'<main[^>]*>(.*?)</main>', vercel, re.DOTALL)
main_content = m.group(1).strip() if m else ''
with open('/data/data/com.termux/files/home/gurukul-network/campus_main.txt', 'w') as f:
    f.write(main_content)
print('wrote', len(main_content), 'chars')

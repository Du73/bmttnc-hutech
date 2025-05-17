print("Nhap cac dong van ban (nhap 'done' de dung):")
lines=[]
while True:
    line = input()
    if line.lower() == 'done':
        break
    lines.append(line)
print("So dong van ban da nhap la:", len(lines))
for line in lines:
    print(line.upper())
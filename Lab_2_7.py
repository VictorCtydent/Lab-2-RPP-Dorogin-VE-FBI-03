text = input('Введите произвольную строку: ')
count = 0
new_str = ""
mid = 0
if len(text) % 2 == 0:
    mid = len(text) // 2
else:
    mid = len(text) // 2 + 1

for i in range(mid):
    if text[i] == '!':
        new_str += "%"
        count += 1
    else:
        new_str += text[i]

for i in range(mid, len(text)):
    new_str += text[i]
print(f"Количество замененных символов: {count}")
print(f"Новая строка: {new_str}")

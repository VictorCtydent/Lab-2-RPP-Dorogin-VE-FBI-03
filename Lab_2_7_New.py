text = input('Введите произвольную строку: ')
count = 0
new_str = ""
for i in range(len(text)//2 + 1):
    if text[i] == '!':
        new_str += "%"
        count += 1
    else:
        new_str += text[i]
print(f"Количество замененных символов: {count}")
print(f"Новая строка: {new_str}")



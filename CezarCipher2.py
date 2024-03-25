upper_en_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower_en_alphabet = 'abcdefghijklmnopqrstuvwxyz'
print('На вход программе подается строка текста на английском языке, в которой нужно зашифровать все слова. Каждое слово строки будет зашифровано с помощью шифра Цезаря (циклического сдвига на длину этого слова). Строчные буквы при этом остаются строчными, а прописные – прописными. Гарантируется, что между различными словами присутствует один пробел.')
print('Введите строку:')
string = input()
s1="".join(c for c in string if c.isalpha() or c == ' ')
listRes = list(s1.split(" "))
result = ''
for i in listRes:
    step = len(i)
    for j in range(len(i)):
        for k in upper_en_alphabet:
            if i[j] == k:
                digit = ord(i[j]) + int(step)
                if digit > 90:
                    digit -= 26
                result += chr(digit)
                break
        for k in lower_en_alphabet:
            if i[j] == k:
                digit = ord(i[j]) + int(step)
                if digit > 122:
                    digit -= 26
                result += chr(digit)
                break
    result += ' '
for i in string:
    for j in result:
        if i.isalpha():
            new_string = string.replace(i,j)
result = result.replace(' ', '')
new_string = ''
index = 0
for i in string:
    if index == len(result):
        new_string += string[-1]
        break
    for j in result[index]:
        if i.isalpha():
            new_string += j
            index += 1
            break
print(new_string)

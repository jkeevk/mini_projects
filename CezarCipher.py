upper_en_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower_en_alphabet = 'abcdefghijklmnopqrstuvwxyz'
upper_ru_alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
lower_ru_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
alphabet_ru, alphabet_en = 32, 26

print('Hail, Caesar!')
print('Зашифровать текст: Введите 1')
print('Дешифровать текст: Введите 2')
encrypt = input()
while encrypt != '1' and encrypt != '2':
    print('Недопустимое значение.')
    print('Чтобы зашифровать ваш текст введите 1. Чтобы расшифровать текст - введите 2')
    encrypt = input()
print('Язык алфавита:')
print('Для работы с русским текстом введите ru')
print('Для работы с английским текстом введите en')
language = input()
while language != 'en' and language != 'ru':
    print('Недопустимое значение. Выберите язык: ru или en')
    language = input()
print('Выберите шаг сдвига:')
if language == 'ru':
    chosen_language = alphabet_ru
    print(f'от 1 до {alphabet_ru} для {language} текста')
else:
    chosen_language = alphabet_en
    print(f'от 1 до {alphabet_en} для {language} текста')
step = input()
while not step.isdigit():
    print('Принимается только число')
    step = input()
while int(step) > int(chosen_language):
    print('Шаг превышает количество букв в алфавите')
    step = input()
    while not step.isdigit():
        print('Принимается только число')
        step = input()
print('Введите текст для шифрования:')
string = input()
def cipher(encrypt, language, string, step):
    result = ''
    if language == 'en':
        upper, lower, lower_limit, upper_limit  = upper_en_alphabet, lower_en_alphabet, 122, 90
    elif language == 'ru':
        upper, lower, lower_limit, upper_limit  = upper_ru_alphabet, lower_ru_alphabet, 1103, 1071
    for i in range(len(string)):
        if string[i].isalpha():
            for k in upper:
                if string[i] == k and encrypt == '1':
                    digit = ord(k) + int(step)
                    if digit > upper_limit:
                        digit -= chosen_language
                    result += chr(digit)
                    break
                elif string[i] == k and encrypt == '2':
                    digit = ord(k) - int(step)
                    if digit <= (upper_limit - chosen_language):
                        digit += chosen_language
                    result += chr(digit)
                    break
            for k in lower:
                if string[i] == k and encrypt == '1':
                    digit = ord(k) + int(step)
                    if digit > lower_limit:
                        digit -= chosen_language
                    result += chr(digit)
                    break
                elif string[i] == k and encrypt == '2':
                    digit = ord(k) - int(step)
                    if digit <= (lower_limit - chosen_language):
                        digit += chosen_language
                    result += chr(digit)
                    break
        else: result += string[i]
    if encrypt == '1':
        print(f'Текст, закодированный шифром Цезаря:')
        print(result)
    else:
        print(f'Расшифрованный текст:')
        print(result)
    
cipher(encrypt, language, string, step)

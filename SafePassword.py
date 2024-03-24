import random
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'
confusing_let = 'il1Lo0O'
chars = ''
print('Укажите количество паролей для генерации:')
amount = int(input())
print('Укажите длину одного пароля:')
lenght = int(input())
print('Включать ли цифры 0123456789? (y/n)')
numbers = input()
print('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (y/n)')
uppers = input()
print('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (y/n)')
lowers = input()
print('Включать ли символы !#$%&*+-=?@^_? (y/n)')
symbols = input()
print('Исключать ли неоднозначные символы il1Lo0O? (y/n)')
confusing_letters = input()
if numbers == 'y' or numbers.lower() == 'да' or numbers.lower() == 'yes':
    chars += digits
if uppers == 'y' or uppers.lower() == 'да' or uppers.lower() == 'yes':
    chars += uppercase_letters
if lowers == 'y' or lowers.lower() == 'да' or lowers.lower() == 'yes':
    chars += lowercase_letters
if symbols == 'y' or symbols.lower() == 'да' or symbols.lower() == 'yes':
    chars += punctuation
if confusing_letters == 'y' or confusing_letters.lower() == 'да' or confusing_letters.lower() == 'yes':
    for i in confusing_let:
        chars = chars.replace(i, '')
print(f'Количество сгенерированных паролей: {amount}')
def generate_password(lenght, chars):
    result = ''
    for i in range(lenght):
        for j in chars:
            result += random.choice(chars)
            break
    print(result)
for i in range(amount):
    generate_password(lenght, chars)
print('Сгенерировать больше паролей?')
again = input()
while again == 'y' or again.lower() == 'да' or again.lower() == 'yes':
    for i in range(amount):
        generate_password(lenght, chars)
    print('Ещё?')
    again = input()
else:
    print('Во имя безопасности! Всего хорошего.')
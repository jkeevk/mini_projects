import random
print('Давайте играть в угадайку слов!')
# функция выбора языка и генерация списка слов на основании выбора
def choose_language():
    print('Какие слова будем угадывать? Русские или Анлийские?')
    print('ru / rus / рус / русские или en / eng / англ / английские')
    choose = input().lower()
    while choose != 'ru' or choose != 'rus' or choose != 'рус' or choose != 'русские' or choose != 'en' or choose != 'eng' or choose != 'англ' or choose != 'английские':
        if choose == 'ru' or choose == 'rus' or choose == 'рус' or choose == 'русские':
            word_list = ['Кофе', 'Луна', 'Электроника', 'Дождь', 'Библиотека', 'Медведь', 
                        'Факел', 'Окно', 'Пианино', 'Авиация', 'Лимон', 'Гитара', 'Киберпанк',
                        'Радуга', 'Карандаш', 'Забор', 'Комета', 'Вода', 'Солнце', 'Книга', 'Бильярд', 
                        'Астероид', 'Самолет', 'Камень', 'Фонарь', 'Дракон', 'Футбол', 'Кресло', 'Ракета',
                        'Галактика', 'Магнит', 'Опера', 'Радиатор', 'Шоколад', 'Ворона', 'Метро', 'Океан',
                        'Арбуз', 'Корова', 'Виолончель', 'Театр', 'Космос', 'Пальма', 'Гирлянда', 'Часы',
                        'Планета', 'Принцесса', 'Чай', 'Макароны', 'Ветер', 'Звезда', 'Рождество', 'Джаз',
                        'Торт', 'Селезень', 'Барабан', 'Флейта', 'Лестница', 'Авокадо', 'Картошка', 'Вино',
                        'Цветок', 'Наушники', 'Загадка', 'Компас', 'Снеговик', 'Шарф', 'Осьминог', 'Маяк',
                        'Лаванда', 'Шарик', 'Коктейль', 'Руль', 'Лира', 'Шахматы', 'Фонарь', 'Водопад', 
                        'Театр', 'Лягушка', 'Аметист', 'Апельсин', 'Дерево', 'Космонавт', 'Фонтан', 'Ключ', 
                        'Марс', 'Папоротник', 'Радиатор', 'Компьютер', 'Шоколадка', 'Котенок', 'Капучино', 
                        'Шахматы', 'Бинокль', 'Шарп', 'Каштан', 'Коммуникатор', 'Цыпленок', 'Густав', 'Катер']
            return word_list
        elif choose == 'en' or choose == 'eng' or choose == 'англ' or choose == 'английские':
            word_list = ['Abandon', 'Bizarre', 'Cancel', 'Daring', 'Earnest', 'Fabric', 'Gallon', 
                         'Habit', 'Iconic', 'Jab', 'Ketchup', 'Labour', 'Machine', 'Nacho', 'Oasis', 
                         'Paddle', 'Quaint', 'Rabbit', 'Saddle', 'Tablet', 'Umbrella', 'Vast', 'Waffle', 
                         'Xenon', 'Yacht', 'Zeppelin', 'Weather', 'Bake', 'Cable', 'Dabble', 'Eager', 
                         'Fabric', 'Gale', 'Habit', 'Icon', 'Jab', 'Kettle', 'Labour', 'Machine', 'Nail', 
                         'Ocean', 'Paddle', 'Quaint', 'Rag', 'Sad', 'Tablet', 'United', 'Vase', 'Waffle', 
                         'Xenon', 'Yawn', 'Zeal', 'Acute', 'Blend', 'Cavity', 'Damp', 'Eager', 'Fabric', 
                         'Gadget', 'Hammer', 'Ice', 'Jacket', 'Kangaroo', 'Lamp', 'Mango', 'Nail', 'Oak', 
                         'Paddle', 'Quilt', 'Rat', 'Sad', 'Table', 'Unit', 'Vane', 'Wagon', 'Xerox', 'Yak', 
                         'Zebra', 'Ankle', 'Belt', 'Cage', 'Dart', 'Eager', 'Fable', 'Game', 'Hat', 
                         'Icecream', 'Jacket', 'Kangaroo', 'Lamb', 'Mango', 'Nail', 'Owl', 'Paddle', 
                         'Quartz', 'Rabbit', 'Starfish', 'Tree', 'Umbrella', 'Vase', 'Water', 'Xylophone', 
                         'Yak', 'Zebra']
            return word_list
        else:
            print('Некорретный формат ввода данных')
            print('ru / rus / рус / русские или en / eng / англ / английские')
            choose = input()

            
        
# функция выбора случайного слова из списка слов
def get_word():
    word = random.choice(choose_language()).upper()
    return word

# функция получения текущего состояния человечка
def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]
# функция вывода текущих показателей
def status(tries, word_completion, guessed_letters, guessed_words, word):
    print('Текущее состояние:')
    print(display_hangman(tries))
    print(f'Количество попыток: {tries}')
    print(word_completion)
    if len(word) >= 5:
        print(f'Длинна загаданного слова: {len(word)} букв')
    else:
        print(f'Длинна загаданного слова: {len(word)} буквы')
    print(f'Уже названные буквы: {', '.join(guessed_letters)}')
    print(f'Уже названные слова: {', '.join(guessed_words)}')

# функция для запуска новой игры
def repeat():
    print('Хотите сыграть ещё? Y / YES / ДА')
    again = input()
    if again.upper() == 'Y' or again.upper() == 'YES' or again.upper() == 'ДА':
        word = get_word()
        play(word)
    else:
        print('До свидания!')

# функция описывающая основную логику игры
def play(word):
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed_letters = []               # список уже названных букв
    guessed_words = []                 # список уже названных слов
    tries = 6                          # количество попыток
    status(tries, word_completion, guessed_letters, guessed_words, word)
    print('Введите букву или слово целиком:')
    print('(Чтобы начать заново или выйти введите exit или quit)')
    while tries > 0:
        guess = input()
        if guess == 'quit' or guess == 'exit':
            break 
        while not guess.isalpha():
            print('Принимается только текст')
            guess = input()
        while len(guess) != len(word) and len(guess) != 1:
            print('Количество букв в слове не совпадает с загаданныи словом')
            print(f'Длинна загаданного слова: {len(word)} букв')
            guess = input()
            while not guess.isalpha():
                print('Принимается только текст')
                guess = input()
        if guess.upper() in guessed_letters:
            status(tries, word_completion, guessed_letters, guessed_words, word)
            print('Такая буква уже была')
            print('Введите букву или слово целиком:')
            continue
        elif guess.upper() in guessed_words:
            status(tries, word_completion, guessed_letters, guessed_words, word)
            print('Такое слово уже было')
            continue
        elif len(guess) == 1 and guess not in guessed_letters:
            guessed_letters.append(guess.upper())
            tries -= 1
        elif len(guess) > 1 and guess.upper() not in guessed_words:
            if guess.upper() == word:
                status(tries, word_completion, guessed_letters, guessed_words, word)
                print('Вы угадали!')
                print(f'Загаданное слово: {word}')
                break
            guessed_words.append(guess.upper())      
            tries -= 1

        for i, j in enumerate(word):
            if guess.upper() == j:
                word_completion = word_completion[:i] + j + word_completion[(i+1):]
        if word_completion == word:
            status(tries, word_completion, guessed_letters, guessed_words, word)
            print('Вы угадали!')
            print(f'Загаданное слово: {word}')
            break
        status(tries, word_completion, guessed_letters, guessed_words, word)
    else:
        print('Попытки закончились. Вы проиграли.')
        print(f'Загаданное слово: {word}')
    repeat()
    
word = get_word()
play(word)

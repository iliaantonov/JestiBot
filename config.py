# Токен Бота

token = '1415264147:AAGjsbQhaVoRJOG1VpC7ja4GZjADAJu_NZc'

# Выгрузка файлов, заполнение списков

# Список стикеров
stickers_file = open('stickers.txt', 'r').read().split('\n')
stickers_list = []

for line in stickers_file:
    stickers_list.append(line)

# Казни
execution_urls_txt = open('videos_data/execution_url.txt', 'r', encoding='utf-8').read().split('\n')
execution_urls = []

for line in execution_urls_txt:
    execution_urls.append(line)

execution_descriptions_txt = open('videos_data/execution_description.txt', 'r', encoding='utf-8').read().split('\n')
execution_descriptions = []

for line in execution_descriptions_txt:
    execution_descriptions.append(line)

# Сообщения бота
info = '''
Я Жесть-Бот
У меня есть кровь, мясо, матюки и голые сиськи

Всё просто: вводишь /pain и наслаждаешься
\nПосле ввода комманды ты соглашаешься с тем, что:
1. Я не несу ответственности за твою психику!
2. Я не призываю тебя ни к какому действию!
3. Тебе больше 18 лет
\nАдмин: @iliaantonov
'''
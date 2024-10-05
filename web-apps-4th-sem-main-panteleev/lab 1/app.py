# import random
# from flask import Flask, render_template
# from faker import Faker

# fake = Faker()

# app = Flask(__name__)
# application = app

# images_ids = ['7d4e9175-95ea-4c5f-8be5-92a6b708bb3c',
#               '2d2ab7df-cdbc-48a8-a936-35bba702def5',
#               '6e12f3de-d5fd-4ebb-855b-8cbc485278b7',
#               'afc2cfe7-5cac-4b80-9b9a-d5c65ef0c728',
#               'cab5b7f2-774e-4884-a200-0c0180fa777f']

# def generate_comments(replies=True):
#     comments = []
#     for i in range(random.randint(1, 3)):
#         comment = { 'author': fake.name(), 'text': fake.text() }
#         if replies:
#             comment['replies'] = generate_comments(replies=False)
#         comments.append(comment)
#     return comments

# def generate_post(i):
#     return {
#         'title': 'Заголовок поста',
#         'text': fake.paragraph(nb_sentences=100),
#         'author': fake.name(),
#         'date': fake.date_time_between(start_date='-2y', end_date='now'),
#         'image_id': f'{images_ids[i]}.jpg',
#         'comments': generate_comments()
#     }

# posts_list = sorted([generate_post(i) for i in range(5)], key=lambda p: p['date'], reverse=True)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/posts')
# def posts():
#     return render_template('posts.html', title='Посты', posts=posts_list)

# @app.route('/posts/<int:index>')
# def post(index):
#     p = posts_list[index]
#     return render_template('post.html', title=p['title'], post=p, img=p['image_id'])

# @app.route('/about')
# def about():
#     return render_template('about.html', title='Об авторе')

# if __name__ == "__main__":
#     app.run(debug=True)

import random  # Импортируем модуль random для генерации случайных чисел
from flask import Flask, render_template  # Импортируем Flask и render_template из библиотеки Flask
from faker import Faker  # Импортируем библиотеку Faker для генерации случайных данных
fake = Faker()  # Создаем экземпляр Faker для генерации фейковых данных
app = Flask(__name__)  # Создаем экземпляр приложения Flask
application = app  # Присваиваем экземпляру приложения имя application для совместимости с WSGI
images_ids = ['7d4e9175-95ea-4c5f-8be5-92a6b708bb3c',  # Список идентификаторов изображений
              '2d2ab7df-cdbc-48a8-a936-35bba702def5',
              '6e12f3de-d5fd-4ebb-855b-8cbc485278b7',
              'afc2cfe7-5cac-4b80-9b9a-d5c65ef0c728',
              'cab5b7f2-774e-4884-a200-0c0180fa777f']

def generate_comments(replies=True):  # Функция для генерации комментариев
    comments = []  # Инициализируем пустой список для комментариев
    for i in range(random.randint(1, 3)):  # Генерируем от 1 до 3 комментариев
        comment = { 'author': fake.name(), 'text': fake.text() }  # Создаем комментарий с фейковым автором и текстом
        if replies:  # Если разрешены ответы на комментарии
            comment['replies'] = generate_comments(replies=False)  # Генерируем ответы на комментарий
        comments.append(comment)  # Добавляем комментарий в список
    return comments  # Возвращаем список комментариев

def generate_post(i):  # Функция для генерации поста
    return {  # Возвращаем словарь с данными поста
        'title': 'Заголовок поста',  # Заголовок поста
        'text': fake.paragraph(nb_sentences=100),  # Текст поста, состоящий из 100 предложений
        'author': fake.name(),  # Фейковый автор поста
        'date': fake.date_time_between(start_date='-2y', end_date='now'),  # Дата поста в диапазоне последних 2 лет
        'image_id': f'{images_ids[i]}.jpg',  # Идентификатор изображения, соответствующий посту
        'comments': generate_comments()  # Генерация комментариев для поста
    }

posts_list = sorted([generate_post(i) for i in range(5)], key=lambda p: p['date'], reverse=True)  # Генерируем 5 постов и сортируем их по дате в обратном порядке

@app.route('/')  # Определяем маршрут для главной страницы
def index():  # Функция для обработки главной страницы
    return render_template('index.html')  # Возвращаем HTML-шаблон для главной страницы

@app.route('/posts')  # Определяем маршрут для страницы со списком постов
def posts():  # Функция для обработки страницы со списком постов
    return render_template('posts.html', title='Посты', posts=posts_list)  # Возвращаем HTML-шаблон со списком постов

@app.route('/posts/<int:index>')  # Определяем маршрут для страницы конкретного поста по индексу
def post(index):  # Функция для обработки страницы конкретного поста
    p = posts_list[index]  # Получаем пост по индексу
    return render_template('post.html', title=p['title'], post=p, img=p['image_id'])  # Возвращаем HTML-шаблон для конкретного поста

@app.route('/about')  # Определяем маршрут для страницы "О авторе"
def about():  # Функция для обработки страницы "О авторе"
    return render_template('about.html', title='Об авторе')  # Возвращаем HTML-шаблон для страницы "О авторе"

if __name__ == "__main__":  # Проверяем, является ли скрипт основным модулем
    app.run(debug=True)  # Запускаем приложение Flask в режиме отладки
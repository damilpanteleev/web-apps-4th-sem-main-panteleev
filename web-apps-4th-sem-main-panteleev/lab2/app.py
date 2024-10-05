# from flask import Flask, render_template, make_response, request

# app = Flask(__name__)

# application = app

# @app.route('/') 
# def index():
#     return render_template('index.html') 

# @app.route('/url')
# def url():
#     return render_template('url.html')
    
# @app.route('/headers')
# def headers():
#     return render_template('headers.html')

# @app.route('/cookies')
# def cookies():
#     resp = make_response(render_template('cookies.html'))
#     if 'user' in request.cookies:
#         resp.delete_cookie('user')
#     else:    
#         resp.set_cookie('user','admin')
#     return resp

# @app.route('/forms', methods=['GET', 'POST'])
# def forms():
#     # if request.method == "POST"
#     return render_template('forms.html')


# @app.route('/calc')
# def calc():
#     a = float(request.args.get('a',0))
#     b = float(request.args.get('b',0))
#     operator = request.args.get('operator')


#     result = 0
#     if operator == "+":
#         result = a+b
#     elif operator == "-":
#         result = a-b
#     elif operator == "*":
#         result = a*b
#     elif operator == "/":
#         result = a/b

#     return render_template('calc.html', result=result)

# @app.route('/phone', methods=['POST', 'GET'])
# def phone():
#     error = None
#     format_phone = ''
#     if request.method == "POST":
#         additional_symvols = [' ', '(', ')', '-', '.', '+']

#         phone_num = request.form['phone']

#         digits = [i for i in phone_num if i.isdigit()]

#         for i in phone_num:
#             if i.isdigit() == False and i not in additional_symvols:
#                 error = 'Недопустимый ввод. В номере телефона встречаются недопустимые символы.'
#                 return render_template('phone.html', error=error)

#         if len(digits) not in [10, 11] or (len(digits) == 11 and digits[0] not in ['7', '8']):
#             error = 'Недопустимый ввод. Неверное количество цифр.'
#             return render_template('phone.html', error=error)
        
#         if len(digits) == 10:
#             digits.insert(0, 8)
        
#         format_phone = f"{8}-{''.join(digits[1:4])}-{''.join(digits[4:7])}-{''.join(digits[7:9])}-{''.join(digits[9:])}"

#     return render_template('phone.html', error=error, format_phone=format_phone)



from flask import Flask, render_template, make_response, request  # Импортируем необходимые модули из Flask
app = Flask(__name__)  # Создаем экземпляр приложения Flask
application = app  # Присваиваем экземпляру приложения имя application для совместимости с WSGI

@app.route('/')  # Определяем маршрут для главной страницы
def index():  # Функция для обработки главной страницы
    return render_template('index.html')  # Возвращаем HTML-шаблон для главной страницы

@app.route('/url')  # Определяем маршрут для страницы URL
def url():  # Функция для обработки страницы URL
    return render_template('url.html')  # Возвращаем HTML-шаблон для страницы URL

@app.route('/headers')  # Определяем маршрут для страницы заголовков
def headers():  # Функция для обработки страницы заголовков
    return render_template('headers.html')  # Возвращаем HTML-шаблон для страницы заголовков

@app.route('/cookies')  # Определяем маршрут для страницы с куками
def cookies():  # Функция для обработки страницы с куками
    resp = make_response(render_template('cookies.html'))  # Создаем ответ с HTML-шаблоном для куков
    if 'user' in request.cookies:  # Проверяем, есть ли кука 'user' в запросе
        resp.delete_cookie('user')  # Удаляем куку 'user', если она существует
    else:    
        resp.set_cookie('user', 'admin')  # Устанавливаем куку 'user' со значением 'admin', если ее нет
    return resp  # Возвращаем ответ с куками

@app.route('/forms', methods=['GET', 'POST'])  # Определяем маршрут для страницы с формами, поддерживающей GET и POST запросы
def forms():  # Функция для обработки страницы с формами
    # if request.method == "POST"  # Закомментированная строка для проверки метода запроса (POST)
    return render_template('forms.html')  # Возвращаем HTML-шаблон для страницы с формами

@app.route('/calc')  # Определяем маршрут для калькулятора
def calc():  # Функция для обработки калькулятора
    a = float(request.args.get('a', 0))  # Получаем параметр 'a' из URL, преобразуем в float, по умолчанию 0
    b = float(request.args.get('b', 0))  # Получаем параметр 'b' из URL, преобразуем в float, по умолчанию 0
    operator = request.args.get('operator')  # Получаем оператор из URL
    result = 0  # Инициализируем переменную для результата
    if operator == "+":  # Проверяем, является ли оператор сложением
        result = a + b  # Выполняем сложение
    elif operator == "-":  # Проверяем, является ли оператор вычитанием
        result = a - b  # Выполняем вычитание
    elif operator == "*":  # Проверяем, является ли оператор умножением
        result = a * b  # Выполняем умножение
    elif operator == "/":  # Проверяем, является ли оператор делением
        result = a / b  # Выполняем деление
    return render_template('calc.html', result=result)  # Возвращаем HTML-шаблон для калькулятора с результатом

@app.route('/phone', methods=['POST', 'GET'])  # Определяем маршрут для страницы с телефоном, поддерживающей POST и GET запросы
def phone():  # Функция для обработки страницы с телефоном
    error = None  # Инициализируем переменную для хранения ошибки
    format_phone = ''  # Инициализируем переменную для форматированного номера телефона
    if request.method == "POST":  # Проверяем, является ли метод запроса POST
        additional_symvols = [' ', '(', ')', '-', '.', '+']  # Допустимые дополнительные символы
        phone_num = request.form['phone']  # Получаем номер телефона из формы
        digits = [i for i in phone_num if i.isdigit()]  # Извлекаем только цифры из номера телефона
        for i in phone_num:  # Проходим по каждому символу в номере телефона
            if i.isdigit() == False and i not in additional_symvols:  # Проверяем, является ли символ недопустимым
                error = 'Недопустимый ввод. В номере телефона встречаются недопустимые символы.'  # Устанавливаем сообщение об ошибке
                return render_template('phone.html', error=error)  # Возвращаем HTML-шаблон с ошибкой
        if len(digits) not in [10, 11] or (len(digits) == 11 and digits[0] not in ['7', '8']):  # Проверяем количество цифр
            error = 'Недопустимый ввод. Неверное количество цифр.'  # Устанавливаем сообщение об ошибке
            return render_template('phone.html', error=error)  # Возвращаем HTML-шаблон с ошибкой
        if len(digits) == 10:  # Если длина цифр равна 10
            digits.insert(0, 8)  # Добавляем 8 в начало списка цифр
        format_phone = f"{8}-{''.join(digits[1:4])}-{''.join(digits[4:7])}-{''.join(digits[7:9])}-{''.join(digits[9:])}"  # Форматируем номер телефона
    return render_template('phone.html', error=error, format_phone=format_phone)  # Возвращаем HTML-шаблон с ошибкой и форматированным номером телефона
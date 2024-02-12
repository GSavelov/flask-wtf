from flask import Flask, render_template

app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('index.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    return render_template('index.html', prof=prof, title="Тренировка")


@app.route('/list_prof/<list>')
def list_prof(list):
    return render_template('index.html', list=list, title="Тренировка")


@app.route('/answer')
@app.route('/auto_answer')
def auto_answer():
    params = {
        "title": 'Анкета',
        "surname": 'Ватный',
        "name": 'Марк',
        "education": 'выше среднего',
        "profession": 'штурман марсохода',
        "sex": 'мужчина',
        "motivation": 'Всегда мечтал застрять на Марсе',
        "ready": 'Готов'
    }

    return render_template('auto_answer.html', **params)


if __name__ == '__main__':
    app.run(port=8080)

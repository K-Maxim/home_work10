from flask import Flask

import utils

candidates_list = utils.uploading_candidates()  # список кандидатов импортированный из JSON
person_str = utils.canditates_str()  # строковые данные записываю в переменную

app = Flask(__name__)  # запускаю фласк


@app.route('/')
def home_page():
    """
    Функция, выводит список кандидатов на главную страницу сайта
    :return: данные всех кандидатов
    """
    return f'<pre>{person_str}<pre>'


@app.route('/candidate/<int:id>')
def candidate(id):
    """
    Функция, которая выводит данные кандидата по их "id"
    :param id: тип данной: int.
    У каждого кандидата свой "id" (в нашем случае числа будут от 1 до 7, так как 7 кандидатов)
    :return: данные определенного кандидата
    """
    person_profile = ''

    for i in range(len(candidates_list)):
        if id == candidates_list[i]["id"]:
            person = f'<img src="{candidates_list[i]["picture"]}">\n' \
                     f'Имя кандидата: {candidates_list[i]["name"]}\n' \
                     f'Позиция кандидата: {candidates_list[i]["position"]}\n' \
                     f'Навыки кандидата: {candidates_list[i]["skills"]}'
            person_profile += person
        elif id > len(candidates_list):
            return f'<h1>Кандидат не найден<h1>'
    return f'<pre>{person_profile}<pre>'


@app.route('/skills/<skills>')
def skills(skills):
    """
    Функция, которая выводит данные кандидата по их "skills"
    :param skills: тип данной: srt.
    :return: данные определенного кандидата по их "skills"
    """
    person_profile = ''
    for i in range(len(candidates_list)):
        candidate_skills = candidates_list[i]["skills"].lower().split(', ')
        if skills in candidate_skills:
            person = f'Имя кандидата: {candidates_list[i]["name"]}\n' \
                     f'Позиция кандидата: {candidates_list[i]["position"]}\n' \
                     f'Навыки кандидата: {candidates_list[i]["skills"]}\n\n'
            person_profile += person
    return f'<pre>{person_profile}<pre>'


app.run()

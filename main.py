import json

from flask import Flask


def uploading_candidates():
    """
    Функция импортирует список из 'candidates.json' и записывает его в переменную
    :return: список словарей
    """
    with open('candidates.json', 'r', encoding='UTF-8') as file:
        candidates_list = json.load(file)
        return candidates_list


candidates_list = uploading_candidates()


def canditates_on_page():
    """
    Функция, которая выводит данные кандидатов
    :return: строковые данные всех кандидатов
    """
    person_str = ''

    for candidate in candidates_list:
        person = f'id: {candidate["id"]}\n' \
                 f'name: {candidate["name"]}\n' \
                 f'picture: {candidate["picture"]}\n' \
                 f'position: {candidate["position"]}\n' \
                 f'gender: {candidate["gender"]}\n' \
                 f'age: {candidate["age"]}\n' \
                 f'skills: {candidate["skills"]}\n\n'
        person_str += person
    return person_str


person_str = canditates_on_page()  # строковые данные записываю в переменную

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

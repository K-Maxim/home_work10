import json


def uploading_candidates():
    """
    Функция импортирует список из 'candidates.json' и записывает его в переменную
    :return: список словарей
    """
    with open('candidates.json', 'r', encoding='UTF-8') as file:
        candidates_list = json.load(file)
        return candidates_list


uploading_candidates()

candidates_list = uploading_candidates()


def canditates_str():
    """
    Функция, которая преобразует данные кандидатов для вывода на страницу
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


canditates_str()
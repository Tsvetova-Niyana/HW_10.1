# импорт библиотек
import json
from classes import Candidats


def load_candidates(path):
    """
    Загрузка списка из json файла
    """
    with open(path, encoding='utf-8') as list_candidates:
        candidates_list = json.load(list_candidates)
    return candidates_list


def get_all(candidates_list):
    """
    Формирование экземпляров класса Candidats и списка кандидатов для отображения
    """
    candidate_list = []
    for candidate in candidates_list:
         candidate_person = Candidats(candidate['pk'], candidate['name'], candidate['picture'], candidate['position'], candidate['skills'])
         candidate_list.append(candidate_person)
    return candidate_list


def get_by_pk(candidate_list, pk):
    """
    Проверка существования кандидата по введенному pk
    На вход подаются аргументы candidate_list, pk, где
    candidate_list - список кандидатов, сформированный из экзепляров класса Candidats (candidate.pk - свойство pk
    у экземпляра класса Candidats)
    pk - номер кандидата
    """
    for candidate in candidate_list:
        if candidate.pk == pk:
            return candidate


def get_by_skill(candidates_list, skill_name):
    """
    Проверка существования кандидата по введенному навыку (skill_name)
    На вход подаются аргументы candidate_list, skill_name, где
    candidate_list - список кандидатов, сформированный из экзепляров класса Candidats (candidate.skills - свойство skills
    у экземпляра класса Candidats)
    skills - навык кандидата
    Проверка навыка осуществляется независимо от регистра ввода
    """
    skills_list = []
    for candidate in candidates_list:
        if skill_name.lower() in candidate.skills.lower():
            skills_list.append(candidate)
    return skills_list



# создание класса "Кандидаты"
class Candidats:
    def __init__(self, pk, name, picture, position, skills):
        self.pk = pk
        self.name = name
        self.picture = picture
        self.position = position
        self.skills = skills

    def __repr__(self):
        """
        Представление класса
        """
        return f"Имя кандидата - {self.name}\n"\
               f"Позиция кандидата {self.position}\n"\
               f"Навыки через запятую {self.skills}\n"
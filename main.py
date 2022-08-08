# импорт библиотек
from flask import Flask
import utils


def main():
    PATH_SOURCE_FILE = "candidates.json"

    path = utils.load_candidates(PATH_SOURCE_FILE)
    candidates_list = utils.get_all(path)

    # создание экземпляра класса Flask
    app = Flask(__name__)

    # создание декораторов и функций
    @app.route("/")
    def page_index():
        candidates = ''
        for candidate in candidates_list:
            candidates += f'<pre>{candidate}</pre>'
        return candidates

    @app.route("/candidates/<int:pk>/")
    def page_candidates(pk):
        candidate = utils.get_by_pk(candidates_list, pk)
        if candidate:
            image_candidate = f"<img src='{candidate.picture}'>"
        return f"{image_candidate}"\
               f"<pre>{candidate}</pre>"

    @app.route("/skills/<skill_name>")
    def page_skills(skill_name):
        candidates_lists = ''
        candidates = utils.get_by_skill(candidates_list, skill_name)
        if candidates:
            for candidate in candidates:
                candidates_lists += f"<pre>{candidate}</pre>"
        return f"{candidates_lists}"

    # запуск сервера
    app.run()


if __name__ == '__main__':
    main()

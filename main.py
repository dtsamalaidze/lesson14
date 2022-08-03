from flask import Flask
from DB import DB
import json

app = Flask(__name__)


@app.get('/movie/<title>/')
def search_by_title(title):
    db = DB()
    result = db.get_by_title(title)
    return app.response_class(
        response=json.dumps(result),
        status=200,
        mimetype="application/json"
    )


@app.get('/movie/<start>/to/<stop>')
def search_by_year(start, stop):
    db = DB()
    result = db.get_between_dates(start, stop)
    return app.response_class(
        response=json.dumps(result),
        status=200,
        mimetype="application/json"
    )


@app.get('/rating/<rating>')
def search_by_rating(rating):
    db = DB()
    my_dict = {
        "children": ('G', 'G'),
        "family": ('G', 'PG', 'PG-13'),
        "adult": ('R', 'NC-17'),
    }
    result = db.get_by_rating(my_dict[rating])
    return app.response_class(
        response=json.dumps(result),
        status=200,
        mimetype="application/json"
    )


@app.get('/genre/<genre>')
def search_by_genre(genre):
    db = DB()
    result = db.get_by_genre(genre)
    return app.response_class(
        response=json.dumps(result),
        status=200,
        mimetype="application/json"
    )


def search_by_cast(actor_first, actor_second):
    db = DB()
    result = []
    dict_name = {}
    for item in db.get_cast(actor_first, actor_second):
        names = set(dict(item).get('cast').split(', ')) - set([actor_first, actor_second])

        for name in names:
            dict_name[str(name).strip()] = dict_name.get(str(name).strip(), 0) + 1

    for k, v in dict_name.items():
        if v < 2:
            result.append(k)

    return result


def search_description(_type, release_year, ganre):
    db = DB()
    result = db.get_description(_type, release_year, ganre)
    return json.dumps(result)


if __name__ == '__main__':
    app.run(host='localhost', debug=True)

from flask import Flask, jsonify, request
from flask_cors import CORS
import uuid
app = Flask(__name__)

app.config.from_object(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/', methods=['GET'])
def greetings():
    return 'Hello, World!'

# TODO: replace to databse SQLite


GAMES = [
    {
        "id": uuid.uuid4().hex,
        "title": "2k21",
        "genre": "sports",
        "played": True
    },
    {
        "id": uuid.uuid4().hex,
        "title": "GoW",
        "genre": "survival",
        "played": True
    },
    {
        "id": uuid.uuid4().hex,
        "title": "The Last of Us",
        "genre": "survival",
        "played": False
    },
]


@app.route("/games", methods=['GET', 'POST'])
def all_games():
    response_object = {"status": "success"}
    if request.method == 'POST':
        post_data = request.get_json()
        GAMES.append({
            "id": uuid.uuid4().hex,
            "title": post_data.get('title'),
            "genre": post_data.get('genre'),
            "played": post_data.get('played')
        })
        response_object['message'] = "Game Added!"
    else:
        response_object['games'] = GAMES
    return jsonify(response_object)


@app.route("/games/<game_id>", methods=['PUT', 'DELETE'])
def game(game_id):
    response_object = {"status": "success"}
    if request.method == 'PUT':
        put_data = request.get_json()
        for game in GAMES:
            if game['id'] == game_id:
                game['title'] = put_data.get('title')
                game['genre'] = put_data.get('genre')
                game['played'] = put_data.get('played')
                response_object['message'] = "Game Updated!"
                break
    elif request.method == 'DELETE':
        for game in GAMES:
            if game['id'] == game_id:
                GAMES.remove(game)
                response_object['message'] = "Game Deleted!"
                break
    return jsonify(response_object)


if __name__ == '__main__':
    app.run(debug=True)

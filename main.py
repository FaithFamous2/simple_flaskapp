from flask import Flask, render_template, request
from waitress import serve
import random

app = Flask(__name__)

locations = ["at the beach 🏖⛱", "in a theme park ⛲🏞", "on a remote island🏝☪",
             "in a space station🛰🌌", "under the sea🌊⛵", "my Room 🏚"]


def save_name_to_file(name):
    with open('usernames.txt', 'a') as file:
        file.write(name + '\n')


def get_saved_names():
    with open('usernames.txt', 'r') as file:
        return file.read()


def generate_locations(name):
    random_locations = random.choice(locations)
    save_name_to_file(name)
    joke = f"Thank you🙇‍♀️ {name}!! for accepting my invites, Birthday party will be at this Location ✅ {random_locations.upper()}. ✅Do have Great time at the party!"
    return joke


@app.route('/')
def index():
    saved_names = get_saved_names
    return render_template('index.html', saved_names=saved_names)


@app.route('/famouz_birthday', methods=['POST'])
def birthday_jokes():
    name = request.form['name']
    names = name
    joke = generate_locations(names)
    # print(joke)
    return render_template('famouz_birthday.html', joke=joke, names=names)


if __name__ == '__main__':
    serve(app, host="0.0.0.0", port=8080)

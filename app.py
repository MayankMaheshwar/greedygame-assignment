from flask import Flask, jsonify, render_template, request
app = Flask(__name__)


class Trie:
    def __init__(self):
        self.head = {}


dataCollection = Trie()
data = dataCollection.head


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/insert', methods=['GET', 'POST'])
def insert():
    if request.method == 'POST':
        device = request.form.get('device')
        country = request.form.get('country')
        webreq = int(request.form.get('webreq'))
        timespent = int(request.form.get('timespent'))

        if country not in data.items():
            data[country] = [webreq, timespent]
        else:
            data[country][0] += webreq
            data[country][1] += timespent

        print(data)
        return "inserted"

    else:

        return render_template('insert.html')


@app.route('/query', methods=['GET', 'POST'])
def query():
    if request.method == 'POST':
        country = request.form.get('country')
        return jsonify({'country': country, 'metrics': {'webreq': data[country][0], 'timespent': data[country][1]}})
    else:
        return render_template('query.html')


if __name__ == '__main__':
    app.run(debug=True)

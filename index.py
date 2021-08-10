from flask import Flask, Response, request, __version__, jsonify
import json
app = Flask(__name__)

#locations = {'Jens': 'home','Kristin' : 'home'}


@app.route('/location/<name>', methods=['GET', 'PUT'])
def location(name):
    with open('./data/locations.json', 'r') as f:
        data = f.read()
        locations = json.loads(data)
    if request.method == 'PUT':
        locations[name] = str(request.get_data())
        with open('./data/locations.json', 'w') as f:
            f.write(json.dumps(locations,))
        return jsonify(locations[name])
    else:
        return locations[name]
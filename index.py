from flask import Flask, Response, request, __version__
app = Flask(__name__)

locations = {'Jens': 'Im sorry',
            'Kristin' : 'work'}


@app.route('/location/<name>', methods=['GET', 'PUT'])
def location(name):
    if request.method == 'PUT':
        locations[name] = str(request.get_data())
        print("location: " + locations[name])
        return ''
    else:
        return locations[name]
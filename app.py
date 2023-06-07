from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/programs')
def programs():

    file_name = "programs.json" # Nombre del archivo JSON

    with open(file_name, "r") as json_file: # Abrir el archivo JSON
        json_data = json.load(json_file)# Cargar el contenido del archivo JSON

    urls = []
    for country in json_data:
        urls.append(country['main-img'])

    return render_template('programs.html', countries=json_data, imagenes=urls) #le paso como parametro la data del json

if __name__ == '__main__':
    app.run(debug=True)
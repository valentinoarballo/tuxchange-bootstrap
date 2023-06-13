from flask import Flask, render_template
import json

app = Flask(__name__)

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html')

@app.route('/')
def index():

    file_name = "countries.json" # Nombre del archivo JSON
    
    with open(file_name, "r", encoding="utf8") as json_file: # Abrir el archivo JSON, EL COLMO
        json_data = json.load(json_file)# Cargar el contenido del archivo JSON

    urls = []
    for country in json_data:
        urls.append(country['landscape_img'])

    return render_template('index.html', countries=json_data, imagenes=urls)

@app.route('/programs')
def programs():

    file_name = "countries.json" # Nombre del archivo JSON

    with open(file_name, "r", encoding="utf8") as json_file: # Abrir el archivo JSON, EL COLMO
        json_data = json.load(json_file)# Cargar el contenido del archivo JSON

    urls = []
    for country in json_data:
        urls.append(country['main_img'])

    return render_template('programs.html', countries=json_data, imagenes=urls) #le paso como parametro la data del json

@app.route('/inscriptions')
def inscriptions():

    file_name = "countries.json" # Nombre del archivo JSON

    with open(file_name, "r", encoding="utf8") as json_file: # Abrir el archivo JSON, EL COLMO
        json_data = json.load(json_file)# Cargar el contenido del archivo JSON

    urls = []
    for country in json_data:
        urls.append(country['main_img'])

    return render_template('inscriptions.html', countries=json_data, imagenes=urls) #le paso como parametro la data del json


if __name__ == '__main__':
    app.run()
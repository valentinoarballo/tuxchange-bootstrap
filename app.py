from flask import Flask, render_template
import json

app = Flask(__name__)

@app.errorhandler(404)
def notFound(e):
    return render_template('404.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/programs')
def programs():

    file_name = "countries.json" # Nombre del archivo JSON

    with open(file_name, "r", encoding="utf8") as json_file: # Abrir el archivo JSON, EL COLMO
        json_data = json.load(json_file)# Cargar el contenido del archivo JSON

    urls = []
    for country in json_data:
        urls.append(country['main_img'])

    return render_template('programs.html', countries=json_data, imagenes=urls) #le paso como parametro la data del json

@app.route('/country/<id>')
def country(id):
    file_name = "countries.json" # Nombre del archivo JSON

    with open(file_name, "r", encoding="utf8") as json_file: 
        json_data = json.load(json_file)
    try:
        id=int(id)
        country=json_data[id]
    except:
        return render_template('404.html')
    else:
        country_name=country['name']
        country_desc=country['description']
        country_img=country['main_img']
        other_country_list=[]
        for country in json_data:
            if country['name'] != country_name:
                other_country_list.append(country)
        return render_template(
                            'country.html',
                            country_name=country_name,
                            country_description=country_desc,
                            country_img=country_img,
                            other_country_list=other_country_list,
                            list_length=len(other_country_list),
                            )

if __name__ == '__main__':
    app.run()
import datetime
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        try: 
            r = request.form['cep']
            cep = str(r)
            cep = cep.replace(" ", "").replace(".", "").replace("-", "")
            
            if len(cep) == 8:
                link = f"https://viacep.com.br//ws/{cep}/json/"

                requisicao = requests.get(link)
                req = requisicao.json()

            return render_template("index.html", req=req)
        except: 
            erro = "CEP inválido"
            return render_template("index.html", erro=erro)
    else:
        return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
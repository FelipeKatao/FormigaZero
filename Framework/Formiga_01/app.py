from flask import Flask, url_for,request
from flask import render_template
from os import listdir

app = Flask(__name__)
NameCliente=""

@app.route('/',methods=['GET',"POST"])
def api_root():
    id_Project=""
    if request.method == 'POST':
        id_Project=request.form['NameProject']
        return id_Project

    return render_template("index.html")

@app.route('/<clientePath>')
def api_root_cliente(clientePath):
    NameCliente=clientePath
    return render_template(NameCliente+"/cliente.html")

@app.route('/Oat',methods=['GET','POST'])
def api_articles():
    if request.method == 'POST':

        with open('Data_01/test3.txt', 'w+') as f:
            f.write(str("Internal source data"))
        return "Atualizado"
    return f
                                    
@app.route('/articles/<articleid>')
def api_article(articleid):
    return 'You are reading ' + articleid

if __name__ == '__main__':
    app.run()
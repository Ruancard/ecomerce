from flask import Flask, render_template, request, redirect

#teste

class produtos:
    def __init__(self, nome, imagem, preco):
        self.nome = nome
        self.imagem = imagem
        self.preco = preco

produto1 = produtos('binco de pompom', '../static/produto.jpg', 762.99)
produto2 = produtos('corrente de ouro', '../static/produto.jpg', 500.99)
produto3 = produtos('pulseira de prata', '../static/produto.jpg', 140.99)
produto4 = produtos('binco de pompom', '../static/produto.jpg', 762.99)
produto5 = produtos('corrente de ouro', '../static/produto.jpg', 500.99)
produto6 = produtos('pulseira de prata', '../static/produto.jpg', 140.99)

lista = [produto1, produto2, produto3, produto4, produto5, produto6]

app = Flask(__name__)

@app.route('/')
def ola():
    return render_template('home.html', produtos = lista)

@app.route('/colecao')
def colecoes():
    return render_template('colecao.html')

@app.route('/destaque')
def destaque():
    return render_template('destaque.html')

@app.route('/favorito')
def favorito():
    return render_template('favorito.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/pulseira')
def pulseira():
    return render_template('pulseira.html')

@app.route('/pulseira')
def pulseeira():
    return render_template('pulseira.html')

@app.route('/colar')
def colar():
    return render_template('colar.html')

@app.route('/brinco')
def brinco():
    return render_template('brinco.html')


app.run(debug=True)
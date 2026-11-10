from flask import Flask, render_template

app = Flask(__name__)

# Cardápio - sem preços, só produtos
CARDAPIO = {
    "Pão de Queijo": [
        {"nome": "Pão de Queijo Tradicional", "desc": "Receita mineira clássica, casquinha crocante e macio por dentro.", "tag": "Clássico"},
        {"nome": "Pão de Queijo Recheado de Frango", "desc": "Recheado com frango desfiado temperado na medida.", "tag": "Mais pedido"},
        {"nome": "Pão de Queijo Recheado de Requeijão", "desc": "Cremoso, com requeijão de verdade derretendo.", "tag": "Cremoso"},
        {"nome": "Pão de Queijo Recheado de Pernil", "desc": "Pernil suculento desfiado, bem temperado.", "tag": "Especial"},
        {"nome": "Pão de Queijo Recheado de Calabresa", "desc": "Calabresa artesanal com um toque de queijo.", "tag": "Picante leve"},
    ],
    "Broas": [
        {"nome": "Broa de Sal", "desc": "Broa de milho tradicional, perfeita com café.", "tag": "Tradicional"},
        {"nome": "Broa Doce", "desc": "Doçura na medida, com gostinho de roça.", "tag": "Doce"},
    ],
    "Cafés": [
        {"nome": "Café Coado", "desc": "Coado na hora, no filtro, do jeito mineiro.", "tag": "Da casa"},
        {"nome": "Cappuccino", "desc": "Cremoso, com espuma aveludada e toque de canela.", "tag": "Cremoso"},
        {"nome": "Café com Leite", "desc": "Clássico de padaria, quentinho e confortável.", "tag": "Clássico"},
    ]
}

WHATSAPP = "5534998618979"

@app.route("/")
def index():
    return render_template("index.html", cardapio=CARDAPIO, whatsapp=WHATSAPP)

@app.route("/sobre")
def sobre():
    return render_template("sobre.html", whatsapp=WHATSAPP)

@app.route("/local")
def local():
    return render_template("local.html", whatsapp=WHATSAPP)

if __name__ == "__main__":
    app.run(debug=True, port=5000)

from flask import Flask, render_template, request
 
app = Flask(__name__)

@app.route("/")
def index():
   return render_template('index.html')

@app.route("/sobre")
def sobre():
   return render_template('sobre.html')

@app.route('/produto')
def produto():
     produto = request.args.get('codigo')
     
     if produto == "1":    
         nome="Devil's Food Cake"
         descricao="A fatia de desse bolo é bem chocolatuda, molhadinha, com recheio de mousse de chocolate meio amargo e cobertura de mousse de chocolate ao leite."
         imagem="/static/devil-food.jfif"
         return render_template('produto.html', nome=nome, descricao=descricao, imagem=imagem)

     if produto == "2":
         nome="Mousse de Chocolate Belga"
         descricao="Mousse de chocolate belga coberto com raspas de chocolate. Aproximadamente 400g. Serve até 4 pessoas."
         imagem="/static/mousse.jfif"
         return render_template('produto.html', nome=nome, descricao=descricao, imagem=imagem)
        
     if produto == "3":
         nome="Bolo Vulcão"
         descricao="Disponível em massa branca, de cenoura ou chocolate e opções de cobertura de chocolate, leite em pó ou deoce de leite. Aproximadamente 800g."
         imagem="/static/bolo-vulcao.jfif"
         return render_template('produto.html', nome=nome, descricao=descricao, imagem=imagem)
     
     if produto == "4":
         nome="Verrine au Chocolat"
         descricao="Exclusivo creme tipo mousse à base de creme fresco, especiarias e chocolate.Adição de morango ou cerejas à parte. Aproximadamente 250g."
         imagem="/static/verrine.jpeg"
         return render_template('produto.html', nome=nome, descricao=descricao, imagem=imagem)   
         
   
if __name__ == '__main__':
    app.run(debug=True)
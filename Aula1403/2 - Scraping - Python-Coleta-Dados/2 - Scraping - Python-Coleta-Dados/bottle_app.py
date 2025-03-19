#Conjunto de importacoes
from bottle import default_app, template, request, post, get
from sklearn.naive_bayes import GaussianNB
from sklearn.externals import joblib

#Defini��o das poss�veis rotas para a fun��o de callback

@get('/')
@get('/form/')
def index():
     #Defini��o de valores iniciais para as express�es animal, classifica��o e probabilidade
     return template('/home/ricardoricrob76/mysite/formulario.html', animal = "-", classificacao = "-", probabilidade = "-")

#Defini��o da rota e fun��o de callback
@post('/form/')
def index_resposta():
    #Pega os valores informados no formul�rio e atribui a variaveis locais
    animal = request.forms.get('animal')
    sangue = request.forms.get('sangue')
    bota_ovo = request.forms.get('bota_ovo')
    voa = request.forms.get('voa')
    mora_agua = request.forms.get('mora_agua')

    modelo_NB = GaussianNB()
    #Carrega o modelo gerado
    modelo_NB = joblib.load('/home/ricardoricrob76/mysite/modelo_mamifero_MNB.pkl')
    #Executa a classifica��o
    res = modelo_NB.predict([[int(sangue), int(bota_ovo), int(voa), int(mora_agua)]])

    #Encontra o valor da confid�ncia
    #probabilidade = modelo_NB.predict_proba([[int(sangue), int(bota_ovo), int(voa), int(mora_agua)]])

    if res == 1:
        classificacao = "Mam�fero"
    elif res == 0:
        classificacao = "N�o Mam�fero"
    else:
        classificacao = "Indefinido"

    #Renderiza o template com os valores passados como argumento
    #return template('/home/ricardoricrob76/mysite/formulario.html', animal = animal, classificacao = classificacao, probabilidade = "%.2f" % probabilidade[res][res])
    return template('/home/ricardoricrob76/mysite/formulario.html', animal = animal, classificacao = classificacao)

application = default_app()

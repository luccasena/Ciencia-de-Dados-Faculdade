import os
import tweepy
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Obtendo as credenciais da API do Twitter (X) a partir do ambiente
BEARER_TOKEN = os.getenv("BEARER_TOKEN")

# Implementação da classe personalizada para streaming
class TwitterStream(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        print(tweet.text)

    def on_connection_error(self):
        print("Erro de conexão. Reiniciando...")
        self.disconnect()

# Função para coletar tweets com a API v2
def coletar_tweets():
    # Criando uma instância do streaming
    stream = TwitterStream(BEARER_TOKEN)

    # Definindo as palavras-chave para filtragem
    palavras_chave = ["bolsonaro", "lula", "brasil", "bbb"]

    # Adicionando regras de filtragem para o stream
    stream.add_rules(tweepy.StreamRule(" OR ".join(palavras_chave)))

    print("Iniciando a coleta de tweets...")
    
    # Iniciando o stream de tweets
    stream.filter()

# Executando a coleta de tweets
if __name__ == "__main__":
    coletar_tweets()

import aiohttp
import asyncio

async def verificar_tempo(sessao, cidade):
    api_key = "fa75abe1f56fdef47be365425295d91b"  # Substitua pelo seu próprio API key
    url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}"

    async with sessao.get(url) as response:
        dados = await response.json()
        if 'cod' in dados and dados['cod'] != 200:
            await tratar_erro(dados)
        return dados

# Trata erros de resposta da API do OpenWeatherMap 
async def tratar_erro(response):
       if response.status == 404:
           raise Exception("Cidade não encontrada.")
       else:
           raise Exception("Ocorreu um erro na solicitação.")

# Busca a previsão do tempo para uma cidade usando a API do OpenWeatherMap.


# Solicita ao usuário o nome das cidades separadas por vírgula para requisição assincrona
async def pega_tempo_multiplo(cidades):
    async with aiohttp.ClientSession() as sessao:
        tasks = []
        for cidade in cidades:
            task = asyncio.ensure_future(verificar_tempo(sessao, cidade))
            tasks.append(task)
        responses = await asyncio.gather(*tasks)
        dados_clima = {}
        for cidade, response in zip(cidades, responses):
            if 'cod' in response and response['cod'] == 200:
                dados_clima[cidade] = response
        return dados_clima

# Extrai as informações relevantes dos dados da previsão do tempo. 
def processar_dados(data):
    principal = data['weather'][0]['main']
    descricao = data['weather'][0]['description']
    temperatura = round(float(data['main']['temp']) - 273, 1)
    umidade = data['main']['humidity']
    vento = data['wind']['speed']

    return {
        'Clima': principal,
        'Descrição': descricao,
        'Temperatura': temperatura,
        'Umidade': umidade,
        'Ventos': vento
    }

# Exibe as informações da previsão do tempo formatadas
def exibe(info_clima):
    print("Informações da Previsão do Tempo:")
    print("-------------------------------")
    for key, value in info_clima.items():
        print(f"{key}: {value}")


async def main():
    cidades = await pega_cidades()
    clima_dado = await pega_tempo_multiplo(cidades)
    for cidade, data in clima_dado.items():
        info_clima = processar_dados(data)
        print(f"Previsão do tempo para {cidade}:")
        exibe(info_clima)
        
# loop do codigo
async def repetir():
    while True:
        try:
            await main()
            escolha = await pega_escolha()
            if escolha.lower() != 's':
                break
        except Exception as e:
            print(f"Ocorreu um erro: {str(e)}")
            escolha = await pega_escolha()
            if escolha.lower() != 's':
                break

async def pega_escolha():
    escolha = input("Deseja fazer outra consulta? (S/N): ")
    while escolha.lower() not in ['s', 'n']:
        escolha = input("Por favor, responda com 'S' para Sim ou 'N' para Não: ")
    return escolha

async def pega_cidades():
    cidades = input("Digite o nome das cidades separadas por vírgula: ").split(',')
    cidades = [cidade.strip() for cidade in cidades]
    return cidades

asyncio.run(repetir())


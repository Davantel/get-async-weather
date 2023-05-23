# get-async-weather

Este projeto consiste em uma aplicação assíncrona em Python para obter a previsão do tempo de uma ou várias cidades utilizando a API OpenWeatherMap. O código utiliza recursos assíncronos para realizar as solicitações HTTP de forma eficiente e paralela.

Funcionalidades
----------------
1. Obter a previsão do tempo de uma única cidade:
   - O usuário pode digitar o nome da cidade desejada.
   - O código fará uma solicitação à API OpenWeatherMap e retornará as informações relevantes sobre a previsão do tempo, incluindo temperatura, descrição, umidade e velocidade do vento.
   - As informações serão exibidas na tela de forma formatada.

2. Obter a previsão do tempo de várias cidades simultaneamente:
   - O usuário pode digitar o nome de várias cidades separadas por vírgula.
   - O código realizará solicitações assíncronas para obter a previsão do tempo de cada cidade.
   - As informações de todas as cidades serão exibidas em paralelo na tela, fornecendo uma visão geral das condições climáticas de cada localidade.

3. Lidar com respostas inválidas:
   - O código verifica se a resposta da API OpenWeatherMap é válida, verificando se o código de status HTTP é 200 (OK). Caso contrário, uma exceção é lançada e uma mensagem de erro é exibida ao usuário.

4. Possibilidade de fazer consultas repetidas:
   - Após obter a previsão do tempo, o usuário tem a opção de fazer consultas repetidas ou encerrar o programa.

Requisitos
-----------
- Python 3.7 ou superior
- Biblioteca `aiohttp` (instalável via pip: `pip install aiohttp`)

Instruções de Uso
------------------
1. Clone ou faça o download deste repositório.

2. Instale as dependências necessárias executando o seguinte comando no terminal:
   ```
   pip install aiohttp
   ```

3. Execute o arquivo `previsao_tempo_assincrono.py` utilizando o Python:
   ```
   python previsao_tempo_assincrono.py
   ```

4. Siga as instruções apresentadas na tela para interagir com o programa e obter a previsão do tempo.

Contribuições
--------------
Contribuições são bem-vindas! Sinta-se à vontade para enviar pull requests com melhorias, correções de bugs ou novas funcionalidades.

Licença
--------
Este projeto é licenciado sob a [MIT License](https://opensource.org/licenses/MIT). Sinta-se à vontade para utilizá-lo de acordo com os termos da licença.

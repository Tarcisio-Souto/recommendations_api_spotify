# RECOMMENDATIONS_API_SPOTIFY

><h3 align="center">Contextualização</h3>
<br>

<p>
Este projeto consiste em um microsserviço de recomendação de trilhas sonoras das playlists existentes no Spotify, que são selecionadas por estilo considerando a temperatura de uma determinada localidade.
<p><br>

<p>A regra de negócio da aplicação retorna resultados de acordo com o seguinte:</p><br>

<ul>
    <li>Se a temperatura (celcius) estiver acima de 30 graus, serão retornadas faixas para festa (party).</li>
    <li>Caso a temperatura esteja entre 15 e 30 graus, serão retornadas faixas de música pop</li>
    <li>Se a temperatura estiver entre 10 e 14 graus, serão retornadas faixas de rock</li>
    <li>Caso contrário, serão retornadas faixas de música clássica</li>
</ul>
<br>

><h3 align="center">Requisitos</h3>
<br>

<p>
<b>Para a execução da aplicação é imprescindível ter os recursos abaixo:</b>
<br><br>
<ul>
    <li>
        <b>Editor de códigos (preferencialmente PyCharm ou Visual Studio Code)</b>
        <ul><br>
            <li>Visual Studio Code - Disponível em: <https://code.visualstudio.com/download></li>
            <li>PyCharm - Disponível em: <https://www.jetbrains.com/pycharm/download></li>
        </ul>  
    </li>
    <br>
    <li>
        <b>Python (preferencialmente a versão utilizada 3.10.4)</b>
        <ul><br>
            <li>Disponível em: <https://www.python.org/downloads></li>
        </ul>  
    </li>
    <br>
    <li>
        <b>Uvicorn (servidor web para Python)</b>
        <ul><br>
            <li>Para instalar, basta abrir o terminal do editor de códigos na pasta do projeto e digitar <b>pip install uvicorn</b></li>
        </ul>  
    </li>
    <br>
    <li>
        <b>FastAPI (framework para API's)</b>
        <ul><br>
            <li>Para instalar, basta abrir o terminal do editor de códigos na pasta do projeto e digitar <b>pip install fastapi</b></li>
        </ul>  
    </li>
    <br>
    <li>
        <b>Spotipy (biblioteca Python para API Web do Spotify)</b>
        <ul><br>
            <li>Para instalar, basta abrir o terminal do editor de códigos na pasta do projeto e digitar <b>pip install spotipy</b></li>
        </ul>  
    </li>
</ul>

<p><br>


><h3 align="center">Iniciando a Aplicação</h3>
<br>


<p>
Para iniciar a aplicação através do Uvicorn, abra o terminal do editor de códigos e insira o seguinte comando: <b>uvicorn main:app --reload --host 0.0.0.0</b>
<br><br>

<p>O próximo passo é acessar a aplicação através do navegador. Neste passo contaremos com um recurso do FastAPI, que nos permite acessar o Swagger UI, onde podemos inserir as coordenadas geográficas (latitude e longitude) ou o nome da cidade.<p>
<br>

<p>
O endereço a ser utilizado no navegador é <b>http://localhost:8000/docs</b>
</p>
<br>

![Screenshot](https://github.com/Tarcisio-Souto/recommendations_api_spotify/blob/main/capturas/home.PNG)

<br><br>

><h3 align="center">Recursos Utilizados</h3>
<br>

<p>
Para a realização do objetivo da aplicação, são utilizados recursos do OpenWeatherMaps API, que retorna informações relacionadas ao clima de alguma localidade, que pode ser encontrada através de alguns tipos de parâmetros, mas para esta experiência é facultativo ao usuário utilizar o nome da cidade ou as coordenadas geográficas de latitude e longitude:
<p><br>

![Screenshot](https://github.com/Tarcisio-Souto/recommendations_api_spotify/blob/main/capturas/endpoint_geographical.PNG)

<br><br>

![Screenshot](https://github.com/Tarcisio-Souto/recommendations_api_spotify/blob/main/capturas/endpoint_city.PNG)

<br><br>

<p>
Seja qual for o endpoint escolhido para executar a aplicação, o resultado será o mesmo:
</p><br>

![Screenshot](https://github.com/Tarcisio-Souto/recommendations_api_spotify/blob/main/capturas/result_json.PNG)

<br><br>

><p>TSS - Vitória/ES - 2022</p>


import os
import sys
import webbrowser
import argparse

def generate_clickjacking_test_page(url, target_filename='clickJ-target.html', attacker_filename='clickJ-attacker.html'):
    html_template = f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Prova de conceito Clickjacking</title>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
        <style>
            /* Estilos para o conteúdo visível */
            iframe {{
                width: 900px;
                height: 600px;
                position: relative;
                z-index: 1;
            }}
            /* Estilos para o conteúdo oculto */
            .clickjacking-iframe {{
                position: absolute;
                left: 20px;
                top: 250px;
                opacity: 0.8;
                background: AliceBlue;
                font-weight: bold;
                width: 900px;
                height: 150px; /* Ajuste a altura do iframe de exemplo conforme necessário */
                border: none;
            }}
            .clickjacking-text {{
                position: absolute;
                top: 50%; /* Ajuste a posição vertical do texto de exemplo conforme necessário */
                left: 50%;
                transform: translate(-50%, -50%);
                z-index: 2;
                cursor: pointer; /* Adicione o cursor pointer para indicar que o texto é clicável */
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1 class="mt-5">Resultados do Teste de Clickjacking</h1>
            <h2>Alvo: <a href="{url}">{url}</a></h2>
            <h3>Se você visualizar o website alvo exibido abaixo, ele está <font color="red">VULNERÁVEL</font>.</h3>
            <div style="position: relative;">
                <iframe src="{url}"></iframe>
                <iframe class="clickjacking-iframe" src="clickJ-attacker.html"></iframe>
                <div class="clickjacking-text" onclick="showPopup()">
                    <center><a href="#">Aqui seria adicionado o link usado na Eng Social</a><br>(normalmente invisível)</center>
                </div>
            </div>
        </div>

        <!-- Script para exibir o popup -->
        <script>
            function showPopup() {{
                alert('Teste efetuado com Sucesso');
            }}
        </script>
    </body>
    </html>
    '''

    html2_template = '''
    <!DOCTYPE html>
    <html>
    </html>
    '''

    with open(target_filename, 'w') as target_file, open(attacker_filename, 'w') as attacker_file:
        target_file.write(html_template)
        attacker_file.write(html2_template)

def main():
    parser = argparse.ArgumentParser(description='Verifica se uma página web é vulnerável a clickjacking.')
    parser.add_argument('url', type=str, help='URL da página web alvo')
    args = parser.parse_args()

    target_filename = 'clickJ-target.html'
    attacker_filename = 'clickJ-attacker.html'

    generate_clickjacking_test_page(args.url, target_filename, attacker_filename)

    local_url = 'file://' + os.path.abspath(target_filename)
    webbrowser.open(local_url)

    print('\n[+] Teste Concluído!')

if __name__ == '__main__':
    main()

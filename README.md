# Prova de Conceito Clickjacking

Esta é uma prova de conceito simples para demonstrar o funcionamento do clickjacking, uma vulnerabilidade que permite a um invasor enganar os usuários, fazendo-os clicar em elementos invisíveis de uma página web, mesmo que não queiram.

## Funcionamento

A prova de conceito utiliza Python para gerar duas páginas HTML: a página alvo e a página atacante. A página alvo contém um iframe que carrega o conteúdo da URL fornecida pelo usuário. A página atacante também possui um iframe oculto e um texto que normalmente estaria invisível.

Quando um usuário visita a página alvo, ele vê o conteúdo carregado no iframe principal e, sem saber, também está clicando em elementos da página atacante oculta. Esse é o conceito do clickjacking.

## Requisitos

- Python 3.x
- Biblioteca argparse

## Como Usar

1. Certifique-se de ter Python 3.x instalado em seu sistema.
2. Instale a biblioteca argparse, caso ainda não tenha:

pip install argparse

3. Execute o script `clickjacking.py` informando a URL da página que deseja testar:

python clickjacking.py <URL_DA_PAGINA_ALVO>

Exemplo:

python clickjacking.py https://www.example.com


4. A prova de conceito gerará dois arquivos: `clickJ-target.html` (página alvo) e `clickJ-attacker.html` (página atacante).
5. Uma janela do navegador será aberta automaticamente com a página alvo. Observe o conteúdo carregado no iframe e a mensagem "Aqui seria adicionado o link usado na Eng Social" que está invisível.

## Resultados

Se o teste for bem-sucedido e a página alvo for vulnerável ao clickjacking, você verá o conteúdo do site alvo no iframe e receberá um popup com a mensagem "Teste efetuado com Sucesso" quando clicar na mensagem invisível.

**AVISO:** Esta prova de conceito destina-se apenas a fins educacionais e de conscientização. Não utilize em sites ou aplicações sem permissão adequada dos proprietários. A exploração de vulnerabilidades sem autorização é ilegal e antiético.

## Referências

- [Projeto base - autor: nxkennedy ](https://github.com/nxkennedy/clickjack)
- [Clickjacking - OWASP](https://owasp.org/www-community/attacks/Clickjacking)
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [Python argparse - Documentação Oficial](https://docs.python.org/3/library/argparse.html)




## Autor

BrotherOfJhonny

---

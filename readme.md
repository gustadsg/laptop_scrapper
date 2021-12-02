# Laptop Scrapper

Este é um projeto de uma API com web scrapping usando Selenium para automatizar as buscas de informações e Flask para servir as informações, desenvolvido para o processo seletivo da Devnology

## Requisitos Funcionais

- ✅ buscar por um notebook (da marca Lenovo) em uma página web por meio de raspagem de dados usando python
- ✅ como padrão, ordenar preços do menor para o maior

## Requisitos Não Funcionais

- ✅ receber uma palavra chave relacionada ao título do produto
- ✅ poder alterar ordenação por meio de query params
- ✅ a cada busca salvar tudo em um banco de dados local
- ✅ poder receber flag que permite a busca no banco de dados (com tolerância de tempo) ao invés da raspagem
- ✅ utilizar selenim ou puppeteer
- ✅ receber parametros de preço minimo e maximo

## Banco de Dados

- id [PK]
- title
- description
- price
- url
- img_url
- rating
- num_reviews

## Como usar

### Instalação

Para instalar, siga o passo a passo:

```bash
git clone git@github.com:gustadsg/laptop_scrapper.git # fazer o download do projeto
cd laptop_scrapper # entrar no diretório do projeto
pip install -r requirements.txt # instalar dependências
python create_database.py # criar o banco de dados
flask run # inicia o servidor em http://localhost:5000
```

### Rotas

Esta aplicação possui uma única rota, por meio da qual são buscados dados do site de notebooks.

<ol>
  <li> /  
  
  Parâmetros (query params)

- q: texto que deve estar contido no título ou descrição do produto
- min_price: preço mínimo do produto
- max_price: preço máximo do produto
- reverse: produtos vêm ordenados de maior para menor preço quando este parâmetro é verdadeiro. Quando este parâmetro é Falso ou não enviado o resultado é ordenado de menor para maior preço
- update_tolerance: tempo máximo em segundos aceitável da última atualização. A depender do estado do banco de dados e do update_tolerance não será feito um novo scrapping e os dados fornecidos serão providos diretamente do banco de dados.

  </li>
</ol>

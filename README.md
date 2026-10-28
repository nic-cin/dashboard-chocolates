# Dashboard Chocolates

**Membros:** Leonardo, Kaique, Nicolas Oliveira

**Dataset:** chocolates, http://flavorsofcacao.com/chocolate_database.html

**App publicado:** https://dashboard-chocolates-c93ecjmdcrqmluyosbht9a.streamlit.app/

## Funcionalidades

- [x] Leitura do CSV
- [x] Conversão das colunas (cacau "76%" vira 76.0, nota vira número, características viram lista de sabores)
- [x] Métricas: total de chocolates, nota média, cacau médio e melhor origem
- [x] Faixas de cacau na tabela: Suave (até 69%), Meio amargo (70 a 79%) e Amargo (80% ou mais)
- [x] Tabela com nomes de coluna legíveis
- [x] Busca por chocolate ou fabricante sem diferenciar maiúsculas de minúsculas
- [x] Filtro por região de origem do cacau, com as opções tiradas dos dados e a opção "Todas"
- [x] Busca e filtros funcionando juntos
- [x] Mensagem quando nenhum chocolate é encontrado
- [x] Código organizado em funções e módulos:
  - `data.py` lê o CSV e converte as colunas
  - `analysis.py` calcula métricas, faixas de cacau e o resumo por país
  - `filters.py` faz a busca e os filtros
  - `app.py` monta a tela, a tabela e o mapa
  - `texts.py` e `locales/pt_br.py` guardam os textos da tela (para outro idioma, basta criar `locales/en.py` com as mesmas chaves)

## Funcionalidades extras

**Mapa por região.** O mapa mostra os países de origem do cacau coloridos por região. Passando o mouse em um país aparece a quantidade de avaliações e a nota média dele. Foi feito com `plotly.express.choropleth`.

**Relação entre % de cacau e a nota.** Os chocolates são separados em três faixas de cacau e o app mostra a nota média de cada faixa, para ver se o chocolate mais amargo recebe nota maior. Resultado: as faixas até 79% ficam perto de 3.2 e a faixa de 80% ou mais cai para 2.95.

**Busca por sabor.** No campo "Sabores" dá para escolher um ou mais sabores das características (fruity, nutty, cocoa...). A tabela mostra só os chocolates que têm todos os sabores escolhidos, ordenados pela nota.

## Como rodar

No Windows, dentro da pasta do projeto:

Antes de iniciar, confirme que o arquivo chocolates.csv está na raiz do projeto, no mesmo nível da pasta src.

```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
streamlit run src/app.py
```

O navegador abre em http://localhost:8501.

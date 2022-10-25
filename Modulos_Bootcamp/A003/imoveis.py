import requests
from bs4 import BeautifulSoup as bs
import pandas as pd


url = 'https://www.vivareal.com.br/venda/sp/mogi-das-cruzes/apartamento_residencial/?pagina={}'


# Get the number of available properties
qtd_imoveis = soup.find(
    'strong', 
    {'class': 'results-summary__count'}
).text.replace('.', '').strip()

qtd_imoveis = float(qtd_imoveis)
 
df = pd.DataFrame(
    columns = [
        'descricao',
        'endereco',
        'area',
        'quartos',
        'banheiro',
        'vagas',
        'valor',
        'condominio',
        'wlink_imovel',
    ]
)

# House properties
i = 0
while qtd_imoveis > df.shape[0]:
    i += 1
    request_page = requests.get(url.format(i))
    soup = bs(request_page.text)

    # Get a list with all houses information
    houses_list = soup.find_all(
        'a', 
        {'class': 'property-card__content-link js-card-title'}
    )

    print(f'Página: {i} \t\t Tamanho da Base: {df.shape[0]}')


    for house in houses_list:
        try:
            descricao = house.find('span', {'class': 'property-card__title'}).text.strip()
        except:
            descricao = ''
        try:
            endereco = house.find('span', {'class': 'property-card__address'}).text.strip()
        except:
            endereco = ''
        try:
            area = house.find('span', {'class': 'property-card__detail-value'}).text.strip()
        except:
            area = ''
        try:
            quartos = house.find('li', {'class': 'property-card__detail-room'}).span.text.strip()
        except:
            quartos = ''
        try:
            banheiro = house.find('li', {'class': 'property-card__detail-bathroom'}).span.text.strip()
        except:
            banheiro = ''
        try:
            vagas = house.find('li', {'class': 'property-card__detail-garage'}).span.text.strip()
        except:
            vagas = ''
        try:
            valor = house.find('div', {'class': 'property-card__price'}).text.strip()
        except:
            valor = ''
        try:
            condominio = house.find('strong', {'class': 'js-condo-price'}).text.strip()
        except:
            condominio = ''
        try:
            wlink_imovel = 'https://www.vivareal.com.br' + house['href']
        except:
            wlink_imovel = ''    

        df.loc[df.shape[0]] = [
            descricao,
            endereco,
            area,
            quartos,
            banheiro,
            vagas,
            valor,
            condominio,
            wlink_imovel,
        ]

df.to_csv('banco_imoveis_mogi_das_cruzes.csv', index=False)

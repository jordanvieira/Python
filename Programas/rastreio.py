import requests
import json

rastreio = requests.get(
    "https://proxyapp.correios.com.br/v1/sro-rastro/LX708971782CN")
rastreio = rastreio.json()
ObRastreio = rastreio['objetos']

# filtrando lista com dicionario \nData de Entrega: {} ObRastreio[s]["dtPrevista"],

for s in range(len(ObRastreio)):
    f = ObRastreio[s]["tipoPostal"]
    print("\n##########   RASTREIO    ##########\n")
    print("Codigo: {}\nTipo: {}\nDescrição: {}\n".format(
        ObRastreio[s]["codObjeto"],  f['categoria'], f['descricao']))
    l = ObRastreio[s]["eventos"]

    for i in range(len(l)):
        print("+-----------------------------------------------------------+")
        print("Codigo:{}\nDth:{}\nDescrição:{}".format(
            l[i]['codigo'], l[i]['dtHrCriado'], l[i]['descricao']))
        t = l[i]['unidade']
        j = l[i]["unidadeDestino"]
        print("Cidade Atual:{}\nUf Atual:{}\nCidade Destino:{}\nUf Destino:{}".format(
            t['endereco']['cidade'], t['endereco']['uf'], j['endereco']['cidade'], j['endereco']['uf']))
        print("+-----------------------------------------------------------+")

# print(rastreio.keys())
# print(rastreio.values())

# for i, v in rastreio.items():
#     print(f'Exebindo {i}')
#     for dk, dv in v.items():
#         print('f\t{dk} = {dv}')

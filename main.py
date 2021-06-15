import json
import random


class Entradas():
    def __init__(self, valor, pesos):
        self.valor = int(valor)
        self.pesos = dict(pesos)


def somatorio(entradas, peso):
    # print(f'Peso do Somatório selecionado = {peso}')
    constante = 0
    valor_somatorio = 0
    for e in entradas:
        valor_somatorio += e['valor'] * e['pesos'][peso]
    return round(valor_somatorio + constante, 2)


def custo(valor_obitido, valor_ideal):
    return round(((valor_obitido - valor_ideal) ** 2), 2)


def gerar_pesos(qtd_pesos):
    pesos = {}
    for n_peso in range(qtd_pesos):
        pesos[f'w{n_peso}'] = round(random.random(), 2)
    return pesos


def gera_lista_entradas(qtd_entradas, qtd_pesos_por_entradas):
    entradas = []
    for n_entradas in range(qtd_entradas):
        vars()[f'e{str(n_entradas)}'] = {
            "nome": f'Entrada {str(n_entradas)}',
            "valor": round(random.random(), 2),
            "pesos": gerar_pesos(qtd_pesos_por_entradas)
        }
        entradas.append(vars()[f'e{str(n_entradas)}'])
    return entradas


def chamada_peso_randomico(entrada):
    return f'w{str(random.randint(0, len(entrada["pesos"]) - 1))}'


def chamada_peso_randomico(valor):
    return f'w{str(random.randint(0, int(valor) - 1))}'


def print_lista_entradas(entradas):
    for item in entradas:
        print(f'{item["nome"]}: valor = {item["valor"]}, pesos = {item["pesos"]} ')
    print('\n')


def print_lista_entradas_bruta(entradas):
    for item in entradas:
        print(item)
    print("\n")


def calibrar(entradas, peso):
    for entrada in entradas:
        if(round(random.random(), 2) <= 0.50):
            entrada['pesos'][peso] = round(random.random(), 2) * -1
    return entradas

def gerarListasSomarioIdeaisCustoFinal(entradas):
    listaSomatorio = []
    listaIdeais = []
    custoFinal = 0
    for x in range(len(entradas[0]['pesos'])):
        somat = somatorio(entradas, f"w{x}")
        ideal = round(random.random(), 2)
        listaSomatorio.append(somat)
        listaIdeais.append(ideal)
        custoFinal += custo(somat, ideal)
    return listaSomatorio, listaIdeais, round(custoFinal, 2)


def exec(qtd_entradas, qtd_pesos, qtd_repeticoes_calibragem):
    print('\n=-=-=-=-=-=-=-= Start =-=-=-=-=-=-=-=\n')
    print(f'Quantidade de entradas: {qtd_entradas}\nQuantidade de pesos por entrada: {qtd_pesos}\n')

    entradas = gera_lista_entradas(qtd_entradas, qtd_pesos)
    print(f"Lista de entrada 0")
    print_lista_entradas(entradas)
    listaSomatorio, listaIdeais, custoFinal = gerarListasSomarioIdeaisCustoFinal(entradas)
    print(f'Lista Somaorio/peso: {listaSomatorio},\nLista Valores Ideais/peso: {listaIdeais},\nCusto Total: {custoFinal}')

    num_entrada = 0
    for x in range(qtd_repeticoes_calibragem):
        num_entrada += 1
        print(f"\nLista de entrada {num_entrada}")
        novasEntradas = calibrar(entradas, chamada_peso_randomico(len(entradas[0]['pesos'])))
        print_lista_entradas(novasEntradas)
        listaSomatorio, listaIdeais, custoFinal = gerarListasSomarioIdeaisCustoFinal(entradas)
        print(f'Lista Somaorio/peso: {listaSomatorio},\nLista Valores Ideais/peso: {listaIdeais},\nCusto Total: {custoFinal}')


    print("Fim da execução")

def run():
    # variaveis de entradas e pesos
    qtd_entradas = 10
    qtd_pesos = 10
    qtd_repeticoes_calibragem = 10
    exec(qtd_entradas, qtd_pesos, qtd_repeticoes_calibragem)




if __name__ == '__main__':
    run()


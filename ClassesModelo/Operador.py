import openpyxl
import Numero


class Funcionario:
    def __init__(self, nome, numeros):
        self.nome = nome
        # lista de objetos da classe numero
        self.numeros = numeros


# recebe o objeto do operador em questao e o adiciona na planilha
def adicionar_operador(operador_):
    book1 = openpyxl.load_workbook('PlanilhaNumeros.xlsx')
    sheet_page = book1['Sheet']

    list_param = []
    # montando lista a ser adicionada na planilha
    for i, n in enumerate(operador_.numeros):
        if i == 0:
            list_param.append(operador_.nome.lower())
        # trata cada atributo da classe numero como um item da lista list_param.append(str(n.numero))
        list_param.append(str(n.numero))
        list_param.append(str(n.ultima_recarga))
        list_param.append(str(n.proxima_recarga))
        list_param.append(str(n.status))

    sheet_page.append(list_param)

    book1.save('PlanilhaNumeros.xlsx')
    print('salvou')


# retorna uma lista com todos os opoeradores para tela inicial a da interface
def seleciona_operadores():
    list_operadores = []
    list_objtsNumeros = []
    book1 = openpyxl.load_workbook('PlanilhaNumeros.xlsx')
    sheet_page = book1['Sheet']

    # divide cada linha em listas menores
    for row in sheet_page:
        for i in range(1, len(row), 4):
            sub_row = list(row[i:i + 4])
            sub_row.insert(0, row[0].value)
            list_objtsNumeros.append(sub_row)

    for n, sub_row in enumerate(list_objtsNumeros):
        lista = []
        for p in sub_row:
            if type(p) != str():
                lista.append(p)

            lista.append(p)

        print(lista)
        numerin = Numero.Numero(*lista)
        print(numerin)
        list_operadores.append(numerin)

    # func = Funcionario(str(row[0].value),)
    # list_operadores.append(Funcionario(str(row[0].value), list_numeros))
    return list_operadores


seleciona_operadores()

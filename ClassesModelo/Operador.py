import openpyxl
import ClassesModelo.Numero as Num


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
    book1 = openpyxl.load_workbook('PlanilhaNumeros.xlsx')
    sheet_page = book1['Sheet']

    for row in sheet_page:
        list_objtsNumeros = []
        # divide cada linha em listas menores
        for i in range(1, len(row), 4):
            sub_row = list(row[i:i + 4])
            # atribui uma string equivalent a um item da lista
            for ind, r in enumerate(sub_row):
                sub_row[ind] = r.value
            # adiciona o nome no começo
            sub_row.insert(0, row[0].value)
            list_objtsNumeros.append(Num.Numero(*sub_row))

        list_operadores.append(Funcionario(list_objtsNumeros[0].operador, list_objtsNumeros))

    return list_operadores




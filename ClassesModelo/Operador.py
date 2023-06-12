import openpyxl


class Funcionario:
    def __init__(self, nome, numeros):
        self.nome = nome
        # lista de objetos da classe numero
        self.numeros = numeros


# recebe o objeto do operador em questao e o adiciona na planilha
def adicionar_operador(operador_):
    list_param = []
    book1 = openpyxl.load_workbook('PlanilhaNumeros.xlsx')
    sheet_page = book1['Sheet']
    #colunas = ['numero', 'ultima_recarga', 'proxima_recarga', 'status']

    #for i in range(4):
       # colunas.extend(colunas)

   # colunas.insert(0, 'nome')
   # sheet_page.append(colunas)

    for rows in sheet_page:

        list_param = []
        # montando lista a ser adicionada na planilha
        for i, n in enumerate(operador_.numeros):
            if i == 0:
                list_param.append(operador_.nome)
            # trata cada atributo da classe numero como um item da lista list_param.append(str(n.numero))
            list_param.append(str(n.numero))
            list_param.append(str(n.ultima_recarga))
            list_param.append(str(n.proxima_recarga))
            list_param.append(str(n.status))

    sheet_page.append(list_param)

    print('chegou')
    book1.save('PlanilhaNumeros.xlsx')
    print('salvou')

import tkinter as tk
import ClassesModelo.Operador as Operador
import ClassesModelo.Numero as numero


def main():
    root = tk.Tk()
    root.title('Controle Números:')

    # Labels
    tk.Label(root, text='Insira um nome para acessar seu números pertencentes:').grid(column=0, row=0)

    # Entradas
    ent_nome = tk.Entry(root)
    ent_nome.grid(column=0, row=1)

    def chama_funcaoalt():
        gerar_telaalt()
        print('Opa ta chamando__', ent_nome.get(), type(ent_nome.get()))

    def chama_funcaoad():
        gerar_telaad()

    # Button
    tk.Button(root, text='Encontrar', command=chama_funcaoalt).grid(column=0, row=2)
    tk.Button(root, text='Adicionar', command=chama_funcaoad).grid(column=0, row=3)
    root.mainloop()


# gera a tela para adicionar o operador em questão
def gerar_telaad():
    list_objnumeros = []
    boot2 = tk.Tk()
    boot2.title('Nome Operador')
    tk.Label(boot2, text=f'Nome').grid(column=0, row=0)
    tk.Label(boot2, text=f'Numeros').grid(column=1, row=0)
    tk.Label(boot2, text=f'Última recarga').grid(column=2, row=0)
    tk.Label(boot2, text=f'Proxima recarga').grid(column=3, row=0)
    tk.Label(boot2, text=f'Status').grid(column=4, row=0)

    op = tk.Entry(boot2)
    # dimenciona os componentes na tela
    for i in range(5):
        op.grid(column=0, row=1)
        # numeros
        num = tk.Entry(boot2)
        num.grid(column=1, row=1 + i)
        # recargas
        recs_u = tk.Entry(boot2)
        recs_u.grid(column=2, row=1 + i)

        recs_p = tk.Entry(boot2)
        recs_p.grid(column=3, row=1 + i)

        # status
        stts = tk.Entry(boot2)
        stts.grid(column=4, row=1 + i)

        # adiciona todas as entradas a uma lista
        list_objnumeros.append(numero.Numero(op.get(), num.get(), recs_u.get(), recs_p.get(), stts.get()))

    # atualiza a lista de objetos e a gera um novo objeto de operador para ser parametro do outro metodo
    def recolhe_dados():

        for n in list_objnumeros:
            n.operador = n.operador
            n.numero = n.numero
            n.ultima_recarga = n.ultima_recarga
            n.proxima_recarga = n.proxima_recarga
            n.status = n.status

        # vai receber um objeto do operadro com uma lista dos numeros realcionados

        # mesmo com o objeto sendo atualizado com strings ainda tive que fazer essa conversao
        print(list_objnumeros[0].operador, 'tipo', type(list_objnumeros[0].operador))

        operad = Operador.Funcionario(list_objnumeros[0].operador, list_objnumeros)

        ad_op(operad)

    tk.Button(boot2, text='Adicionar Número', command=num_amais).grid(column=4, row=10)
    tk.Button(boot2, text='Adicionar operador', command=recolhe_dados).grid(column=3, row=10)


def ad_op(operador):
    print("Adiciona o user ai nene")
    # metodo para adicionar os dados
    Operador.adicionar_operador(operador)


# receberar todas as informações do objeto operador e as mostrara ao usuarios
def gerar_telaalt():
    boot2 = tk.Tk()
    boot2.title('Nome Operador')
    tk.Label(boot2, text=f'Numeros').grid(column=1, row=0)
    tk.Label(boot2, text=f'Última recarga').grid(column=2, row=0)
    tk.Label(boot2, text=f'Proxima recarga').grid(column=3, row=0)
    tk.Label(boot2, text=f'Status').grid(column=4, row=0)

    # usar o indice dessa lista de forma espelhada com a lista de numeros
    # para saber c qual deles sera deletado
    list_chebutton = []

    # recebe uma lengh do tamanho da lista de numeros atribuida ao operador
    for i in range(4):
        list_chebutton.append(tk.Checkbutton(boot2).grid(column=0, row=1 + i))
        # numeros
        tk.Entry(boot2).grid(column=1, row=1 + i)
        # recargas
        tk.Entry(boot2).grid(column=2, row=1 + i)
        tk.Entry(boot2).grid(column=3, row=1 + i)

        # status
        tk.Entry(boot2).grid(column=4, row=1 + i)

    # Button
    tk.Button(boot2, text='Alterar').grid(column=3, row=6)
    tk.Button(boot2, text='Apagar').grid(column=4, row=6, columnspan=100)
    boot2.mainloop()


# gera uma tela menor para a adiçao de um numero extra a lista de um operador
def num_amais():
    boot2 = tk.Tk()
    boot2.title('Nome Operador')
    tk.Label(boot2, text=f'Nome').grid(column=0, row=0)
    tk.Label(boot2, text=f'Numeros').grid(column=1, row=0)
    tk.Label(boot2, text=f'Última recarga').grid(column=2, row=0)
    tk.Label(boot2, text=f'Proxima recarga').grid(column=3, row=0)
    tk.Label(boot2, text=f'Status').grid(column=4, row=0)

    for i in range(5):
        tk.Entry(boot2).grid(column=i, row=1)


main()

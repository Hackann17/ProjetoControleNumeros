import tkinter as tk
import ClassesModelo.Operador as Operador
import ClassesModelo.Numero as numero
from tkinter import messagebox


def gerador_botoes(root):
    def chama_funcaoalt(nome_operador):
        print(nome_operador)
        gerar_telaalt(nome_operador)

    def chama_funcaoad():
        gerar_telaad(root)

    list_Nop = Operador.seleciona_operadores()
    n_coluna = 1
    n_linha = 0

    for n, op in enumerate(list_Nop):
        n_linha += 1
        if n % 5 == 0:
            n_linha = 0
            n_coluna += 1

        tk.Button(root, text=op.nome, command=lambda t=op: chama_funcaoalt(t)).grid(column=n_coluna, row=n_linha,
                                                                                    padx=22)

    tk.Button(root, text='Adicionar', command=chama_funcaoad).grid(column=0, row=3)

    # listando nomes do soperadores registrados na planilha


def main():
    root = tk.Tk()
    root.title('Controle Números:')

    # Labels
    tk.Label(root, text='Insira um nome para acessar seu números pertencentes:').grid(column=0, row=0)

    gerador_botoes(root)

    root.mainloop()


# linpa os slots de entrada
def limpa_prompts(list_Entrynumeros):
    ent = 0
    while ent < len(list_Entrynumeros):
        list_Entrynumeros[ent].operador.delete(0, len(list_Entrynumeros[ent].operador.get()))
        list_Entrynumeros[ent].numero.delete(0, len(list_Entrynumeros[ent].numero.get()))
        list_Entrynumeros[ent].ultima_recarga.delete(0, len(list_Entrynumeros[ent].ultima_recarga.get()))
        list_Entrynumeros[ent].proxima_recarga.delete(0, len(list_Entrynumeros[ent].proxima_recarga.get()))
        list_Entrynumeros[ent].status.delete(0, len(list_Entrynumeros[ent].status.get()))
        ent += 1


# gera a tela para adicionar o operador em questão
def gerar_telaad(boot1):
    list_Entrynumeros = []
    boot2 = tk.Tk()
    boot2.title('Nome Operador')
    tk.Label(boot2, text=f'Nome').grid(column=0, row=0)
    tk.Label(boot2, text=f'Numeros').grid(column=1, row=0)
    tk.Label(boot2, text=f'Última recarga').grid(column=2, row=0)
    tk.Label(boot2, text=f'Proxima recarga').grid(column=3, row=0)
    tk.Label(boot2, text=f'Status').grid(column=4, row=0)

    op = tk.Entry(boot2)
    # dimenciona os componentes na tela
    for i in range(4):
        op.grid(column=0, row=1)
        # numeros
        num = tk.Entry(boot2, )
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
        list_Entrynumeros.append(numero.Numero(op, num, recs_u, recs_p, stts))

    # atualiza a lista de objetos e a gera um novo objeto de operador para ser parametro do outro metodo
    def recolhe_dados():
        list_numeros = []
        s = ''
        # gera uma nova lista de numero com cada atributo sendo uma string de fato, mantendo a lista inicial
        for n in list_Entrynumeros:
            objtNum = numero.Numero(n.operador.get(), n.numero.get(), n.ultima_recarga.get(), n.proxima_recarga.get(),
                                    n.status.get())

            if objtNum.operador == '':
                messagebox.showwarning('Atenção!', 'Iforme pelo menos o nome do operador ')
                break

            # substitui espaços sem numero pela string 'vazio'
            objtNum.numero = 'vazio' if objtNum.ultima_recarga == '' else objtNum.numero

            objtNum.ultima_recarga = 'vazio' if objtNum.ultima_recarga == '' else objtNum.ultima_recarga

            objtNum.proxima_recarga = 'vazio' if objtNum.proxima_recarga == '' else objtNum.proxima_recarga

            objtNum.status = 'vazio' if objtNum.status == '' else objtNum.status

            list_numeros.append(objtNum)

        # vai receber um objeto do operador com uma lista dos numeros relacionados
        operad = Operador.Funcionario(list_numeros[0].operador, list_numeros)
        Operador.adicionar_operador(operad)
        limpa_prompts(list_Entrynumeros)
        boot2.destroy()
        gerador_botoes(boot1)

    tk.Button(boot2, text='Adicionar Número', command=num_amais).grid(column=4, row=10)
    tk.Button(boot2, text='Adicionar operador', command=recolhe_dados).grid(column=3, row=10)


# recebera todas as informações do objeto operador e as mostrara ao usuario,
# realizando uma alteraçao sempre, seja com os mesmos dados quer com outros
def gerar_telaalt(oper_):
    boot2 = tk.Tk()
    boot2.title(oper_.nome)
    tk.Label(boot2, text=f'Numeros').grid(column=1, row=0)
    tk.Label(boot2, text=f'Última recarga').grid(column=2, row=0)
    tk.Label(boot2, text=f'Proxima recarga').grid(column=3, row=0)
    tk.Label(boot2, text=f'Status').grid(column=4, row=0)

    # recebe uma lengh do tamanho da lista de numeros atribuida ao operador
    for i, n in enumerate(oper_.numeros):
        """todos as entradas sao geradas,
        dimencionadas e tem um texto atribuido para cada uma"""

        # numeros
        numer = tk.Entry(boot2)
        numer.grid(column=1, row=1 + i)
        numer.insert(0, n.numero)
        # recargas
        recar_u = tk.Entry(boot2)
        recar_u.grid(column=2, row=1 + i)
        recar_u.insert(0, n.ultima_recarga)

        recarga_p = tk.Entry(boot2)
        recarga_p.grid(column=3, row=1 + i)
        recarga_p.insert(0, n.proxima_recarga)

        # status
        sts = tk.Entry(boot2)
        sts.grid(column=4, row=1 + i)
        sts.insert(0, n.status)

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

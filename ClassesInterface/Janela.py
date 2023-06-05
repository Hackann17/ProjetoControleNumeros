import tkinter as tk
from tkinter import ttk


def main():
    root = tk.Tk()
    root.title('Controle Números:')

    # Labels
    tk.Label(root, text='Insira um nome para acessar seu números pertencentes:').grid(column=0, row=0)

    # Entradas
    ent_nome = tk.Entry(root)
    ent_nome.grid(column=0, row=1)

    def chama_funcaoAlt():
        gerar_telaAlt()
        print('Opa ta chamando__', ent_nome.get(), type(ent_nome.get()))

    def chama_funcaoAd():
        gerar_telaAd()
        print('Opa ta chamando__', ent_nome.get(), type(ent_nome.get()))

    # Button
    tk.Button(root, text='Encontrar', command=chama_funcaoAlt).grid(column=0, row=2)
    tk.Button(root, text='Adicionar', command=chama_funcaoAd).grid(column=0, row=3)
    root.mainloop()


# receberar todas as informações do objeto operador e as mostrara ao usuarios
def gerar_telaAlt():
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


def gerar_telaAd():
    boot2 = tk.Tk()
    boot2.title('Nome Operador')
    tk.Label(boot2, text=f'Nome').grid(column=0, row=0)
    tk.Label(boot2, text=f'Numeros').grid(column=1, row=0)
    tk.Label(boot2, text=f'Última recarga').grid(column=2, row=0)
    tk.Label(boot2, text=f'Proxima recarga').grid(column=3, row=0)
    tk.Label(boot2, text=f'Status').grid(column=4, row=0)

    # se mantem sempre na mesma linha
    for i in range(5):
        tk.Entry(boot2).grid(column=i, row=1)
        tk.Entry(boot2).grid(column=1, row=1 + i)
        # recargas
        tk.Entry(boot2).grid(column=2, row=1 + i)
        tk.Entry(boot2).grid(column=3, row=1 + i)

        # status
        tk.Entry(boot2).grid(column=4, row=1 + i)

    tk.Button(boot2, text='Adicionar Número', command=num_amais).grid(column=4, row=10)


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

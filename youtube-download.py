from tkinter import *   
from pytube import YouTube
from tkinter import filedialog

janela = Tk()
janela.title('Baixar vídeos do youtube')

def download(link_):
    pasta = filedialog.askdirectory()
    try:
        YouTube(link_).streams.get_highest_resolution().download(pasta)
        print("funcionou")
    except Exception as err:
        print(err)


quadro = Frame(janela)
quadro.pack()

Label(quadro, text='Inserir link: ', font='arial 12 bold').pack(side='left')
link =  Entry(quadro, font='arial 20', width=50)
link.pack(side='left')

Button(quadro, bg='green', text='>>>', bd='1', fg='white', width=4, height=2, command=lambda: download(link.get())).pack()
janela.mainloop()
#Ana Beatriz Delgado e Lucas Dantas
from tkinter import *
from tkinter import messagebox

class Velha():
    def __init__(self):
        self.jan1()

    def jan1(self):
        self.root = Tk()
        self.root.title("Janela Principal")
        self.root.geometry("800x640")
        self.root.minsize(600,640)
        self.root.maxsize(1000,640)
        self.root.resizable(True,True)
        self.root.config(bg = "#00FF7F")
        self.widgets(self.root)
        self.root.mainloop()
        
    
    def widgets(self, janela):
        self.lbl1 = Label(janela, text = "Jogo da Velha", font= "Arial/Mt/Bold 50", bg = "#00FF7F", fg = "#FFF")
        self.lbl1.place(relx = 0.262, rely = 0.1)
        
        self.jogarB = Button(janela, text = "Jogar", font = "Arial/Mt/Bold 25", bg = "#FFF", fg = "#000", command = self.jogar)
        self.jogarB.place(relwidth= 0.2, relheight = 0.1, relx = 0.65, rely = 0.85)

        self.lbl2 = Label(janela, text = "Digite um nome:", font= "Arial/Mt/Bold 30", bg = "#00FF7F", fg = "#FFF")
        self.lbl2.place(relx = 0.14, rely = 0.55)

        self.nomePlayer = Entry(janela, font = "Arial/Mt/Bold 30")
        self.nomePlayer.place(relx = 0.30, rely = 0.65, relwidth= 0.35, relheight= 0.08)
    
    def jogar(self):
        if self.nomePlayer.get() == "":
            messagebox.showerror("Erro de dados","Não é possível iniciar o jogo sem um nome.")
        else:
            self.nome = self.nomePlayer.get()
            self.root.destroy()
            self.jan2()

    def jan2(self):
        self.jogo = Tk()
        self.jogo.title("Jogo da Velha")
        self.jogo.geometry("800x640")
        self.jogo.minsize(600,640)
        self.jogo.maxsize(1000,640)
        self.jogo.resizable(True,True)
        self.jogo.configure(bg= "#000000")

        self.player = Label(self.jogo, text = self.nome + ":", font = "Arial/Mt/Bold 30", bg = "#000", fg = "#FFF")
        self.player.place(relx = 0.13, rely = 0.03, relwidth= 0.3, relheight= 0.1)

        self.ia = Label(self.jogo, text = "Máquina" + ":", font = "Arial/Mt/Bold 30", bg = "#000", fg = "#FFF")
        self.ia.place(relx = 0.15, rely = 0.10, relwidth= 0.3, relheight= 0.1)
        
        self.l1c1 = Button(self.jogo, command = lambda: self.marcaX(self.l1c1))
        self.l1c1.place(relx = 0.24, rely = 0.27, relwidth = 0.15, relheight = 0.15)

        self.l1c2 = Button(self.jogo, command = lambda: self.marcaX(self.l1c2))
        self.l1c2.place(relx = 0.41, rely = 0.27, relwidth = 0.15, relheight = 0.15)

        self.l1c3 = Button(self.jogo, command = lambda: self.marcaX(self.l1c3))
        self.l1c3.place(relx = 0.58, rely = 0.27, relwidth = 0.15, relheight = 0.15)

        self.l2c1 = Button(self.jogo, command = lambda: self.marcaX(self.l2c1))
        self.l2c1.place(relx = 0.24, rely = 0.44, relwidth = 0.15, relheight = 0.15)
            
        self.l2c2 = Button(self.jogo, command = lambda: self.marcaX(self.l2c2))
        self.l2c2.place(relx = 0.41, rely = 0.44, relwidth = 0.15, relheight = 0.15)

        self.l2c3 = Button(self.jogo, command = lambda: self.marcaX(self.l2c3))
        self.l2c3.place(relx = 0.58, rely = 0.44, relwidth = 0.15, relheight = 0.15)
            
        self.l3c1 = Button(self.jogo, command = lambda: self.marcaX(self.l3c1))
        self.l3c1.place(relx = 0.24, rely = 0.61, relwidth = 0.15, relheight = 0.15)
            
        self.l3c2 = Button(self.jogo, command = lambda: self.marcaX(self.l3c2))
        self.l3c2.place(relx = 0.41, rely = 0.61, relwidth = 0.15, relheight = 0.15)

        self.l3c3 = Button(self.jogo, command = lambda: self.marcaX(self.l3c3))
        self.l3c3.place(relx = 0.58, rely = 0.61, relwidth = 0.15, relheight = 0.15)
           
        self.jogo.mainloop()
    
    def marcaX(self, botao):
        self.jogada = self.ia
        self.ia = botao
        self.jogador = botao
        self.jogador.configure(text = "X", font = "Arial/Mt/Bold 25")

        '''if self.jogador.configure(Text) == "X":
            self.ia.configure(Text = "O", font = "Arial/Mt/Bold 25")
'''
if __name__ == "__main__":
    game = Velha()
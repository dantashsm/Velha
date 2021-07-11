#Ana Beatriz Delgado e Lucas Dantas
from tkinter import *

class Principal():
    def _init_(self, corpo):
        self.root = corpo
        self.root.title("Janela Principal")
        self.root.geometry("800x640")
        self.root.resizable(True,True)
        #self.root.minsize(200, 300)
        #self.widgets(self.root)
        
    
    ''' def widgets(self, janela):
        lbl1 = Label(janela, text = "Jogo da Velha", font= "Arial 50")
        lbl1.place(relx = 0.24, rely = 0.1)
        btn1 = Button(janela, text = "Jogar", font = "Arial 30")
        btn1.place(width= 250, height = 50, relx = 0.35, rely = 0.65)'''
    
    '''class AbrirJogo(object):
        def _init_(self):
            self.jogo = Tk()
            self.jogo.geometry("640x600")
            self.jogo.configure(bg= "#000000")
           
            self.l1c1 = Label(self.jogo)
            self.l1c1.place(relx = 0.03, rely = 0.02, relwidth = 0.30, relheight = 0.30)

            self.l1c2 = Label(self.jogo)
            self.l1c2.place(relx = 0.35, rely = 0.02, relwidth = 0.30, relheight = 0.30)

            self.l1c3 = Label(self.jogo)
            self.l1c3.place(relx = 0.67, rely = 0.02, relwidth = 0.30, relheight = 0.30)

            self.l2c1 = Label(self.jogo)
            self.l2c1.place(relx = 0.03, rely = 0.34, relwidth = 0.30, relheight = 0.30)
            
            self.l2c2 = Label(self.jogo)
            self.l2c2.place(relx = 0.35, rely = 0.34, relwidth = 0.30, relheight = 0.30)

            self.l2c3 = Label(self.jogo)
            self.l2c3.place(relx = 0.67, rely = 0.34, relwidth = 0.30, relheight = 0.30)
            
            self.l3c1 = Label(self.jogo)
            self.l3c1.place(relx = 0.03, rely = 0.66, relwidth = 0.30, relheight = 0.30)
            
            self.l3c2 = Label(self.jogo)
            self.l3c2.place(relx = 0.35, rely = 0.66, relwidth = 0.30, relheight = 0.30)

            self.l3c3 = Label(self.jogo)
            self.l3c3.place(relx = 0.67, rely = 0.66, relwidth = 0.30, relheight = 0.30)
            
            
            self.jogo.mainloop()'''

    if __name__ == "_main_":
        Janela = Tk()
        Principal(Janela)
        Janela.mainloop()

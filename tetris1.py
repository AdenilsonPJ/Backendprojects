from tkinter import *
import random

# dimensões
lado=20
q_largura=12
q_altura=22
largura=lado*q_largura
altura=lado*q_altura

def randomPeca():
    return random.randint(1,7)

class Peca:
    def __init__(self,x,y,tipo):
        self.x=x
        self.y=y
        self.tipo=tipo
        if(tipo==1):
            self.grade=[[0,0,0],[1,1,0],[0,1,1]]
            self.size=3
        elif (tipo==2):
            self.grade=[[0,0,0],[0,tipo,tipo],[tipo,tipo,0]]
            self.size=3
        elif (tipo==3):
            self.grade=[[0,0,0],[0,tipo,tipo],[0,tipo,tipo]]
            self.size=3
        elif (tipo==4):
            self.grade=[[0,0,0],[0,0,tipo],[tipo,tipo,tipo]]
            self.size=3
        elif (tipo==5):
            self.grade=[[0,0,0],[tipo,0,0],[tipo,tipo,tipo]]
            self.size=3
        elif (tipo==6):
            self.grade=[[0,0,0],[0,tipo,0],[tipo,tipo,tipo]]
            self.size=3
        elif (tipo==7):
            self.grade=[[0,tipo,0,0],[0,tipo,0,0],[0,tipo,0,0],[0,tipo,0,0]]
            self.size=4

    def vira(self,Tela):
        copia=[[0 for i in range(self.size)] for j in range(self.size)]
        # fazer copia girar a peça
        for lin in range(self.size):
            for col in range(self.size):
                copia[self.size-1-col][lin]=self.grade[lin][col]
        # verificar colisão (copia)
        for lin in range(self.size):
            for col in range(self.size):
                if copia[lin][col] !=0 and (self.y+lin) >= q_altura:
                    return 0
                if copia[lin][col] !=0 and Tela.grade[self.y+lin][self.x+col] !=0:
                    return 0
        # passar copia para self.grade
        for lin in range(self.size):
            for col in range(self.size):
                self.grade[lin][col]=copia[lin][col]
        return 1

    def desce(self,Tela):
        for i in range(self.size):
            for j in range(self.size):
                if self.grade[i][j] !=0 and (self.y+1+i) >= q_altura:
                    return 0
                if self.grade[i][j] !=0 and Tela.grade[self.y+i+1][self.x+j] !=0:
                    return 0
        self.y=self.y+1
        return 1
    
    def direita(self,Tela):
        for i in range(self.size):
            for j in range(self.size):
                if self.grade[i][j] !=0 and (self.x+1+j) > q_largura-1:
                    return 0
                if Tela.grade[self.y][self.x+1]*self.grade[i][j] !=0:
                    return 0
        self.x=self.x+1
        return 1
    def esquerda(self,Tela):
        for i in range(self.size):
            for j in range(self.size):
                if self.grade[i][j] !=0 and (self.x-1+j) < 0:
                    return 0
                if Tela.grade[self.y][self.x-1]*self.grade[i][j] !=0:
                    return 0
        self.x=self.x-1
        return 1

class Tela:
    def __init__(self):
        self.grade=[[0 for i in range(q_largura)] for j in range(q_altura)]

    def elimina(self):
        l_elimina=[]
        for lin in range(q_altura-1,-1,-1):
            for col in range(q_largura):
                if (self.grade[lin][col]==0):
                    break
                if col==q_largura-1:
                    l_elimina.append(lin)
        return l_elimina

    def descelinhas(self,l_elimina):
        for i in l_elimina:
            for lin in range(i,0,-1):
                for col in range(q_largura):
                    self.grade[lin][col]=self.grade[lin-1][col]
            for j in range(len(l_elimina)):
                l_elimina[j] +=1

            for col in range(q_largura):
                self.grade[0][col]=0

    def addPeca(self,p):
        for lin in range(p.size):
            for col in range(p.size):
                if p.grade[lin][col] !=0:
                    self.grade[lin+p.y][col+p.x]=p.grade[lin][col]

    #def desenha(self):

class Game:
    def __init__(self):
        self.window = Tk()
        self.canvas = Canvas(self.window, width=largura, height=altura, bg='black')
        self.canvas.pack()
        self.p = Peca(3, 1, randomPeca())
        self.nump = 0
        self.t = Tela()

        self.window.bind('<Right>', self.moveDireita)
        self.window.bind('<Left>', self.moveEsquerda)
        self.window.bind('<Up>', self.gira)

    # Restarts the game
    def restart(self):
        self.p = Peca(3, 1, randomPeca())
        self.t = Tela()

    def gira(self, event):
        self.p.vira(self.t)

    def moveEsquerda(self, event):
        self.p.esquerda(self.t)

    def moveDireita(self, event):
        self.p.direita(self.t)

    def meDeACor(self, tipo):
        if tipo == 1:
            cor = 'blue'
        elif tipo == 2:
            cor = 'yellow'
        elif tipo == 3:
            cor = 'red'
        elif tipo == 4:
            cor = 'orange'
        elif tipo == 5:
            cor = 'green'
        elif tipo == 6:
            cor = 'purple'
        elif tipo == 7:
            cor = 'white'
        return cor

    def desenha(self):
        for i in range(self.p.size):
            for j in range(self.p.size):
                if self.p.grade[i][j] != 0:
                    self.canvas.create_polygon([(self.p.x + j) * lado + 2, (self.p.y + i) * lado + 2,
                                                (self.p.x + j) * lado + lado - 2, (self.p.y + i) * lado + 2,
                                                (self.p.x + j) * lado + lado - 2, (self.p.y + i) * lado + lado - 2,
                                                (self.p.x + j) * lado + 2, (self.p.y + i) * lado + lado - 2],
                                                fill=self.meDeACor(self.p.tipo))
        for lin in range(q_altura):
            for col in range(q_largura):
                if self.t.grade[lin][col] != 0:
                    self.canvas.create_polygon([col * lado + 2, lin * lado + 2, col * lado + lado - 2,
                                                lin * lado + 2, col * lado + lado - 2, lin * lado + lado - 2,
                                                col * lado + 2, lin * lado + lado - 2],
                                                fill=self.meDeACor(self.t.grade[lin][col]))

    def run(self):
        time = 0

        while True:
            self.canvas.delete('all')

            if time == 5:
                desceu = self.p.desce(self.t)
                time = 0
                if desceu == 0:
                    self.t.addPeca(self.p)
                    l_elimina = self.t.elimina()
                    if len(l_elimina) > 0:
                        self.t.descelinhas(l_elimina)
                    self.p = Peca(3, 1, randomPeca())
                    for lin in range(self.p.size):
                        for col in range(self.p.size):
                            if self.p.grade[lin][col] != 0 and self.t.grade[self.p.y + lin][self.p.x + col] != 0:
                                self.restart()  # Restart the game if a new piece cannot be placed
            else:
                time += 1

            self.desenha()
            self.canvas.after(50)
            self.window.update_idletasks()
            self.window.update()


g = Game()
g.run()

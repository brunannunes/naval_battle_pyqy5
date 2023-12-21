from PyQt5 import QtWidgets, uic, QtCore
import random
import sys
 
class telas:
    def __init__(self):
        self.app = QtWidgets.QApplication([])
        self.telaInicial = uic.loadUi("telas/inicial.ui")
        self.tabuleiro = uic.loadUi("telas/jogo.ui")
        self.telaGameOver = uic.loadUi("telas/perdeu.ui")
        self.telaWinner = uic.loadUi("telas/vencedor.ui")
        self.telaInicial.show()
        self.telaInicial.start.clicked.connect(self.mudar_telaInicial)
        self.telaInicial.Exit.clicked.connect(self.fechar_tela)
        self.telaGameOver.sair.clicked.connect(self.fechar_tela)
        self.telaWinner.sairGanhou.clicked.connect(self.fechar_tela)
        self.telaGameOver.againGameOver.clicked.connect(self.again)
        self.telaWinner.again.clicked.connect(self.again)
        self.tentativas_max = 6
        self.tentativas = 0

        coordenadasLetras = ["A", "B", "C", "D", "E"]
        coordenadasNumeros = ["1","2","3","4","5"]
        sorteio = []
 
        sorteio1 = random.sample(coordenadasLetras, 3)
 
        while True:
            sorteio2 = random.sample(coordenadasNumeros, 3)
            if int(sorteio2[1]) > 4:
                continue
            if int(sorteio2[2]) > 3:
                continue
            else:
                break
 
 
        for i in range(len(sorteio1)):
            sorteio.append(f"{sorteio1[i]}{sorteio2[i]}")
 
        print(sorteio)
 
 
        self.barcos = []
 
        for a in range(len(sorteio)):
            if a == 0:
                for i in range(len(sorteio)):
                    self.barcos.append(sorteio[i])
 
            if a == 1:
                print("\nCOMEÇA O 2")
                separado = list(sorteio[a])
                print(separado)
                self.barcos.append(f"{separado[0]}{int(separado[1])+1}")
                print(self.barcos)
               
           
            if a == 2:
                for i in range(2):
                    print("\nCOMEÇA O 3")
                    separado = list(sorteio[a])
                    print(separado)
                    self.barcos.append(f"{separado[0]}{int(separado[1])+(i + 1)}")
                    print(self.barcos)
 
            if a == 3:
                    for i in range(3):
                        print("\nCOMEÇA O 4")
                        separado = list(sorteio[a])
                        print(separado)
                        self.barcos.append(f"{separado[0]}{int(separado[1])+(i+1)}")
                        print(self.barcos)
 
        for button in self.tabuleiro.findChildren(QtWidgets.QPushButton):
            button.clicked.connect(self.selecionarBotao)
                   
           
        self.app.exec()
        sys.exit(self.app.exec_())

    def restart(self):
        QtCore.QCoreApplication.quit() #permite sair da aplicação
        QtCore.QProcess.startDetached(sys.executable, sys.argv) # permite que o programa incie novamente antes de sair por completo da aplicação

    def again(self):
        self.telaGameOver.close()
        self.telaWinner.close()
        self.restart()
            
 
    def mudar_telaInicial(self):
        self.telaInicial.close()
        self.tabuleiro.show()
    
    def fechar_tela(self):
        self.telaGameOver.close()
        self.telaWinner.close()
        self.telaInicial.close()
        exit()
    
    # def again(self):
    #     self.telaGameOver.close()
    #     self.telaInicial.show()
 
 
   
    # def selecionarBotao(self):
    #     sender = self.telaInicial.sender()
    #     senderCoordenada = sender.objectName()
 
       
    #     if senderCoordenada in self.barcos:
    #         sender.setStyleSheet("background-image: url('imagens/bomba_estourou.png'); border: none")
    #         self.barcos.remove(senderCoordenada)
 
    #         if len(self.barcos) == 0:
    #             self.tabuleiro.close()
    #             self.telaWinner.show()
 
    #     else:
    #         sender.setStyleSheet("background-image: url('imagens/bomba.png'); border: none")

    def selecionarBotao(self):
        sender = self.telaInicial.sender()
        senderCoordenada = sender.objectName()
       
     

        if self.tentativas < self.tentativas_max:
            
            if senderCoordenada in self.barcos:
                sender.setStyleSheet("background-image: url('imagens/bomba_estourou.png'); border: none")
                self.barcos.remove(senderCoordenada)
                
                if len(self.barcos) == 0:
                    self.tabuleiro.close()
                    self.telaWinner.show()
                    
                    
            else:
                sender.setStyleSheet("background-image: url('imagens/bomba.png'); border: none")
                self.tentativas += 1
                print(self.tentativas)

        else:
            self.tabuleiro.close()
            self.telaGameOver.show()
            

                

 
 
if __name__ == '__main__':
    c = telas()
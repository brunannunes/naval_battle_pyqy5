from PyQt5 import QtWidgets, uic, QtCore
import random
import sys


class telas:
    #classe para executar as telas
    def __init__(self):
        self.app = QtWidgets.QApplication([])
        self.telaInicial = uic.loadUi("telas/inicial.ui")
        self.tabuleiro = uic.loadUi("telas/jogo.ui")
        self.telaGameOver = uic.loadUi("telas/perdeu.ui")
        self.telaWinner = uic.loadUi("telas/vencedor.ui")
        #comando para exibr a tela de inicio
        self.telaInicial.show()

        #comando para linkar o botão com as telas desejadas
        self.telaInicial.start.clicked.connect(self.mudar_telaInicial)
        self.telaInicial.Exit.clicked.connect(self.fechar_tela)
        self.telaGameOver.sair.clicked.connect(self.fechar_tela)
        self.telaWinner.sairGanhou.clicked.connect(self.fechar_tela)

        #comando para jogar novamente o jogo
        self.telaGameOver.againGameOver.clicked.connect(self.again)
        self.telaWinner.again.clicked.connect(self.again)

        #tentativas durante o jogo
        self.tentativas_max = 6
        self.tentativas = 0

        #sortear as cordenadas dos barcos
        coordenadasLetras = ["A", "B", "C", "D", "E"]
        coordenadasNumeros = ["1","2","3","4","5"]
        sorteio = []
 
        #sorteia 3 caracteres de uma vez sem repetição
        sorteio1 = random.sample(coordenadasLetras, 3)
 
        #laço de repetição para sortear novamente caso a posiçao for invalida para o barco
        while True:
            sorteio2 = random.sample(coordenadasNumeros, 3)
            if int(sorteio2[1]) > 4:
                continue
            if int(sorteio2[2]) > 3:
                continue
            else:
                break
 
        #concatena as cordenadas sorteadas que possui o mesmo nome dos botões       
        for i in range(len(sorteio1)):
            sorteio.append(f"{sorteio1[i]}{sorteio2[i]}")
 
        print(sorteio)
 
        #lista para adicionar as cordenadas dos barcos
        self.barcos = []
 
        #lçao de repetição para separar os caracteres letras de numeros de cada cordenada
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
 
        #comando que irá executar smepre que os boto~es da tela forem clicados
        for button in self.tabuleiro.findChildren(QtWidgets.QPushButton):
            button.clicked.connect(self.selecionarBotao)
                   
        #comando que irá executra o pyqt   
        self.app.exec()
        #comando que irá "matar" o pyqt para ser possivel reiniciar o jogo
        sys.exit(self.app.exec_())

    #função que irá reiniciar o jogo
    def restart(self):
        QtCore.QCoreApplication.quit() #permite sair da aplicação
        QtCore.QProcess.startDetached(sys.executable, sys.argv) # permite que o programa incie novamente antes de sair por completo da aplicação

    #função que irá fechar as telas abertas e reiniciar o jogo
    def again(self):
        self.telaGameOver.close()
        self.telaWinner.close()
        self.restart()
            
 
    #função que irá fechar a tela inicial e abrir a tela do tabuleiro
    def mudar_telaInicial(self):
        self.telaInicial.close()
        self.tabuleiro.show()
    
    #função feita somente para fechar telas
    def fechar_tela(self):
        self.telaGameOver.close()
        self.telaWinner.close()
        self.telaInicial.close()
        exit()
   
   #função para jogar
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
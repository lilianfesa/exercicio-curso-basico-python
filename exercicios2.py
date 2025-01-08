#1. Crie uma classe que modele o objeto "carro".

class Carro:
    def __init__(self, marca, modelo, cor, ano, quilometragem=0):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.quilometragem = quilometragem
        self.ligado = False
    
    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print(f'O {self.modelo} está agora ligado.')
        else:
            print(f'O {self.modelo} já está ligado.')

    def desligar(self):
        if self.ligado:
            self.ligado = False
            print(f'O {self.modelo} está agora desligado.')
        else:
            print(f'O {self.modelo} já está desligado.')

    def andar(self, distancia):
        if self.ligado:
            self.quilometragem += distancia
            print(f'O {self.modelo} percorreu {distancia} km.')
        else:
            print(f'O {self.modelo} precisa estar ligado para andar.')

    def mostrar_informacoes(self):
        print(f'Marca: {self.marca}')
        print(f'Modelo: {self.modelo}')
        print(f'Cor: {self.cor}')
        print(f'Ano: {self.ano}')
        print(f'Quilometragem: {self.quilometragem} km')
        print(f"Status: {'Ligado' if self.ligado else 'Desligado'}")





#2. Um carro tem os seguintes atributos: ligado, cor, modelo, velocidade
class Carro:
    def __init__(self, cor, modelo, velocidade=0):
        self.ligado = False   # O carro começa desligado
        self.cor = cor
        self.modelo = modelo
        self.velocidade = velocidade

    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print(f'O {self.modelo} está agora ligado.')
        else:
            print(f'O {self.modelo} já está ligado.')

    def desligar(self):
        if self.ligado:
            self.ligado = False
            self.velocidade = 0  # Ao desligar o carro, a velocidade é zerada
            print(f'O {self.modelo} está agora desligado.')
        else:
            print(f'O {self.modelo} já está desligado.')

    def acelerar(self, aumento):
        if self.ligado:
            self.velocidade += aumento
            print(f'O {self.modelo} acelerou para {self.velocidade} km/h.')
        else:
            print(f'O {self.modelo} precisa estar ligado para acelerar.')

    def frear(self, reducao):
        if self.ligado:
            self.velocidade -= reducao
            if self.velocidade < 0:
                self.velocidade = 0
            print(f'O {self.modelo} reduziu a velocidade para {self.velocidade} km/h.')
        else:
            print(f'O {self.modelo} precisa estar ligado para frear.')

    def mostrar_informacoes(self):
        print(f'Carro modelo: {self.modelo}')
        print(f'Cor: {self.cor}')
        print(f'Status: {"Ligado" if self.ligado else "Desligado"}')
        print(f'Velocidade: {self.velocidade} km/h')






#3. Um carro tem os seguintes comportamentos: liga, desliga, acelera,desacelera.

class Carro:
    def __init__(self, cor, modelo):
        self.ligado = False   # O carro começa desligado
        self.cor = cor
        self.modelo = modelo
        self.velocidade = 0   # A velocidade começa em 0

    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print(f'O {self.modelo} está agora ligado.')
        else:
            print(f'O {self.modelo} já está ligado.')

    def desligar(self):
        if self.ligado:
            self.ligado = False
            self.velocidade = 0  # A velocidade é zerada ao desligar o carro
            print(f'O {self.modelo} está agora desligado.')
        else:
            print(f'O {self.modelo} já está desligado.')

    def acelerar(self, aumento):
        if self.ligado:
            self.velocidade += aumento
            print(f'O {self.modelo} acelerou para {self.velocidade} km/h.')
        else:
            print(f'O {self.modelo} precisa estar ligado para acelerar.')

    def desacelerar(self, reducao):
        if self.ligado:
            self.velocidade -= reducao
            if self.velocidade < 0:
                self.velocidade = 0
            print(f'O {self.modelo} desacelerou para {self.velocidade} km/h.')
        else:
            print(f'O {self.modelo} precisa estar ligado para desacelerar.')

    def mostrar_informacoes(self):
        print(f'Carro modelo: {self.modelo}')
        print(f'Cor: {self.cor}')
        print(f'Status: {"Ligado" if self.ligado else "Desligado"}')
        print(f'Velocidade: {self.velocidade} km/h')





#4. Crie uma instância da classe carro.

class Carro:
    def __init__(self, cor, modelo):
        self.ligado = False   # O carro começa desligado
        self.cor = cor
        self.modelo = modelo
        self.velocidade = 0   # A velocidade começa em 0

    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print(f'O {self.modelo} está agora ligado.')
        else:
            print(f'O {self.modelo} já está ligado.')

    def desligar(self):
        if self.ligado:
            self.ligado = False
            self.velocidade = 0  # A velocidade é zerada ao desligar o carro
            print(f'O {self.modelo} está agora desligado.')
        else:
            print(f'O {self.modelo} já está desligado.')

    def acelerar(self, aumento):
        if self.ligado:
            self.velocidade += aumento
            print(f'O {self.modelo} acelerou para {self.velocidade} km/h.')
        else:
            print(f'O {self.modelo} precisa estar ligado para acelerar.')

    def desacelerar(self, reducao):
        if self.ligado:
            self.velocidade -= reducao
            if self.velocidade < 0:
                self.velocidade = 0
            print(f'O {self.modelo} desacelerou para {self.velocidade} km/h.')
        else:
            print(f'O {self.modelo} precisa estar ligado para desacelerar.')

    def mostrar_informacoes(self):
        print(f'Carro modelo: {self.modelo}')
        print(f'Cor: {self.cor}')
        print(f'Status: {"Ligado" if self.ligado else "Desligado"}')
        print(f'Velocidade: {self.velocidade} km/h')





#5. Faça o carro "andar" utilizando os métodos da sua classe.

class Carro:
    def __init__(self, cor, modelo):
        self.ligado = False   # O carro começa desligado
        self.cor = cor
        self.modelo = modelo
        self.velocidade = 0   # A velocidade começa em 0

    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print(f'O {self.modelo} está agora ligado.')
        else:
            print(f'O {self.modelo} já está ligado.')

    def desligar(self):
        if self.ligado:
            self.ligado = False
            self.velocidade = 0  # A velocidade é zerada ao desligar o carro
            print(f'O {self.modelo} está agora desligado.')
        else:
            print(f'O {self.modelo} já está desligado.')

    def acelerar(self, aumento):
        if self.ligado:
            self.velocidade += aumento
            print(f'O {self.modelo} acelerou para {self.velocidade} km/h.')
        else:
            print(f'O {self.modelo} precisa estar ligado para acelerar.')

    def desacelerar(self, reducao):
        if self.ligado:
            self.velocidade -= reducao
            if self.velocidade < 0:
                self.velocidade = 0
            print(f'O {self.modelo} desacelerou para {self.velocidade} km/h.')
        else:
            print(f'O {self.modelo} precisa estar ligado para desacelerar.')

    def andar(self, distancia):
        if self.ligado:
            # Vamos supor que a velocidade média durante o "andar" é 30 km/h
            tempo = distancia / 30  # Tempo para percorrer a distância em horas
            self.velocidade = 30  # O carro estará a 30 km/h enquanto anda
            print(f'O {self.modelo} andou {distancia} km em {tempo:.2f} horas.')
        else:
            print(f'O {self.modelo} precisa estar ligado para andar.')

    def mostrar_informacoes(self):
        print(f'Carro modelo: {self.modelo}')
        print(f'Cor: {self.cor}')
        print(f'Status: {"Ligado" if self.ligado else "Desligado"}')
        print(f'Velocidade: {self.velocidade} km/h')




#6. Faça o carro "parar" utilizando os métodos da sua classe.
class Carro:
    def __init__(self, cor, modelo):
        self.ligado = False   # O carro começa desligado
        self.cor = cor
        self.modelo = modelo
        self.velocidade = 0   # A velocidade começa em 0

    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print(f'O {self.modelo} está agora ligado.')
        else:
            print(f'O {self.modelo} já está ligado.')

    def desligar(self):
        if self.ligado:
            self.ligado = False
            self.velocidade = 0  # A velocidade é zerada ao desligar o carro
            print(f'O {self.modelo} está agora desligado.')
        else:
            print(f'O {self.modelo} já está desligado.')

    def acelerar(self, aumento):
        if self.ligado:
            self.velocidade += aumento
            print(f'O {self.modelo} acelerou para {self.velocidade} km/h.')
        else:
            print(f'O {self.modelo} precisa estar ligado para acelerar.')

    def desacelerar(self, reducao):
        if self.ligado:
            self.velocidade -= reducao
            if self.velocidade < 0:
                self.velocidade = 0
            print(f'O {self.modelo} desacelerou para {self.velocidade} km/h.')
        else:
            print(f'O {self.modelo} precisa estar ligado para desacelerar.')

    def frear(self):
        if self.ligado:
            while self.velocidade > 0:
                self.velocidade -= 10  # Diminuindo a velocidade em 10 km/h a cada "freada"
                if self.velocidade < 0:
                    self.velocidade = 0
                print(f'O {self.modelo} desacelerou para {self.velocidade} km/h.')
            print(f'O {self.modelo} parou completamente.')
        else:
            print(f'O {self.modelo} precisa estar ligado para frear.')

    def parar(self):
        if self.ligado:
            self.frear()  # Chama o método de frear para parar o carro
        else:
            print(f'O {self.modelo} já está parado, pois está desligado.')

    def mostrar_informacoes(self):
        print(f'Carro modelo: {self.modelo}')
        print(f'Cor: {self.cor}')
        print(f'Status: {"Ligado" if self.ligado else "Desligado"}')
        print(f'Velocidade: {self.velocidade} km/h')



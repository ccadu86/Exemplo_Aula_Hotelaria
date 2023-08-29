class Hotel:
    def __init__(self, nome, endereco, cnpj):
        self.nome = nome
        self.endereco = endereco
        self.cnpj = cnpj
        self.cliente = {}
        self.reserva = {}

    def cadastrarCliente(self, id, nome, cpf, tel):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.tel = tel        
        self.cliente[self.id] = [self.nome, self.cpf, self.tel]
    
    def listarClientes(self):
        for chave,valor in self.cliente.items():
            print(f"ID:{chave} - Nome: {valor[0]} - CPF: {valor[1]} - Telefone: {valor[2]}")

    def reservarQuarto(self, idCli, reserva_quarto):
        self.idCli = idCli
        self.reserva_quarto = reserva_quarto

        match self.reserva_quarto:
            case 1:
                x = "Quarto Deluxe"
            case 2:
                x = "Quarto de Casal"
            case 3:
                x = "Quarto de solteiro"
            case _:
                x = "N/A"                    

        self.reserva[self.idCli] = x

    def listarReservas(self):
        for chave,valor in self.reserva.items():
            print(f"ID:{chave} - Quarto:{valor}")

    def cancelarReserva():
        pass

    def disponibilidadeQuarto():
        pass

class Quarto:
    def __init__(self, qtd, capacidade, valor, desc):
        self.qtd = qtd
        self.capacidade = capacidade
        self.valor = valor
        self.desc = desc
        
    def getQtdQuarto(self):
        return self.qtd
    
    def setReservaQuarto(self, qtd):
        self.qtd = qtd
    
class DeluxeQuarto(Quarto):
    pass    

class CasalQuarto(Quarto):
    pass

class SolteiroQuarto(Quarto):
    pass

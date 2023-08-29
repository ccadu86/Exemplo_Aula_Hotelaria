from Classes import *
import os

def main():
    contID = 0

    hotel = Hotel("Quality","Av. Brasil", "10.123.321/0001-5")
    quarto_deluxe = DeluxeQuarto(2,4,500,"Quarto com varanda, cama de casal e hidromassagem")
    quarto_casal = CasalQuarto(4,2,300,"Quarto com cama de casal")
    quarto_solteiro = SolteiroQuarto(8,1,150,"Quarto com cama de solteiro")
    
    sair = False
    while sair == False:
        try:
            os.system("cls")
            print("---MENU---")
            print("01 - CADASTRAR CLIENTE")
            print("02 - DISPONIBILIDADE DE QUARTOS")
            print("03 - RESERVAR QUARTO")
            print("04 - CANCELAR RESERVA")
            print("05 - LISTAR CLIENTES")
            print("06 - LISTAR RESERVAS")
            print("00 - SAIR")
            print("--------")
            print("")

            print("Qual opção deseja?")
            menu = int(input(">> "))
            os.system("pause")

            match menu:
                case 1:
                    os.system("cls")
                    print("---CADASTRO DE CLIENTE---")
                    print("INFORME OS SEUS DADOS")
                    contID += 1
                    id = contID
                    nome = input("Nome - ")
                    cpf = int(input("CPF - "))
                    tel = int(input("Telefone - "))                    

                    hotel.cadastrarCliente(id, nome, cpf, tel)

                    print("CLIENTE CADASTRADO")
                    print("--------")
                    os.system("pause")

                case 2:
                    os.system("cls")
                    print("---DISPONIBILIDADE DE QUARTOS---")
                    print(f"Quantidade de quartos DELUXE: {quarto_deluxe.getQtdQuarto()}")
                    print(f"Quantidade de quartos CASAL: {quarto_casal.getQtdQuarto()}")
                    print(f"Quantidade de quantos SOLTEIRO: {quarto_solteiro.getQtdQuarto()}")
                    os.system("pause")

                case 3:
                    os.system("cls")
                    print("---DISPONIBILIDADE DE QUARTOS---")
                    print(f"Quantidade de quartos DELUXE: {quarto_deluxe.getQtdQuarto()}")
                    print(f"Quantidade de quartos CASAL: {quarto_casal.getQtdQuarto()}")
                    print(f"Quantidade de quantos SOLTEIRO: {quarto_solteiro.getQtdQuarto()}")
                    print("------")
                    print(" ")
                    print("---QUAL QUARTO DESEJA RESERVAR---")
                    print("01 - DELUXE")
                    print("02 - CASAL")
                    print("03 - SOLTEIRO")

                    reserva_quarto = int(input(">> "))
                    idCli = int(input("Informe o ID do Cliente: "))

                    if reserva_quarto > 0 and reserva_quarto <= 3:
                        hotel.reservarQuarto(idCli, reserva_quarto)
                    else:
                        print("Valor Invalido")

                    match reserva_quarto:
                        case 1:                            
                            quarto_deluxe.setReservaQuarto(quarto_deluxe.getQtdQuarto() - 1)
                        case 2:
                            quarto_casal.setReservaQuarto(quarto_casal.getQtdQuarto() - 1)
                        case 3:
                            quarto_solteiro.setReservaQuarto(quarto_solteiro.getQtdQuarto() - 1)

                case 4:
                    pass

                case 5:
                    os.system("cls")
                    print("LISTA DE CLIENTES")
                    hotel.listarClientes()
                    os.system("pause")

                case 6:
                    os.system("cls")
                    print("LISTA DE RESERVAS")
                    hotel.listarReservas()
                    os.system("pause")

                case 0:
                    print("SAINDO ...")
                    print("------")
                    sair = True

                case _:
                    print("Valor invalido")
                    print("------")

        except Exception as erro:
            print("Valor invalido")
            print(erro.__class__.__name__)
            print("")
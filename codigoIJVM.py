from funções import Funcoes

#Essa classe vai ser responsavel por realizar o tratamento final do codigo e retornar o codigo em ijvm
class CodigoIJVM():
    '''
    Esse metodo vai ser responsavel por retornar o numero de endereços que o codigo possui
    '''
    def quantidadeEndereco(self,listaCodigo):
        cont = 0
        for j in range(len(listaCodigo)):
            txt_atual = ""
            for i in range(len(listaCodigo[j])):
                txt_atual += listaCodigo[j][i]
                if (txt_atual == "BIPUSH"):
                    cont += 2
                    break
                if (txt_atual == "ILOAD"):
                    cont += 2
                    break
                if (txt_atual == "ISTORE"):
                    cont += 2
                    break
                if (txt_atual == "IADD"):
                    cont += 1
                    break
                if (txt_atual == "ISUB"):
                    cont += 1
                    break
                if (txt_atual == "IAND"):
                    cont += 1
                    break
                if (txt_atual == "ISUB"):
                    cont += 1
                    break
                if (txt_atual == "IOR"):
                    cont += 1
                    break
                if (txt_atual == "NOP"):
                    cont += 1
                    break
                if (txt_atual == "DUP"):
                    cont += 1
                    break
                if (txt_atual == "GOTO"):
                    cont += 3
                    break
                if (txt_atual == "IFLT"):
                    cont += 3
                    break
        i = 2
        cont = hex(cont)
        cont1 = ""
        while (i < len(cont)):
            cont1 += cont[i]
            i += 1
        return cont1

    # Essa função vai ser responsavel por retornar o codigo inicial padrão do programa ijvm
    def codigoInicial(self, cont):
        inicio = ""
        if (len(cont) == 1):
            inicio = "1deadfad0001000000000000000000000000000" + cont
        if (len(cont) == 2):
            inicio = "1deadfad000100000000000000000000000000" + cont
        if (len(cont) == 3):
            inicio = "1deadfad00010000000000000000000000000" + cont
        if (len(cont) == 4):
            inicio = "1deadfad0001000000000000000000000000" + cont
        if (len(cont) == 5):
            inicio = "1deadfad000100000000000000000000000" + cont
        if (len(cont) == 6):
            inicio = "1deadfad00010000000000000000000000" + cont
        if (len(cont) == 7):
            inicio = "1deadfad0001000000000000000000000" + cont
        if (len(cont) == 8):
            inicio = "1deadfad000100000000000000000000" + cont
        if (len(cont) == 9):
            inicio = "1deadfad00010000000000000000000" + cont
        if (len(cont) == 10):
            inicio = "1deadfad0001000000000000000000" + cont
        if (len(cont) == 11):
            inicio = "1deadfad000100000000000000000" + cont
        if (len(cont) == 12):
            inicio = "1deadfad00010000000000000000" + cont
        if (len(cont) == 13):
            inicio = "1deadfad0001000000000000000" + cont
        return inicio

    '''
    A função transforma_codigo() vai ser a função main
    Essa função vai rodar todo codigo identificando as palavras IJVM(BIPUSH OR ILOAD BY EXAMPLE)
    Quando a função identificar a palavra ela vai chamar a função correspondente a palavra
    A função correspondente vai receber como parametro a lista e a posição da lista que a palavra está guardada
    Após isso a função deve retornar o valor em HEXADECIMAL correspondente a palavra
    '''
    def transforma_codigo(self,listaCodigo):
        function = Funcoes()
        saidaHexadecimal = ""
        for i in range(len(listaCodigo)):
            txt_atual = ""
            if (listaCodigo[i] == ".var"):
                listaVariaveis = function.ponto_var(listaCodigo, i)

            for j in range(len(listaCodigo[i])):
                txt_atual += listaCodigo[i][j]
                if (txt_atual == "BIPUSH"):
                    saidaHexadecimal += function.bipush(listaCodigo[i])
                    break
                if (txt_atual == "ISTORE"):
                    saidaHexadecimal += function.istore(listaCodigo[i], listaVariaveis)
                    break
                if (txt_atual == "IADD"):
                    saidaHexadecimal += "60"
                    break
                if (txt_atual == "GOTO"):
                    saidaHexadecimal += function.goto(listaCodigo[i], listaCodigo, i)
                    if (saidaHexadecimal == 0):
                        print("erro")
                    break
                if (txt_atual == "IFLT"):
                    saidaHexadecimal += function.iflt(listaCodigo[i], listaCodigo, i)
                    if (saidaHexadecimal == 0):
                        print("erro")
                    break
                if (txt_atual == "ISUB"):
                    saidaHexadecimal += "64"
                    break
                if (txt_atual == "IAND"):
                    saidaHexadecimal += "7e"
                    break
                if (txt_atual == "IOR"):
                    saidaHexadecimal += "b0"
                    break
                if (txt_atual == "ILOAD"):
                    saidaHexadecimal += function.iload(listaCodigo[i], listaVariaveis)
                    break
                if (txt_atual == "NOP"):
                    saidaHexadecimal += "00"
                    break
                if (txt_atual == "DUP"):
                    saidaHexadecimal += "59"
                    break
        print(saidaHexadecimal)
        return saidaHexadecimal

    # Esse metodo vai ser responsavel por retornar o codigo final em ijvm
    def converteCodigo(self, listaCodigo):
        cont = self.quantidadeEndereco(listaCodigo)
        codigoInicial = self.codigoInicial(cont)
        valorHexadecimal = self.transforma_codigo(listaCodigo)
        codigo = ""
        codigo = codigoInicial + valorHexadecimal
        textoCodigo = ""
        for i in range(len(codigo)):
            if (i % 4 == 0 and i!=0):
                textoCodigo += " "
            if (i % 32 == 0 and i!=0):
                textoCodigo += "\n"
            textoCodigo += codigo[i]
        return textoCodigo, codigo


'''
Essa classe contém todas os meotodos que vão ser responsaveis por retornar um valor equivalente em ijvm.
'''

class Funcoes():
    '''
    A função bipush() vai receber o comando BIPUSH seguido do valor que deve ser colocado na pilha
    Ela vai retornar o codigo em hexadecimal correspondente a função BIPUSH
    '''
    def bipush(self,linhaBipush):
        valor = ""
        lista_valor = []
        lista_valor.extend(linhaBipush)
        i = 6
        # esse while vai rodar pela linha e vai receber o valor que ta sendo enviado para a pilha por meio da função BIPUSH
        while (i < len(linhaBipush)):
            valor += linhaBipush[i]
            i += 1
        valor_inteiro = int(valor)
        # Se o valor n estiver dentro do intervalo de operação do BIPUSH ele chamará a função erro
        if (valor_inteiro < 0 or valor_inteiro > 255):
            print("erro")
        valor_hex = hex(valor_inteiro)  # converte o valor para hexadecimal
        valor = "10"
        lista_valor = []
        lista_valor.extend(valor_hex)
        if (len(lista_valor) == 3):
            temp = "0" + lista_valor[2]
            return valor + temp
        i = 2
        while (i < len(lista_valor)):
            valor += lista_valor[i]
            i += 1
        return valor

    '''
    Esse metodo vai ser responsavel por retornar o valor em IJVM da função ISTORE
    '''
    def istore(self,linhaIstore, listaVariaveis):
        variavel = ""
        i = 6
        # Esse while vai receber a variavel
        while (i < len(linhaIstore)):
            variavel += linhaIstore[i]
            i += 1
        # Se a variavel for igual a alguma variavel que foi declarada, esse for vai retornar o endereço dessa variavel na memoria
        for i in range(len(listaVariaveis)):
            if (variavel == listaVariaveis[i][0]):
                endVariavel = listaVariaveis[i][
                    1]  # endVariavel armazena o endereço da variavel que está sendo colocada na pilha
        valorEnd = []
        valorEnd.extend(endVariavel)
        if (len(endVariavel) == 3):
            valorHexadecimal = "360" + valorEnd[2]
            return valorHexadecimal
        if (len(endVariavel) == 4):
            valorHexadecimal = "36" + valorEnd[2] + valorEnd[3]
            return valorHexadecimal
        if (len(endVariavel) > 4 or len(endVariavel) < 3):
            print("erro")

    '''
    Esse metodo vai ser responsavel por retornar o valor em ijvm da função ILOAD
    '''
    def iload(self,linhaIload, listaVariaveis):
        variavel = ""
        i = 5
        # Esse while vai receber a variavel
        while (i < len(linhaIload)):
            variavel += linhaIload[i]
            i += 1
        # Se a variavel for igual a alguma variavel que foi declarada, esse for vai retornar o endereço dessa variavel na memoria
        for i in range(len(listaVariaveis)):
            if (variavel == listaVariaveis[i][0]):
                endVariavel = listaVariaveis[i][
                    1]  # endVariavel armazena o endereço da variavel que está sendo colocada na pilha
        valorEnd = []
        valorEnd.extend(endVariavel)
        if (len(endVariavel) == 3):
            valorHexadecimal = "150" + valorEnd[2]
            return valorHexadecimal
        if (len(endVariavel) == 4):
            valorHexadecimal = "15" + valorEnd[2] + valorEnd[3]
            return valorHexadecimal
        if (len(endVariavel) > 4 or len(endVariavel) < 3):
            print("erro")

    '''
    Esse metodo vai ser responsavel por retornar uma lista, onde cada posição contém outra lista.
    Cada posição da primeira lista vai conter uma variavel e o endereço dessa variavel no codigo.
    A primeira posição da segunda lista vai conter o nome da variavel.
    A segunda posição da segunda lista vai conter o endereço da variavel no codigo.
    '''
    def ponto_var(self, listaCodigo, i):
        j = i + 1
        valor = 0
        listaVariaveis = []  # Essa lista vai guardar as variaveis e seu endereço na memoria
        '''
        Esse while vai ser responsavel por rodar o codigo do .var até o .end-var
        Ele vai guardar todas as variaveis declaradas junto com seu valor na pilha(posição da pilha)
        '''
        while (listaCodigo[j] != ".end-var"):
            listaVariaveis.append([listaCodigo[j], hex(valor)])
            valor += 1
            j += 1
        return listaVariaveis

    '''
    Esse metodo vai ser responsavel por retornar o codigo em ijvm equivalente a função GOTO
    Ele poderá retornar o codigo em ijvm, ou o valor "0".
    Caso ele retorne o valor 0, isso vai significar que o codigo contem um erro.
    '''
    def goto(self,linhaGoto, listaCodigo, j):
        variavel = ""
        i = 4
        cont = 0
        # Esse while vai ser responsavel por pegar a variavel do GOTO
        while (i < len(linhaGoto)):
            variavel += linhaGoto[i]
            i += 1
        while (j < len(listaCodigo)):
            txt_atual = ""
            k = 0
            while (k < len(listaCodigo[j])):
                txt_atual += listaCodigo[j][k]
                if (txt_atual == (variavel + ":")):
                    cont1 = ""
                    cont2 = hex(cont)
                    i = 2
                    while(i<len(cont2)):
                        cont1 += cont2[i]
                        i += 1
                    if (len(cont1) == 1):
                        return "a700" + "0" + cont1
                    return "a700" + cont1
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
                k += 1
            j += 1
        return 0
    '''
    Esse metodo vai ser responsavel por retornar o codigo em ijvm equivalente a função IFLT
    Ele poderá retornar o codigo em ijvm, ou o valor "0".
    Caso ele retorne o valor 0, isso vai significar que o codigo contem um erro.
    '''
    def iflt(self,linhaIflt, listaCodigo, j):
        variavel = ""
        i = 4
        cont = 0
        # Esse while vai ser responsavel por pegar a variavel do GOTO
        while (i < len(linhaIflt)):
            variavel += linhaIflt[i]
            i += 1
        while (j < len(listaCodigo)):
            txt_atual = ""
            k = 0
            while (k < len(listaCodigo[j])):
                txt_atual += listaCodigo[j][k]
                if (txt_atual == (variavel + ":")):
                    cont1 = ""
                    cont2 = hex(cont)
                    i = 2
                    while(i<len(cont2)):
                        cont1 += cont2[i]
                        i += 1
                    if (len(cont1) == 1):
                        return "9b00" + "0" + cont1
                    return "9b00" + cont1
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
                k += 1
            j += 1
        return 0
from registradores import Registradores
class ChamaRegistradores:

    def __init__(self):
        self.listaReg = []


    def recebeCodigo(self, codigo, i, posSP, linha, h, pilha, variaveis):
        reg = Registradores()

        comando = codigo[i] + codigo[i+1]
        try:
            proxInstrucao = codigo[i + 4] + codigo[i + 5]
        except:
            proxInstrucao = "ff"
        if(comando == "10"): #BIPUSH
            pilha[1] = pilha[0]
            pilha[0] = codigo[i + 2] + codigo[i + 3]
            posSP += 1
            linha += 2
            string = "10 BIPUSH " + pilha[0]
            self.listaReg = reg.registrador(string,pilha[0],posSP, linha, proxInstrucao, h)
            i += 4
            return i, posSP,linha,h,pilha,variaveis,self.listaReg

        if (comando == "59"):
            linha += 1
            print("DUP")
            i += 2
            return i, posSP,linha,h,pilha,variaveis,self.listaReg


        if (comando == "7e"): #IAND MDR  E TOS COM ERRO
            linha += 1
            posSP -= 1
            if (len(pilha[0]) == 1):
                h = "0000000" + pilha[0]
            else:
                h = "000000" + pilha[0]
            try:
                proxInstrucao = codigo[i + 2] + codigo[i + 3]
            except:
                proxInstrucao = "ff"

            string = "7e IAND"
            pilha[0] = "00"
            pilha[1] = "00"
            self.listaReg = reg.registrador(string, pilha[0], posSP, linha, proxInstrucao, h)
            i += 2
            return i, posSP,linha,h,pilha,variaveis, self.listaReg


        if (comando == "60"): #IADD
            linha += 1
            posSP -= 1
            try:
                proxInstrucao = codigo[i + 2] + codigo[i + 3]
            except:
                proxInstrucao = "ff"

            if(len(pilha[0]) == 1):
                h = "0000000" + pilha[0]
            else:
                h = "000000" + pilha[0]

            valorSoma = int(pilha[0],16) + int(pilha[1],16) #pega os dois valores da pilha, converte de hex para int e soma os valores
            valorSomaHex = ""
            k=2
            while(k<len(hex(valorSoma))):
                valorSomaHex += hex(valorSoma)[k]
                k +=1
            string = "60 IADD"
            pilha[0] = valorSomaHex
            pilha[1] = "00"
            self.listaReg = reg.registrador(string, pilha[0], posSP, linha, proxInstrucao, h)
            i += 2
            return i, posSP,linha,h,pilha,variaveis, self.listaReg


        if (comando == "b0"): ##IOR MDR  E TOS COM ERRO
            linha += 1
            posSP -= 1
            if (len(pilha[0]) == 1):
                h = "0000000" + pilha[0]
            else:
                h = "000000" + pilha[0]
            try:
                proxInstrucao = codigo[i + 2] + codigo[i + 3]
            except:
                proxInstrucao = "ff"

            string = "7e IAND"
            pilha[0] = "00"
            pilha[1] = "00"
            self.listaReg = reg.registrador(string, pilha[0], posSP, linha, proxInstrucao, h)
            i += 2
            return i, posSP,linha,h,pilha,variaveis, self.listaReg


        if (comando == "15"): ## ILOAD
            linha += 2
            posSP += 1
            endereco = codigo[i + 2] + codigo[i + 3]
            for j in range(len(variaveis)):
                if(variaveis[j][0]== endereco):
                    pilha[1] = pilha[0]
                    pilha[0] = variaveis[j][1]
                    break
            string = "15 ILOAD " + endereco
            self.listaReg = reg.registrador(string, pilha[0], posSP, linha, proxInstrucao, h)
            i += 4
            return i, posSP,linha,h,pilha,variaveis, self.listaReg

        if (comando == "64"):  # ISUB
            linha += 1
            posSP -= 1
            try:
                proxInstrucao = codigo[i + 2] + codigo[i + 3]
            except:
                proxInstrucao = "ff"

            if (len(pilha[0]) == 1):
                h = "0000000" + pilha[0]
            else:
                h = "000000" + pilha[0]

            valorSub = int(pilha[1], 16) - int(pilha[0], 16)  # pega os dois valores da pilha, converte de hex para int e subtrai os valores
            valorSubHex = ""
            k = 2
            hexx = self.tohex(valorSub)
            print(hexx)
            while (k < len(hexx)):
                valorSubHex += hexx[k]
                k += 1
            string = "60 IADD"
            print(valorSubHex)
            pilha[0] = valorSubHex
            pilha[1] = "00"
            self.listaReg = reg.registrador(string, pilha[0], posSP, linha, proxInstrucao, h)
            i += 2
            return i, posSP, linha, h, pilha, variaveis, self.listaReg


        if (comando == "00"): ##NOP
            string = "00 NOP"
            try:
                proxInstrucao = codigo[i + 2] + codigo[i + 3]
            except:
                proxInstrucao = "ff"
            self.listaReg = reg.registrador(string,pilha[0], posSP, linha, proxInstrucao, h)
            i += 2
            return i, posSP,linha,h,pilha,variaveis, self.listaReg


        if (comando == "36"): ##ISTORE
            posSP -= 1
            linha += 2
            endereco = codigo[i + 2] + codigo[i + 3]
            variaveis.append([endereco,pilha[0]])
            pilha[0] = pilha[1]
            pilha[1] = "00"
            h = "00008000"
            string = "36 ISTORE " + endereco
            self.listaReg = reg.registrador(string,pilha[0], posSP, linha, proxInstrucao, h)
            i += 4
            return i, posSP,linha,h,pilha,variaveis, self.listaReg
        i += 1
        return i, posSP, linha, h, pilha, variaveis, self.listaReg

    def tohex(self,val):
        return hex((val + (1 << 32)) % (1 << 32))



# r = ChamaRegistradores()
# a = "1deadfad00010000000000000000000000000008100410056010067e"
# r.recebeCodigo(a)
# print(a)

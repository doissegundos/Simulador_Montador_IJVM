
class Registradores:
    def inicio(self):
        mar = "00000000"
        mdr = "00000000"
        pc = "ffffffff"
        sp = "00008010"
        lv = "00008000"
        cpp = "00004000"
        tos = "00000000"
        opc = "00000000"
        h = "00000000"
        mbr = "00"
        return mar,mdr,pc,mbr,sp,lv,cpp,tos,opc,h

    def registrador(self,string,valor,posicao,linha, proxInstrucao, h):
        if(len(valor) == 8):
            mdr = valor
            tos = valor
        else:
            mdr = "000000" + valor
            tos = "000000" + valor

        sp = "0000801" + str(posicao)
        mar = "0000801" + str(posicao)
        cpp = "00004000"
        opc = "00000000"
        h = h
        lv = "00008000"
        mbr = proxInstrucao
        i = 2
        pcHex = ""
        while(i<len(hex(linha))):
            pcHex += hex(linha)[i]
            i += 1

        if(len(str(linha)) == 1):
            pc = "0000000" + pcHex
        else:
            pc = "000000" + pcHex
        #self.exibir(mar, mdr, pc, mbr, sp, lv, cpp, tos, opc, h)
        listaRegistradores = mar, mdr, pc, mbr, sp, lv, cpp, tos, opc, h
        return listaRegistradores

    # #DESABILITEI POR CAUSA DA INTERFACE
    # def exibir(self,mar,mdr,pc,mbr,sp,lv,cpp,tos,opc,h):
    #     print("MAR: " + mar)
    #     print("MDR: " + mdr)
    #     print("PC: " + pc)
    #     print("MBR: " + mbr)
    #     print("SP: " + sp)
    #     print("LV: " + lv)
    #     print("CPP: " + cpp)
    #     print("TOS: " + tos)
    #     print("OPC: " + opc)
    #     print("H: " + h)
    #     print("\n")








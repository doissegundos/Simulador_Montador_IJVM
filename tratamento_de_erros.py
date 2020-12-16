'''
Essa classe contém metodos para tratamento de codigo e verificação de possiveis erros
'''
class Tratamento():
    '''
    O metodo converte_txt_lista() é responsavel por separar o arquivo texto do codigo .jas em uma lista
    onde cada posição dessa lista guarda os comandos de uma linha do codigo .jas
    '''
    def converte_txt_lista(self,texto):
        listaCodigo = []
        linha = ""
        for i in range(len(texto)):
            if (texto[i] != "\n"):
                linha += texto[i]
            if (texto[i] == "\n" or linha == ".end-main"):
                listaCodigo.append(linha)
                linha = ""
        return listaCodigo

    '''
    A função formatar_linha() é responsavel por formatar a linha, ela vai retirar os espaços vazios e \t da linha.
    '''
    def formatar_linha(self,listaCodigo):
        for i in range(len(listaCodigo)):
            txt_format = ""
            temp = listaCodigo[i]
            # esse for vai ser responsavel por remover os espaços vazios e os \t da linha e apagar os possiveis comentarios que possam ter na linha.
            for j in range(len(listaCodigo[i])):
                if (temp[j] == "/" and temp[j + 1] == "/"):
                    break
                if (temp[j] != "\t" and temp[j] != " "):
                    txt_format += temp[j]
            listaCodigo[i] = txt_format
        return listaCodigo

    '''
    A função remove_linhas_nulas() vai excluir linhas vazias ou nulas
    '''
    def remove_linhas_nulas(self, txt):
        txtformat = []
        for i in range(len(txt)):
            if (txt[i] != ""):
                txtformat.append(txt[i])
        return txtformat

    '''
    A função pontomain() testa se o programa está sendo inicializado de forma correta.
    Sendo assim se o codigo não iniciar com ".main" e n terminar com ".end-main", o programa dará um erro
    '''
    def pontomain(self,listaCodigo):
        i = len(listaCodigo) - 1  # define o valor da ultima posição da lista
        if (listaCodigo[0] != ".main" or listaCodigo[i] != ".end-main"):
            print("erro")
            exit(1)



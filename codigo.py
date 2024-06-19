import glob;

""" Contador de PHE """
numero_PHE = 0

""" Adicione o caminho dos arquivos """
lista = glob.glob("Aqui adicione o caminho\\*.pdb");

""" Adicionar a resposta no arquivo que você preferir """
arq_resposta = open("Aqui adicione o caminho\\resposta.txt", "w")

for i in lista:
    arq = open(i, "r")
    for j in arq:
        if j[0:4] == "ATOM" and j[13:20] == "CA  PHE" and j[21] == "A":
            numero_PHE+=1

""" Gera o arquivo resposta """
arq_resposta.write("Quantidade de PHE: " + str(numero_PHE))
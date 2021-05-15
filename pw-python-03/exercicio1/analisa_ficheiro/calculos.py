import sys


def calcula_linhas(ficheiro):
    try:
        f = open(ficheiro, "r")
        line_count = 0
        for line in f:
            if line != "\n":
                line_count += 1
        f.close()
        return line_count
    except OSError:
        print("Nao consegui abrir ler o ficheiro", ficheiro)
        sys.exit()


def calcula_carateres(ficheiro):
    try:
        f = open(ficheiro, "r")
        data = f.read().replace(" ", "")
        nrCharacters = len(f)
        f.close()
        return nrCharacters
    except OSError:
        print("Nao consegui abrir ler o ficheiro", ficheiro)
        sys.exit()


def calcula_palavra_comprida(ficheiro):
    f = open(ficheiro, "r")
    words = f.read().split()
    maxLenWord = max(words, key=len)
    return maxLenWord
    f.close()


def calcula_ocorrencia_de_letras(ficheiro):
    f = open(ficheiro, "r")
    dicionario = {}
    print("ola")


def main():
    print("ola")


if __name__ == "__main__":
    main()





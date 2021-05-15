import sys


def pede_nome():

    exists = False
    while exists:
        ficheiro = input("Insira o nome do ficheiro")
        try:
            f = open(ficheiro, "r")
            print(f"o nome do ficheiro e {ficheiro}")
            exists = True
            return ficheiro
        except OSError:
            print("Nao consegui abrir ler o ficheiro", ficheiro)
            sys.exit()


def gera_nome(ficheiro):

    newName = ficheiro.split()[0]
    newName.append(".json")
    return newName


def main():
    print("ola")


if __name__ == "__main__":
    main()

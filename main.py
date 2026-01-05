from datetime import datetime
from tarefas import (
    criar_lista,
    ver_listas,
    adicionar_tarefa,
    ver_tarefas,
    deletar_tarefa,
    concluir_tarefa,
    deletar_lista
)

def saudacao():
    hora = datetime.now().hour
    if hora < 12:
        print("☀️ Bom dia!")
    elif hora < 18:
        print("🌤️ Boa tarde!")
    else:
        print("🌙 Boa noite!")


def menu():
    print("\===== MENU =====")
    print("1 - Criar nova lista")
    print("2 - Ver listas")
    print("3 - Adicionar tarefa") #Vai ter que mandar para a parte 1 e 2 
    print("4 - Ver tarefas de uma lista")
    print("5 - Marcar tarefa como concluída")
    print("6 - Deletar tarefa")
    print("7 - Deletar lista inteira")
    print("0 - Sair")
    return input("Escolha uma opção: ")


def main():
    saudacao()

    while True:
        opcao = menu()

        if opcao == "1":
            criar_lista()
            adicionar_tarefa()
        elif opcao == "2":
            ver_listas()
        elif opcao == "3":
            adicionar_tarefa()
        elif opcao == "4":
            ver_tarefas()
        elif opcao == "5":
            concluir_tarefa()
        elif opcao == "6":
            deletar_tarefa()
        elif opcao == "7":
            deletar_lista()
        elif opcao == "0":
            print("👋 Até mais!")
            break
        else:
            print("❌ Opção inválida.")


if __name__ == "__main__":
    main()

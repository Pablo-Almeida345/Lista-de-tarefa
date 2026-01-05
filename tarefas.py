from db import conectar

# 📋 Ver todas as listas
def ver_listas():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT id, nome FROM listas")
    listas = cursor.fetchall()

    if not listas:
        print("❌ Nenhuma lista encontrada.")
    else:
        print("\n📋 Listas disponíveis:")
        for lista in listas:
            print(f"ID: {lista[0]} | Nome: {lista[1]}")

    cursor.close()
    conexao.close()


# Criação da lista 
def criar_lista():
    nome = input("Nome da nova lista: ")

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "INSERT INTO listas (nome) VALUES (%s)",
        (nome,)
    )

    conexao.commit()
    cursor.close()
    conexao.close()

    print("✅ Lista criada com sucesso!")


# ➕ Adicionar tarefa
def adicionar_tarefa():
    ver_listas()
    lista_id = input("\nDigite o ID da lista: ")
    descricao = input("Descrição da tarefa: ")

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "INSERT INTO tarefas (descricao, lista_id) VALUES (%s, %s)",
        (descricao, lista_id)
    )

    conexao.commit()
    cursor.close()
    conexao.close()

    print("✅ Tarefa adicionada com sucesso!")


# 📋 Ver tarefas
def ver_tarefas():
    ver_listas()
    lista_id = input("\nDigite o ID da lista: ")

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "SELECT id, descricao, concluida FROM tarefas WHERE lista_id = %s",
        (lista_id,)
    )

    tarefas = cursor.fetchall()

    if not tarefas:
        print("❌ Nenhuma tarefa encontrada.")
    else:
        print("\n📝 Tarefas:")
        for tarefa in tarefas:
            status = "✔️" if tarefa[2] else "❌"
            print(f"ID: {tarefa[0]} | {status} {tarefa[1]}")

    cursor.close()
    conexao.close()


# ✔️ Concluir tarefa
def concluir_tarefa():
    ver_tarefas()
    tarefa_id = input("\nDigite o ID da tarefa: ")

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "UPDATE tarefas SET concluida = TRUE WHERE id = %s",
        (tarefa_id,)
    )

    conexao.commit()
    cursor.close()
    conexao.close()

    print("✅ Tarefa concluída!")


# 🗑️ Deletar tarefa
def deletar_tarefa():
    ver_tarefas()
    tarefa_id = input("\nDigite o ID da tarefa: ")

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "DELETE FROM tarefas WHERE id = %s",
        (tarefa_id,)
    )

    conexao.commit()
    cursor.close()
    conexao.close()

    print("🗑️ Tarefa deletada!")


# 🗑️ Deletar lista inteira
def deletar_lista():
    ver_listas()
    lista_id = input("\nDigite o ID da lista: ")

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "DELETE FROM listas WHERE id = %s",
        (lista_id,)
    )

    conexao.commit()
    cursor.close()
    conexao.close()

    print("🗑️ Lista deletada!")

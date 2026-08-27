import os
import sqlite3

CAMINHO_BANCO = "jogos.db"

def exibir_cabecalho(texto):
    os.system('cls')

    linha = "*" * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()

exibir_cabecalho("GameVault")

def inicializar_banco():
    # Abre a conexão com o banco de dados (O indicado em: "CAMINHO_BANCO" no caso: "jogos.db")
    conn = sqlite3.connect(CAMINHO_BANCO)

    # Diz ao BD que de fato SQL está habilitado
    cursor = conn.cursor()

    #Executa de fato o comando SQL
    cursor. execute(
        """

        CREATE TABLE IF NOT EXISTS jogos (
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             titulo TEXT NOT NULL,
             plataforma TEXT NOT NULL,
             zerado BOOLEAN NOT NULL DEFAULT 0  
        )
        """
    )

    #Funciona como salva, onde ele grava
    conn.commit()
    # fecha a conexãp
    conn.close()

#Chamando a funnçao
inicializar_banco()

# Busca todos os jogos cadastrados e imprime formatado.
def listar_jogos():
    conn = sqlite3.connect(CAMINHO_BANCO)
    cursor = conn.cursor()

    # SELECT trazendo só as colunas que interessam pra exibição
    # (não precisamos do "id" aqui, por exemplo).
    cursor.execute("SELECT titulo, plataforma, zerado FROM jogos")

    # 6. fetchall() devolve TODAS as linhas do resultado, como uma lista de tuplas
    jogos = cursor.fetchall()

    conn.close()

    # Caso especial: banco vazio. Sem esse "if", o cabeçalho da tabela
    # apareceria sozinho, sem nenhuma linha embaixo — confuso pro usuário.
    if not jogos:
        print("Nenhum jogo cadastrado ainda.\n")
        return

    print(f"{'Título'.ljust(25)} | {'Plataforma'.ljust(12)} | Status")
    print("-" * 55)


    for titulo, plataforma, zerado in jogos:
        status = "zerado" if zerado else "jogando"
        print(f"{titulo.ljust(25)} | {plataforma.ljust(12)} | {status}")

    print()  # linha em branco no final, pra não colar com o próximo print


# chamada de teste — remova ou comente depois de confirmar que funciona
listar_jogos()

def adicionar_jogo(titulo, plataforma):
    conn = sqlite3.connect(CAMINHO_BANCO)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO jogos(titulo, plataforma, zerado) VALUES(?, ?, ?)", (titulo, plataforma, False),
    )

    conn.commit()
    conn.close()

def marcar_como_zerado(titulo):
    conn = sqlite3.connect(CAMINHO_BANCO)
    cursor = conn.cursor()
    cursor.execute("UPDATE jogos SET zerado = ? WHERE titulo = ?", (True, titulo),
        )

    #Guarda quantas linhas foram afetadas na atualizçao
    encontrou = cursor.rowcount > 0

    conn.commit()
    conn.close()
    return encontrou 

def exibir_menu():
    exibir_cabecalho("🎮 GameVault")
    print("1.Adicionar Jogo")
    print("2.Lista de Jogos")
    print("3.Marcar Jogo como zerado")
    print("4.Apagar jogo")
    print("5.Sair\n")

def pausar():
    input("Pressione Enter para voltar ao menu...")

def remover_jogo(titulo):
    conn = sqlite3.connect(CAMINHO_BANCO)
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM jogos WHERE titulo = ?",
        (titulo,)
    )

    encontrou = cursor.rowcount > 0

    conn.commit()
    conn.close()

    return encontrou

def main():
    inicializar_banco()

    while True:
        exibir_menu()
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            exibir_cabecalho("Adicionar jogo")
            titulo = input("Título do Jogo: ")
            plataforma = input("Plataforma: ")
            adicionar_jogo(titulo, plataforma)
            print(f"\n'{titulo}' adicionado com sucesso!")
            pausar()

        elif  opcao == 2:
            exibir_cabecalho("seus jogos")
            listar_jogos()
            pausar()
        elif opcao == 3:
            exibir_cabecalho("Marcar como zerado")
            titulo = input("Título do jogo que zerou: ")

            if marcar_como_zerado(titulo):
                print(f"\n'{titulo}' marcado como zerado!")
            else:
                print(f"\n'{titulo}' Não encontrado!")
                print("Confira se digitou correamente.")

            pausar()

        elif opcao == 4:
            exibir_cabecalho("Apagar jogo")
            titulo = input("Título do jogo que deseja apagar: ")

            if remover_jogo(titulo):
                print(f"\n'{titulo}' removido com sucesso!")
            else:
                print(f"\n'{titulo}' não encontrado!")
                print("Confira se digitou corretamente.")

            pausar()

        elif opcao == 5:
            print("Até a próxima👋! ")
            break

        else:
            # Caso o usuário digite uma opção inválida.
            print("Opção inválida! Escolha um número de 1 a 5.")
            pausar()

# Fechamento da função main
if __name__ == "__main__":
    main()
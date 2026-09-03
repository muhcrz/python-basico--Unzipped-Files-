# Exemplo de Interface — versão orientada a objetos
# Janela simples: digita um texto, clica no botão, o texto aparece no rótulo.

import tkinter as tk

# Classe principal
class InterfaceExemplo:
    # Método construtor (Para criar janela "Tela" principal)
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Exemplo de Interface")
        self.janela.geometry("400x150")
        # Cor de fundo da janela (opcional)
        #self.janela.configure(bg="lightgray")
        self.criar_widgets()

    # Montar todos os elementos visuais da tela
    def criar_widgets(self): 
        # Caixa de entrada "Entry" ou input onde o usuário digita o texto
        self.caixa_texto = tk.Entry(self.janela, width=60)
        self.caixa_texto.pack(pady=10)

        # Botão que dispara  mostrar_mensagem ao ser clicado
        self.botao = tk.Button(self.janela, text="Mostrar texto", command=self.mostrar_mensagem)
        self.botao.pack(pady=10)

        # Rótulo "Label" que mostra a mensagem se o usuário clicar no botão
        self.label_rotulo = tk.Label(self.janela, text="", fg="blue", font=("Arial", 14))
        self.label_rotulo.pack(pady=10)
        #self.label_rotulo.pack(pady=10, padx=10, anchor="w")

    # Captura o texto digitado pelo usuário (no Entry ou "Input") e transfere ele para variável texto para ser exibido em "label_resultado"
    def mostrar_mensagem(self):
        # Pega o texto digitado na caixa de entrada
        texto = self.caixa_texto.get()
        # Atualiza o rótulo com o texto digitado
        self.label_rotulo.config(text=texto)

    # Inicia o loop principal da Tela (Isso mantem a tela sendo exibida)
    def executar(self):
        self.janela.mainloop()

# Conecta a classe principal "InterfaceExemplo" e roda o método "executar" para fazer o programa funcionar
if __name__ == "__main__":
    app = InterfaceExemplo()
    app.executar()
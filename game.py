#importação das biblootecas

import tkinter as tk # Serve para interface grafica 
import random # Randomico
#------------------------------------------------------------------------------------------------------------------------
# Configurações de inicio
#Tamanho da tela e valocidade

largura = 700
altura = 700
tamanho_quadrado = 20
velocidade_inicial = 100
jogo_em_andamento = True
#------------------------------------------------------------------------------------------------------------------------

# Direções possíveis
direcoes = {
    "w": [0, -tamanho_quadrado],
    "s": [0, tamanho_quadrado],
    "a": [-tamanho_quadrado, 0],
    "d": [tamanho_quadrado, 0]
}
#------------------------------------------------------------------------------------------------------------------------

# Funções do jogo
def mover_cobra():
    global posicoes_cobra, direcao, ponto, velocidade_inicial, ponto_objeto, jogo_em_andamento

    # Move a cabeça da cobra
    nova_cabeca = [posicoes_cobra[0][0] + direcao[0], posicoes_cobra[0][1] + direcao[1]]
    
    # Vai verifica se a cobra colidiu com ela mesma ou com as bordas
    if (nova_cabeca in posicoes_cobra or
        nova_cabeca[0] < 0 or nova_cabeca[0] >= largura or
        nova_cabeca[1] < 0 or nova_cabeca[1] >= altura):
        fim_de_jogo()
        return
#------------------------------------------------------------------------------------------------------------------------

    # Adiciona mais um quadrado para o corpo (se comer o ponto)
    posicoes_cobra.insert(0, nova_cabeca)
    if nova_cabeca == ponto:
        canvas.delete(ponto_objeto)  # Remove o ponto já comido
        ponto = gerar_ponto()
        ponto_objeto = canvas.createcre_croval(ponto[0], ponto[1], ponto[0] + tamanho_quadrado, ponto[1] + tamanho_quadrado, fill="#FF6347", outline="#FFA07A", width=2)
        velocidade_inicial = max(20, velocidade_inicial - 5)  # Aqui é para limitar a velocidade mínima
    else:
        posicoes_cobra.pop()
#------------------------------------------------------------------------------------------------------------------------

    # Atualiza a cobra
    canvas.delete("cobra")
    for i, pos in enumerate(posicoes_cobra):
        cor = "#31CC66" if i == 0 else "#27A227"
        canvas.create_rectangle(pos[0], pos[1], pos[0] + tamanho_quadrado, pos[1] + tamanho_quadrado, fill=cor, outline="#2E8B57", tags="cobra")
#------------------------------------------------------------------------------------------------------------------------   

    # Continua o movimento da cobra
    if jogo_em_andamento:
        root.after(velocidade_inicial, mover_cobra)
#------------------------------------------------------------------------------------------------------------------------

def mudar_direcao(nova_direcao):
    global direcao

    # impede que a cobra mude para a direção oposta que ela estava indo
    if (direcao[0] + nova_direcao[0] != 0) or (direcao[1] + nova_direcao[1] != 0):
        direcao = nova_direcao
#------------------------------------------------------------------------------------------------------------------------

def gerar_ponto():
    while True:
        x = random.randint(0, (largura // tamanho_quadrado) - 1) * tamanho_quadrado
        y = random.randint(0, (altura // tamanho_quadrado) - 1) * tamanho_quadrado
        if [x, y] not in posicoes_cobra:
            return [x, y]
#------------------------------------------------------------------------------------------------------------------------

def fim_de_jogo():
    global jogo_em_andamento
    canvas.create_text(largura / 2, altura / 2, text="Fim de jogo!", fill="red", font=("Arial", 24, "bold"), tags="fim_de_jogo")
    jogo_em_andamento = False
    root.bind("<space>", reiniciar_jogo)
#------------------------------------------------------------------------------------------------------------------------

def reiniciar_jogo(event=None):
    global posicoes_cobra, direcao, ponto, velocidade_inicial, ponto_objeto, jogo_em_andamento
    
    # Limpa a tela
    canvas.delete("all")
#------------------------------------------------------------------------------------------------------------------------
#    
    # Redefine as variáveis
    direcao = [0, -tamanho_quadrado]
    posicoes_cobra = [[200, 200], [200, 220], [200, 240]]
    velocidade_inicial = 100  # Reinicia a velocidade de inicio
    jogo_em_andamento = True
#------------------------------------------------------------------------------------------------------------------------     
    # Desenha a cobra novamente
    for pos in posicoes_cobra:
        canvas.create_rectangle(pos[0], pos[1], pos[0] + tamanho_quadrado, pos[1] + tamanho_quadrado, fill="#32CD32", outline="#2E8B57", tags="cobra")
#------------------------------------------------------------------------------------------------------------------------
    
    # Desenha o ponto novamente
    ponto = gerar_ponto()
    ponto_objeto = canvas.create_oval(ponto[0], ponto[1], ponto[0] + tamanho_quadrado, ponto[1] + tamanho_quadrado, fill="#FF6347", outline="#FFA07A", width=2)
#------------------------------------------------------------------------------------------------------------------------    
    # Aqui é definido as teclas de direção
    root.bind("<w>", lambda event: mudar_direcao(direcoes["w"]))
    root.bind("<s>", lambda event: mudar_direcao(direcoes["s"]))
    root.bind("<a>", lambda event: mudar_direcao(direcoes["a"]))
    root.bind("<d>", lambda event: mudar_direcao(direcoes["d"]))
#------------------------------------------------------------------------------------------------------------------------
    # Aqui é definido o reinicio do jogo (caso tenha perdido)
    root.unbind("<space>")
#------------------------------------------------------------------------------------------------------------------------   
    # Inicia o movimento da cobra
    mover_cobra()
#------------------------------------------------------------------------------------------------------------------------

# Configuração da interface gráfica
root = tk.Tk()
root.title("Jogo da Cobrinha")

canvas = tk.Canvas(root, width=largura, height=altura, bg="#000000", highlightthickness=0)
canvas.pack()
#------------------------------------------------------------------------------------------------------------------------

# Inicia o jogo pela primeira vez
reiniciar_jogo()
#------------------------------------------------------------------------------------------------------------------------

# Loop até fechar 'o jogo'... perdi
root.mainloop()
#------------------------------------------------------------------------------------------------------------------------
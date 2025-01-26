import random

def gerar_cartela_rapida():
    cartela = []
    coluna1 = random.sample(range(1, 11), 2)
    coluna2 = random.sample(range(11, 21), 2)
    coluna3 = random.sample(range(21, 31), 2)
    cartela.append(coluna1)
    cartela.append(coluna2)
    cartela.append(coluna3)
    return cartela

def gerar_cartela_demorado():
    cartela = []
    coluna1 = random.sample(range(1, 11), 4)
    coluna2 = random.sample(range(11, 21), 4)
    coluna3 = random.sample(range(21, 31), 4)
    coluna4 = random.sample(range(31, 41), 4)
    cartela.append(coluna1)
    cartela.append(coluna2)
    cartela.append(coluna3)
    cartela.append(coluna4)
    return cartela

def imprimir_cartelas(cartelas, sorteadas):
    for jogador, cartela in cartelas.items():
        print(f"\nCartela do jogador {jogador}:")
        for linha in cartela:
            linha_impressa = []
            for numero in linha:
                if numero in sorteadas:
                    linha_impressa.append(f"[{numero}]")  
                else:
                    linha_impressa.append(f" {numero} ")  
            print(" ".join(linha_impressa))


def jogar_bingo():
    print("Bem-vindo ao Bingo!")
    modo = input("Escolha o modo (rapido/demorado): ").strip().lower()
    
  
    if modo == "rapido":
        num_cartelas = 2
        gerar_cartela = gerar_cartela_rapida
        intervalo = [1, 30] 
    elif modo == "demorado":
        num_cartelas = 4
        gerar_cartela = gerar_cartela_demorado
        intervalo = [1, 40]  
    else:
        print("Modo inválido.")
        return
    
    
    cartelas = {}
    for i in range(1, num_cartelas + 1):
        jogador = input(f"Digite o nome do jogador {i}: ").strip()
        cartelas[jogador] = gerar_cartela()
    
   
    sorteadas = []
    while True:
        
        numero_sorteado = random.randint(intervalo[0], intervalo[1])
        while numero_sorteado in sorteadas:
            numero_sorteado = random.randint(intervalo[0], intervalo[1])
        
        sorteadas.append(numero_sorteado)
        sorteadas.sort()
        
        
        print(f"\nÚltima dezena sorteada: {numero_sorteado}")
        print(f"Dezenas sorteadas até agora: {', '.join(map(str, sorteadas))}")
        
       
        imprimir_cartelas(cartelas, sorteadas)
        
       
        ganhadores = []
        for jogador, cartela in cartelas.items():
            if all(any(numero in sorteadas for numero in linha) for linha in cartela):
                ganhadores.append(jogador)
        
        if ganhadores:
            print(f"\nGanhadores: {', '.join(ganhadores)}")
            break
        
        continuar = input("\nDeseja continuar o sorteio? (sim - não): ").strip().lower()
        if continuar != 'sim':
            print("Jogo encerrado.")
            break


jogar_bingo()
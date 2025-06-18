with open("lista-das-proteinas-identificadas.txt", "r") as arquivo:
    primeiro_filtro = [linha.strip() for linha in arquivo if linha.startswith('>')] # Deixando apenas conteúdo como ">A0A7K5Y528"
    print("\n".join(primeiro_filtro))

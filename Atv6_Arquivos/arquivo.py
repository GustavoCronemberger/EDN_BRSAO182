nome_arquivo = "minhas_notas.txt"

with open(nome_arquivo, 'w', encoding='utf-8') as f:
    f.write("Esta é a primeira frase inicial.\n")
    f.write("Esta é a segunda frase inicial.\n")
    f.write("Esta é a terceira frase inicial.\n")

print(f"As 3 frases iniciais foram gravadas em '{nome_arquivo}'.")

with open(nome_arquivo, 'a', encoding='utf-8') as f:
    f.write("Esta é a quarta frase adicionada.\n")
    f.write("Esta é a quinta frase adicionada.\n")

print(f"Mais 2 frases foram adicionadas a '{nome_arquivo}'.")

print(f"\nConteúdo completo de '{nome_arquivo}':")
with open(nome_arquivo, 'r', encoding='utf-8') as f:
    conteudo = f.read()
    print(conteudo)
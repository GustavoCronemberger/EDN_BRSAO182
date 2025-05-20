#Código inicial refatorado, antes de substituir o while por list comprehension

# def obter_nota():
#     entrada = input("Digite uma nota (ou 'fim' para encerrar): ")
    
#     if entrada.lower() == "fim":
#         return None
    
#     try:
#         nota = float(entrada)
#     except ValueError:
#         print("Entrada inválida. Digite um número.")
#         return obter_nota()
    
#     if nota < 0 or nota > 10:
#         print("Nota inválida. Insira um valor entre 0 e 10.")
#         return obter_nota()
    
#     return nota

# def coletar_notas():
#     notas = []
#     while (nota := obter_nota()) is not None:
#         notas.append(nota)
#     return notas

# def calcular_media(notas):
#     if not notas:
#         print("Nenhuma nota válida foi inserida.")
#         return
    
#     media = sum(notas) / len(notas)
#     print(f"Média da turma: {media:.2f}")

# notas = coletar_notas()
# calcular_media(notas)

#Aplicação do list comprehension, resultado: código ainda mais enxuto e de fácil entendimento.

def obter_nota():
    entrada = input("Digite uma nota (ou 'fim' para encerrar): ")
    if entrada.lower() == "fim":
        return None
    try:
        nota = float(entrada)
        return nota if 0 <= nota <= 10 else print("Nota inválida. Insira um valor entre 0 e 10.") or obter_nota()
    except ValueError:
        print("Entrada inválida. Digite um número.")
        return obter_nota()

notas = list(iter(lambda: obter_nota(), None))
print(f"Média da turma: {sum(notas) / len(notas):.2f}" if notas else "Nenhuma nota válida foi inserida.")
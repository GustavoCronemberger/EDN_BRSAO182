import matematica

from meu_pacote.mensagens import boas_vindas
from meu_pacote.operacoes import multiplica

def executar_demonstracao():
    nome_usuario = "Gustavo"
    print(boas_vindas(nome_usuario))


    print(f"Soma de 5 + 2: {matematica.soma(5, 2)}")
    print(f"Subtração de 10 - 4: {matematica.subtrai(10, 4)}")
    print(f"Módulo de 5: {matematica.modulo(5, 2)}")
    print(f"Multiplicação de 3 * 7: {multiplica(3, 7)}")
    print("**********************************")

if __name__ == "__main__":
    executar_demonstracao()
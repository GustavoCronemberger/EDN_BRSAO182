def senha_forte(senha: str) -> bool:
    return len(senha) >= 8 and any(char.isdigit() for char in senha)

while (senha := input("Digite uma senha (ou 'sair' para encerrar): ").strip().lower()) != "sair":
    if senha_forte(senha):
        print("Cadastro concluído.")
        break
    print("Senha fraca! Mínimo: 8 dígitos com 1 numeral!")

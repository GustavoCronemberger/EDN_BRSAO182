def senha_forte(senha: str) -> bool:
    return len(senha) >= 8 and any(char.isdigit() for char in senha)

def obter_senha() -> str:
    while True:
        senha = input("Digite uma senha (ou 'sair' para encerrar): ").strip()
        if senha.lower() == "sair":
            print("Programa encerrado.")
            return None
        elif senha_forte(senha):
            print("Cadastro concluído.")
            return senha
        else:
            print("Senha fraca. Mínimo: 8 dígitos com 1 numeral!")

senha_usuario = obter_senha()

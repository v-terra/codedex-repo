def main():
    code = input("entre com o código do ingresso: ")
    clean_code = code.strip().upper()
    if clean_code.endswith("-VIP") and clean_code.startswith("2026-"):
        print("Acesso liberado: Área VIP") 
    elif clean_code.endswith("-STD") and clean_code.startswith("2026-"):
        print("Acesso liberado: Pista")
    elif not (clean_code.startswith("2026-")):
        print("Ingresso expirado")
    else:
        print("Ingresso inválido")

main() 
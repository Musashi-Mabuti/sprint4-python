import qrcode
import csv
import random

def avaliar_prioridade(febre, dor_intensa, dificuldade_respirar):
    if dificuldade_respirar == "sim":
        return "Emergência"
    elif dor_intensa == "sim" or febre == "sim":
        return "Urgência"
    else:
        return "Normal"

def salvar_dados_csv(paciente):
    with open("pre_triagem.csv", mode="a", newline="") as file:
        escritor = csv.writer(file)
        escritor.writerow([paciente["id"], paciente["nome"], paciente["idade"], paciente["prioridade"]])

def gerar_qr_code(paciente):
    dados_qr = f"ID: {paciente['id']}\nNome: {paciente['nome']}\nPrioridade: {paciente['prioridade']}"
    qr = qrcode.make(dados_qr)
    qr.save(f"qr_{paciente['id']}.png")
    print(f"\nQR Code gerado com sucesso: qr_{paciente['id']}.png")

def pre_triagem():
    print("\n--- Sistema de Pré-Triagem Remota - Hospital Sabará ---")
    nome = input("Nome completo: ")
    idade = input("Idade: ")

    febre = input("Está com febre? (sim/nao): ").lower()
    dor_intensa = input("Sente dor intensa? (sim/nao): ").lower()
    dificuldade_respirar = input("Tem dificuldade para respirar? (sim/nao): ").lower()

    prioridade = avaliar_prioridade(febre, dor_intensa, dificuldade_respirar)

    # Gerar ID fictício
    id_paciente = random.randint(100000, 999999)

    paciente = {
        "id": id_paciente,
        "nome": nome,
        "idade": idade,
        "prioridade": prioridade
    }

    salvar_dados_csv(paciente)
    gerar_qr_code(paciente)

    print(f"\nPaciente {nome} classificado como: {prioridade}")
    print(f"Leve o QR Code gerado no celular ou impresso para facilitar sua triagem no hospital.")

# Executa a pré-triagem
pre_triagem()

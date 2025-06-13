# 🏥 Pré-Triagem Hospitalar Automatizada - Hospital Sabará

Este projeto tem como objetivo auxiliar hospitais, como o Hospital Sabará, no processo de **pré-triagem de pacientes**, permitindo que eles forneçam informações básicas sobre seus sintomas **antes de chegar ao atendimento presencial**, com geração de um **QR Code contendo os dados essenciais para a recepção médica**.

---

## 📌 Funcionalidades

✅ Coleta de informações do paciente (nome, idade e sintomas)  
✅ Classificação automática da prioridade médica: **Emergência, Urgência ou Normal**  
✅ Geração de **ID único aleatório** para cada paciente  
✅ Armazenamento dos dados em um arquivo `.csv`  
✅ Geração automática de um **QR Code com os dados do paciente**  
✅ Interface em linha de comando simples e funcional

---

## 🚀 Como Executar o Projeto

1. **Clone o repositório**
   ```bash
   git clone https://github.com/seu-usuario/pre-triagem-hospitalar.git
   cd pre-triagem-hospitalar
2. **Instale as dependências**
   ```bash
   pip install qrcode[pil]
3. **Execute o sistema de pré-triagem**
   ```bash
   python pre_triagem.py
4. ***Siga as instruções no terminal***
   ```bash
   O script solicitará dados como nome, idade e sintomas. Após isso, um QR Code será gerado e salvo automaticamente.




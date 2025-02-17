# **Cadastro de Usuários** 📝  

Este projeto é um sistema simples de cadastro de usuários desenvolvido com **HTML, CSS, JavaScript e Python (Flask)**. Ele permite que os usuários preencham um formulário com seus dados pessoais e enviem essas informações para um servidor que armazena os dados em um banco de dados SQL.  

## 🚀 **Tecnologias Utilizadas**  
- **Frontend**: HTML, CSS e JavaScript  
- **Backend**: Python (Flask)  
- **Banco de Dados**: SQL (SQLite/MySQL/PostgreSQL)  
- **Protocolo de Comunicação**: REST API  

## ⚙️ **Funcionalidades**  
✔️ Formulário de cadastro com campos como nome, e-mail, telefone, CPF, endereço, etc.  
✔️ Envio dos dados para um servidor Flask via **fetch API**.  
✔️ Armazenamento dos dados no banco de dados SQL.  
✔️ Validação de campos obrigatórios no frontend.  

## 📌 **Como Executar o Projeto**  

### **1️⃣ Clonar o repositório**
```sh
git clone https://github.com/SEU_USUARIO/cadastro-usuarios.git
cd cadastro-usuarios
```

### **2️⃣ Criar e ativar um ambiente virtual**
```sh
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate      # Windows
```

### **3️⃣ Instalar as dependências**
```sh
pip install -r requirements.txt
```

### **4️⃣ Rodar o servidor Flask**
```sh
python app.py
```
O servidor estará disponível em **http://127.0.0.1:5000/**.

## 🏗 **Melhorias Futuras**
- Adicionar validação de CPF e telefone.  
- Criar um painel para visualizar os usuários cadastrados.  
- Implementar autenticação de usuários.

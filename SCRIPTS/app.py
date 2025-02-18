from flask import Flask, request, jsonify, render_template
import pyodbc

app = Flask(__name__)

# Configuração do banco de dados SQL Server
server = "######\\SQLEXPRESS"
database = "TESTESSQL"
conn_str = f"DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;"

# Rota para exibir o formulário HTML
@app.route("/")
def index():
    return render_template("index.html")

# Rota para processar o cadastro do usuário
@app.route("/cadastro", methods=["POST"])
def cadastrar_usuario():
    try:
        nome = request.form.get("nome")
        email = request.form.get("email")
        telefone = request.form.get("telefone")
        data_nascimento = request.form.get("data_nascimento")
        cpf = request.form.get("cpf")
        endereco = request.form.get("endereco")
        cidade = request.form.get("cidade")
        estado = request.form.get("estado")
        pais = request.form.get("pais", "Brasil")  # Padrão Brasil

        if not nome or not email:
            return jsonify({"error": "Nome e Email são obrigatórios!"}), 400

        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO usuarios (nome, email, telefone, data_nascimento, cpf, endereco, cidade, estado, pais)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (nome, email, telefone, data_nascimento, cpf, endereco, cidade, estado, pais))

        conn.commit()
        cursor.close()
        conn.close()

        return jsonify({"message": "Usuário cadastrado com sucesso!"})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)

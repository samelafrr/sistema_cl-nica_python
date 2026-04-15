#GRUPO: Sâmela Feitosa Ferreira
#Conexão com o banco de dados:
import mysql.connector
from datetime import datetime #usado para converter a data e a hora para o formato adequado

def connectar():
    try:
        cnn = mysql.connector.connect(
            host = "127.0.0.1",
            user = "root",
            password = "samelasql",
            port = "3306",
            database = "db_sys_clinic"
        )
        print("Bem vindo ao sistema SysClinic!")
        return cnn
    except Exception as ex:
        print(ex)

#Conexão feita!

#Menu principal:
def menu_principal(conexao):
    while True:
        print("""--- SysClinic ---
[1] Clientes
[2] Agendamentos
[3] Médicos
[0] Sair
""")
        opcao_principal = int(input("Escolha uma opção: "))
        if opcao_principal == 1:
            clientes(conexao)
        elif opcao_principal == 2:
            agendamentos(conexao)
        elif opcao_principal == 3:
            medicos(conexao)
        elif opcao_principal == 0:
            break

#Menu dos clientes:
def menu_clientes():
     print("""--- Selecione uma opção: ---
[1] Cadastro de novo cliente
[2] Listar clientes
[3] Exclusão de cliente
[4] Alteração de cliente
[5] Menu principal
""")

#Menu dos médicos:
def menu_medicos():
    print("""--- Selecione uma opção: ---
[1] Cadastro de novo médico
[2] Listar médicos
[3] Exclusão de médico
[4] Alteração de médico
[5] Menu principal
""")

#Menu de agendamento:
def menu_agendamentos():
    print("""--- Selecione uma opção: ---
[1] Cadastro de novo agendamento
[2] Listar agendamentos
[3] Exclusão de agendamento
[4] Alteração de agendamento
[5] Menu principal
""")

#Função de listar os clientes no banco:
def listar_clientes(conexao):
    try:
        cursor = conexao.cursor()
        sql = "SELECT * from tb_clientes"
        cursor.execute(sql)
        resultados = cursor.fetchall()
        print("\n--- LISTA DE CLIENTES ---")
        for cliente in resultados:
            print(f"""
ID: {cliente[0]}
Nome: {cliente[1]}
Telefone: {cliente[2]}
Email: {cliente[3]}
Status: {"Inativo" if cliente[4] == 1 else "Ativo"}
-----------------------------""")
        cursor.close()
    except Exception as ex:
        conexao.rollback()
        print(ex)

#Função para alterar algum dado dos clientes:
def alterar_clientes(conexao):
    listar_clientes(conexao)
    id_cliente = int(input("Qual o ID do cliente que você deseja alterar? "))
    nome_cliente = input("Nome: ")
    while True: #validação de email e telefone
        telefone = input("Telefone: ")
        if telefone.isdigit() and len(telefone) >= 10:
            break
        else:
            print("Telefone inválido! Digite apenas números com DDD, sem espaços.")
    while True:
        email = input("Email: ")
        if "@" in email and "." in email:
            break
        else:
            print("Email inválido! Tente novamente.")
    inativo = int(input("0 ativo / 1 inativo: "))
    try:
        cursor = conexao.cursor()
        sql = (
            "UPDATE tb_clientes SET nome_cliente = %s, telefone = %s, "
            "email = %s, inativo = %s WHERE id_cliente = %s"
        )
        valores = (nome_cliente, telefone, email, inativo, id_cliente)
        cursor.execute(sql, valores)
        conexao.commit()
        print("Cliente atualizado com sucesso!")
        cursor.close()
    except Exception as ex:
        conexao.rollback()
        print(ex)

#Função para excluir algum cliente do banco:
def exclusao_clientes(conexao):
    listar_clientes(conexao)
    id_cliente = int(input("Qual o ID do cliente que você deseja excluir? "))
    try:
        cursor = conexao.cursor()
        sql = "DELETE FROM tb_clientes WHERE id_cliente = %s"
        valores = (id_cliente,)
        cursor.execute(sql, valores)
        conexao.commit()
        print("Excluído com sucesso!")
        cursor.close()
    except Exception as ex:
        conexao.rollback()
        print(ex)

#Função de cadastro clientes e elif`s para as outras funções:
def clientes(conexao):
    while True:
        menu_clientes()
        opcao_clientes = int(input("Escolha uma opção: "))
        if opcao_clientes == 1:
            nome_cliente = input("Nome: ")
            while True: #validação de email e telefone
                telefone = input("Telefone: ")
                if telefone.isdigit() and len(telefone) >= 10:
                    break
                else:
                    print("Telefone inválido! Digite apenas números com DDD, sem espaços.")
            while True:
                email = input("Email: ")
                if "@" in email and "." in email:
                    break
                else:
                    print("Email inválido! Tente novamente.")
            inativo = int(input("0 ativo / 1 inativo: "))
            try:
                cursor = conexao.cursor()
                sql = "INSERT INTO tb_clientes (nome_cliente, telefone, email, inativo) VALUES (%s, %s, %s, %s)"
                valores = (nome_cliente, telefone, email, inativo)
                cursor.execute(sql, valores)
                conexao.commit()
                cursor.close()
                print("Cliente cadastrado!")
            except Exception as ex:
                conexao.rollback()
                print(ex)
        elif opcao_clientes == 2:
            listar_clientes(conexao)
        elif opcao_clientes == 3:
            exclusao_clientes(conexao)
        elif opcao_clientes == 4:
            alterar_clientes(conexao)
        elif opcao_clientes == 5:
            menu_principal(conexao)


#Função do menu médicos para listar os médicos salvos no banco:
def listar_medicos(conexao):
    try:
        cursor = conexao.cursor()
        sql = "SELECT * from tb_medicos"
        cursor.execute(sql)
        resultados = cursor.fetchall()
        print("\n--- LISTA DE MÉDICOS ---")
        for medico in resultados:
            print(f"""
ID: {medico[0]}
Nome: {medico[1]}
Telefone: {medico[2]}
CRM: {medico[3]}
Especialidade: {medico[4]}
-----------------------------""")
        cursor.close()
    except Exception as ex:
        conexao.rollback()
        print(ex)

#Função que permite alterar os dados dos médicos:
def alterar_medicos(conexao):
    listar_medicos(conexao)
    id_medico = int(input("Qual o ID do médico que você deseja alterar? "))
    nome_medico = input("Nome: ")
    while True: #validação de telefone
        telefone = input("Telefone: ")
        if telefone.isdigit() and len(telefone) >= 10:
            break
        else:
            print("Telefone inválido! Digite apenas números com DDD, sem espaços.")
    crm = input("CRM: ")
    especialidade = input("Especialidade: ")
    try:
        cursor = conexao.cursor()
        sql = (
            "UPDATE tb_medicos SET nome_medico = %s, telefone = %s, "
            "crm = %s, especialidade = %s WHERE id_medico = %s"
        )
        valores = (nome_medico, telefone, crm, especialidade, id_medico)
        cursor.execute(sql, valores)
        conexao.commit()
        print("Médico atualizado com sucesso!")
        cursor.close()
    except Exception as ex:
        conexao.rollback()
        print(ex)

#Função que permite excluir médicos do banco:
def exclusao_medicos(conexao):
    listar_medicos(conexao)
    id_medico = int(input("Qual o ID do médico que você deseja excluir? "))
    try:
        cursor = conexao.cursor()
        sql = "DELETE FROM tb_medicos WHERE id_medico = %s"
        valores = (id_medico,)
        cursor.execute(sql, valores)
        conexao.commit()
        print("Excluído com sucesso!")
        cursor.close()
    except Exception as ex:
        conexao.rollback()
        print(ex)

#Função cadastrar médicos e elif`s do menu médicos
def medicos(conexao):
    while True:
        menu_medicos()
        opcao_medicos = int(input("Escolha uma opção: "))
        if opcao_medicos == 1:
            nome_medico = input("Nome: ")
            while True: #validação de telefone
                telefone = input("Telefone: ")
                if telefone.isdigit() and len(telefone) >= 10:
                    break
                else:
                    print("Telefone inválido! Digite apenas números com DDD, sem espaços.")
            crm = input("CRM: ")
            especialidade = input("Especialidade: ")
            try:
                cursor = conexao.cursor()
                sql = "INSERT INTO tb_medicos (nome_medico, telefone, crm, especialidade) VALUES (%s, %s, %s, %s)"
                valores = (nome_medico, telefone, crm, especialidade)
                cursor.execute(sql, valores)
                conexao.commit()
                cursor.close()
                print("Médico cadastrado!")
            except Exception as ex:
                conexao.rollback()
                print(ex)
        elif opcao_medicos == 2:
            listar_medicos(conexao)
        elif opcao_medicos == 3:
            exclusao_medicos(conexao)
        elif opcao_medicos == 4:
            alterar_medicos(conexao)
        elif opcao_medicos == 5:
            menu_principal(conexao)


#Função de listar os agendamentos salvos no banco:
def listar_agendamento(conexao):
    try:
        cursor = conexao.cursor()
        sql = """
        SELECT 
            a.id_agendamento,
            c.nome_cliente,
            m.nome_medico,
            a.data_agendamento,
            a.hora_agendamento,
            a.observacao,
            a.status_agendamento
        FROM tb_agendamentos a
        JOIN tb_clientes c ON a.id_cliente = c.id_cliente
        JOIN tb_medicos m ON a.id_medico = m.id_medico
        """
        cursor.execute(sql)
        resultados = cursor.fetchall()
        for agendamento in resultados:
            print(f"""
--- AGENDAMENTO ---
ID DO AGENDAMENTO: {agendamento[0]}
Cliente: {agendamento[1]}
Médico: {agendamento[2]}
Data: {agendamento[3]}
Hora: {agendamento[4]}
Status: {agendamento[6]}
Obs: {agendamento[5]}
-----------------------------
""")
        cursor.close()
    except Exception as ex:
        conexao.rollback()
        print(ex)

#Função de excluir algum agendamento:
def exclusao_agendamento(conexao):
    listar_agendamento(conexao)
    id_agendamento = int(input("Qual o ID do agendamento que você deseja excluir? "))
    try:
        cursor = conexao.cursor()
        sql = "DELETE FROM tb_agendamentos WHERE id_agendamento = %s"
        valores = (id_agendamento,)
        cursor.execute(sql, valores)
        conexao.commit()
        print("Excluído com sucesso!")
        cursor.close()
    except Exception as ex:
        conexao.rollback()
        print(ex)

#Função para alterar dados de algum agendamento:
def alterar_agendamento(conexao):
    listar_agendamento(conexao)
    id_agendamento = int(input("Qual o ID do agendamento que você deseja alterar? "))
    listar_clientes(conexao)
    id_cliente = int(input("ID CLIENTE: "))
    listar_medicos(conexao)
    id_medico = input("ID MÉDICO: ")
    try:
        data = input("Digite a data (DD/MM/AAAA): ")
        data_agendamento = datetime.strptime(data, "%d/%m/%Y").strftime("%Y-%m-%d")
        hora = input("Digite a hora (HH:MM): ")
        hora_agendamento = datetime.strptime(hora, "%H:%M").strftime("%H:%M:%S")
    except ValueError:
        print("Formato inválido! Tente novamente.")
    observacao = input("Observação? ")
    status_agendamento = input("Status: ")
    try:
        cursor = conexao.cursor()
        sql = (
            "UPDATE tb_agendamentos SET id_cliente = %s, id_medico = %s, data_agendamento = %s, hora_agendamento = %s, "
            "observacao = %s, status_agendamento = %s WHERE id_agendamento = %s "
        )
        valores = (id_cliente, id_medico, data_agendamento, hora_agendamento, observacao, status_agendamento, id_agendamento)
        cursor.execute(sql, valores)
        conexao.commit()
        print("Agendamento atualizado com sucesso!")
        cursor.close()
    except Exception as ex:
        conexao.rollback()
        print(ex)



#Função cadastrar agendamento e elif`s do menu agendamentos:
def agendamentos(conexao):
    menu_agendamentos()
    opcao_agendamento = int(input("Escolha uma opção: "))
    if opcao_agendamento == 1:
        listar_clientes(conexao)
        id_cliente = int(input("Qual o ID do cliente que deseja agendar? "))
        listar_medicos(conexao)
        id_medico = int(input("Qual o ID do médico que deseja agendar? "))
        try:
            data = input("Digite a data (DD/MM/AAAA): ")
            data_agendamento = datetime.strptime(data, "%d/%m/%Y").strftime("%Y-%m-%d")
            hora = input("Digite a hora (HH:MM): ")
            hora_agendamento = datetime.strptime(hora, "%H:%M").strftime("%H:%M:%S")
        except ValueError:
            print("Formato inválido! Tente novamente.")
        observacao = input("Alguma observação? ")
        try:
            cursor = conexao.cursor()
            sql = (
                "INSERT INTO tb_agendamentos (id_cliente, id_medico, data_agendamento, hora_agendamento, observacao) "
                "VALUES (%s, %s, %s, %s, %s)"
            )
            valores = (id_cliente, id_medico, data_agendamento, hora_agendamento, observacao)
            cursor.execute(sql, valores)
            conexao.commit()
            cursor.close()
            print("Agendamento finalizado!")
        except Exception as ex:
            conexao.rollback()
            print(ex)
    elif opcao_agendamento == 2:
        listar_agendamento(conexao)
    elif opcao_agendamento == 3:
        exclusao_agendamento(conexao)
    elif opcao_agendamento == 4:
        alterar_agendamento(conexao)
    elif opcao_agendamento == 5:
        menu_principal(conexao)
#Conexão com HEIDI:
cnn = connectar()
menu_principal(cnn)
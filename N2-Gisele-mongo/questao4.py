import psycopg2



class Postconexao():
    def get_connection(self):
        Postconexao = psycopg2.connect(user="postgres",password="1234", host="127.0.0.1", port="5432", database="prova")
        return Postconexao
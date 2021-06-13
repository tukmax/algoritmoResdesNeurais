import sqlite3

def run():
    conn = sqlite3.connect('redes-neurais.db')
    cursor = conn.cursor()

    # cursor.execute("""
    # CREATE TABLE neuronios (
    #         id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    #         nome TEXT NOT NULL,
    #         valor INTEGER,
    #         pesos TEXT
    # );
    # """)

    cursor.execute("""
    CREATE TABLE neuronio (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            neuronio TEXT NOT NULL
    );
    """)



    print('Tabela criada com sucesso.')
    conn.close()


if __name__ == '__main__':
    run()

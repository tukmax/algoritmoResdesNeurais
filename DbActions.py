import sqlite3


def insert(item):
    conn = sqlite3.connect('redes-neurais.db')
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO neuronio(neuronio) VALUES (?)""", [item])
    conn.commit()
    print('Dados inseridos com sucesso.')
    conn.close()





def insertAll(list):
    conn = sqlite3.connect('redes-neurais.db')
    cursor = conn.cursor()
    cursor.executemany("""INSERT INTO neuronio(neuronio) VALUES (?)""", list)
    conn.commit()
    print('Dados inseridos com sucesso.')
    conn.close()




def run():
    listokInsertall = [[("item1")], [("item2")]]
    list = [("test",),("teste1",)]

    print(type(list))
    # insert(list)
    insertAll(list)


if __name__ == '__main__':
    run()

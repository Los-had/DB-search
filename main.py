from sqlite3 import Error
import sqlite3
from time import sleep

def main():
  try:
    conn = sqlite3.connect('info.db')
    cursor = conn.cursor()
  except Error:
    print(f'Um erro aconteceu! ERRO: {Error}')
  escolha = input('Deseja procurar nome exato ou (talvez) nome exato com resultados parecidos?(n/r)\n >  ')
  if escolha == 'r':
    item_a_ser_pesquisado = input('Pesquise um nome(em inglês)\n >  ')
    cursor.execute(f'''
    SELECT * FROM info
    WHERE nome LIKE '{item_a_ser_pesquisado[0]}%'
    ''')
    for h in cursor.fetchall():
      print(f'{h}')
    sleep(60)
    main()
  elif escolha == 'n':
    item_a_ser_pesquisado = input('Pesquise um nome(em inglês)\n >  ')
    cursor.execute(f'''
    SELECT * FROM info
    WHERE nome = '{item_a_ser_pesquisado}'
    ''')
    for h in cursor.fetchall():
      print(f'Nome, email, idade e ID na db: {h}')
    sleep(60)
    main()

if __name__ == '__main__':
  main()
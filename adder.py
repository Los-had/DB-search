from random import choice, randint
import string
import names
import sqlite3
from sqlite3 import Error
from time import sleep

try:
  conn = sqlite3.connect('info.db')
  cursor = conn.cursor()
  cursor.execute('''
  CREATE TABLE IF NOT EXISTS info (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL,
    idade TEXT NOT NULL
  );
  ''')
except Error:
  print(f'Um erro aconteceu! ERRO: {Error}')

repetidor = 100
#caracteres += string.punctuation

def gerar_email():
  caracteres = string.ascii_letters
  caracteres += string.digits
  email = ""
  endereços_de_email = ['@outlook.com', '@gmail.com', '@hotmail.com']
  #lista_de_emails = []
  for g in range(10):
    email += choice(caracteres)
  email += choice(endereços_de_email)
  #lista_de_emails.append(email)
  return email

for i in range(repetidor):
  sleep(0.1)
  nome = names.get_full_name()
  idade = randint(1, 100)
  sleep(1.5)
  try:
    cursor.execute(f"""
    INSERT INTO info (nome, email, idade)
    VALUES ('{nome}', '{gerar_email()}', '{str(idade)} Anos')
    """)
    conn.commit()
  except Error:
    print(f'Um erro aconteceu! ERRO: {Error}')
sleep(10)
cursor.execute('''
SELECT * FROM info
''')
for i in cursor.fetchall():
  print(f'{i}\n')

conn.close()
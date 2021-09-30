import ply.lex
import re
import codecs
import os
import sys

reservadas = ['AND', 'EFFACER', 'POUR', 'EST', 'AUGMENTER', 'AFFIRMER', 'CHANGER', 'DE', 'ANONYME',
              'REVENIR', 'PAUSE', 'AUTRE', 'GLOBAL', 'NE_PAS', 'ESSAYER', 'CLASSER', 'SAUF', 'OUI',
              'OU', 'TANDIS_QUE', 'CONTINUEZ', 'DYNAMIQUE', 'IMPORTER', 'PASSE', 'AVEC', 'DEFINIR',
              'FINALEMENT', 'DANS', 'IMPRIMER', 'RENDEMENT']

tokens = reservadas+['Id', 'Numerals', 'Op_sum', 'Op_res', 'Op_mul', 'Op_div', 'Op_por',
          'Op_igu', 'Op_may', 'Op_men', 'Op_mayI', 'Op_menI',
          'P_der', 'P_izq', 'C_der', 'C_izq', 'Ll_der', 'Ll_izq',
          'Coma', 'pComa', 'point', 'pIgual']

t_Op_sum = r'\+\+'
t_Op_res = r'\-\-'
t_Op_mul = r'\*\*'
t_Op_div = r'\/\/'
t_Op_por = r'\%\%'
t_Op_igu = r'='
t_Op_may = r'>'
t_Op_men = r'<'
t_Op_mayI = r'>='
t_Op_menI = r'<='
t_P_der = r'\)'
t_P_izq = r'\('
t_C_der = r'\]'
t_C_izq = r'\['
t_Ll_der = r'\}'
t_Ll_izq = r'\{'
t_Coma = r','
t_pComa = r';'
t_point = r'\.'
t_pIgual = r':='

def t_Id(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value.upper() in reservadas:
        t.value = t.value.upper()
        t.type = t.value
    return t

def t_comment(t):
    r'\-.*'
    pass

def t_number(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
    print ("illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def buscarFicheros(directorio):
    ficheros = []
    numArchivo = ''
    respuesta = False
    cont = 1

    for base, dirs, files in os.walk(directorio):
        ficheros.append(files)

    for file in files:
        print (str(cont)+"."+file)
        cont = cont+1

    while respuesta == False:
        numArchivo = input('\n Numero del test: ')
        for file in files:
            if file == files[int(numArchivo)-1]:
                respuesta = True
                break

    print ("Has escogido \"%s\" \n" %files[int(numArchivo)-1])

    return files[int(numArchivo)-1]

directorio = '/Users/TOTTUS/PycharmProjects/pythonProject/txt/'
archivo = buscarFicheros(directorio)
test = directorio+archivo
fp = codecs.open(test, "r", "utf-8")
cadena = fp.read()
fp.close()

analizador = ply.lex.lex()

analizador.input(cadena)

while True:
    tok = analizador.token()
    if not tok:
        break
    print(tok)
import ply.lex as lex  # importando a biblioteca ply para o léxico

reserved = {
    'int': 'INT',
    'char': 'CHAR',
    'false': 'FALSE',
    'true': 'TRUE',
    'if': 'IF',
    'else': 'ELSE',
    'void': 'VOID',
    'class': 'CLASS',
    'new': 'NEW',
    'return': 'RETURN',
    'for': 'FOR',
    'while': 'WHILE',
    'do': 'DO'
}

#Definindo Tokens e seus padroes
tokens = [
    'SOMA',
    'INT_V',
    'ID',
    'STRING',
    'CHAR_V',
    'PARENT_ABRE',
    'PARENT_FECHA',
    'ASPAS_SIMPLES',
    'ASPAS_DUPLAS',
] + list(reserved.values())

t_PARENT_ABRE = r'\('
t_PARENT_FECHA = r'\)' 
t_SOMA = r'\+'
t_STRING = '.+|^".+"$'
t_CHAR_V = "^'.'$"
t_ignore = ' \t'


def t_ID(t):
    #r'[A-Z_a-z][A-Z_a-z0-9]*'
    r'^[A-Z]+|^[a-z]+'
    t.type = reserved.get(t.value, 'ID')
    return t


def t_INT_V(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_newline(t):  #funcao para quebra de linha
    r'\n+'  #token de quebra de linha
    t.lexer.lineno += len(t.value)  #incrementa o número de linhas


def t_error(t):
    print("Caractere incorreto: ", t.value[0])
    t.lexer.skip(1)  #pula o caractere incorreto


#Criando analisador Lexico
lexema = lex.lex()

#Lendo conteúdo que será analisado pelo analisador léxico

lexema.input('')  #input será o código em c++ propriamente dito

for token in lexema:
    print(token.type, token.value, token.lineno, token.lexpos)
    #print(token.value)

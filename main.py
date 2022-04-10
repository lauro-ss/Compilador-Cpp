import ply.lex as lex  # importando a biblioteca ply para o léxico

reserved = {
    'typedef': 'TYPEDEF',
    'using': 'USING',
    'namespace': 'NAMESPACE',
    'sizeof': 'SIZEOF',
    'typeid': 'TYPEID',
    'try': 'TRY',
    #TIPOS
    'bool': 'BOOL',
    'int': 'INT',
    #Booleanos
    'false': 'FALSE',
    'true': 'TRUE',
    'not': 'NOT',
    'or': 'OR',
    'xor': 'XOR',
    'and': 'AND',
    #Condicionais
    'if': 'IF',
    'else': 'ELSE',
    #Funcoes/Structs
    'struct': 'STRUCT',
    'void': 'VOID',
    'return': 'RETURN',
    #Classes
    'static': 'STATIC',
    'public': 'PUBLIC',
    'this': 'THIS',
    'class': 'CLASS',
    'new': 'NEW',
    #Repeticao
    'for': 'FOR',
    'while': 'WHILE',
}

#Definindo Tokens e seus padroes
tokens = [
    'SOMA',
    'SUB',
    'MULT',
    'DIV',
    'INT_V',
    'ID',
    'STRING',
    'PARENT_ABRE',
    'PARENT_FECHA',
    'COMENTARIO',
] + list(reserved.values())

t_PARENT_ABRE = r'\('
t_PARENT_FECHA = r'\)' 
t_SOMA = r'\+'
t_SUB = r'-'
t_MULT = r'\*'
t_DIV = r'/'
t_STRING = r'"(.|\n)*"'
t_ignore = ' \t'

def t_COMENTARIO(t):
  r'(/\*(.|\n)*\*/)|(//.*)'
  #r'(/\*(.|\n)*?\*/)|(//.*)'
  return t


def t_ID(t):
    r'[A-Z_a-z][A-Z_a-z0-9]*'
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

lexema.input('/')  #input será o código em c++ propriamente dito

for token in lexema:
    print(token.type, token.value, token.lineno, token.lexpos)
    #print(token.value)

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
    'MODULO',
    'INT_V',
    'ID',
    'RECEBER',
    'MAIOR_Q',
    'MAIOR_IGUAL',
    'MENOR_IGUAL',
    'MENOR_Q',
    'IGUAL',
    'DIFERENTE',
    'OP_E',
    'OP_OU',
    'OP_OU_EX',
    'OP_NOT',
    'STRING',
    'PARENT_ABRE',
    'PARENT_FECHA',
    'COLCHETE_ABRE',
    'COLCHETE_FECHA',
    'CHAVE_ABRE',
    'CHAVE_FECHA',
    'COMENTARIO',
    'PONTO_VIRG',
    'VIRGULA',
    'ENDERECO',
] + list(reserved.values())

t_PARENT_ABRE = r'\('
t_PARENT_FECHA = r'\)' 
t_COLCHETE_ABRE = r'\['
t_COLCHETE_FECHA = r'\]'
t_CHAVE_ABRE = r'{'
t_CHAVE_FECHA = r'}'
t_SOMA = r'\+'
t_SUB = r'-'
t_MULT = r'\*'
t_DIV = r'/'
t_MAIOR_Q = r'>'
t_MENOR_Q = r'<'
t_MAIOR_IGUAL = '>='
t_MENOR_IGUAL = '<='
t_OP_E = r'&&'
t_OP_OU = r'\|\|'
t_OP_OU_EX = r'\^'
t_OP_NOT = '!'
t_MODULO = '%'
t_STRING = r'"(.|\n)*"'
t_ignore = ' \t'
t_PONTO_VIRG = ';'
t_ENDERECO = '&'
t_IGUAL = '=='
t_DIFERENTE = '!='
t_RECEBER = '='
t_VIRGULA = ','

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

lexema.input('')  #input será o código em c++ propriamente dito

for token in lexema:
    print(token.type, token.value, token.lineno, token.lexpos)
    #print(token.value)

import ply.lex as lex

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
    'string': 'STRING',
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
    'STRING_V',
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
    'PONTO',
    'SETA',
    'DOIS_PONTOS',
    'MAIS_MAIS',
    'MENOS_MENOS'
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
t_STRING_V = '"(.|\n)*"'
t_PONTO_VIRG = ';'
t_ENDERECO = '&'
t_IGUAL = '=='
t_DIFERENTE = '!='
t_RECEBER = '='
t_VIRGULA = ','
t_PONTO = r'\.'
t_SETA = r'-\>'
t_DOIS_PONTOS = r':'
t_MAIS_MAIS = r'\+\+'
t_MENOS_MENOS = r'\-\-'

t_ignore = ' \t'

def t_COMENTARIO(t):
  r'(/\*(.|\n)*?\*/)|(//.*)'
  #r'(/\*(.|\n)*?\*/)|(//.*)'
  pass


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

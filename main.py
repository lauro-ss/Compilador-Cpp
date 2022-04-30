from lexico import *
from sintatico import *

lexema = lex.lex()

lexema.input('teste')
parser = yacc.yacc()
printf(parser.parser(debug=False))

#for token in lexema:
#    print(token.type, token.value, token.lineno, #token.lexpos)
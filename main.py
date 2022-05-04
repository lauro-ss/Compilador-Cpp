from lexico import *
from sintatico import *

lexema = lex.lex()

e = '''int main(){
                  if(2 > 3){
                    int a;
                   } 
                  int b; 
                  int c; 
                  return 0;
}'''

cl = '''
class skullmonkey{
          public:
          int teste(){
              typedef int inteiro,eu,tu;
          }
};
'''

lexema.input(cl)
parser = yacc.yacc()
#parser.parse(debug=True)
parser.parse(debug=False)
#for token in lexema:
#    print(token.type, token.value, token.lineno, #token.lexpos)
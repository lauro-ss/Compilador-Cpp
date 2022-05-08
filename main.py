from lexico import *
from sintatico import *

lexema = lex.lex()

e = '''int main(){
                  if(2 > 3){
                    int a;
                   } 
                  int b, a, c, d, e; 
                  int c; 
                  return c;
}'''

d = '''
void main(){
  teste = "2";
  if(a){
    if(2+2){
      a = "2";
      a = "2";
    }
  }else{
    if(2+2){
      a = "2";
    }
  if(true)
    if(true)
      if(true)
          a = 2;
      else
          a = 3;
    else{
          a = 2;}
}
}'''

cl = '''
class teste{
          public:
          void carro(){
              return 2;
          }
          string ttt(int c){
            return c;
          }
};
'''

lexema.input(d)
parser = yacc.yacc()
#parser.parse(debug=True)
parser.parse(debug=False)
#for token in lexema:
#    print(token.type, token.value, token.lineno, token.lexpos)
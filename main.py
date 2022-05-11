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
      int a;
      int a;
};
'''
ttt = '''
void main(int n){

}
'''


teste = '''
    using namespace std;
    typedef int inteiro, realkkk;
    typedef int inteiro, realkkk;
    using teste::testado;
int main (void){
    typedef int inteiro, realkkk;
    using teste::testado;
}'''

lexema.input(cl)
parser = yacc.yacc()
#parser.parse(debug=True)
result = parser.parse(debug=False)
visitor = vis.Visitor()
#for token in lexema:
#    print(token.type, token.value, token.lineno, token.lexpos)
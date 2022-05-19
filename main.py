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
  if (true) {} else if (true) {}

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
using namespace std;
using std::cout;
typedef int inteiro, abc;
class teste{
    public:
      int c, d, e = a->t, d = (2+2);
      int d = 2 * 2, a = 3 / 3, c = 3 % 3;
      static void teste( string b, bool c, tipo d){
      }
};

'''
ttt = '''
void main(int n){
 teste(a,c);
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
result.accept(visitor)
#for token in lexema:
#    print(token.type, token.value, token.lineno, token.lexpos)
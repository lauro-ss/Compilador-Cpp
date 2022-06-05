from lexico import *
from sintatico import *

lexema = lex.lex()

e = '''int main(){
                  if(2 > 3){
                    int a;
                   } 
                  int b, a, c, d, e; 
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
    for(a = 2;;a++){

    }
}
}'''

cl = '''
using namespace std;
using std::cout;
typedef int inteiro, abc, dan, rosa, rola;
class teste{
    public:
      int c, d, e = a->t, d = teste(a,b,c,d);
      int d = 2 * 2, a = 3 / 3, c = 3 % 3;
      static void teste( string b, bool c, tipo d){
        int a;
        a = teste(a,b,c,d);
        if(2+2){
          if(2+2)
            2 + 2;
        }
        while(true){
          teste(a,b,c);
        }
        for(int a; 2 > 2; a++){
          teste(a,b,c);
        }
      }
};

'''
ttt = '''
void main(int n){
 teste(a,c);
}
'''


teste = '''
  int c;
  int main(int a){
    a = 2;
    c = 2;
    return 2;
    for(a = 2;a < 10;a++){
      int cc;
    }
  }
  int a = main(2);
  int b;
  class pessoa{
    public:
      int d;
    int corpo(){}
  };
'''
teste2 = '''
    int main(int a){
    for(a = 2;a < 10;a++){
      int cc;
    }
    while(true){}
}
'''

lexema.input(teste2)
parser = yacc.yacc()
#parser.parse(debug=True)
result = parser.parse(debug=False)
visitor = sv.SemanticVisitor()
result.accept(visitor)
visitor = vis.Visitor()
result.accept(visitor)
#for token in lexema:
#    print(token.type, token.value, token.lineno, token.lexpos)
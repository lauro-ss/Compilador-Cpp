import ply.yacc as yacc
from lexico import *

#program -> cpp$
#cpp -> decl_classe 
#     | decl_funcao 
#     | decl_variavel
#     | decl_classe  cpp
#     | decl_funcao  cpp
#     | decl_variavel cpp
#decl_classe -> CLASS ID body;

#decl_funcao -> tipo ID(parametros) body
#parametros -> ID ID
#            | ID ID , parametros
#body -> { comandos }
#comandos ->   decl_variavel
#            | decl_variavel comandos
#            | WHILE(exp) body
#            | WHILE(exp) body comandos
#decl_variavel ->  tipo ID; | tipo ID = exp;
#tipo -> INT | BOOL | ID

def p_cpp(p):
  '''cpp : decl_classe
         | decl_funcao
         | decl_variavel
         | decl_classe  cpp
         | decl_funcao  cpp
         | decl_variavel cpp'''

def p_decl_classe(p):
  '''decl_classe : CLASS ID body PONTO_VIRG'''
  
def p_decl_funcao(p):
  '''decl_funcao : tipo ID PARENT_ABRE parametros PARENT_FECHA body'''
  
def p_parametros(p):
  '''parametros : tipo ID
                | tipo ID VIRGULA parametros'''
  
def p_decl_variavel(p):
  '''decl_variavel : tipo ID PONTO_VIRG 
                   | tipo ID RECEBER exp PONTO_VIRG'''
  
def p_body(p):
  '''body : CHAVE_ABRE comandos CHAVE_FECHA'''
  
def p_comandos(p):
  '''comandos : decl_variavel
              | decl_variavel comandos
              | condicional body
              | condicional body comandos
              | repeticao body
              | repeticao body comandos'''

def p_tipo(p):
  '''tipo : INT 
          | BOOL 
          | ID'''

def p_error(p):
  print("Erro sintático")
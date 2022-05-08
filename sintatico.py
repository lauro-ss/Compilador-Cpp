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
    '''decl_classe : CLASS ID body_class PONTO_VIRG'''


def p_body_class(p):
    '''body_class : CHAVE_ABRE PUBLIC DOIS_PONTOS content_class CHAVE_FECHA'''


def p_content_class(p):
    '''content_class : decl_variavel content_class
                   | decl_funcao content_class
                   | decl_variavel
                   | decl_funcao'''


def p_decl_funcao(p):
    '''decl_funcao : tipo ID PARENT_ABRE parametros PARENT_FECHA body
                 | tipo ID PARENT_ABRE PARENT_FECHA body
                 | tipo ID PARENT_ABRE VOID PARENT_FECHA body
                 | VOID ID PARENT_ABRE parametros PARENT_FECHA body
                 | VOID ID PARENT_ABRE PARENT_FECHA body
                 | VOID ID PARENT_ABRE VOID PARENT_FECHA body'''


def p_parametros(p):
    '''parametros : tipo ID
                | tipo ID VIRGULA parametros'''


def p_decl_variavel(p):
    '''decl_variavel : tipo ID PONTO_VIRG 
                   | tipo ID RECEBER exp PONTO_VIRG
                   | tipo ID decl_variavel_n PONTO_VIRG 
                   | tipo ID RECEBER exp decl_variavel_n PONTO_VIRG
                   | TYPEDEF tipo ID PONTO_VIRG
                   | TYPEDEF tipo ID decl_variavel_n'''


def p_decl_variavel_n(p):
    '''decl_variavel_n : VIRGULA ID decl_variavel_n
                     | VIRGULA ID RECEBER exp decl_variavel_n
                     | VIRGULA ID 
                     '''


def p_body(p):
    '''body : CHAVE_ABRE comandos CHAVE_FECHA
            | CHAVE_ABRE CHAVE_FECHA'''


def p_comandos(p):
    ''' comandos : comando 
               | comando comandos'''


def p_comando(p):
    '''comando : condicional_1
               | condicional_2'''


def p_exp(p):
    '''exp : exp RECEBER exp_1
         | exp_1'''


def p_exp_1(p):
    '''exp_1 : exp_1 OP_OU exp_2 
           | exp_1 OR exp_2
           | exp_2'''


def p_exp_2(p):
    '''exp_2 : exp_2 OP_E exp_3
           | exp_2 AND exp_3
           | exp_3'''


def p_exp_3(p):
    '''exp_3 : exp_3 OP_OU_EX exp_4
           | exp_3 XOR exp_4
           | exp_4'''


def p_exp_4(p):
    '''exp_4 : exp_4 IGUAL exp_5
           | exp_4 DIFERENTE exp_5
           | exp_5'''


def p_exp_5(p):
    '''exp_5 : exp_5 MENOR_Q exp_6
           | exp_5 MAIOR_Q exp_6
           | exp_5 MAIOR_IGUAL exp_6
           | exp_5 MENOR_IGUAL exp_6
           | exp_6'''


def p_exp_6(p):
    '''exp_6 : exp_6 SOMA exp_7
           | exp_6 SUB exp_7
           | exp_7'''


def p_exp_7(p):
    '''exp_7 : exp_7 MULT exp_8
           | exp_7 DIV exp_8
           | exp_7 MODULO exp_8
           | exp_8'''


def p_exp_8(p):
    '''exp_8 : OP_NOT exp_9
           | NOT exp_9
           | exp_9 MAIS_MAIS
           | exp_9 MENOS_MENOS
           | SIZEOF PARENT_ABRE exp_9 PARENT_FECHA
           | exp_9'''


def p_exp_9(p):
    '''exp_9 : ID
           | INT_V
           | TRUE
           | FALSE
           | chamada_funcao
           | STRING
           | PARENT_ABRE exp PARENT_FECHA'''


def p_chamada_funcao(p):
    '''chamada_funcao : ID PARENT_ABRE parametros PARENT_FECHA
                    | ID PARENT_ABRE PARENT_FECHA
                    | TYPEID PARENT_ABRE exp PARENT_FECHA'''

def p_condicional_1(p):
    '''condicional_1 : IF PARENT_ABRE exp PARENT_FECHA rest_if
                     | exp PONTO_VIRG 
                     | decl_variavel
                     | WHILE PARENT_ABRE exp PARENT_FECHA body
                     | FOR PARENT_ABRE for_log PARENT_FECHA body
                     | RETURN exp PONTO_VIRG
                     | RETURN PONTO_VIRG'''

def p_condicional_2(p):
    '''condicional_2 : IF PARENT_ABRE exp PARENT_FECHA body
                     | IF PARENT_ABRE exp PARENT_FECHA comando'''

def p_rest_if(p):
    '''rest_if : condicional_1 ELSE condicional_1
               | condicional_1 ELSE body
               | body ELSE body
               | body ELSE condicional_1'''


def p_for_log(p):
    '''for_log : decl_variavel PONTO_VIRG
             | decl_variavel exp PONTO_VIRG
             | decl_variavel exp PONTO_VIRG exp
             | decl_variavel PONTO_VIRG exp
             | PONTO_VIRG exp PONTO_VIRG exp
             | PONTO_VIRG exp PONTO_VIRG
             | PONTO_VIRG PONTO_VIRG exp
             | PONTO_VIRG PONTO_VIRG'''


def p_tipo(p):
    '''tipo : INT 
          | BOOL 
          | ID
          | STRING'''


def p_error(p):
    print("Erro Sintático")

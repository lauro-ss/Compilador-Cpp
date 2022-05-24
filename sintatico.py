import ply.yacc as yacc
from lexico import *
import sintaxe_abstrata as sa
import Visitor as vis


def p_cpp(p):
    '''cpp : decl_classe
         | decl_funcao
         | decl_variavel
         | typedef
         | using
         | decl_classe  cpp
         | decl_funcao  cpp
         | decl_variavel cpp
         | typedef cpp
         | using cpp'''
    if(len(p) == 3):
      p[0] = sa.cppConcrete(p[1],p[2])
    else:
      p[0] = sa.cppConcrete(p[1],None)
    

def p_decl_classe(p):
    '''decl_classe : CLASS ID body_class PONTO_VIRG'''
    p[0] = sa.decl_classeConcrete(p[1],p[2],p[3])


def p_body_class(p):
    '''body_class : CHAVE_ABRE PUBLIC DOIS_PONTOS content_class CHAVE_FECHA
                  | CHAVE_ABRE CHAVE_FECHA'''
    if(len(p) > 3):
      p[0] = sa.body_classConcrete(p[2],p[4])
    else:
      p[0] = sa.body_classConcrete(None,None)


def p_content_class(p):
    '''content_class : decl_variavel
                     | decl_funcao
                     | STATIC decl_variavel
                     | STATIC decl_funcao
                     | decl_variavel content_class
                     | decl_funcao content_class
                     | STATIC decl_variavel content_class
                     | STATIC decl_funcao content_class'''
    if(len(p) == 4):
      p[0] = sa.content_classConcrete(p[1],p[2],p[3])
    elif(len(p) == 3 and p[1] == "static"):
      p[0] = sa.content_classConcrete(p[1],p[2],None)
    elif(len(p) == 3):
      p[0] = sa.content_classConcrete(None,p[1],p[2])
    else:
      p[0] = sa.content_classConcrete(None,p[1],None)


def p_decl_funcao(p):
    '''decl_funcao : tipo ID PARENT_ABRE parametros PARENT_FECHA body
                 | tipo ID PARENT_ABRE PARENT_FECHA body
                 | tipo ID PARENT_ABRE VOID PARENT_FECHA body
                 | VOID ID PARENT_ABRE parametros PARENT_FECHA body
                 | VOID ID PARENT_ABRE PARENT_FECHA body
                 | VOID ID PARENT_ABRE VOID PARENT_FECHA body'''
    if(len(p) == 7):
      p[0] = sa.decl_funcaoConcrete(p[1],p[2],p[4],p[6])
    elif(len(p) == 6):
      p[0] = sa.decl_funcaoConcrete(p[1],p[2],None,p[5])


def p_parametros(p):
    '''parametros : tipo ID
                | tipo ID VIRGULA parametros'''
    if(len(p) == 5):
      p[0] = sa.parametrosConcrete(p[1],p[2],p[4])
    else:
      p[0] = sa.parametrosConcrete(p[1],p[2],None)


def p_decl_variavel(p):
    '''decl_variavel : tipo ID PONTO_VIRG 
                   | tipo ID RECEBER exp PONTO_VIRG
                   | tipo ID decl_variavel_n PONTO_VIRG 
                   | tipo ID RECEBER exp decl_variavel_n PONTO_VIRG'''
    if(len(p) == 7):
      p[0] = sa.decl_variavelConcrete(p[1],p[2],p[4],p[5])
    elif(len(p) == 6):
       p[0] = sa.decl_variavelConcrete(p[1],p[2],p[4],None)
    elif(len(p) == 5):
       p[0] = sa.decl_variavelConcrete(p[1],p[2],None,p[3])
    elif(len(p) == 4):
       p[0] = sa.decl_variavelConcrete(p[1],p[2],None,None)


def p_decl_variavel_n(p):
    '''decl_variavel_n : VIRGULA ID decl_variavel_n
                     | VIRGULA ID RECEBER exp decl_variavel_n
                     | VIRGULA ID RECEBER exp
                     | VIRGULA ID 
                     '''
    if(len(p) == 6):
      p[0] = sa.decl_variavel_nConcrete(p[2],p[4],p[5])
    elif(len(p) == 5):
      p[0] = sa.decl_variavel_nConcrete(p[2],p[4],None)
    elif(len(p) == 4):
      p[0] = sa.decl_variavel_nConcrete(p[2],None,p[3])
    elif(len(p) == 3):
      p[0] = sa.decl_variavel_nConcrete(p[2],None,None)

def p_typedef(p):
    '''typedef : TYPEDEF tipo ID PONTO_VIRG
               | TYPEDEF tipo ID decl_typedef_n PONTO_VIRG'''
    if(len(p) == 5):
      p[0] = sa.typedefConcrete(p[1], p[2], p[3])
    if(len(p) == 6):
      p[0] = sa.typedefConcrete1(p[1], p[2], p[3], p[4])

def p_decl_typedef_n(p):
    '''decl_typedef_n : VIRGULA ID decl_typedef_n
                      | VIRGULA ID'''
    if(len(p) == 4):
      p[0] = sa.decl_typedef_nConcrete(p[2], p[3])
    elif(len(p) == 3):
      p[0] = sa.decl_typedef_nConcrete(p[2], None)

def p_using(p):
    '''using : USING ID 2X_DOIS_PONTOS ID PONTO_VIRG
             | USING ID ID PONTO_VIRG'''
    if(len(p) == 6):
      p[0] = sa.usingConcrete1(p[1], p[2], p[4])
    elif(len(p) == 5):
      p[0] = sa.usingConcrete(p[1], p[2], p[3])

def p_body(p):
    '''body : CHAVE_ABRE comandos CHAVE_FECHA
            | CHAVE_ABRE CHAVE_FECHA'''
    if(len(p) == 4):
      p[0] = sa.bodyConcrete(p[2])


def p_comandos(p):
    ''' comandos : comando 
               | comando comandos'''
    if(len(p) == 2):
      p[0] = sa.comandosConcrete(p[1], None)
    elif(len(p) == 3):
      p[0] = sa.comandosConcrete(p[1], p[2])


def p_comando(p):
    '''comando : condicional_1
               | condicional_2'''
    if(isinstance(p[1],sa.condicional_1)):
      p[0] = sa.comandoConcrete(p[1])
    elif(isinstance(p[1],sa.condicional_2)):
      p[0] = sa.comandoConcrete(p[1])


def p_exp(p):
    '''exp : exp RECEBER exp_1
           | exp_1'''
    if(len(p) == 4):
      p[0] = sa.expConcrete(p[1],p[3])
    else:
      p[0] = sa.expConcrete(None,p[1])


def p_exp_1(p):
    '''exp_1 : exp_1 OP_OU exp_2 
           | exp_1 OR exp_2
           | exp_2'''
    if(len(p) == 4 and p[2] == "or"):
      p[0] = sa.exp_1_OR(p[1],p[3])
    elif(len(p) == 4 and p[2] == "||"):
      p[0] = sa.exp_1_OP_OU(p[1],p[3])
    elif(len(p) == 2):
      p[0] = sa.exp_1Concrete(p[1])


def p_exp_2(p):
    '''exp_2 : exp_2 OP_E exp_3
           | exp_2 AND exp_3
           | exp_3'''
    if(len(p) == 4 and p[2] == "and"):
      p[0] = sa.exp_2_AND(p[1],p[3])
    elif(len(p) == 4 and p[2] == "&&"):
      p[0] = sa.exp_2_OP_E(p[1],p[3])
    elif(len(p) == 2):
      p[0] = sa.exp_2Concrete(p[1])


def p_exp_3(p):
    '''exp_3 : exp_3 OP_OU_EX exp_4
           | exp_3 XOR exp_4
           | exp_4'''
    if(len(p) == 4 and p[2]  == "xor"):
      p[0] = sa.exp_3_XOR(p[1],p[3])
    elif(len(p) == 4 and p[2]  == "^"):
      p[0] = sa.exp_3_OP_OU_EX(p[1],p[3])
    elif(len(p) == 2):
      p[0] = sa.exp_3Concrete(p[1])


def p_exp_4(p):
    '''exp_4 : exp_4 IGUAL exp_5
           | exp_4 DIFERENTE exp_5
           | exp_5'''
    if(len(p) == 4 and p[2] == "=="):
      p[0] = sa.exp_4_IGUAL(p[1],p[3])
    elif(len(p) == 4 and p[2] == "!="):
      p[0] = sa.exp_4_DIFERENTE(p[1],p[3])
    elif(len(p) == 2):
      p[0] = sa.exp_4Concrete(p[1])


def p_exp_5(p):
    '''exp_5 : exp_5 MENOR_Q exp_6
           | exp_5 MAIOR_Q exp_6
           | exp_5 MAIOR_IGUAL exp_6
           | exp_5 MENOR_IGUAL exp_6
           | exp_6'''
    if(len(p) == 4 and p[2] == "<"):
      p[0] = sa.exp_5_MENOR_Q(p[1],p[3])
    elif(len(p) == 4 and p[2] == ">"):
      p[0] = sa.exp_5_MAIOR_Q(p[1],p[3])
    elif(len(p) == 4 and p[2] == ">="):
      p[0] = sa.exp_5_MAIOR_IGUAL(p[1],p[3])
    elif(len(p) == 4 and p[2] == "<="):
      p[0] = sa.exp_5_MENOR_IGUAL(p[1],p[3])
    elif(len(p) == 2):
      p[0] = sa.exp_5Concrete(None,p[1])


def p_exp_6(p):
    '''exp_6 : exp_6 SOMA exp_7
           | exp_6 SUB exp_7
           | exp_7'''
    if(len(p) == 4 and p[2] == "+"):
      p[0] = sa.exp_6_SOMA(p[1],p[3])
    elif(len(p) == 4 and p[2] == "-"):
      p[0] = sa.exp_6_SUB(p[1],p[3])
    elif(len(p) == 2):
      p[0] = sa.exp_6Concrete(p[1])


def p_exp_7(p):
    '''exp_7 : exp_7 MULT exp_8
           | exp_7 DIV exp_8
           | exp_7 MODULO exp_8
           | exp_8'''
    if(len(p) == 4 and p[2] == "*"):
      p[0] = sa.exp_7_MULT(p[1],p[3])
    elif(len(p) == 4 and p[2] == "/"):
      p[0] = sa.exp_7_DIV(p[1],p[3])
    elif(len(p) == 4 and p[2] == "%"):
      p[0] = sa.exp_7_MODULO(p[1],p[3])
    elif(len(p) == 2):
      p[0] = sa.exp_7Concrete(p[1])


def p_exp_8(p):
    '''exp_8 : OP_NOT exp_9
           | NOT exp_9
           | exp_9 MAIS_MAIS
           | exp_9 MENOS_MENOS
           | SIZEOF PARENT_ABRE exp_9 PARENT_FECHA
           | NEW tipo
           | exp_9'''
    if(len(p) == 5):
      p[0] = sa.exp_8_SIZEOF(p[1],p[3])
    
    elif(len(p) == 3 and p[1] == '!'):
      p[0] = sa.exp_8_OP_NOT(p[2])
    
    elif(len(p) == 3 and p[1] == 'not'):
      p[0] = sa.exp_8_NOT(p[2])
    
    elif(len(p) == 3 and p[1] == 'new'):
      p[0] = sa.exp_8_NEW(p[2])
    
    elif(len(p) == 3 and p[2] == '++'):
      p[0] = sa.exp_8_MAIS_MAIS(p[1])
    
    elif(len(p) == 3 and p[2] == '--'):
      p[0] = sa.exp_8_MENOS_MENOS(p[1])
    
    elif(len(p) == 2):
      p[0] = sa.exp_8Concrete(p[1])

def p_exp_9(p):
    '''exp_9 : exp_9 PONTO exp_10
             | exp_9 SETA exp_10
             | exp_10'''
    if(len(p) == 4 and p[2] == '.'):
      p[0] = sa.exp_9_PONTO(p[1],p[3])
    elif(len(p) == 4 and p[2] == '->'):
      p[0] = sa.exp_9_SETA(p[1],p[3])
    elif(len(p) == 2):
      p[0] = sa.exp_9Concrete(p[1])


def p_exp_10(p):
    '''exp_10 : ID
           | INT_V
           | TRUE
           | FALSE
           | chamada_funcao
           | STRING_V
           | THIS
           | PARENT_ABRE exp PARENT_FECHA'''
    if(len(p) == 4):
      p[0] = sa.exp_10_exp(p[2])
    
    elif(isinstance(p[1],sa.chamada_funcao)):
      p[0] = sa.exp_10_funcao(p[1])
    
    elif(len(p) == 2):
      p[0] = sa.exp_10Concrete(p[1])


def p_chamada_funcao(p):
    '''chamada_funcao : ID PARENT_ABRE parametros_chamada PARENT_FECHA
                      | ID PARENT_ABRE PARENT_FECHA
                      | TYPEID PARENT_ABRE exp PARENT_FECHA'''
      
    if(len(p) == 5):
      p[0] = sa.chamada_funcaoConcrete(p[1],p[3])
    elif(len(p) == 4 and p[1] == "typeid"):
      p[0] = sa.chamada_funcaoTypeid(p[1],p[3])
    elif(len(p) == 4):
      p[0] = sa.chamada_funcaoConcrete(p[1],None)
      
def p_parametros_chamada(p):
    '''parametros_chamada : ID VIRGULA parametros_chamada
                          | ID'''
    if(len(p) == 4):
      p[0] = sa.parametros_chamadaConcrete(p[1],p[3])
    elif(len(p) == 2):
      p[0] = sa.parametros_chamadaConcrete(p[1],None)

def p_condicional_1(p):
    '''condicional_1 : IF PARENT_ABRE exp PARENT_FECHA rest_if
                     | exp PONTO_VIRG 
                     | decl_variavel
                     | typedef
                     | using
                     | chamada_funcao
                     | WHILE PARENT_ABRE exp PARENT_FECHA body
                     | FOR PARENT_ABRE for_log PARENT_FECHA body
                     | WHILE PARENT_ABRE exp PARENT_FECHA condicional_1
                     | FOR PARENT_ABRE for_log PARENT_FECHA condicional_1
                     | RETURN exp PONTO_VIRG
                     | RETURN PONTO_VIRG'''
    if(len(p) == 6 and p[1] == 'if'):
      p[0] = sa.condicional_1_IF(p[1], p[2], p[5])
    
    elif(len(p) == 6 and p[1] == 'while'):
      p[0] = sa.condicional_1_WHILE(p[1], p[2], p[5])
    
    elif(len(p) == 6 and p[1] == 'for'):
      p[0] = sa.condicional_1Concrete(p[1], p[2], p[5])
    
    elif(len(p) == 4):
      p[0] = sa.condicional_1_RETURN(p[1],p[2])
    
    elif(len(p) == 3 and p[1] == 'return'):
      p[0] = sa.condicional_1_RETURN(p[1],None)
    
    elif(len(p) == 3):
      p[0] = sa.condicional_1_EXP(p[1])
    
    elif(isinstance(p[1],sa.chamada_funcao)):
      p[0] = sa.exp_10_funcao(p[1])
    
    elif(isinstance(p[1],sa.decl_variavel)):
      p[0] = sa.condicional_1_decl_variavel(p[1])
    
    elif(isinstance(p[1],sa.typedef)):
      p[0] = sa.condicional_1_typedef(p[1])
    
    elif(isinstance(p[1],sa.using)):
      p[0] = sa.condicional_1_using(p[1])

def p_condicional_2(p):
    '''condicional_2 : IF PARENT_ABRE exp PARENT_FECHA body
                     | IF PARENT_ABRE exp PARENT_FECHA comando
                     | IF PARENT_ABRE exp PARENT_FECHA condicional_1 ELSE condicional_2
                     | IF PARENT_ABRE exp PARENT_FECHA body ELSE condicional_2'''
    if(len(p) == 6):
      p[0] = sa.condicional_2Concrete(p[1],p[3],p[5])
    elif(len(p) == 8):
      p[0] = sa.condicional_2Concrete_2(p[1],p[3],p[5],p[6],p[7])

def p_rest_if(p):
    '''rest_if : condicional_1 ELSE condicional_1
               | body ELSE body
               | condicional_1 ELSE body
               | body ELSE condicional_1'''
    if(isinstance(p[1],sa.condicional_1) and isinstance(p[3],sa.condicional_1)):
      p[0] = sa.rest_ifConcrete(p[1],p[2],p[3])
    elif(isinstance(p[1],sa.body) and isinstance(p[3],sa.body)):
      p[0] = sa.rest_ifConcrete(p[1],p[2],p[3])
    elif(isinstance(p[1],sa.condicional_1) and isinstance(p[3],sa.body)):
      p[0] = sa.rest_ifConcrete(p[1],p[2],p[3])
    elif(isinstance(p[1],sa.body) and isinstance(p[1],sa.condicional_1)):
      p[0] = sa.rest_ifConcrete(p[1],p[2],p[3])


def p_for_log(p):
    '''for_log : decl_variavel PONTO_VIRG
             | decl_variavel exp PONTO_VIRG
             | decl_variavel exp PONTO_VIRG exp
             | decl_variavel PONTO_VIRG exp
             | PONTO_VIRG exp PONTO_VIRG exp
             | PONTO_VIRG exp PONTO_VIRG
             | PONTO_VIRG PONTO_VIRG exp
             | PONTO_VIRG PONTO_VIRG'''
    if(len(p) == 3):
      p[0] = sa.for_logConcrete(p[1],None,None)
    
    elif(len(p) == 4 and p[3] == ';'):
      p[0] = sa.for_logConcrete(p[1],p[2],None)
    
    elif(len(p) == 5 and p[3] == ';'):
      p[0] = sa.for_logConcrete(p[1],p[2],p[4])
    
    elif(len(p) == 4 and p[2] == ';'):
      p[0] = sa.for_logConcrete(p[1],None,p[3])
    
    elif(len(p) == 5 and p[1] == ';'):
      p[0] = sa.for_logConcrete(None,p[2],p[4])
    
    elif(len(p) == 4 and p[1] == ';'):
      p[0] = sa.for_logConcrete(None,p[2],None)
    
    elif(len(p) == 4 and p[1] == ';' and p[2] == ';'):
      p[0] = sa.for_logConcrete(p[1])
    
    elif(len(p) == 3 and p[1] == ';' and p[2] == ';'):
      p[0] = sa.for_logConcrete(p[1])


def p_tipo(p):
    '''tipo : INT 
          | BOOL 
          | ID
          | STRING'''
    p[0] = sa.tipoConcrete(p[1])


def p_error(p):
    print("Erro Sintático")

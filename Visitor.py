from visitor_abstract import visitor_abstract
import sintaxe_abstrata as sa


tab = 0

def blank():
    p = ''
    for x in range(tab):
        p = p + ' '
    return p

class Visitor(visitor_abstract):
  
    def visit_cppConcrete(self, cppConcrete):
      
      if(cppConcrete.decl):
        cppConcrete.decl.accept(self)
      
      if(cppConcrete.cpp):
        cppConcrete.cpp.accept(self)

    ###
    
    def visit_decl_classeConcrete(self, decl_classeConcrete):
      print(blank(), decl_classeConcrete.Class,' ' ,decl_classeConcrete.id, '{', end='', sep='')
      
      if(decl_classeConcrete.body_class):
        decl_classeConcrete.body_class.accept(self)
      
      print('\n','}',';', end='', sep='')

    ###
  
    def visit_body_classConcrete(self, body_classConcrete):
      print('\n','\t',body_classConcrete.public, ':', end='', sep='')
      
      if(body_classConcrete.content_class):
        body_classConcrete.content_class.accept(self)

    ###
    
    def visit_content_classConcrete(self, content_classConcrete):
      print('\n','\t', end='', sep='')
      
      if(content_classConcrete.static):
        print(content_classConcrete.static,' ',end='', sep='')
      
      if(content_classConcrete.decl):
        content_classConcrete.decl.accept(self)
      
      if(content_classConcrete.content_class):
        content_classConcrete.content_class.accept(self)

    ###
        
    def visit_decl_funcaoConcrete(self, decl_funcaoConcrete):
      if(decl_funcaoConcrete.tipo):
        if(decl_funcaoConcrete.tipo != 'void'):
          decl_funcaoConcrete.tipo.accept(self)
          print(' ',end='', sep='') 
        else:
          print(decl_funcaoConcrete.tipo,' ',end='', sep='') 
          
      print(decl_funcaoConcrete.id, '(', end='', sep='')

      if(decl_funcaoConcrete.parametros):
        if(decl_funcaoConcrete.parametros != 'void'):
          decl_funcaoConcrete.parametros.accept(self)
        else:
          print(decl_funcaoConcrete.parametros,end='', sep='')
          
      print(')',end='', sep='')
      if(decl_funcaoConcrete.body):
        decl_funcaoConcrete.body.accept(self)
      else:
        print('{','}',end='', sep='')

    ###
  
    def visit_parametrosConcrete(self, parametrosConcrete):
      if(parametrosConcrete.tipo):
          parametrosConcrete.tipo.accept(self)
      print(' ',parametrosConcrete.id ,end='', sep='')
      if(parametrosConcrete.parametros):
        print(",", end='', sep='')
        parametrosConcrete.parametros.accept(self)

    ###

    def visit_decl_variavelConcrete(self, decl_variavelConcrete):
      decl_variavelConcrete.tipo.accept(self)
      print(' ',decl_variavelConcrete.id,end='', sep='')
      if(decl_variavelConcrete.exp):
        print(" = ",end='', sep='')
        decl_variavelConcrete.exp.accept(self)
      if(decl_variavelConcrete.decl_variavel_n):
        decl_variavelConcrete.decl_variavel_n.accept(self)
      print(";")
        
    ###

    def visit_decl_variavel_nConcrete(self, decl_variavel_nConcrete):
      print(", ", decl_variavel_nConcrete.id,end='', sep='')
      if(decl_variavel_nConcrete.exp):
        print(" = ",end='', sep='')
        decl_variavel_nConcrete.exp.accept(self)
      if(decl_variavel_nConcrete.decl_variavel_n):
        decl_variavel_nConcrete.decl_variavel_n.accept(self)

    ###

    def visit_bodyConcrete(self, bodyConcrete):
      print(blank(),'{\n',end='', sep='')
      global tab
      #tab = tab + 1;
      if(bodyConcrete.comandos):
        bodyConcrete.comandos.accept(self)
      tab = tab + 1;
      print(blank(),'}')

    ###

    def visit_comandosConcrete(self, comandosConcrete):
      if(comandosConcrete.comando):
        print(blank(),end='', sep='')
        comandosConcrete.comando.accept(self)
      if(comandosConcrete.comandos):
        #print("\n",end='', sep='')
        comandosConcrete.comandos.accept(self)

    ###

    def visit_comandoConcrete(self, comandoConcrete):
      comandoConcrete.condicional.accept(self)

    ###

    def visit_expConcrete(self, expConcrete):
      if(expConcrete.exp):
        expConcrete.exp.accept(self)
        print(" = ",end='', sep='')
      if(expConcrete.exp_1):
        expConcrete.exp_1.accept(self)

    ###

    def visit_exp_1_OR(self,exp_1Concrete):
      if(exp_1Concrete.exp_1):
        exp_1Concrete.exp_1.accept(self)
        print(" or ",end='', sep='')
      if(exp_1Concrete.exp_2):
        exp_1Concrete.exp_2.accept(self)

    def visit_exp_1_OP_OU(self,exp_1Concrete):
      if(exp_1Concrete.exp_1):
        exp_1Concrete.exp_1.accept(self)
        print(" || ",end='', sep='')
      if(exp_1Concrete.exp_2):
        exp_1Concrete.exp_2.accept(self)

    def visit_exp_1Concrete(self,exp_1Concrete):
      if(exp_1Concrete.exp_2):
       exp_1Concrete.exp_2.accept(self)

    ###
        
    def visit_exp_2_AND(self,exp_2Concrete):
      if(exp_2Concrete.exp_2):
        exp_2Concrete.exp_2.accept(self)
        print(" and ",end='', sep='')
      if(exp_2Concrete.exp_3):
        exp_2Concrete.exp_3.accept(self)

    def visit_exp_2_OP_E(self,exp_2Concrete):
      if(exp_2Concrete.exp_2):
        exp_2Concrete.exp_2.accept(self)
        print(" && ",end='', sep='')
      if(exp_2Concrete.exp_3):
        exp_2Concrete.exp_3.accept(self)
        
    def visit_exp_2Concrete(self,exp_2Concrete):
      if(exp_2Concrete.exp_3):
        exp_2Concrete.exp_3.accept(self)
    
    ###

    def visit_exp_3_XOR(self,exp_3Concrete):
      if(exp_3Concrete.exp_3):
        exp_3Concrete.exp_3.accept(self)
        print(" xor ",end='', sep='')
      if(exp_3Concrete.exp_4):
        exp_3Concrete.exp_4.accept(self)

    def visit_exp_3_OP_OU_EX(self,exp_3Concrete):
      if(exp_3Concrete.exp_3):
        exp_3Concrete.exp_3.accept(self)
        print(" ^ ",end='', sep='')
      if(exp_3Concrete.exp_4):
        exp_3Concrete.exp_4.accept(self)

    def visit_exp_3Concrete(self,exp_3Concrete):
      if(exp_3Concrete.exp_4):
        exp_3Concrete.exp_4.accept(self)

    ###

    def visit_exp_4Concrete(self,exp_4Concrete):
      if(exp_4Concrete.exp_5):
        exp_4Concrete.exp_5.accept(self)
    
    def visit_exp_4_IGUAL(self,exp_4Concrete):
      if(exp_4Concrete.exp_4):
        exp_4Concrete.exp_4.accept(self)
        print(" == ",end='', sep='')
      if(exp_4Concrete.exp_5):
        exp_4Concrete.exp_5.accept(self)

    def visit_exp_4_DIFERENTE(self,exp_4Concrete):
      if(exp_4Concrete.exp_4):
        exp_4Concrete.exp_4.accept(self)
        print(" != ",end='', sep='')
      if(exp_4Concrete.exp_5):
        exp_4Concrete.exp_5.accept(self)

    ###

    def visit_exp_5Concrete(self,exp_5Concrete):
      if(exp_5Concrete.exp_6):
        exp_5Concrete.exp_6.accept(self)

    def visit_exp_5_MENOR_Q(self,exp_5Concrete):
      if(exp_5Concrete.exp_5):
        exp_5Concrete.exp_5.accept(self)
        print(" < ",end='', sep='')
      if(exp_5Concrete.exp_6):
        exp_5Concrete.exp_6.accept(self)

    def visit_exp_5_MAIOR_Q(self,exp_5Concrete):
      if(exp_5Concrete.exp_5):
        exp_5Concrete.exp_5.accept(self)
        print(" > ",end='', sep='')
      if(exp_5Concrete.exp_6):
        exp_5Concrete.exp_6.accept(self)

    def visit_exp_5_MAIOR_IGUAL(self,exp_5Concrete):
      if(exp_5Concrete.exp_5):
        exp_5Concrete.exp_5.accept(self)
        print(" >= ",end='', sep='')
      if(exp_5Concrete.exp_6):
        exp_5Concrete.exp_6.accept(self)

    def visit_exp_5_MENOR_IGUAL(self,exp_5Concrete):
      if(exp_5Concrete.exp_5):
        exp_5Concrete.exp_5.accept(self)
        print(" <= ",end='', sep='')
      if(exp_5Concrete.exp_6):
        exp_5Concrete.exp_6.accept(self)

    ###

    def visit_exp_6Concrete(self,exp_6Concrete):
      if(exp_6Concrete.exp_7):
        exp_6Concrete.exp_7.accept(self)

    def visit_exp_6_SOMA(self,exp_6Concrete):
      if(exp_6Concrete.exp_6):
        exp_6Concrete.exp_6.accept(self)
        print(" + ",end='', sep='')
      if(exp_6Concrete.exp_7):
        exp_6Concrete.exp_7.accept(self)

    def visit_exp_6_SUB(self,exp_6Concrete):
      if(exp_6Concrete.exp_6):
        exp_6Concrete.exp_6.accept(self)
        print(" - ",end='', sep='')
      if(exp_6Concrete.exp_7):
        exp_6Concrete.exp_7.accept(self)

    ###

    def visit_exp_7Concrete(self,exp_7Concrete):
      if(exp_7Concrete.exp_8):
        exp_7Concrete.exp_8.accept(self)

    def visit_exp_7_MULT(self,exp_7Concrete):
      if(exp_7Concrete.exp_7):
        exp_7Concrete.exp_7.accept(self)
        print(" * ",end='', sep='')
      if(exp_7Concrete.exp_8):
        exp_7Concrete.exp_8.accept(self)

    def visit_exp_7_DIV(self,exp_7Concrete):
      if(exp_7Concrete.exp_7):
        exp_7Concrete.exp_7.accept(self)
        print(" / ",end='', sep='')
      if(exp_7Concrete.exp_8):
        exp_7Concrete.exp_8.accept(self)

    def visit_exp_7_MODULO(self,exp_7Concrete):
      if(exp_7Concrete.exp_7):
        exp_7Concrete.exp_7.accept(self)
        print(" % ",end='', sep='')
      if(exp_7Concrete.exp_8):
        exp_7Concrete.exp_8.accept(self)

    ###

    def visit_exp_8Concrete(self,exp_8Concrete):
      exp_8Concrete.exp_9.accept(self)

    def visit_exp_8_SIZEOF(self,exp_8Concrete):
      print("sizeof","(",end='', sep='')
      exp_8Concrete.exp_9.accept(self)
      print(")",end='', sep='')

    def visit_exp_8_OP_NOT(self,exp_8Concrete):
      print("!",end='', sep='')
      exp_8Concrete.exp_9.accept(self)

    def visit_exp_8_NOT(self,exp_8Concrete):
      print("not ",end='', sep='')
      exp_8Concrete.exp_9.accept(self)

    def visit_exp_8_NEW(self,exp_8Concrete):
      print("new ",end='', sep='')
      exp_8Concrete.tipo.accept(self)

    def visit_exp_8_MAIS_MAIS(self,exp_8Concrete):
      exp_8Concrete.exp_9.accept(self)
      print("++",end='', sep='')

    def visit_exp_8_MENOS_MENOS(self,exp_8Concrete):
      exp_8Concrete.exp_9.accept(self)
      print("--",end='', sep='')

    ###

    def visit_exp_9Concrete(self,exp_9Concrete):
      if(exp_9Concrete.exp_10):
        exp_9Concrete.exp_10.accept(self)

    def visit_exp_9_PONTO(self,exp_9Concrete):
      if(exp_9Concrete.exp_9):
        exp_9Concrete.exp_9.accept(self)
        print(".",end='', sep='')
      if(exp_9Concrete.exp_10):
        exp_9Concrete.exp_10.accept(self)

    def visit_exp_9_SETA(self,exp_9Concrete):
      if(exp_9Concrete.exp_9):
        exp_9Concrete.exp_9.accept(self)
        print("->",end='', sep='')
      if(exp_9Concrete.exp_10):
        exp_9Concrete.exp_10.accept(self)
      
    ###

    def visit_exp_10Concrete(self,exp_10Concrete):
      print(exp_10Concrete.value,end='', sep='')

    def visit_exp_10_funcao(self,exp_10_funcao):
      exp_10_funcao.funcao.accept(self)

    def visit_exp_10_exp(self,exp_10Concrete):
      print('(',end='', sep='')
      exp_10Concrete.exp.accept(self)
      print(')',end='', sep='')
      
    ###

    def visit_chamada_funcaoConcrete(self, chamada_funcaoConcrete):
      print(chamada_funcaoConcrete.id, "(",end='', sep='')
      if(chamada_funcaoConcrete.parametros_chamada):
        chamada_funcaoConcrete.parametros_chamada.accept(self)
      print(")",end='', sep='')

    def visit_chamada_funcaoTypeid(self, chamada_funcaoTypeid):
      print(chamada_funcaoTypeid.typeid, "(",end='', sep='')
      chamada_funcaoTypeid.exp.accept(self)
      print(")",end='', sep='')

    def visit_parametros_chamadaConcrete(self, parametros_chamadaConcrete):
      parametros_chamadaConcrete.id.accept(self)
      if(parametros_chamadaConcrete.parametros_chamada):
        print(",",end='', sep='')
        parametros_chamadaConcrete.parametros_chamada.accept(self)
      
    ###

    def visit_condicional_1_IF(self, condicional_1_IF):
      print(condicional_1_IF.IF, "(",end='', sep='')
      condicional_1_IF.exp.accept(self)
      print(")",end='', sep='')
      condicional_1_IF.rest_if.accept(self)

    def visit_condicional_1_WHILE(self, condicional_1_WHILE):
      print(condicional_1_WHILE.WHILE, "(",end='', sep='')
      condicional_1_WHILE.exp.accept(self)
      print(")",end='', sep='')
      if(condicional_1_WHILE.body):
        condicional_1_WHILE.body.accept(self)

    def visit_condicional_1_FOR(self, condicional_1_FOR):
      print(condicional_1_FOR.FOR, "(",end='', sep='')
      condicional_1_FOR.for_log.accept(self)
      print(")",end='', sep='')
      if(condicional_1_FOR.body):
        condicional_1_FOR.body.accept(self)

    def visit_condicional_1_RETURN(self, condicional_1_RETURN):
      print(condicional_1_RETURN.RETURN," ",end='', sep='')
      if(condicional_1_RETURN.exp):
        condicional_1_RETURN.exp.accept(self)
      print(";",end='', sep='')

    def visit_condicional_1_EXP(self, condicional_1_EXP):
      condicional_1_EXP.exp.accept(self)
      print(";",end='', sep='')

    def visit_condicional_1_decl_variavel(self, condicional_1_decl_variavel):
      condicional_1_decl_variavel.decl_variavel.accept(self)

    def visit_condicional_1_typedef(self, condicional_1_typedef):
      condicional_1_typedef.typedef.accept(self)

    def visit_condicional_1_using(self, condicional_1_using):
      condicional_1_using.using.accept(self)
        
    ###

    def visit_condicional_2Concrete(self, condicional_2Concrete):
      print(condicional_2Concrete.IF, "(",end='', sep='')
      condicional_2Concrete.exp.accept(self)
      print(")\n",end='', sep='')
      if(condicional_2Concrete.body):
        condicional_2Concrete.body.accept(self)
      else:
        print("{ }",end='', sep='')
    
    def visit_condicional_2Concrete_2(self, condicional_2Concrete_2):
      print(condicional_2Concrete_2.IF, "(" ,end='', sep='')
      condicional_2Concrete_2.exp.accept(self)
      print(")\n",end='', sep='')
      if(condicional_2Concrete_2.body):
        condicional_2Concrete_2.body.accept(self)
      print(condicional_2Concrete_2.ELSE, "\n",end='', sep='')
      condicional_2Concrete_2.condicional_2.accept(self)
      
    ###

    def visit_rest_ifConcrete(self, rest_ifConcrete):
      rest_ifConcrete.body_1.accept(self)
      print(rest_ifConcrete.ELSE, "\n",end='', sep='')
      rest_ifConcrete.body_2.accept(self)
      
    ###

    def visit_for_logConcrete(self, for_logConcrete):
      if(for_logConcrete.decl_variavel):
        if(isinstance(for_logConcrete.decl_variavel,sa.exp)):
          for_logConcrete.decl_variavel.accept(self)
          print(";",end='', sep='')
        else:
          for_logConcrete.decl_variavel.accept(self)
      else:
        print(";",end='', sep='')
      if(for_logConcrete.exp_1):
        for_logConcrete.exp_1.accept(self)
      print(";",end='', sep='')
      if(for_logConcrete.exp_2):
        for_logConcrete.exp_2.accept(self)
      
    ###

    def visit_tipoConcrete(self, tipoConcrete):
      print(tipoConcrete.tipo_v,end='', sep='')

    ###

    def visit_usingConcrete(self, usingConcrete):
      print(usingConcrete.using, ' ', usingConcrete.id1, ' ', usingConcrete.id2, ';','\n' , end='', sep='')

    def visit_usingConcrete1(self, usingConcrete1):
      print(usingConcrete1.using, ' ', usingConcrete1.id1, '::', usingConcrete1.id2, ';' , '\n' , end='', sep='')

    ###
    def visit_typedefConcrete(self, typedefConcrete):
      print(typedefConcrete.typedef,' ', end='', sep='')
      typedefConcrete.tipo.accept(self)      
      print(' ', typedefConcrete.id, ';', '\n' , end='', sep='')

    def visit_typedefConcrete1(self, typedefConcrete1):
      print(typedefConcrete1.typedef,' ', end='', sep='')
      typedefConcrete1.tipo.accept(self)      
      print(' ', typedefConcrete1.id, end='', sep='')
      typedefConcrete1.decl_typedef_n.accept(self)
      print(';', '\n' , end='', sep='')

    ###
    def visit_decl_typedef_nConcrete(self, decl_typedef_nConcrete):
      print(',', decl_typedef_nConcrete.id, end='', sep='')

    def visit_decl_typedef_nConcrete1(self, decl_typedef_nConcrete1):
      print(',', decl_typedef_nConcrete1.id, end='', sep='')
      if(decl_typedef_nConcrete1.decl_typedef_n):
        decl_typedef_nConcrete1.decl_typedef_n.accept(self)
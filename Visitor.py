from visitor_abstract import visitor_abstract

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
      print(parametrosConcrete.id ,end='', sep='')
      if(parametrosConcrete.parametros):
        print(",", end='', sep='')
        parametrosConcrete.parametros.accept(self)

    ###

    def visit_decl_variavelConcrete(self, decl_variavelConcrete):
      decl_variavelConcrete.tipo.accept(self)
      print(decl_variavelConcrete.id,end='', sep='')
      if(decl_variavelConcrete.exp):
        print(" = ",end='', sep='')
        decl_variavelConcrete.exp.accept(self)
      if(decl_variavelConcrete.decl_variavel_n):
        decl_variavelConcrete.decl_variavel_n.accept(self)
      print(";",end='', sep='')
        
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
      print('{',end='', sep='')
      if(bodyConcrete.comandos):
        bodyConcrete.comandos.accept(self)
      print('}',end='', sep='')

    ###

    def visit_expConcrete(self, expConcrete):
      if(expConcrete.exp):
        expConcrete.exp.accept(self)
        print("=",end='', sep='')
      if(expConcrete.exp_1):
        expConcrete.exp_1.accept(self)

    ###

    def visit_exp_1Concrete(self,exp_1Concrete):
      if(exp_1Concrete.exp_1):
        exp_1Concrete.exp_1.accept(self)
        print("OR",end='', sep='')
      if(exp_1Concrete.exp_2):
        exp_1Concrete.exp_2.accept(self)

    ###

    def visit_exp_2Concrete(self,exp_2Concrete):
      if(exp_2Concrete.exp_2):
        exp_2Concrete.exp_2.accept(self)
        print("AND",end='', sep='')
      if(exp_2Concrete.exp_3):
        exp_2Concrete.exp_3.accept(self)
    
    ###

    def visit_exp_3Concrete(self,exp_3Concrete):
      if(exp_3Concrete.exp_3):
        exp_3Concrete.exp_3.accept(self)
        print("XOR",end='', sep='')
      if(exp_3Concrete.exp_4):
        exp_3Concrete.exp_4.accept(self)

    ###

    def visit_exp_4Concrete(self,exp_4Concrete):
      if(exp_4Concrete.exp_4):
        exp_4Concrete.exp_4.accept(self)
        print("==",end='', sep='')
      if(exp_4Concrete.exp_5):
        exp_4Concrete.exp_5.accept(self)

      ###

    def visit_exp_5Concrete(self,exp_5Concrete):
      if(exp_5Concrete.exp_5):
        exp_5Concrete.exp_5.accept(self)
        print("<",end='', sep='')
      if(exp_5Concrete.exp_6):
        exp_5Concrete.exp_6.accept(self)

      ###

    def visit_exp_6Concrete(self,exp_6Concrete):
      if(exp_6Concrete.exp_6):
        exp_6Concrete.exp_6.accept(self)
        print("+",end='', sep='')
      if(exp_6Concrete.exp_7):
        exp_6Concrete.exp_7.accept(self)

      ###

    def visit_exp_7Concrete(self,exp_7Concrete):
      if(exp_7Concrete.exp_7):
        exp_7Concrete.exp_7.accept(self)
        print("*",end='', sep='')
      if(exp_7Concrete.exp_8):
        exp_7Concrete.exp_8.accept(self)

      ###

    def visit_exp_8Concrete(self,exp_8Concrete):
      exp_8Concrete.exp_9.accept(self)

      ###

    def visit_exp_9Concrete(self,exp_9Concrete):
      if(exp_9Concrete.exp_9):
        exp_9Concrete.exp_9.accept(self)
        print(".",end='', sep='')
      if(exp_9Concrete.exp_10):
        exp_9Concrete.exp_10.accept(self)
      
    ###

    def visit_exp_10Concrete(self,exp_10Concrete):
      print(exp_10Concrete.value,end='', sep='')
      
    ###

    def visit_tipoConcrete(self, tipoConcrete):
      print(tipoConcrete.tipo_v, ' ',end='', sep='')
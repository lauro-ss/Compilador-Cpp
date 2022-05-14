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
      print(decl_variavelConcrete.id,';',end='', sep='')
      ## definir visitor exp
      if(decl_variavelConcrete.exp):
        decl_variavelConcrete.exp.accept(self)
        
    ###

    def visit_decl_variavel_nConcrete(self, decl_variavel_nConcrete):
      pass

    ###

    def visit_bodyConcrete(self, bodyConcrete):
      print('{',end='', sep='')
      #bodyConcrete.comandos.accept(self)
      print('}',end='', sep='')

    ###

    def visit_tipoConcrete(self, tipoConcrete):
      print(tipoConcrete.tipo_v, ' ',end='', sep='')
from abc import abstractmethod
from abc import ABCMeta
from Visitor import Visitor

class cpp(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class cppConcrete(cpp):
  def __init__(self, decl, recursao):
    self.decl = decl
    self.recursao = recursao
    
  def accept(self, visitor):
    return visitor.visit_cppConcrete(self)

###
###

class decl_classe(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class decl_classeConcrete(decl_classe):
     def __init__(self, Class, id, body_class):
       self.Class = Class
       self.id = id
       self.body_class = body_class
       
     def accept(self, visitor):
        return visitor.visit_decl_classeConcrete(self)


###
###
       
class body_class(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class body_classConcrete(body_class):
    def __init__(self, public, content_class):
      self.public = public
      self.content_class = content_class
      
    def accept(self, visitor):
      return visitor.visit_body_classConcrete(self)
      
###
###

class content_class(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class content_classConcrete(content_class):
    def __init__(self, static, decl, recursao):
      self.static = static
      self.decl = decl
      self.recursao = recursao
    
    def accept(self, visitor):
      return visitor.visit_decl_classeConcrete(self)
        
###
###

class decl_funcao(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class decl_funcaoConcrete(decl_funcao):
    def __init__(self, tipo, id, parametros, body):
      self.tipo = tipo
      self.id = id
      self.parametros = parametros
      self.body = body
    def accept(self, visitor):
      return visitor.visit_decl_funcaoConcrete(self)

###
###

class parametros(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class parametrosConcrete(parametros):
    def __init__():
      ''''''
    def accept(self, visitor):
      return visitor.visit_parametrosConcrete(self)
###
###

class decl_variavel(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class decl_variavelConcrete(decl_variavel):
    def __init__():
      ''''''
    def accept(self, visitor):
      return visitor.visit_decl_variavelConcrete(self)
###
###

class decl_variavel_n(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass
      
class decl_variavel_nConcrete(decl_variavel_n):
    def __init__():
      ''''''
    def accept(self, visitor):
      return visitor.visit_decl_variavel_nConcrete(self)
###
###

class typedef(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class typedefConcrete(typedef):
    def __init__():
      ''''''
    def accept(self, visitor):
      return visitor.visit_typedefConcrete(self)
###
###

class decl_typedef_n(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class decl_typedef_nConcrete(decl_typedef_n):
    def __init__():
      ''''''
    def accept(self, visitor):
      return visitor.visit_decl_typedef_nConcrete(self)
###
###

class using(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class usingConcrete(using):
    def __init__():
      ''''''
    def accept(self, visitor):
      return visitor.visit_usingConcrete(self)
###
###

class body(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class bodyConcrete(body):
    def __init__():
      ''''''
    def accept(self, visitor):
      return visitor.visit_bodyConcrete(self)
###
###

class comandos(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class comandosConcrete(comandos):
    def __init__():
      ''''''
    def accept(self, visitor):
      return visitor.visit_comandosConcrete(self)
###
###

class comando(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class comandoConcrete(comando):
    def __init__():
      ''''''
    def accept(self, visitor):
      return visitor.visit_comandoConcrete(self)
###
###

class exp(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class expConcrete(exp):
    def __init__():
      ''''''
    def accept(self, visitor):
      return visitor.visit_expConcrete(self)
###
###

class exp_1(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class exp_1Concrete(exp_1):
    def __init__():
      ''''''
    def accept(self, visitor):
      return visitor.visit_exp_1Concrete(self)
###
###

class exp_2(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class exp_2Concrete(exp_2):
    def __init__():
      ''''''
    def accept(self, visitor):
      return visitor.visit_exp_2Concrete(self)
###
###

class exp_3(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class exp_3Concrete(exp_3):
    def __init__():
      ''''''
    def accept(self, visitor):
      return visitor.visit_exp_3Concrete(self)
###
###

class exp_4(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class exp_4Concrete(exp_4):
    def __init__():
      ''''''
    def accept(self, visitor):
      return visitor.visit_exp_4Concrete(self)
###
###

class exp_5(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class exp_5Concrete(exp_5):
    def __init__():
      ''''''
    def accept(self, visitor):
      return visitor.visit_exp_5Concrete(self)
###
###

class exp_6(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class exp_6Concrete(exp_6):
    def __init__():
      ''''''
    def accept(self, visitor):
      return visitor.visit_exp_6Concrete(self)
###
###

class exp_7(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class exp_7Concrete(exp_7):
    def __init__():
      ''''''
    def accept(self, visitor):
      return visitor.visit_exp_7Concrete(self)
###
###
      
class exp_8(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class exp_8Concrete(exp_8):
    def __init__():
      ''''''
    def accept(self, visitor):
      return visitor.visit_exp_8Concrete(self)
###
###

class exp_9(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class exp_9Concrete(exp_9):
    def __init__():
      ''''''
    def accept(self, visitor):
      return visitor.visit_exp_9Concrete(self)
###
###

class exp_10(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class exp_10Concrete(exp_10):
    def __init__():
      ''''''
    def accept(self, visitor):
      return visitor.visit_exp_10Concrete(self)
###
###

class chamada_funcao(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class chamada_funcaoConcrete(chamada_funcao):
    def __init__():
      ''''''
    def accept(self, visitor):
      return visitor.visit_chamada_funcaoConcrete(self)
###
###

class condicional_1(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class condicional_1Concrete(condicional_1):
    def __init__():
      ''''''
    def accept(self, visitor):
      return visitor.visit_condicional_1Concrete(self)
###
###

class condicional_2(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class condicional_2Concrete(condicional_2):
    def __init__():
      ''''''
    def accept(self, visitor):
      return visitor.visit_condicional_2Concrete(self)
###
###

class rest_if(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class rest_ifConcrete(rest_if):
    def __init__():
      ''''''
    def accept(self, visitor):
      return visitor.visit_rest_ifConcrete(self)
###
###

class for_log(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class for_logConcrete(for_log):
    def __init__():
      ''''''
    def accept(self, visitor):
      return visitor.visit_for_logConcrete(self)
###
###

class tipo(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class tipoConcrete(tipo):
    def __init__():
      ''''''
    def accept(self, visitor):
      return visitor.visit_tipoConcrete(self)
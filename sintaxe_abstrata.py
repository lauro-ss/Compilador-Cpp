from abc import abstractmethod
from abc import ABCMeta
from Visitor import Visitor

class cpp(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class cppConcrete(cpp):
  def __init__(self, decl, cpp):
    self.decl = decl
    self.cpp = cpp
    
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
    def __init__(self, static, decl, content_class):
      self.static = static
      self.decl = decl
      self.content_class = content_class
    
    def accept(self, visitor):
      return visitor.visit_content_classConcrete(self)
        
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
    def __init__(self, tipo, id, parametros):
      self.tipo = tipo
      self.id = id
      self.parametros = parametros
    def accept(self, visitor):
      return visitor.visit_parametrosConcrete(self)
###
###

class decl_variavel(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class decl_variavelConcrete(decl_variavel):
    def __init__(self, tipo, id, exp, decl_variavel_n):
      self.tipo = tipo
      self.id = id
      self.exp = exp
      self.decl_variavel_n = decl_variavel_n
      
    def accept(self, visitor):
      return visitor.visit_decl_variavelConcrete(self)
###
###

class decl_variavel_n(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass
      
class decl_variavel_nConcrete(decl_variavel_n):
    def __init__(self, id, exp, decl_variavel_n):
      self.id = id
      self.exp = exp
      self.decl_variavel_n = decl_variavel_n
      
    def accept(self, visitor):
      return visitor.visit_decl_variavel_nConcrete(self)

###
###

class typedef(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class typedefConcrete(typedef):
    def __init__(self, typedef, tipo, id):
      self.typedef = typedef
      self.tipo = tipo
      self.id = id
      
    def accept(self, visitor):
      return visitor.visit_typedefConcrete(self)

class typedefConcrete1(typedef):
    def __init__(self, typedef, tipo, id, decl_typedef_n):
      self.typedef = typedef
      self.tipo = tipo
      self.id = id
      self.decl_typedef_n = decl_typedef_n
      
    def accept(self, visitor):
      return visitor.visit_typedefConcrete1(self)
###
###

class decl_typedef_n(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class decl_typedef_nConcrete(decl_typedef_n):
    def __init__(self, id):
      self.id = id
      
    def accept(self, visitor):
      return visitor.visit_decl_typedef_nConcrete(self)

class decl_typedef_nConcrete1(decl_typedef_n):
    def __init__(self, id, decl_typedef_n):
      self.id = id
      self.decl_typedef_n = decl_typedef_n
      
    def accept(self, visitor):
      return visitor.visit_decl_typedef_nConcrete1(self)
###
###

class using(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class usingConcrete(using):
    def __init__(self, using, id1, id2):
      self.using = using
      self.id1 = id1
      self.id2 = id2
      
    def accept(self, visitor):
      return visitor.visit_usingConcrete(self)
      
class usingConcrete1(using):
    def __init__(self, using, id1, id2):
      self.using = using
      self.id1 = id1
      self.id2 = id2
      
    def accept(self, visitor):
      return visitor.visit_usingConcrete1(self)
      
###
###

class body(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class bodyConcrete(body):
    def __init__(self, comandos):
      self.comandos = comandos
      
    def accept(self, visitor):
      return visitor.visit_bodyConcrete(self)
###
###

class comandos(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class comandosConcrete(comandos):
    def __init__(self, comando, comandos):
      self.comando = comando
      self.comandos = comandos
    def accept(self, visitor):
      return visitor.visit_comandosConcrete(self)
###
###

class comando(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class comandoConcrete(comando):
    def __init__(self, condicional):
      self.condicional = condicional
    def accept(self, visitor):
      return visitor.visit_comandoConcrete(self)
###
###

class exp(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class expConcrete(exp):
    def __init__(self, exp, exp_1):
      self.exp = exp
      self.exp_1 = exp_1
      
    def accept(self, visitor):
      return visitor.visit_expConcrete(self)
###
###

class exp_1(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class exp_1Concrete(exp_1):
    def __init__(self, exp_2):
      self.exp_2 = exp_2
      
    def accept(self, visitor):
      return visitor.visit_exp_1Concrete(self)


class exp_1_OP_OU(exp_1):
    def __init__(self, exp_1, exp_2):
      self.exp_1 = exp_1
      self.exp_2 = exp_2
      
    def accept(self, visitor):
      return visitor.visit_exp_1_OP_OU(self)


class exp_1_OR(exp_1):
    def __init__(self, exp_1, exp_2):
      self.exp_1 = exp_1
      self.exp_2 = exp_2
      
    def accept(self, visitor):
      return visitor.visit_exp_1_OR(self)
      
###
###

class exp_2(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class exp_2Concrete(exp_2):
    def __init__(self, exp_3):
      self.exp_3 = exp_3
      
    def accept(self, visitor):
      return visitor.visit_exp_2Concrete(self)

class exp_2_OP_E(exp_2):
    def __init__(self, exp_2, exp_3):
      self.exp_2 = exp_2
      self.exp_3 = exp_3
      
    def accept(self, visitor):
      return visitor.visit_exp_2_OP_E(self)

class exp_2_AND(exp_2):
    def __init__(self, exp_2, exp_3):
      self.exp_2 = exp_2
      self.exp_3 = exp_3
      
    def accept(self, visitor):
      return visitor.visit_exp_2_AND(self)
###
###

class exp_3(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class exp_3Concrete(exp_3):
    def __init__(self, exp_4):
      self.exp_4 = exp_4
    def accept(self, visitor):
      return visitor.visit_exp_3Concrete(self)

class exp_3_XOR(exp_3):
    def __init__(self, exp_3, exp_4):
      self.exp_3 = exp_3
      self.exp_4 = exp_4
    def accept(self, visitor):
      return visitor.visit_exp_3_XOR(self)

class exp_3_OP_OU_EX(exp_3):
    def __init__(self, exp_3, exp_4):
      self.exp_3 = exp_3
      self.exp_4 = exp_4
    def accept(self, visitor):
      return visitor.visit_exp_3_OP_OU_EX(self)
###
###

class exp_4(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class exp_4Concrete(exp_4):
    def __init__(self, exp_5):
      self.exp_5 = exp_5
      
    def accept(self, visitor):
      return visitor.visit_exp_4Concrete(self)

class exp_4_IGUAL(exp_4):
    def __init__(self, exp_4, exp_5):
      self.exp_4 = exp_4
      self.exp_5 = exp_5
    def accept(self, visitor):
      return visitor.visit_exp_4_IGUAL(self)

class exp_4_DIFERENTE(exp_4):
    def __init__(self, exp_4, exp_5):
      self.exp_4 = exp_4
      self.exp_5 = exp_5
    def accept(self, visitor):
      return visitor.visit_exp_4_DIFERENTE(self)
###
###

class exp_5(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class exp_5Concrete(exp_5):
    def __init__(self, exp_5, exp_6):
      self.exp_6 = exp_6
      
    def accept(self, visitor):
      return visitor.visit_exp_5Concrete(self)

class exp_5_MENOR_Q(exp_5):
    def __init__(self, exp_5, exp_6):
      self.exp_5 = exp_5
      self.exp_6 = exp_6
    def accept(self, visitor):
      return visitor.visit_exp_5_MENOR_Q(self)

class exp_5_MAIOR_Q(exp_5):
    def __init__(self, exp_5, exp_6):
      self.exp_5 = exp_5
      self.exp_6 = exp_6
    def accept(self, visitor):
      return visitor.visit_exp_5_MAIOR_Q(self)

class exp_5_MAIOR_IGUAL(exp_5):
    def __init__(self, exp_5, exp_6):
      self.exp_5 = exp_5
      self.exp_6 = exp_6
    def accept(self, visitor):
      return visitor.visit_exp_5_MAIOR_IGUAL(self)

class exp_5_MENOR_IGUAL(exp_5):
    def __init__(self, exp_5, exp_6):
      self.exp_5 = exp_5
      self.exp_6 = exp_6
    def accept(self, visitor):
      return visitor.visit_exp_5_MENOR_IGUAL(self)
      
###
###

class exp_6(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class exp_6Concrete(exp_6):
    def __init__(self, exp_7):
      self.exp_7 = exp_7
      
    def accept(self, visitor):
      return visitor.visit_exp_6Concrete(self)

class exp_6_SOMA(exp_6):
    def __init__(self, exp_6, exp_7):
      self.exp_6 = exp_6
      self.exp_7 = exp_7
    def accept(self, visitor):
      return visitor.visit_exp_6_SOMA(self)

class exp_6_SUB(exp_6):
    def __init__(self, exp_6, exp_7):
      self.exp_6 = exp_6
      self.exp_7 = exp_7
    def accept(self, visitor):
      return visitor.visit_exp_6_SUB(self)
###
###

class exp_7(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class exp_7Concrete(exp_7):
    def __init__(self, exp_8):
      self.exp_8 = exp_8
      
    def accept(self, visitor):
      return visitor.visit_exp_7Concrete(self)

class exp_7_MULT(exp_7):
    def __init__(self, exp_7, exp_8):
      self.exp_7 = exp_7
      self.exp_8 = exp_8
    def accept(self, visitor):
      return visitor.visit_exp_7_MULT(self)

class exp_7_DIV(exp_7):
    def __init__(self, exp_7, exp_8):
      self.exp_7 = exp_7
      self.exp_8 = exp_8
    def accept(self, visitor):
      return visitor.visit_exp_7_DIV(self)

class exp_7_MODULO(exp_7):
    def __init__(self, exp_7, exp_8):
      self.exp_7 = exp_7
      self.exp_8 = exp_8
    def accept(self, visitor):
      return visitor.visit_exp_7_MODULO(self)
###
###
      
class exp_8(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class exp_8Concrete(exp_8):
    def __init__(self, exp_9):
      self.exp_9 = exp_9
    def accept(self, visitor):
      return visitor.visit_exp_8Concrete(self)

class exp_8_SIZEOF(exp_8):
    def __init__(self, sizeof, exp_9):
      self.sizeof = sizeof
      self.exp_9 = exp_9
    def accept(self, visitor):
      return visitor.visit_exp_8_SIZEOF(self)

class exp_8_OP_NOT(exp_8):
    def __init__(self, exp_9):
      self.exp_9 = exp_9
    def accept(self, visitor):
      return visitor.visit_exp_8_OP_NOT(self)

class exp_8_NOT(exp_8):
    def __init__(self, exp_9):
      self.exp_9 = exp_9
    def accept(self, visitor):
      return visitor.visit_exp_8_NOT(self)

class exp_8_NEW(exp_8):
    def __init__(self, tipo):
      self.tipo = tipo
    def accept(self, visitor):
      return visitor.visit_exp_8_NEW(self)

class exp_8_MAIS_MAIS(exp_8):
    def __init__(self, exp_9):
      self.exp_9 = exp_9
    def accept(self, visitor):
      return visitor.visit_exp_8_MAIS_MAIS(self)

class exp_8_MENOS_MENOS(exp_8):
    def __init__(self, exp_9):
      self.exp_9 = exp_9
    def accept(self, visitor):
      return visitor.visit_exp_8_MENOS_MENOS(self)
###
###

class exp_9(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class exp_9Concrete(exp_9):
    def __init__(self, exp_10):
      self.exp_10 = exp_10
      
    def accept(self, visitor):
      return visitor.visit_exp_9Concrete(self)

class exp_9_PONTO(exp_9):
    def __init__(self, exp_9, exp_10):
      self.exp_9 = exp_9
      self.exp_10 = exp_10
    def accept(self, visitor):
      return visitor.visit_exp_9_PONTO(self)

class exp_9_SETA(exp_9):
    def __init__(self, exp_9, exp_10):
      self.exp_9 = exp_9
      self.exp_10 = exp_10
    def accept(self, visitor):
      return visitor.visit_exp_9_SETA(self)
###
###

class exp_10(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class exp_10Concrete(exp_10):
    def __init__(self, value):
      self.value = value
      
    def accept(self, visitor):
      return visitor.visit_exp_10Concrete(self)

class exp_10_funcao(exp_10):
    def __init__(self, funcao):
      self.funcao = funcao
      
    def accept(self, visitor):
      return visitor.visit_exp_10_funcao(self)

class exp_10_exp(exp_10):
    def __init__(self, exp):
      self.exp = exp
      
    def accept(self, visitor):
      return visitor.visit_exp_10_exp(self)
###
###

class chamada_funcao(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class chamada_funcaoConcrete(chamada_funcao):
    def __init__(self, id, parametros_chamada):
      self.id = id
      self.parametros_chamada = parametros_chamada
    def accept(self, visitor):
      return visitor.visit_chamada_funcaoConcrete(self)

class chamada_funcaoTypeid(chamada_funcao):
    def __init__(self, typeid, exp):
      self.typeid = typeid
      self.exp = exp
    def accept(self, visitor):
      return visitor.visit_chamada_funcaoTypeid(self)

###
###

class parametros_chamada(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class parametros_chamadaConcrete(parametros_chamada):
    def __init__(self, id, parametros_chamada):
      self.id = id
      self.parametros_chamada = parametros_chamada
    def accept(self, visitor):
      return visitor.visit_parametros_chamadaConcrete(self)
      
###
###

class condicional_1(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class condicional_1_IF(condicional_1):
    def __init__(self, IF, exp , rest_if):
      self.IF = IF
      self.exp = exp
      self.rest_if = rest_if
    def accept(self, visitor):
      return visitor.visit_condicional_1_IF(self)

class condicional_1_WHILE(condicional_1):
    def __init__(self, WHILE, exp, body):
      self.WHILE = WHILE
      self.exp = exp
      self.body = body
    def accept(self, visitor):
      return visitor.visit_condicional_1_WHILE(self)

class condicional_1_FOR(condicional_1):
    def __init__(self, FOR, for_log, body):
      self.FOR = FOR
      self.for_log = for_log
      self.body = body
    def accept(self, visitor):
      return visitor.visit_condicional_1_FOR(self)

class condicional_1_RETURN(condicional_1):
    def __init__(self, RETURN, exp):
      self.RETURN = RETURN
      self.exp = exp
    def accept(self, visitor):
      return visitor.visit_condicional_1_RETURN(self)

class condicional_1_EXP(condicional_1):
    def __init__(self, exp):
      self.exp = exp
    def accept(self, visitor):
      return visitor.visit_condicional_1_EXP(self)

class condicional_1_decl_variavel(condicional_1):
    def __init__(self, decl_variavel):
      self.decl_variavel = decl_variavel
      
    def accept(self, visitor):
      return visitor.visit_condicional_1_decl_variavel(self)

class condicional_1_typedef(condicional_1):
    def __init__(self, typedef):
      self.typedef = typedef
      
    def accept(self, visitor):
      return visitor.visit_condicional_1_typedef(self)

class condicional_1_using(condicional_1):
    def __init__(self, using):
      self.using = using
      
    def accept(self, visitor):
      return visitor.visit_condicional_1_using(self)
###
###

class condicional_2(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class condicional_2Concrete(condicional_2):
    def __init__(self, IF, exp, body):
      self.IF = IF
      self.exp = exp
      self.body = body
    def accept(self, visitor):
      return visitor.visit_condicional_2Concrete(self)

class condicional_2Concrete_2(condicional_2):
    def __init__(self, IF, exp, body, ELSE, condicional_2):
      self.IF = IF
      self.exp = exp
      self.body = body
      self.ELSE = ELSE
      self.condicional_2 = condicional_2
    def accept(self, visitor):
      return visitor.visit_condicional_2Concrete_2(self)
###
###

class rest_if(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class rest_ifConcrete(rest_if):
    def __init__(self, body_1, ELSE, body_2):
      self.body_1 = body_1
      self.ELSE = ELSE
      self.body_2 = body_2
    def accept(self, visitor):
      return visitor.visit_rest_ifConcrete(self)
###
###

class for_log(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class for_logConcrete(for_log):
    def __init__(self, decl_variavel, exp_1, exp_2):
      self.decl_variavel = decl_variavel
      self.exp_1 = exp_1
      self.exp_2 = exp_2
    def accept(self, visitor):
      return visitor.visit_for_logConcrete(self)
###
###

class tipo(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class tipoConcrete(tipo):
    def __init__(self, tipo_v):
      self.tipo_v = tipo_v
    def accept(self, visitor):
      return visitor.visit_tipoConcrete(self)
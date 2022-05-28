from abc import abstractmethod
from abc import ABCMeta

class visitor_abstract(metaclass=ABCMeta):

    @abstractmethod
    def visit_cppConcrete(self, cppConcrete):
        pass
    
    @abstractmethod
    def visit_decl_classeConcrete(self, decl_classeConcrete):
        pass

    @abstractmethod
    def visit_body_classConcrete(self, body_classConcrete):
        pass

    @abstractmethod
    def visit_content_classConcrete(self, content_classConcrete):
      pass

    @abstractmethod
    def visit_decl_funcaoConcrete(self, decl_funcaoConcrete):
      pass

    @abstractmethod
    def visit_parametrosConcrete(self, parametrosConcrete):
      pass

    @abstractmethod
    def visit_decl_variavelConcrete(self, decl_variavelConcrete):
      pass

    @abstractmethod
    def visit_decl_variavel_nConcrete(self, decl_variavel_nConcrete):
      pass

    @abstractmethod
    def visit_bodyConcrete(self, bodyConcrete):
      pass

    @abstractmethod
    def visit_comandosConcrete(self, comandosConcrete):
      pass

    @abstractmethod
    def visit_comandoConcrete(self, comandoConcrete):
      pass

    @abstractmethod
    def visit_expConcrete(self, expConcrete):
      pass

    @abstractmethod
    def visit_exp_1_OR(self,exp_1Concrete):
      pass

    @abstractmethod
    def visit_exp_1_OP_OU(self,exp_1Concrete):
      pass

    @abstractmethod
    def visit_exp_1Concrete(self,exp_1Concrete):
      pass

    @abstractmethod
    def visit_exp_2_AND(self,exp_2Concrete):
      pass

    @abstractmethod
    def visit_exp_2_OP_E(self,exp_2Concrete):
      pass

    @abstractmethod
    def visit_exp_2Concrete(self,exp_2Concrete):
      pass

    @abstractmethod
    def visit_exp_3_XOR(self,exp_3Concrete):
      pass

    @abstractmethod
    def visit_exp_3_OP_OU_EX(self,exp_3Concrete):
      pass

    @abstractmethod
    def visit_exp_3Concrete(self,exp_3Concrete):
      pass

    @abstractmethod
    def visit_exp_4Concrete(self,exp_4Concrete):
      pass

    @abstractmethod
    def visit_exp_4_IGUAL(self,exp_4Concrete):
      pass

    @abstractmethod
    def visit_exp_4_DIFERENTE(self,exp_4Concrete):
      pass

    @abstractmethod
    def visit_exp_5Concrete(self,exp_5Concrete):
      pass

    @abstractmethod
    def visit_exp_5_MENOR_Q(self,exp_5Concrete):
      pass

    @abstractmethod
    def visit_exp_5_MAIOR_Q(self,exp_5Concrete):
      pass

    @abstractmethod
    def visit_exp_5_MAIOR_IGUAL(self,exp_5Concrete):
      pass

    @abstractmethod
    def visit_exp_5_MENOR_IGUAL(self,exp_5Concrete):
      pass

    @abstractmethod
    def visit_exp_6Concrete(self,exp_6Concrete):
      pass

    @abstractmethod
    def visit_exp_6_SOMA(self,exp_6Concrete):
      pass

    @abstractmethod
    def visit_exp_6_SUB(self,exp_6Concrete):
      pass

    @abstractmethod
    def visit_exp_7Concrete(self,exp_7Concrete):
      pass

    @abstractmethod
    def visit_exp_7_MULT(self,exp_7Concrete):
      pass

    @abstractmethod
    def visit_exp_7_DIV(self,exp_7Concrete):
      pass

    @abstractmethod
    def visit_exp_7_MODULO(self,exp_7Concrete):
      pass

    @abstractmethod
    def visit_exp_8Concrete(self,exp_8Concrete):
      pass

    @abstractmethod
    def visit_exp_8_SIZEOF(self,exp_8Concrete):
      pass

    @abstractmethod
    def visit_exp_8_OP_NOT(self,exp_8Concrete):
      pass

    @abstractmethod
    def visit_exp_8_NOT(self,exp_8Concrete):
      pass

    @abstractmethod
    def visit_exp_8_NEW(self,exp_8Concrete):
      pass

    @abstractmethod
    def visit_exp_8_MAIS_MAIS(self,exp_8Concrete):
      pass

    @abstractmethod
    def visit_exp_8_MENOS_MENOS(self,exp_8Concrete):
      pass

    @abstractmethod
    def visit_exp_9Concrete(self,exp_9Concrete):
      pass

    @abstractmethod
    def visit_exp_9_PONTO(self,exp_9Concrete):
      pass

    @abstractmethod
    def visit_exp_9_SETA(self,exp_9Concrete):
      pass

    @abstractmethod
    def visit_exp_10Concrete(self,exp_10Concrete):
      pass

    @abstractmethod
    def visit_exp_10_funcao(self,exp_10_funcao):
      pass

    @abstractmethod
    def visit_exp_10_exp(self,exp_10Concrete):
      pass

    @abstractmethod
    def visit_chamada_funcaoConcrete(self, chamada_funcaoConcrete):
      pass

    @abstractmethod
    def visit_chamada_funcaoTypeid(self, chamada_funcaoTypeid):
      pass

    @abstractmethod
    def visit_parametros_chamadaConcrete(self, parametros_chamadaConcrete):
      pass

    @abstractmethod
    def visit_condicional_1_IF(self, condicional_1_IF):
      pass

    @abstractmethod
    def visit_condicional_1_WHILE(self, condicional_1_WHILE):
      pass

    @abstractmethod
    def visit_condicional_1_FOR(self, condicional_1_FOR):
      pass

    @abstractmethod
    def visit_condicional_1_RETURN(self, condicional_1_RETURN):
      pass

    @abstractmethod
    def visit_condicional_1_EXP(self, condicional_1_EXP):
      pass

    @abstractmethod
    def visit_condicional_1_decl_variavel(self, condicional_1_decl_variavel):
      pass

    @abstractmethod
    def visit_condicional_1_typedef(self, condicional_1_typedef):
      pass
      
    @abstractmethod
    def visit_condicional_1_using(self, condicional_1_using):
      pass

    @abstractmethod
    def visit_condicional_2Concrete(self, condicional_2Concrete):
      pass

    @abstractmethod
    def visit_condicional_2Concrete_2(self, condicional_2Concrete_2):
      pass

    @abstractmethod
    def visit_rest_ifConcrete(self, rest_ifConcrete):
      pass

    @abstractmethod
    def visit_for_logConcrete(self, for_logConcrete):
      pass

    @abstractmethod
    def visit_tipoConcrete(self, tipoConcrete):
      pass

    @abstractmethod
    def visit_usingConcrete(self, usingConcrete):
      pass

    @abstractmethod
    def visit_usingConcrete1(self, usingConcrete1):
      pass

    @abstractmethod
    def visit_typedefConcrete(self, typedefConcrete):
      pass

    @abstractmethod
    def visit_typedefConcrete1(self, typedefConcrete1):
      pass

    @abstractmethod
    def visit_decl_typedef_nConcrete(self, decl_typedef_nConcrete):
      pass

    @abstractmethod
    def visit_decl_typedef_nConcrete1(self, decl_typedef_nConcrete1):
      pass
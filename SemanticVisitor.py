from visitor_abstract import visitor_abstract
import SymbolTable as st
from Visitor import Visitor
import sintaxe_abstrata as sa

def coercion(type1, type2, operador):
  if(operador == "bool"):
    if (type1 in st.Number and type2 in st.Number):
      return st.BOOL
  else:
    if (type1 in st.Number and type2 in st.Number):
        return st.INT
    elif(type1 in st.Logic and type2 in st.Logic):
        return st.BOOL
    else:
      return None

class SemanticVisitor(visitor_abstract):
    def __init__(self):
      self.printer = Visitor()
      st.beginScope('main')
    
    def visit_cppConcrete(self, cppConcrete):
      if(cppConcrete.decl):
        cppConcrete.decl.accept(self)
      if(cppConcrete.cpp):
        cppConcrete.cpp.accept(self)
    
    def visit_decl_classeConcrete(self, decl_classeConcrete):
      if(st.getBindable(decl_classeConcrete.id) == None):
        st.addClass(decl_classeConcrete.id)
        st.beginScope(decl_classeConcrete.id)
        if(decl_classeConcrete.body_class):
          decl_classeConcrete.body_class.accept(self)
      else:
        print("[Error] - Não é possível existir duas classes com mesmo nome.")

   
    def visit_body_classConcrete(self, body_classConcrete):
      if(body_classConcrete.content_class):
        body_classConcrete.content_class.accept(self)
      st.endScope()

    def visit_content_classConcrete(self, content_classConcrete):
      if(content_classConcrete.decl):
        content_classConcrete.decl.accept(self)
      if(content_classConcrete.content_class):
        content_classConcrete.content_class.accept(self)

    def visit_decl_funcaoConcrete(self, decl_funcaoConcrete):
      if(st.getBindable(decl_funcaoConcrete.id) == None):
        params = {}
        if(decl_funcaoConcrete.parametros):
          params = decl_funcaoConcrete.parametros.accept(self)
          st.addFunction(decl_funcaoConcrete.id, params, decl_funcaoConcrete.tipo.accept(self))
        else:
          if(decl_funcaoConcrete.tipo != "void"):
            st.addFunction(decl_funcaoConcrete.id, params, decl_funcaoConcrete.tipo.accept(self))
          else:
            st.addFunction(decl_funcaoConcrete.id, params, None)
        st.beginScope(decl_funcaoConcrete.id)
        for k in range(0, len(params), 2):
          st.addVar(params[k], params[k+1])
        if(decl_funcaoConcrete.body):
          decl_funcaoConcrete.body.accept(self)
      else:
        print("[Erro] - Não é possível exisitr duas ou mais funções com o mesmo nome.")

    def visit_parametrosConcrete(self, parametrosConcrete):
      if(parametrosConcrete.tipo):
        return [parametrosConcrete.id] + [parametrosConcrete.tipo.accept(self)]
      if(parametrosConcrete.parametros):
        return [parametrosConcrete.id] + [parametrosConcrete.tipo.accept(self)] + [parametrosConcrete.parametros.accept(self)]

    def visit_decl_variavelConcrete(self, decl_variavelConcrete):
      tipoVariavel = decl_variavelConcrete.tipo.accept(self)
      if(st.getBindable(decl_variavelConcrete.id) == None):
        st.addVar(decl_variavelConcrete.id, tipoVariavel)
        if(decl_variavelConcrete.exp):
          tipoExp = decl_variavelConcrete.exp.accept(self)
          if(tipoExp != tipoVariavel):
            print("[Error] - O retorno da expressão não é compatível.")
        if(decl_variavelConcrete.decl_variavel_n):
          decl_variavelConcrete.decl_variavel_n.accept(self)
      else:
        print("[Erro] - A variável já está declarada.")

    def visit_decl_variavel_nConcrete(self, decl_variavel_nConcrete):
      if(decl_variavel_nConcrete.exp):
        decl_variavel_nConcrete.exp.accept(self)
      if(decl_variavel_nConcrete.decl_variavel_n):
        decl_variavel_nConcrete.decl_variavel_n.accept(self)

    def visit_bodyConcrete(self, bodyConcrete):
      if(bodyConcrete.comandos):
        bodyConcrete.comandos.accept(self)

    def visit_comandosConcrete(self, comandosConcrete):
      if(comandosConcrete.comando):
        comandosConcrete.comando.accept(self)
      if(comandosConcrete.comandos):
        comandosConcrete.comandos.accept(self)

    def visit_comandoConcrete(self, comandoConcrete):
      comandoConcrete.condicional.accept(self)

    def visit_expConcrete(self, expConcrete):
      if(expConcrete.exp):
        tipoVariavel = expConcrete.exp.accept(self)
        tipoExp = expConcrete.exp_1.accept(self)
        if(tipoVariavel == tipoExp):
          return expConcrete.exp_1.accept(self)
        else:
          print("[Error] - O identificador não é compatível com a expressão ou não está declarado.")
      else:
        return expConcrete.exp_1.accept(self)

    def visit_exp_1_OR(self,exp_1Concrete):
      tipoExp1 = exp_1Concrete.exp_1.accept(self)
      tipoExp2 = exp_1Concrete.exp_2.accept(self)
      c = coercion(tipoExp1, tipoExp2, "bool")
      if (c == None):
        exp_1Concrete.accept(self.printer)
        print('\n\t[Erro] - A expressao ', end='')
        exp_1Concrete.exp_1.accept(self.printer)
        print(' eh do tipo', tipoExp1, 'enquanto a expressao ', end='')
        exp_1Concrete.exp_2.accept(self.printer)
        print(' eh do tipo', tipoExp2,'\n')
      return c

    def visit_exp_1_OP_OU(self,exp_1Concrete):
      tipoExp1 = exp_1Concrete.exp_1.accept(self)
      tipoExp2 = exp_1Concrete.exp_2.accept(self)
      c = coercion(tipoExp1, tipoExp2,"bool")
      if (c == None):
        exp_1Concrete.accept(self.printer)
        print('\n\t[Erro] - A expressao ', end='')
        exp_1Concrete.exp_1.accept(self.printer)
        print(' eh do tipo', tipoExp1, 'enquanto a expressao ', end='')
        exp_1Concrete.exp_2.accept(self.printer)
        print(' eh do tipo', tipoExp2,'\n')
      return c

    def visit_exp_1Concrete(self,exp_1Concrete):
      return exp_1Concrete.exp_2.accept(self)

    def visit_exp_2_AND(self,exp_2Concrete):
      tipoExp1 = exp_2Concrete.exp_2.accept(self)
      tipoExp2 = exp_2Concrete.exp_3.accept(self)
      c = coercion(tipoExp1, tipoExp2,"bool")
      if (c == None):
        exp_2Concrete.accept(self.printer)
        print('\n\t[Erro] - A expressao ', end='')
        exp_2Concrete.exp_2.accept(self.printer)
        print(' eh do tipo', tipoExp1, 'enquanto a expressao ', end='')
        exp_2Concrete.exp_3.accept(self.printer)
        print(' eh do tipo', tipoExp2,'\n')
      return c

    def visit_exp_2_OP_E(self,exp_2Concrete):
      tipoExp1 = exp_2Concrete.exp_2.accept(self)
      tipoExp2 = exp_2Concrete.exp_3.accept(self)
      c = coercion(tipoExp1, tipoExp2,"bool")
      if (c == None):
        exp_2Concrete.accept(self.printer)
        print('\n\t[Erro] - A expressao ', end='')
        exp_2Concrete.exp_2.accept(self.printer)
        print(' eh do tipo', tipoExp1, 'enquanto a expressao ', end='')
        exp_2Concrete.exp_3.accept(self.printer)
        print(' eh do tipo', tipoExp2,'\n')
      return c

    def visit_exp_2Concrete(self,exp_2Concrete):
      return exp_2Concrete.exp_3.accept(self)

    def visit_exp_3_XOR(self,exp_3Concrete):
      tipoExp1 = exp_3Concrete.exp_3.accept(self)
      tipoExp2 = exp_3Concrete.exp_4.accept(self)
      c = coercion(tipoExp1, tipoExp2,"bool")
      if (c == None):
        exp_3Concrete.accept(self.printer)
        print('\n\t[Erro] - A expressao ', end='')
        exp_3Concrete.exp_3.accept(self.printer)
        print(' eh do tipo', tipoExp1, 'enquanto a expressao ', end='')
        exp_3Concrete.exp_4.accept(self.printer)
        print(' eh do tipo', tipoExp2,'\n')
      return c

    def visit_exp_3_OP_OU_EX(self,exp_3Concrete):
      tipoExp1 = exp_3Concrete.exp_3.accept(self)
      tipoExp2 = exp_3Concrete.exp_4.accept(self)
      c = coercion(tipoExp1, tipoExp2,"bool")
      if (c == None):
        exp_3Concrete.accept(self.printer)
        print('\n\t[Erro] - A expressao ', end='')
        exp_3Concrete.exp_3.accept(self.printer)
        print(' eh do tipo', tipoExp1, 'enquanto a expressao ', end='')
        exp_3Concrete.exp_4.accept(self.printer)
        print(' eh do tipo', tipoExp2,'\n')
      return c
      
    def visit_exp_3Concrete(self,exp_3Concrete):
      return exp_3Concrete.exp_4.accept(self)

    def visit_exp_4Concrete(self,exp_4Concrete):
      return exp_4Concrete.exp_5.accept(self)

    def visit_exp_4_IGUAL(self,exp_4Concrete):
      tipoExp1 = exp_4Concrete.exp_4.accept(self)
      tipoExp2 = exp_4Concrete.exp_5.accept(self)
      c = coercion(tipoExp1, tipoExp2,"bool")
      if (c == None):
        exp_4Concrete.accept(self.printer)
        print('\n\t[Erro] - A expressao ', end='')
        exp_4Concrete.exp_4.accept(self.printer)
        print(' eh do tipo', tipoExp1, 'enquanto a expressao ', end='')
        exp_4Concrete.exp_5.accept(self.printer)
        print(' eh do tipo', tipoExp2,'\n')
      return c

    def visit_exp_4_DIFERENTE(self,exp_4Concrete):
      tipoExp1 = exp_4Concrete.exp_4.accept(self)
      tipoExp2 = exp_4Concrete.exp_5.accept(self)
      c = coercion(tipoExp1, tipoExp2,"bool")
      if (c == None):
        exp_4Concrete.accept(self.printer)
        print('\n\t[Erro] - A expressao ', end='')
        exp_4Concrete.exp_4.accept(self.printer)
        print(' eh do tipo', tipoExp1, 'enquanto a expressao ', end='')
        exp_4Concrete.exp_5.accept(self.printer)
        print(' eh do tipo', tipoExp2,'\n')
      return c

    def visit_exp_5Concrete(self,exp_5Concrete):
      return exp_5Concrete.exp_6.accept(self)

    def visit_exp_5_MENOR_Q(self,exp_5Concrete):
      tipoExp1 = exp_5Concrete.exp_5.accept(self)
      tipoExp2 = exp_5Concrete.exp_6.accept(self)
      c = coercion(tipoExp1, tipoExp2,"bool")
      if (c == None):
        exp_5Concrete.accept(self.printer)
        print('\n\t[Erro] - A expressao ', end='')
        exp_5Concrete.exp_5.accept(self.printer)
        print(' eh do tipo', tipoExp1, 'enquanto a expressao ', end='')
        exp_5Concrete.exp_6.accept(self.printer)
        print(' eh do tipo', tipoExp2,'\n')
      return c

    def visit_exp_5_MAIOR_Q(self,exp_5Concrete):
      tipoExp1 = exp_5Concrete.exp_5.accept(self)
      tipoExp2 = exp_5Concrete.exp_6.accept(self)
      c = coercion(tipoExp1, tipoExp2, "bool")
      if (c == None):
        exp_5Concrete.accept(self.printer)
        print('\n\t[Erro] - A expressao ', end='')
        exp_5Concrete.exp_5.accept(self.printer)
        print(' eh do tipo', tipoExp1, 'enquanto a expressao ', end='')
        exp_5Concrete.exp_6.accept(self.printer)
        print(' eh do tipo', tipoExp2,'\n')
      return c

    def visit_exp_5_MAIOR_IGUAL(self,exp_5Concrete):
      tipoExp1 = exp_5Concrete.exp_5.accept(self)
      tipoExp2 = exp_5Concrete.exp_6.accept(self)
      c = coercion(tipoExp1, tipoExp2,"bool")
      if (c == None):
        exp_5Concrete.accept(self.printer)
        print('\n\t[Erro] - A expressao ', end='')
        exp_5Concrete.exp_5.accept(self.printer)
        print(' eh do tipo', tipoExp1, 'enquanto a expressao ', end='')
        exp_5Concrete.exp_6.accept(self.printer)
        print(' eh do tipo', tipoExp2,'\n')
      return c

    def visit_exp_5_MENOR_IGUAL(self,exp_5Concrete):
      tipoExp1 = exp_5Concrete.exp_5.accept(self)
      tipoExp2 = exp_5Concrete.exp_6.accept(self)
      c = coercion(tipoExp1, tipoExp2, "bool")
      if (c == None):
        exp_5Concrete.accept(self.printer)
        print('\n\t[Erro] - A expressao ', end='')
        exp_5Concrete.exp_5.accept(self.printer)
        print(' eh do tipo', tipoExp1, 'enquanto a expressao ', end='')
        exp_5Concrete.exp_6.accept(self.printer)
        print(' eh do tipo', tipoExp2,'\n')
      return c

    def visit_exp_6Concrete(self,exp_6Concrete):
      return exp_6Concrete.exp_7.accept(self)

    def visit_exp_6_SOMA(self,exp_6Concrete):
      tipoExp1 = exp_6Concrete.exp_6.accept(self)
      tipoExp2 = exp_6Concrete.exp_7.accept(self)
      c = coercion(tipoExp1, tipoExp2,"number")
      if (c == None):
        exp_6Concrete.accept(self.printer)
        print('\n\t[Erro] Soma invalida. A expressao ', end='')
        exp_6Concrete.exp_6.accept(self.printer)
        print(' eh do tipo', tipoExp1, 'enquanto a expressao ', end='')
        exp_6Concrete.exp_7.accept(self.printer)
        print(' eh do tipo', tipoExp2,'\n')
      return c

    def visit_exp_6_SUB(self,exp_6Concrete):
      tipoExp1 = exp_6Concrete.exp_6.accept(self)
      tipoExp2 = exp_6Concrete.exp_7.accept(self)
      c = coercion(tipoExp1, tipoExp2,"number")
      if (c == None):
        exp_6Concrete.accept(self.printer)
        print('\n\t[Erro] Sub invalida. A expressao ', end='')
        exp_6Concrete.exp_6.accept(self.printer)
        print(' eh do tipo', tipoExp1, 'enquanto a expressao ', end='')
        exp_6Concrete.exp_7.accept(self.printer)
        print(' eh do tipo', tipoExp2,'\n')
      return c

    def visit_exp_7Concrete(self,exp_7Concrete):
      return exp_7Concrete.exp_8.accept(self)

    def visit_exp_7_MULT(self,exp_7Concrete):
      tipoExp1 = exp_7Concrete.exp_7.accept(self)
      tipoExp2 = exp_7Concrete.exp_8.accept(self)
      c = coercion(tipoExp1, tipoExp2,"number")
      if (c == None):
        exp_7Concrete.accept(self.printer)
        print('\n\t[Erro] Sub invalida. A expressao ', end='')
        exp_7Concrete.exp_7.accept(self.printer)
        print(' eh do tipo', tipoExp1, 'enquanto a expressao ', end='')
        exp_7Concrete.exp_8.accept(self.printer)
        print(' eh do tipo', tipoExp2,'\n')
      return c

    def visit_exp_7_DIV(self,exp_7Concrete):
      tipoExp1 = exp_7Concrete.exp_7.accept(self)
      tipoExp2 = exp_7Concrete.exp_8.accept(self)
      c = coercion(tipoExp1, tipoExp2,"number")
      if (c == None):
        exp_7Concrete.accept(self.printer)
        print('\n\t[Erro] Sub invalida. A expressao ', end='')
        exp_7Concrete.exp_7.accept(self.printer)
        print(' eh do tipo', tipoExp1, 'enquanto a expressao ', end='')
        exp_7Concrete.exp_8.accept(self.printer)
        print(' eh do tipo', tipoExp2,'\n')
      return c

    def visit_exp_7_MODULO(self,exp_7Concrete):
      tipoExp1 = exp_7Concrete.exp_7.accept(self)
      tipoExp2 = exp_7Concrete.exp_8.accept(self)
      c = coercion(tipoExp1, tipoExp2,"number")
      if (c == None):
        exp_7Concrete.accept(self.printer)
        print('\n\t[Erro] Sub invalida. A expressao ', end='')
        exp_7Concrete.exp_7.accept(self.printer)
        print(' eh do tipo', tipoExp1, 'enquanto a expressao ', end='')
        exp_7Concrete.exp_8.accept(self.printer)
        print(' eh do tipo', tipoExp2,'\n')
      return c

    def visit_exp_8Concrete(self,exp_8Concrete):
      return exp_8Concrete.exp_9.accept(self)

    def visit_exp_8_SIZEOF(self,exp_8Concrete):
      exp_8Concrete.exp_9.accept(self)

    def visit_exp_8_OP_NOT(self,exp_8Concrete):
      exp_8Concrete.exp_9.accept(self)

    def visit_exp_8_NOT(self,exp_8Concrete):
      exp_8Concrete.exp_9.accept(self)

    def visit_exp_8_NEW(self,exp_8Concrete):
      exp_8Concrete.tipo.accept(self)

    def visit_exp_8_MAIS_MAIS(self,exp_8Concrete):
      tipoExp1 = exp_8Concrete.exp_9.accept(self)
      c = coercion(tipoExp1, st.INT,"number")
      if (c == None):
        print("[Error] - A utilização do comando '++' só é válido para váriaveis de tipo númerico.")
      return c
      #return exp_8Concrete.exp_9.accept(self)

    def visit_exp_8_MENOS_MENOS(self,exp_8Concrete):
      tipoExp1 = exp_8Concrete.exp_9.accept(self)
      c = coercion(tipoExp1, st.INT,"number")
      if (c == None):
        print("[Error] - A utilização do comando '--' só é válido para váriaveis de tipo númerico.")
      return c
      #return exp_8Concrete.exp_9.accept(self)

    def visit_exp_9Concrete(self,exp_9Concrete):
      return exp_9Concrete.exp_10.accept(self)

    def visit_exp_9_PONTO(self,exp_9Concrete):
      return exp_9Concrete.exp_10.accept(self)

    def visit_exp_9_SETA(self,exp_9Concrete):
      return exp_9Concrete.exp_10.accept(self)

    def visit_exp_10Concrete(self,exp_10Concrete):
      if(isinstance(exp_10Concrete.value, int)):
        return st.INT
      elif(exp_10Concrete.value == 'true' or exp_10Concrete.value == 'false'):
        return st.BOOL
      idName = st.getBindable(exp_10Concrete.value)
      if(idName):
        return idName[st.TYPE]
      elif(exp_10Concrete.value.__contains__('\"')):
        return st.STRING
      else:
        return None

    def visit_exp_10_funcao(self,exp_10_funcao):
      return exp_10_funcao.funcao.accept(self)

    def visit_exp_10_exp(self,exp_10Concrete):
      return exp_10Concrete.exp.accept(self)

    def visit_chamada_funcaoConcrete(self, chamada_funcaoConcrete):
      bindable = st.getBindable(chamada_funcaoConcrete.id)
      if (bindable != None and bindable[st.BINDABLE] == st.FUNCTION):
        typeParams = chamada_funcaoConcrete.parametros_chamada.accept(self)
        if (list(bindable[st.PARAMS][1::2]).__contains__(typeParams)):
          return bindable[st.TYPE]
        else:
          print("[Erro] - Chamada de funcao invalida.")
      else:
        print("[Erro] - A função não foi declarada.")
      return None

    def visit_chamada_funcaoTypeid(self, chamada_funcaoTypeid):
      pass

    def visit_parametros_chamadaConcrete(self, parametros_chamadaConcrete):
      return parametros_chamadaConcrete.id.accept(self)

    def visit_condicional_1_IF(self, condicional_1_IF):
      type = condicional_1_IF.exp.accept(self)
      if(type != st.BOOL):
        print("[Error] - O comando IF espera uma expressão booleana.")

    def visit_condicional_1_WHILE(self, condicional_1_WHILE):
      type = condicional_1_WHILE.exp.accept(self)
      if(type != st.BOOL):
        print("[Error] - O comando WHILE espera uma expressão booleana.")

    def visit_condicional_1_FOR(self, condicional_1_FOR):
      condicional_1_FOR.for_log.accept(self)

    def visit_condicional_1_RETURN(self, condicional_1_RETURN):
      if(condicional_1_RETURN.exp):
        tipoExp = condicional_1_RETURN.exp.accept(self)
        scope = st.symbolTable[-1][st.SCOPE]
        bindable = st.getBindable(scope)
        if (tipoExp != bindable[st.TYPE]):
          condicional_1_RETURN.accept(self.printer)
          print('\t[Erro] O retorno da funcao', scope, 'eh do tipo', bindable[st.TYPE],end='')
          print(' no entanto, o retorno passado foi do tipo', tipoExp, '\n')
      st.endScope()

    def visit_condicional_1_EXP(self, condicional_1_EXP):
      condicional_1_EXP.exp.accept(self)

    def visit_condicional_1_decl_variavel(self, condicional_1_decl_variavel):
      condicional_1_decl_variavel.decl_variavel.accept(self)

    def visit_condicional_1_typedef(self, condicional_1_typedef):
      pass
      
    def visit_condicional_1_using(self, condicional_1_using):
      pass

    def visit_condicional_2Concrete(self, condicional_2Concrete):
      tipo = condicional_2Concrete.exp.accept(self)
      if(tipo != st.BOOL):
        print("[Error] - O comando IF espera uma expressão booleana.")

    def visit_condicional_2Concrete_2(self, condicional_2Concrete_2):
      tipo = condicional_2Concrete_2.exp.accept(self)
      if(tipo != st.BOOL):
        print("[Error] - O comando IF espera uma expressão booleana.")

    def visit_rest_ifConcrete(self, rest_ifConcrete):
      if(rest_ifConcrete.body_1):
        rest_ifConcrete.body_1.accept(self)
      if(rest_ifConcrete.body_2):
        rest_ifConcrete.body_2.accept(self)

    def visit_for_logConcrete(self, for_logConcrete):
      tipo = for_logConcrete.exp_1.accept(self)
      if(tipo != st.BOOL):
        print("[Error] - O comando FOR espera uma expressão booleana.")

    def visit_tipoConcrete(self, tipoConcrete):
      if(tipoConcrete.tipo_v == 'int'):
        return st.INT
      elif(tipoConcrete.tipo_v == 'boolean'):
        return st.BOOL
      elif(tipoConcrete.tipo_v == 'id'):
        return st.TYPE
      elif(tipoConcrete.tipo_v == 'string'):
        return st.STRING
        

    def visit_usingConcrete(self, usingConcrete):
      pass

    def visit_usingConcrete1(self, usingConcrete1):
      pass

    def visit_typedefConcrete(self, typedefConcrete):
      pass

    def visit_typedefConcrete1(self, typedefConcrete1):
      pass

    def visit_decl_typedef_nConcrete(self, decl_typedef_nConcrete):
      pass

    def visit_decl_typedef_nConcrete1(self, decl_typedef_nConcrete1):
      pass
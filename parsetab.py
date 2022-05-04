
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND BOOL CHAVE_ABRE CHAVE_FECHA CLASS COLCHETE_ABRE COLCHETE_FECHA COMENTARIO DIFERENTE DIV DOIS_PONTOS ELSE ENDERECO FALSE FOR ID IF IGUAL INT INT_V MAIOR_IGUAL MAIOR_Q MAIS_MAIS MENOR_IGUAL MENOR_Q MENOS_MENOS MODULO MULT NAMESPACE NEW NOT OP_E OP_NOT OP_OU OP_OU_EX OR PARENT_ABRE PARENT_FECHA PONTO PONTO_VIRG PUBLIC RECEBER RETURN SETA SIZEOF SOMA STATIC STRING STRUCT SUB THIS TRUE TRY TYPEDEF TYPEID USING VIRGULA VOID WHILE XORcpp : decl_classe\n         | decl_funcao\n         | decl_variavel\n         | decl_classe  cpp\n         | decl_funcao  cpp\n         | decl_variavel cppdecl_classe : CLASS ID body_class PONTO_VIRGbody_class : CHAVE_ABRE PUBLIC DOIS_PONTOS content_class CHAVE_FECHAcontent_class : decl_variavel\n                   | decl_funcaodecl_funcao : tipo ID PARENT_ABRE parametros PARENT_FECHA body\n                 | tipo ID PARENT_ABRE PARENT_FECHA body\n                 | tipo ID PARENT_ABRE VOID PARENT_FECHA body\n                 | VOID ID PARENT_ABRE parametros PARENT_FECHA body\n                 | VOID ID PARENT_ABRE PARENT_FECHA body\n                 | VOID ID PARENT_ABRE VOID PARENT_FECHA bodyparametros : tipo ID\n                | tipo ID VIRGULA parametrosdecl_variavel : tipo ID PONTO_VIRG \n                   | tipo ID RECEBER exp PONTO_VIRG\n                   | tipo ID decl_variavel_n\n                   | tipo ID RECEBER exp decl_variavel_n\n                   | TYPEDEF tipo ID PONTO_VIRG\n                   | TYPEDEF tipo ID decl_variavel_ndecl_variavel_n : VIRGULA ID decl_variavel_n\n                     | VIRGULA ID RECEBER exp decl_variavel_n\n                     | PONTO_VIRGbody : CHAVE_ABRE comandos CHAVE_FECHA\n          | CHAVE_ABRE CHAVE_FECHA\n          | CHAVE_ABRE comandos RETURN exp CHAVE_FECHA\n          | CHAVE_ABRE CHAVE_FECHA RETURN expcomandos : condicional_1\n              | condicional_2\n              | exp PONTO_VIRG comandos\n              | exp PONTO_VIRGexp : exp RECEBER exp_1\n         | exp_1exp_1 : exp_1 OP_OU exp_2 \n           | exp_1 OR exp_2\n           | exp_2exp_2 : exp_2 OP_E exp_3\n           | exp_2 AND exp_3\n           | exp_3exp_3 : exp_3 OP_OU_EX exp_4\n           | exp_3 XOR exp_4\n           | exp_4exp_4 : exp_4 IGUAL exp_5\n           | exp_4 DIFERENTE exp_5\n           | exp_5exp_5 : exp_5 MENOR_Q exp_6\n           | exp_5 MAIOR_Q exp_6\n           | exp_5 MAIOR_IGUAL exp_6\n           | exp_5 MENOR_IGUAL exp_6\n           | exp_6exp_6 : exp_6 SOMA exp_7\n           | exp_6 SUB exp_7\n           | exp_7exp_7 : exp_7 MULT exp_8\n           | exp_7 DIV exp_8\n           | exp_7 MODULO exp_8\n           | exp_8exp_8 : OP_NOT exp_9\n           | NOT exp_9\n           | exp_9 MAIS_MAIS\n           | exp_9 MENOS_MENOS\n           | SIZEOF PARENT_ABRE exp_9 PARENT_FECHA\n           | exp_9exp_9 : ID\n           | INT_V\n           | TRUE\n           | FALSE\n           | chamada_funcao\n           | tipo\n           | PARENT_ABRE exp PARENT_FECHAchamada_funcao : ID PARENT_ABRE parametros PARENT_FECHA\n                    | ID PARENT_ABRE PARENT_FECHA\n                    | TYPEID PARENT_ABRE exp PARENT_FECHAcondicional_1 : IF PARENT_ABRE exp PARENT_FECHA condicional_1 body ELSE condicional_1 body\n                   | decl_variavel\n                   | decl_variavel condicional_1\n                   | repeticao\n                   | repeticao condicional_1\n                   | RETURN exp PONTO_VIRGcondicional_2 : IF PARENT_ABRE exp PARENT_FECHA body comandos\n                   | IF PARENT_ABRE exp PARENT_FECHA body condicional_1 ELSE body condicional_2repeticao : WHILE PARENT_ABRE exp PARENT_FECHA body\n               | FOR PARENT_ABRE for_log PARENT_FECHA bodyfor_log : decl_variavel PONTO_VIRG\n             | decl_variavel exp PONTO_VIRG\n             | decl_variavel exp PONTO_VIRG exp\n             | decl_variavel PONTO_VIRG exp\n             | PONTO_VIRG exp PONTO_VIRG exp\n             | PONTO_VIRG exp PONTO_VIRG\n             | PONTO_VIRG PONTO_VIRG exp\n             | PONTO_VIRG PONTO_VIRGtipo : INT \n          | BOOL \n          | ID\n          | STRING'
    
_lr_action_items = {'CLASS':([0,2,3,4,10,11,12,23,25,29,35,36,38,39,40,41,42,43,44,45,47,51,52,53,54,60,61,65,70,71,89,90,91,92,96,98,101,107,109,121,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,143,146,147,151,164,165,166,167,169,178,],[5,5,5,5,-96,-97,-99,-19,-21,-7,-73,-68,-37,-40,-43,-46,-49,-54,-57,-61,-67,-69,-70,-71,-72,-23,-24,-12,-20,-22,-62,-64,-65,-63,-25,-27,-15,-11,-29,-13,-76,-36,-38,-39,-41,-42,-44,-45,-47,-48,-50,-51,-52,-53,-55,-56,-58,-59,-60,-74,-16,-14,-28,-75,-66,-77,-26,-31,-30,]),'VOID':([0,2,3,4,10,11,12,22,23,25,27,29,35,36,38,39,40,41,42,43,44,45,47,51,52,53,54,60,61,62,65,70,71,89,90,91,92,96,98,101,107,109,121,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,143,146,147,151,164,165,166,167,169,178,],[8,8,8,8,-96,-97,-99,34,-19,-21,57,-7,-73,-68,-37,-40,-43,-46,-49,-54,-57,-61,-67,-69,-70,-71,-72,-23,-24,8,-12,-20,-22,-62,-64,-65,-63,-25,-27,-15,-11,-29,-13,-76,-36,-38,-39,-41,-42,-44,-45,-47,-48,-50,-51,-52,-53,-55,-56,-58,-59,-60,-74,-16,-14,-28,-75,-66,-77,-26,-31,-30,]),'TYPEDEF':([0,2,3,4,10,11,12,23,25,29,35,36,38,39,40,41,42,43,44,45,47,51,52,53,54,60,61,62,65,66,70,71,89,90,91,92,96,98,101,107,109,115,116,121,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,143,146,147,151,155,163,164,165,166,167,169,178,179,188,189,190,191,201,],[9,9,9,9,-96,-97,-99,-19,-21,-7,-73,-68,-37,-40,-43,-46,-49,-54,-57,-61,-67,-69,-70,-71,-72,-23,-24,9,-12,9,-20,-22,-62,-64,-65,-63,-25,-27,-15,-11,-29,9,9,-13,-76,-36,-38,-39,-41,-42,-44,-45,-47,-48,-50,-51,-52,-53,-55,-56,-58,-59,-60,-74,-16,-14,-28,9,9,-75,-66,-77,-26,-31,-30,9,9,9,-86,-87,9,]),'INT':([0,2,3,4,9,10,11,12,22,23,24,25,27,29,35,36,38,39,40,41,42,43,44,45,46,47,48,50,51,52,53,54,60,61,62,65,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,95,96,97,98,101,106,107,109,110,115,116,121,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,143,146,147,151,152,153,155,156,162,163,164,165,166,167,169,173,176,177,178,179,183,185,188,189,190,191,193,195,201,208,],[10,10,10,10,10,-96,-97,-99,10,-19,10,-21,10,-7,-73,-68,-37,-40,-43,-46,-49,-54,-57,-61,10,-67,10,10,-69,-70,-71,-72,-23,-24,10,-12,10,10,10,-20,-22,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,-62,-64,-65,-63,10,10,-25,10,-27,-15,10,-11,-29,10,10,10,-13,-76,-36,-38,-39,-41,-42,-44,-45,-47,-48,-50,-51,-52,-53,-55,-56,-58,-59,-60,-74,-16,-14,-28,10,10,10,10,10,10,-75,-66,-77,-26,-31,10,10,10,-30,10,10,10,10,10,-86,-87,10,10,10,10,]),'BOOL':([0,2,3,4,9,10,11,12,22,23,24,25,27,29,35,36,38,39,40,41,42,43,44,45,46,47,48,50,51,52,53,54,60,61,62,65,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,95,96,97,98,101,106,107,109,110,115,116,121,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,143,146,147,151,152,153,155,156,162,163,164,165,166,167,169,173,176,177,178,179,183,185,188,189,190,191,193,195,201,208,],[11,11,11,11,11,-96,-97,-99,11,-19,11,-21,11,-7,-73,-68,-37,-40,-43,-46,-49,-54,-57,-61,11,-67,11,11,-69,-70,-71,-72,-23,-24,11,-12,11,11,11,-20,-22,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,-62,-64,-65,-63,11,11,-25,11,-27,-15,11,-11,-29,11,11,11,-13,-76,-36,-38,-39,-41,-42,-44,-45,-47,-48,-50,-51,-52,-53,-55,-56,-58,-59,-60,-74,-16,-14,-28,11,11,11,11,11,11,-75,-66,-77,-26,-31,11,11,11,-30,11,11,11,11,11,-86,-87,11,11,11,11,]),'ID':([0,2,3,4,5,6,7,8,9,10,11,12,19,22,23,24,25,26,27,29,31,35,36,38,39,40,41,42,43,44,45,46,47,48,50,51,52,53,54,60,61,62,65,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,95,96,97,98,101,105,106,107,109,110,115,116,117,118,121,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,143,146,147,151,152,153,155,156,159,162,163,164,165,166,167,169,173,176,177,178,179,183,185,188,189,190,191,193,195,201,208,],[6,6,6,6,16,-98,17,18,6,-96,-97,-99,28,6,-19,36,-21,56,6,-7,63,-73,-68,-37,-40,-43,-46,-49,-54,-57,-61,36,-67,36,36,-69,-70,-71,-72,-23,-24,6,-12,118,6,36,-20,-22,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,-62,-64,-65,-63,36,36,-25,36,-27,-15,149,6,-11,-29,36,6,6,161,-98,-13,-76,-36,-38,-39,-41,-42,-44,-45,-47,-48,-50,-51,-52,-53,-55,-56,-58,-59,-60,-74,-16,-14,-28,36,36,118,36,161,36,6,-75,-66,-77,-26,-31,36,36,36,-30,6,36,36,118,6,-86,-87,36,36,6,36,]),'STRING':([0,2,3,4,9,10,11,12,22,23,24,25,27,29,35,36,38,39,40,41,42,43,44,45,46,47,48,50,51,52,53,54,60,61,62,65,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,95,96,97,98,101,106,107,109,110,115,116,121,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,143,146,147,151,152,153,155,156,162,163,164,165,166,167,169,173,176,177,178,179,183,185,188,189,190,191,193,195,201,208,],[12,12,12,12,12,-96,-97,-99,12,-19,12,-21,12,-7,-73,-68,-37,-40,-43,-46,-49,-54,-57,-61,12,-67,12,12,-69,-70,-71,-72,-23,-24,12,-12,12,12,12,-20,-22,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,-62,-64,-65,-63,12,12,-25,12,-27,-15,12,-11,-29,12,12,12,-13,-76,-36,-38,-39,-41,-42,-44,-45,-47,-48,-50,-51,-52,-53,-55,-56,-58,-59,-60,-74,-16,-14,-28,12,12,12,12,12,12,-75,-66,-77,-26,-31,12,12,12,-30,12,12,12,12,12,-86,-87,12,12,12,12,]),'$end':([1,2,3,4,10,11,12,13,14,15,23,25,29,35,36,38,39,40,41,42,43,44,45,47,51,52,53,54,60,61,65,70,71,89,90,91,92,96,98,101,107,109,121,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,143,146,147,151,164,165,166,167,169,178,],[0,-1,-2,-3,-96,-97,-99,-4,-5,-6,-19,-21,-7,-73,-68,-37,-40,-43,-46,-49,-54,-57,-61,-67,-69,-70,-71,-72,-23,-24,-12,-20,-22,-62,-64,-65,-63,-25,-27,-15,-11,-29,-13,-76,-36,-38,-39,-41,-42,-44,-45,-47,-48,-50,-51,-52,-53,-55,-56,-58,-59,-60,-74,-16,-14,-28,-75,-66,-77,-26,-31,-30,]),'MAIS_MAIS':([10,11,12,35,36,47,51,52,53,54,117,118,123,143,164,166,],[-96,-97,-99,-73,-68,90,-69,-70,-71,-72,-73,-68,-76,-74,-75,-77,]),'MENOS_MENOS':([10,11,12,35,36,47,51,52,53,54,117,118,123,143,164,166,],[-96,-97,-99,-73,-68,91,-69,-70,-71,-72,-73,-68,-76,-74,-75,-77,]),'MULT':([10,11,12,35,36,44,45,47,51,52,53,54,89,90,91,92,117,118,123,137,138,139,140,141,143,164,165,166,],[-96,-97,-99,-73,-68,86,-61,-67,-69,-70,-71,-72,-62,-64,-65,-63,-73,-68,-76,86,86,-58,-59,-60,-74,-75,-66,-77,]),'DIV':([10,11,12,35,36,44,45,47,51,52,53,54,89,90,91,92,117,118,123,137,138,139,140,141,143,164,165,166,],[-96,-97,-99,-73,-68,87,-61,-67,-69,-70,-71,-72,-62,-64,-65,-63,-73,-68,-76,87,87,-58,-59,-60,-74,-75,-66,-77,]),'MODULO':([10,11,12,35,36,44,45,47,51,52,53,54,89,90,91,92,117,118,123,137,138,139,140,141,143,164,165,166,],[-96,-97,-99,-73,-68,88,-61,-67,-69,-70,-71,-72,-62,-64,-65,-63,-73,-68,-76,88,88,-58,-59,-60,-74,-75,-66,-77,]),'SOMA':([10,11,12,35,36,43,44,45,47,51,52,53,54,89,90,91,92,117,118,123,133,134,135,136,137,138,139,140,141,143,164,165,166,],[-96,-97,-99,-73,-68,84,-57,-61,-67,-69,-70,-71,-72,-62,-64,-65,-63,-73,-68,-76,84,84,84,84,-55,-56,-58,-59,-60,-74,-75,-66,-77,]),'SUB':([10,11,12,35,36,43,44,45,47,51,52,53,54,89,90,91,92,117,118,123,133,134,135,136,137,138,139,140,141,143,164,165,166,],[-96,-97,-99,-73,-68,85,-57,-61,-67,-69,-70,-71,-72,-62,-64,-65,-63,-73,-68,-76,85,85,85,85,-55,-56,-58,-59,-60,-74,-75,-66,-77,]),'MENOR_Q':([10,11,12,35,36,42,43,44,45,47,51,52,53,54,89,90,91,92,117,118,123,131,132,133,134,135,136,137,138,139,140,141,143,164,165,166,],[-96,-97,-99,-73,-68,80,-54,-57,-61,-67,-69,-70,-71,-72,-62,-64,-65,-63,-73,-68,-76,80,80,-50,-51,-52,-53,-55,-56,-58,-59,-60,-74,-75,-66,-77,]),'MAIOR_Q':([10,11,12,35,36,42,43,44,45,47,51,52,53,54,89,90,91,92,117,118,123,131,132,133,134,135,136,137,138,139,140,141,143,164,165,166,],[-96,-97,-99,-73,-68,81,-54,-57,-61,-67,-69,-70,-71,-72,-62,-64,-65,-63,-73,-68,-76,81,81,-50,-51,-52,-53,-55,-56,-58,-59,-60,-74,-75,-66,-77,]),'MAIOR_IGUAL':([10,11,12,35,36,42,43,44,45,47,51,52,53,54,89,90,91,92,117,118,123,131,132,133,134,135,136,137,138,139,140,141,143,164,165,166,],[-96,-97,-99,-73,-68,82,-54,-57,-61,-67,-69,-70,-71,-72,-62,-64,-65,-63,-73,-68,-76,82,82,-50,-51,-52,-53,-55,-56,-58,-59,-60,-74,-75,-66,-77,]),'MENOR_IGUAL':([10,11,12,35,36,42,43,44,45,47,51,52,53,54,89,90,91,92,117,118,123,131,132,133,134,135,136,137,138,139,140,141,143,164,165,166,],[-96,-97,-99,-73,-68,83,-54,-57,-61,-67,-69,-70,-71,-72,-62,-64,-65,-63,-73,-68,-76,83,83,-50,-51,-52,-53,-55,-56,-58,-59,-60,-74,-75,-66,-77,]),'IGUAL':([10,11,12,35,36,41,42,43,44,45,47,51,52,53,54,89,90,91,92,117,118,123,129,130,131,132,133,134,135,136,137,138,139,140,141,143,164,165,166,],[-96,-97,-99,-73,-68,78,-49,-54,-57,-61,-67,-69,-70,-71,-72,-62,-64,-65,-63,-73,-68,-76,78,78,-47,-48,-50,-51,-52,-53,-55,-56,-58,-59,-60,-74,-75,-66,-77,]),'DIFERENTE':([10,11,12,35,36,41,42,43,44,45,47,51,52,53,54,89,90,91,92,117,118,123,129,130,131,132,133,134,135,136,137,138,139,140,141,143,164,165,166,],[-96,-97,-99,-73,-68,79,-49,-54,-57,-61,-67,-69,-70,-71,-72,-62,-64,-65,-63,-73,-68,-76,79,79,-47,-48,-50,-51,-52,-53,-55,-56,-58,-59,-60,-74,-75,-66,-77,]),'OP_OU_EX':([10,11,12,35,36,40,41,42,43,44,45,47,51,52,53,54,89,90,91,92,117,118,123,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,143,164,165,166,],[-96,-97,-99,-73,-68,76,-46,-49,-54,-57,-61,-67,-69,-70,-71,-72,-62,-64,-65,-63,-73,-68,-76,76,76,-44,-45,-47,-48,-50,-51,-52,-53,-55,-56,-58,-59,-60,-74,-75,-66,-77,]),'XOR':([10,11,12,35,36,40,41,42,43,44,45,47,51,52,53,54,89,90,91,92,117,118,123,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,143,164,165,166,],[-96,-97,-99,-73,-68,77,-46,-49,-54,-57,-61,-67,-69,-70,-71,-72,-62,-64,-65,-63,-73,-68,-76,77,77,-44,-45,-47,-48,-50,-51,-52,-53,-55,-56,-58,-59,-60,-74,-75,-66,-77,]),'OP_E':([10,11,12,35,36,39,40,41,42,43,44,45,47,51,52,53,54,89,90,91,92,117,118,123,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,143,164,165,166,],[-96,-97,-99,-73,-68,74,-43,-46,-49,-54,-57,-61,-67,-69,-70,-71,-72,-62,-64,-65,-63,-73,-68,-76,74,74,-41,-42,-44,-45,-47,-48,-50,-51,-52,-53,-55,-56,-58,-59,-60,-74,-75,-66,-77,]),'AND':([10,11,12,35,36,39,40,41,42,43,44,45,47,51,52,53,54,89,90,91,92,117,118,123,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,143,164,165,166,],[-96,-97,-99,-73,-68,75,-43,-46,-49,-54,-57,-61,-67,-69,-70,-71,-72,-62,-64,-65,-63,-73,-68,-76,75,75,-41,-42,-44,-45,-47,-48,-50,-51,-52,-53,-55,-56,-58,-59,-60,-74,-75,-66,-77,]),'OP_OU':([10,11,12,35,36,38,39,40,41,42,43,44,45,47,51,52,53,54,89,90,91,92,117,118,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,143,164,165,166,],[-96,-97,-99,-73,-68,72,-40,-43,-46,-49,-54,-57,-61,-67,-69,-70,-71,-72,-62,-64,-65,-63,-73,-68,-76,72,-38,-39,-41,-42,-44,-45,-47,-48,-50,-51,-52,-53,-55,-56,-58,-59,-60,-74,-75,-66,-77,]),'OR':([10,11,12,35,36,38,39,40,41,42,43,44,45,47,51,52,53,54,89,90,91,92,117,118,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,143,164,165,166,],[-96,-97,-99,-73,-68,73,-40,-43,-46,-49,-54,-57,-61,-67,-69,-70,-71,-72,-62,-64,-65,-63,-73,-68,-76,73,-38,-39,-41,-42,-44,-45,-47,-48,-50,-51,-52,-53,-55,-56,-58,-59,-60,-74,-75,-66,-77,]),'PONTO_VIRG':([10,11,12,17,20,23,25,28,35,36,37,38,39,40,41,42,43,44,45,47,51,52,53,54,56,60,61,70,71,89,90,91,92,96,98,111,117,118,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,143,145,148,149,154,161,163,164,165,166,167,176,177,184,186,],[-96,-97,-99,23,29,-19,-21,60,-73,-68,70,-37,-40,-43,-46,-49,-54,-57,-61,-67,-69,-70,-71,-72,98,-23,-24,-20,-22,-62,-64,-65,-63,-25,-27,155,-73,-68,-76,-36,-38,-39,-41,-42,-44,-45,-47,-48,-50,-51,-52,-53,-55,-56,-58,-59,-60,-74,98,-8,23,170,23,177,-75,-66,-77,-26,183,185,193,195,]),'RECEBER':([10,11,12,17,35,36,37,38,39,40,41,42,43,44,45,47,51,52,53,54,56,89,90,91,92,94,111,117,118,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,143,144,145,149,154,161,164,165,166,168,169,172,174,180,184,186,192,194,199,200,209,],[-96,-97,-99,24,-73,-68,69,-37,-40,-43,-46,-49,-54,-57,-61,-67,-69,-70,-71,-72,97,-62,-64,-65,-63,69,69,-73,-68,-76,-36,-38,-39,-41,-42,-44,-45,-47,-48,-50,-51,-52,-53,-55,-56,-58,-59,-60,-74,69,69,24,69,24,-75,-66,-77,69,69,69,69,69,69,69,69,69,69,69,69,]),'VIRGULA':([10,11,12,17,28,35,36,37,38,39,40,41,42,43,44,45,47,51,52,53,54,56,63,89,90,91,92,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,143,145,149,161,164,165,166,],[-96,-97,-99,26,26,-73,-68,26,-37,-40,-43,-46,-49,-54,-57,-61,-67,-69,-70,-71,-72,26,106,-62,-64,-65,-63,-76,-36,-38,-39,-41,-42,-44,-45,-47,-48,-50,-51,-52,-53,-55,-56,-58,-59,-60,-74,26,26,26,-75,-66,-77,]),'PARENT_FECHA':([10,11,12,22,27,32,34,35,36,38,39,40,41,42,43,44,45,47,51,52,53,54,57,58,63,68,89,90,91,92,94,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,150,164,165,166,172,174,175,180,183,185,192,193,194,195,199,200,209,],[-96,-97,-99,33,59,64,67,-73,-68,-37,-40,-43,-46,-49,-54,-57,-61,-67,-69,-70,-71,-72,99,100,-17,123,-62,-64,-65,-63,143,164,-76,-36,-38,-39,-41,-42,-44,-45,-47,-48,-50,-51,-52,-53,-55,-56,-58,-59,-60,165,-74,166,-18,-75,-66,-77,179,181,182,189,-88,-95,-91,-89,-94,-93,-90,-92,210,]),'CHAVE_FECHA':([10,11,12,23,25,35,36,38,39,40,41,42,43,44,45,47,51,52,53,54,60,61,65,66,70,71,89,90,91,92,96,98,101,102,103,104,107,108,109,112,113,115,116,121,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,143,146,147,151,155,157,160,164,165,166,167,168,169,170,171,178,190,191,197,198,205,207,],[-96,-97,-99,-19,-21,-73,-68,-37,-40,-43,-46,-49,-54,-57,-61,-67,-69,-70,-71,-72,-23,-24,-12,109,-20,-22,-62,-64,-65,-63,-25,-27,-15,148,-9,-10,-11,151,-29,-32,-33,-79,-81,-13,-76,-36,-38,-39,-41,-42,-44,-45,-47,-48,-50,-51,-52,-53,-55,-56,-58,-59,-60,-74,-16,-14,-28,-35,-80,-82,-75,-66,-77,-26,178,-31,-83,-34,-30,-86,-87,-84,-32,-78,-85,]),'IF':([10,11,12,23,25,35,36,38,39,40,41,42,43,44,45,47,51,52,53,54,60,61,66,70,71,89,90,91,92,96,98,109,115,116,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,143,151,155,164,165,166,167,169,178,179,188,189,190,191,201,204,],[-96,-97,-99,-19,-21,-73,-68,-37,-40,-43,-46,-49,-54,-57,-61,-67,-69,-70,-71,-72,-23,-24,114,-20,-22,-62,-64,-65,-63,-25,-27,-29,158,158,-76,-36,-38,-39,-41,-42,-44,-45,-47,-48,-50,-51,-52,-53,-55,-56,-58,-59,-60,-74,-28,114,-75,-66,-77,-26,-31,-30,158,114,158,-86,-87,158,206,]),'RETURN':([10,11,12,23,25,35,36,38,39,40,41,42,43,44,45,47,51,52,53,54,60,61,66,70,71,89,90,91,92,96,98,108,109,112,113,115,116,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,143,151,155,157,160,164,165,166,167,169,170,171,178,179,188,189,190,191,197,198,201,205,207,],[-96,-97,-99,-19,-21,-73,-68,-37,-40,-43,-46,-49,-54,-57,-61,-67,-69,-70,-71,-72,-23,-24,110,-20,-22,-62,-64,-65,-63,-25,-27,152,153,-32,-33,110,110,-76,-36,-38,-39,-41,-42,-44,-45,-47,-48,-50,-51,-52,-53,-55,-56,-58,-59,-60,-74,-28,110,-80,-82,-75,-66,-77,-26,-31,-83,-34,-30,110,110,110,-86,-87,-84,-32,110,-78,-85,]),'WHILE':([10,11,12,23,25,35,36,38,39,40,41,42,43,44,45,47,51,52,53,54,60,61,66,70,71,89,90,91,92,96,98,109,115,116,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,143,151,155,164,165,166,167,169,178,179,188,189,190,191,201,],[-96,-97,-99,-19,-21,-73,-68,-37,-40,-43,-46,-49,-54,-57,-61,-67,-69,-70,-71,-72,-23,-24,119,-20,-22,-62,-64,-65,-63,-25,-27,-29,119,119,-76,-36,-38,-39,-41,-42,-44,-45,-47,-48,-50,-51,-52,-53,-55,-56,-58,-59,-60,-74,-28,119,-75,-66,-77,-26,-31,-30,119,119,119,-86,-87,119,]),'FOR':([10,11,12,23,25,35,36,38,39,40,41,42,43,44,45,47,51,52,53,54,60,61,66,70,71,89,90,91,92,96,98,109,115,116,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,143,151,155,164,165,166,167,169,178,179,188,189,190,191,201,],[-96,-97,-99,-19,-21,-73,-68,-37,-40,-43,-46,-49,-54,-57,-61,-67,-69,-70,-71,-72,-23,-24,120,-20,-22,-62,-64,-65,-63,-25,-27,-29,120,120,-76,-36,-38,-39,-41,-42,-44,-45,-47,-48,-50,-51,-52,-53,-55,-56,-58,-59,-60,-74,-28,120,-75,-66,-77,-26,-31,-30,120,120,120,-86,-87,120,]),'OP_NOT':([10,11,12,23,24,25,35,36,38,39,40,41,42,43,44,45,47,50,51,52,53,54,60,61,66,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,95,96,97,98,109,110,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,143,151,152,153,155,156,162,164,165,166,167,169,173,176,177,178,183,185,188,193,195,208,],[-96,-97,-99,-19,46,-21,-73,-68,-37,-40,-43,-46,-49,-54,-57,-61,-67,46,-69,-70,-71,-72,-23,-24,46,46,-20,-22,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,-62,-64,-65,-63,46,-25,46,-27,-29,46,-76,-36,-38,-39,-41,-42,-44,-45,-47,-48,-50,-51,-52,-53,-55,-56,-58,-59,-60,-74,-28,46,46,46,46,46,-75,-66,-77,-26,-31,46,46,46,-30,46,46,46,46,46,46,]),'NOT':([10,11,12,23,24,25,35,36,38,39,40,41,42,43,44,45,47,50,51,52,53,54,60,61,66,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,95,96,97,98,109,110,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,143,151,152,153,155,156,162,164,165,166,167,169,173,176,177,178,183,185,188,193,195,208,],[-96,-97,-99,-19,48,-21,-73,-68,-37,-40,-43,-46,-49,-54,-57,-61,-67,48,-69,-70,-71,-72,-23,-24,48,48,-20,-22,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,-62,-64,-65,-63,48,-25,48,-27,-29,48,-76,-36,-38,-39,-41,-42,-44,-45,-47,-48,-50,-51,-52,-53,-55,-56,-58,-59,-60,-74,-28,48,48,48,48,48,-75,-66,-77,-26,-31,48,48,48,-30,48,48,48,48,48,48,]),'SIZEOF':([10,11,12,23,24,25,35,36,38,39,40,41,42,43,44,45,47,50,51,52,53,54,60,61,66,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,95,96,97,98,109,110,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,143,151,152,153,155,156,162,164,165,166,167,169,173,176,177,178,183,185,188,193,195,208,],[-96,-97,-99,-19,49,-21,-73,-68,-37,-40,-43,-46,-49,-54,-57,-61,-67,49,-69,-70,-71,-72,-23,-24,49,49,-20,-22,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,-62,-64,-65,-63,49,-25,49,-27,-29,49,-76,-36,-38,-39,-41,-42,-44,-45,-47,-48,-50,-51,-52,-53,-55,-56,-58,-59,-60,-74,-28,49,49,49,49,49,-75,-66,-77,-26,-31,49,49,49,-30,49,49,49,49,49,49,]),'INT_V':([10,11,12,23,24,25,35,36,38,39,40,41,42,43,44,45,46,47,48,50,51,52,53,54,60,61,66,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,95,96,97,98,109,110,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,143,151,152,153,155,156,162,164,165,166,167,169,173,176,177,178,183,185,188,193,195,208,],[-96,-97,-99,-19,51,-21,-73,-68,-37,-40,-43,-46,-49,-54,-57,-61,51,-67,51,51,-69,-70,-71,-72,-23,-24,51,51,-20,-22,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,-62,-64,-65,-63,51,51,-25,51,-27,-29,51,-76,-36,-38,-39,-41,-42,-44,-45,-47,-48,-50,-51,-52,-53,-55,-56,-58,-59,-60,-74,-28,51,51,51,51,51,-75,-66,-77,-26,-31,51,51,51,-30,51,51,51,51,51,51,]),'TRUE':([10,11,12,23,24,25,35,36,38,39,40,41,42,43,44,45,46,47,48,50,51,52,53,54,60,61,66,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,95,96,97,98,109,110,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,143,151,152,153,155,156,162,164,165,166,167,169,173,176,177,178,183,185,188,193,195,208,],[-96,-97,-99,-19,52,-21,-73,-68,-37,-40,-43,-46,-49,-54,-57,-61,52,-67,52,52,-69,-70,-71,-72,-23,-24,52,52,-20,-22,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,-62,-64,-65,-63,52,52,-25,52,-27,-29,52,-76,-36,-38,-39,-41,-42,-44,-45,-47,-48,-50,-51,-52,-53,-55,-56,-58,-59,-60,-74,-28,52,52,52,52,52,-75,-66,-77,-26,-31,52,52,52,-30,52,52,52,52,52,52,]),'FALSE':([10,11,12,23,24,25,35,36,38,39,40,41,42,43,44,45,46,47,48,50,51,52,53,54,60,61,66,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,95,96,97,98,109,110,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,143,151,152,153,155,156,162,164,165,166,167,169,173,176,177,178,183,185,188,193,195,208,],[-96,-97,-99,-19,53,-21,-73,-68,-37,-40,-43,-46,-49,-54,-57,-61,53,-67,53,53,-69,-70,-71,-72,-23,-24,53,53,-20,-22,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,-62,-64,-65,-63,53,53,-25,53,-27,-29,53,-76,-36,-38,-39,-41,-42,-44,-45,-47,-48,-50,-51,-52,-53,-55,-56,-58,-59,-60,-74,-28,53,53,53,53,53,-75,-66,-77,-26,-31,53,53,53,-30,53,53,53,53,53,53,]),'PARENT_ABRE':([10,11,12,17,18,23,24,25,35,36,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,60,61,66,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,95,96,97,98,109,110,114,118,119,120,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,143,149,151,152,153,155,156,158,162,164,165,166,167,169,173,176,177,178,183,185,188,193,195,206,208,],[-96,-97,-99,22,27,-19,50,-21,-73,68,-37,-40,-43,-46,-49,-54,-57,-61,50,-67,50,93,50,-69,-70,-71,-72,95,-23,-24,50,50,-20,-22,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,-62,-64,-65,-63,50,50,-25,50,-27,-29,50,156,68,162,163,-76,-36,-38,-39,-41,-42,-44,-45,-47,-48,-50,-51,-52,-53,-55,-56,-58,-59,-60,-74,22,-28,50,50,50,50,173,50,-75,-66,-77,-26,-31,50,50,50,-30,50,50,50,50,50,208,50,]),'TYPEID':([10,11,12,23,24,25,35,36,38,39,40,41,42,43,44,45,46,47,48,50,51,52,53,54,60,61,66,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,95,96,97,98,109,110,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,143,151,152,153,155,156,162,164,165,166,167,169,173,176,177,178,183,185,188,193,195,208,],[-96,-97,-99,-19,55,-21,-73,-68,-37,-40,-43,-46,-49,-54,-57,-61,55,-67,55,55,-69,-70,-71,-72,-23,-24,55,55,-20,-22,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,-62,-64,-65,-63,55,55,-25,55,-27,-29,55,-76,-36,-38,-39,-41,-42,-44,-45,-47,-48,-50,-51,-52,-53,-55,-56,-58,-59,-60,-74,-28,55,55,55,55,55,-75,-66,-77,-26,-31,55,55,55,-30,55,55,55,55,55,55,]),'CHAVE_ABRE':([10,11,12,16,23,25,33,35,36,38,39,40,41,42,43,44,45,47,51,52,53,54,59,60,61,64,67,70,71,89,90,91,92,96,98,99,100,109,115,116,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,143,151,157,160,164,165,166,167,169,170,178,179,181,182,187,190,191,202,203,205,210,],[-96,-97,-99,21,-19,-21,66,-73,-68,-37,-40,-43,-46,-49,-54,-57,-61,-67,-69,-70,-71,-72,66,-23,-24,66,66,-20,-22,-62,-64,-65,-63,-25,-27,66,66,-29,-79,-81,-76,-36,-38,-39,-41,-42,-44,-45,-47,-48,-50,-51,-52,-53,-55,-56,-58,-59,-60,-74,-28,-80,-82,-75,-66,-77,-26,-31,-83,-30,66,66,66,66,-86,-87,66,66,-78,66,]),'ELSE':([10,11,12,23,25,35,36,38,39,40,41,42,43,44,45,47,51,52,53,54,60,61,70,71,89,90,91,92,96,98,109,115,116,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,143,151,157,160,164,165,166,167,169,170,178,190,191,196,198,205,],[-96,-97,-99,-19,-21,-73,-68,-37,-40,-43,-46,-49,-54,-57,-61,-67,-69,-70,-71,-72,-23,-24,-20,-22,-62,-64,-65,-63,-25,-27,-29,-79,-81,-76,-36,-38,-39,-41,-42,-44,-45,-47,-48,-50,-51,-52,-53,-55,-56,-58,-59,-60,-74,-28,-80,-82,-75,-66,-77,-26,-31,-83,-30,-86,-87,201,202,-78,]),'PUBLIC':([21,],[30,]),'DOIS_PONTOS':([30,],[62,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'cpp':([0,2,3,4,],[1,13,14,15,]),'decl_classe':([0,2,3,4,],[2,2,2,2,]),'decl_funcao':([0,2,3,4,62,],[3,3,3,3,104,]),'decl_variavel':([0,2,3,4,62,66,115,116,155,163,179,188,189,201,],[4,4,4,4,103,115,115,115,115,176,115,115,115,115,]),'tipo':([0,2,3,4,9,22,24,27,46,48,50,62,66,68,69,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,93,95,97,106,110,115,116,152,153,155,156,162,163,173,176,177,179,183,185,188,189,193,195,201,208,],[7,7,7,7,19,31,35,31,35,35,35,105,117,31,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,31,35,159,159,35,35,117,35,35,159,35,35,35,159,35,35,117,159,35,35,159,35,]),'body_class':([16,],[20,]),'decl_variavel_n':([17,28,37,56,145,149,161,],[25,61,71,96,167,25,25,]),'parametros':([22,27,68,106,],[32,58,122,150,]),'exp':([24,50,66,95,97,110,152,153,155,156,162,173,176,177,183,185,188,193,195,208,],[37,94,111,144,145,154,168,169,111,172,174,180,184,186,192,194,111,199,200,209,]),'exp_1':([24,50,66,69,95,97,110,152,153,155,156,162,173,176,177,183,185,188,193,195,208,],[38,38,38,124,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,]),'exp_2':([24,50,66,69,72,73,95,97,110,152,153,155,156,162,173,176,177,183,185,188,193,195,208,],[39,39,39,39,125,126,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,]),'exp_3':([24,50,66,69,72,73,74,75,95,97,110,152,153,155,156,162,173,176,177,183,185,188,193,195,208,],[40,40,40,40,40,40,127,128,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,]),'exp_4':([24,50,66,69,72,73,74,75,76,77,95,97,110,152,153,155,156,162,173,176,177,183,185,188,193,195,208,],[41,41,41,41,41,41,41,41,129,130,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,]),'exp_5':([24,50,66,69,72,73,74,75,76,77,78,79,95,97,110,152,153,155,156,162,173,176,177,183,185,188,193,195,208,],[42,42,42,42,42,42,42,42,42,42,131,132,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,]),'exp_6':([24,50,66,69,72,73,74,75,76,77,78,79,80,81,82,83,95,97,110,152,153,155,156,162,173,176,177,183,185,188,193,195,208,],[43,43,43,43,43,43,43,43,43,43,43,43,133,134,135,136,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,]),'exp_7':([24,50,66,69,72,73,74,75,76,77,78,79,80,81,82,83,84,85,95,97,110,152,153,155,156,162,173,176,177,183,185,188,193,195,208,],[44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,137,138,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,]),'exp_8':([24,50,66,69,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,95,97,110,152,153,155,156,162,173,176,177,183,185,188,193,195,208,],[45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,139,140,141,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,]),'exp_9':([24,46,48,50,66,69,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,93,95,97,110,152,153,155,156,162,173,176,177,183,185,188,193,195,208,],[47,89,92,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,142,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,]),'chamada_funcao':([24,46,48,50,66,69,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,93,95,97,110,152,153,155,156,162,173,176,177,183,185,188,193,195,208,],[54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,]),'body':([33,59,64,67,99,100,179,181,182,187,202,203,210,],[65,101,107,121,146,147,188,190,191,196,204,205,188,]),'content_class':([62,],[102,]),'comandos':([66,155,188,],[108,171,197,]),'condicional_1':([66,115,116,155,179,188,189,201,],[112,157,160,112,187,198,187,203,]),'condicional_2':([66,155,188,204,],[113,113,113,207,]),'repeticao':([66,115,116,155,179,188,189,201,],[116,116,116,116,116,116,116,116,]),'for_log':([163,],[175,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> cpp","S'",1,None,None,None),
  ('cpp -> decl_classe','cpp',1,'p_cpp','sintatico.py',25),
  ('cpp -> decl_funcao','cpp',1,'p_cpp','sintatico.py',26),
  ('cpp -> decl_variavel','cpp',1,'p_cpp','sintatico.py',27),
  ('cpp -> decl_classe cpp','cpp',2,'p_cpp','sintatico.py',28),
  ('cpp -> decl_funcao cpp','cpp',2,'p_cpp','sintatico.py',29),
  ('cpp -> decl_variavel cpp','cpp',2,'p_cpp','sintatico.py',30),
  ('decl_classe -> CLASS ID body_class PONTO_VIRG','decl_classe',4,'p_decl_classe','sintatico.py',34),
  ('body_class -> CHAVE_ABRE PUBLIC DOIS_PONTOS content_class CHAVE_FECHA','body_class',5,'p_body_class','sintatico.py',37),
  ('content_class -> decl_variavel','content_class',1,'p_content_class','sintatico.py',40),
  ('content_class -> decl_funcao','content_class',1,'p_content_class','sintatico.py',41),
  ('decl_funcao -> tipo ID PARENT_ABRE parametros PARENT_FECHA body','decl_funcao',6,'p_decl_funcao','sintatico.py',44),
  ('decl_funcao -> tipo ID PARENT_ABRE PARENT_FECHA body','decl_funcao',5,'p_decl_funcao','sintatico.py',45),
  ('decl_funcao -> tipo ID PARENT_ABRE VOID PARENT_FECHA body','decl_funcao',6,'p_decl_funcao','sintatico.py',46),
  ('decl_funcao -> VOID ID PARENT_ABRE parametros PARENT_FECHA body','decl_funcao',6,'p_decl_funcao','sintatico.py',47),
  ('decl_funcao -> VOID ID PARENT_ABRE PARENT_FECHA body','decl_funcao',5,'p_decl_funcao','sintatico.py',48),
  ('decl_funcao -> VOID ID PARENT_ABRE VOID PARENT_FECHA body','decl_funcao',6,'p_decl_funcao','sintatico.py',49),
  ('parametros -> tipo ID','parametros',2,'p_parametros','sintatico.py',52),
  ('parametros -> tipo ID VIRGULA parametros','parametros',4,'p_parametros','sintatico.py',53),
  ('decl_variavel -> tipo ID PONTO_VIRG','decl_variavel',3,'p_decl_variavel','sintatico.py',56),
  ('decl_variavel -> tipo ID RECEBER exp PONTO_VIRG','decl_variavel',5,'p_decl_variavel','sintatico.py',57),
  ('decl_variavel -> tipo ID decl_variavel_n','decl_variavel',3,'p_decl_variavel','sintatico.py',58),
  ('decl_variavel -> tipo ID RECEBER exp decl_variavel_n','decl_variavel',5,'p_decl_variavel','sintatico.py',59),
  ('decl_variavel -> TYPEDEF tipo ID PONTO_VIRG','decl_variavel',4,'p_decl_variavel','sintatico.py',60),
  ('decl_variavel -> TYPEDEF tipo ID decl_variavel_n','decl_variavel',4,'p_decl_variavel','sintatico.py',61),
  ('decl_variavel_n -> VIRGULA ID decl_variavel_n','decl_variavel_n',3,'p_decl_variavel_n','sintatico.py',64),
  ('decl_variavel_n -> VIRGULA ID RECEBER exp decl_variavel_n','decl_variavel_n',5,'p_decl_variavel_n','sintatico.py',65),
  ('decl_variavel_n -> PONTO_VIRG','decl_variavel_n',1,'p_decl_variavel_n','sintatico.py',66),
  ('body -> CHAVE_ABRE comandos CHAVE_FECHA','body',3,'p_body','sintatico.py',69),
  ('body -> CHAVE_ABRE CHAVE_FECHA','body',2,'p_body','sintatico.py',70),
  ('body -> CHAVE_ABRE comandos RETURN exp CHAVE_FECHA','body',5,'p_body','sintatico.py',71),
  ('body -> CHAVE_ABRE CHAVE_FECHA RETURN exp','body',4,'p_body','sintatico.py',72),
  ('comandos -> condicional_1','comandos',1,'p_comandos','sintatico.py',75),
  ('comandos -> condicional_2','comandos',1,'p_comandos','sintatico.py',76),
  ('comandos -> exp PONTO_VIRG comandos','comandos',3,'p_comandos','sintatico.py',77),
  ('comandos -> exp PONTO_VIRG','comandos',2,'p_comandos','sintatico.py',78),
  ('exp -> exp RECEBER exp_1','exp',3,'p_exp','sintatico.py',81),
  ('exp -> exp_1','exp',1,'p_exp','sintatico.py',82),
  ('exp_1 -> exp_1 OP_OU exp_2','exp_1',3,'p_exp_1','sintatico.py',85),
  ('exp_1 -> exp_1 OR exp_2','exp_1',3,'p_exp_1','sintatico.py',86),
  ('exp_1 -> exp_2','exp_1',1,'p_exp_1','sintatico.py',87),
  ('exp_2 -> exp_2 OP_E exp_3','exp_2',3,'p_exp_2','sintatico.py',90),
  ('exp_2 -> exp_2 AND exp_3','exp_2',3,'p_exp_2','sintatico.py',91),
  ('exp_2 -> exp_3','exp_2',1,'p_exp_2','sintatico.py',92),
  ('exp_3 -> exp_3 OP_OU_EX exp_4','exp_3',3,'p_exp_3','sintatico.py',95),
  ('exp_3 -> exp_3 XOR exp_4','exp_3',3,'p_exp_3','sintatico.py',96),
  ('exp_3 -> exp_4','exp_3',1,'p_exp_3','sintatico.py',97),
  ('exp_4 -> exp_4 IGUAL exp_5','exp_4',3,'p_exp_4','sintatico.py',100),
  ('exp_4 -> exp_4 DIFERENTE exp_5','exp_4',3,'p_exp_4','sintatico.py',101),
  ('exp_4 -> exp_5','exp_4',1,'p_exp_4','sintatico.py',102),
  ('exp_5 -> exp_5 MENOR_Q exp_6','exp_5',3,'p_exp_5','sintatico.py',105),
  ('exp_5 -> exp_5 MAIOR_Q exp_6','exp_5',3,'p_exp_5','sintatico.py',106),
  ('exp_5 -> exp_5 MAIOR_IGUAL exp_6','exp_5',3,'p_exp_5','sintatico.py',107),
  ('exp_5 -> exp_5 MENOR_IGUAL exp_6','exp_5',3,'p_exp_5','sintatico.py',108),
  ('exp_5 -> exp_6','exp_5',1,'p_exp_5','sintatico.py',109),
  ('exp_6 -> exp_6 SOMA exp_7','exp_6',3,'p_exp_6','sintatico.py',112),
  ('exp_6 -> exp_6 SUB exp_7','exp_6',3,'p_exp_6','sintatico.py',113),
  ('exp_6 -> exp_7','exp_6',1,'p_exp_6','sintatico.py',114),
  ('exp_7 -> exp_7 MULT exp_8','exp_7',3,'p_exp_7','sintatico.py',117),
  ('exp_7 -> exp_7 DIV exp_8','exp_7',3,'p_exp_7','sintatico.py',118),
  ('exp_7 -> exp_7 MODULO exp_8','exp_7',3,'p_exp_7','sintatico.py',119),
  ('exp_7 -> exp_8','exp_7',1,'p_exp_7','sintatico.py',120),
  ('exp_8 -> OP_NOT exp_9','exp_8',2,'p_exp_8','sintatico.py',123),
  ('exp_8 -> NOT exp_9','exp_8',2,'p_exp_8','sintatico.py',124),
  ('exp_8 -> exp_9 MAIS_MAIS','exp_8',2,'p_exp_8','sintatico.py',125),
  ('exp_8 -> exp_9 MENOS_MENOS','exp_8',2,'p_exp_8','sintatico.py',126),
  ('exp_8 -> SIZEOF PARENT_ABRE exp_9 PARENT_FECHA','exp_8',4,'p_exp_8','sintatico.py',127),
  ('exp_8 -> exp_9','exp_8',1,'p_exp_8','sintatico.py',128),
  ('exp_9 -> ID','exp_9',1,'p_exp_9','sintatico.py',131),
  ('exp_9 -> INT_V','exp_9',1,'p_exp_9','sintatico.py',132),
  ('exp_9 -> TRUE','exp_9',1,'p_exp_9','sintatico.py',133),
  ('exp_9 -> FALSE','exp_9',1,'p_exp_9','sintatico.py',134),
  ('exp_9 -> chamada_funcao','exp_9',1,'p_exp_9','sintatico.py',135),
  ('exp_9 -> tipo','exp_9',1,'p_exp_9','sintatico.py',136),
  ('exp_9 -> PARENT_ABRE exp PARENT_FECHA','exp_9',3,'p_exp_9','sintatico.py',137),
  ('chamada_funcao -> ID PARENT_ABRE parametros PARENT_FECHA','chamada_funcao',4,'p_chamada_funcao','sintatico.py',140),
  ('chamada_funcao -> ID PARENT_ABRE PARENT_FECHA','chamada_funcao',3,'p_chamada_funcao','sintatico.py',141),
  ('chamada_funcao -> TYPEID PARENT_ABRE exp PARENT_FECHA','chamada_funcao',4,'p_chamada_funcao','sintatico.py',142),
  ('condicional_1 -> IF PARENT_ABRE exp PARENT_FECHA condicional_1 body ELSE condicional_1 body','condicional_1',9,'p_condicional_1','sintatico.py',149),
  ('condicional_1 -> decl_variavel','condicional_1',1,'p_condicional_1','sintatico.py',150),
  ('condicional_1 -> decl_variavel condicional_1','condicional_1',2,'p_condicional_1','sintatico.py',151),
  ('condicional_1 -> repeticao','condicional_1',1,'p_condicional_1','sintatico.py',152),
  ('condicional_1 -> repeticao condicional_1','condicional_1',2,'p_condicional_1','sintatico.py',153),
  ('condicional_1 -> RETURN exp PONTO_VIRG','condicional_1',3,'p_condicional_1','sintatico.py',154),
  ('condicional_2 -> IF PARENT_ABRE exp PARENT_FECHA body comandos','condicional_2',6,'p_condicional_2','sintatico.py',157),
  ('condicional_2 -> IF PARENT_ABRE exp PARENT_FECHA body condicional_1 ELSE body condicional_2','condicional_2',9,'p_condicional_2','sintatico.py',158),
  ('repeticao -> WHILE PARENT_ABRE exp PARENT_FECHA body','repeticao',5,'p_repeticao','sintatico.py',161),
  ('repeticao -> FOR PARENT_ABRE for_log PARENT_FECHA body','repeticao',5,'p_repeticao','sintatico.py',162),
  ('for_log -> decl_variavel PONTO_VIRG','for_log',2,'p_for_log','sintatico.py',166),
  ('for_log -> decl_variavel exp PONTO_VIRG','for_log',3,'p_for_log','sintatico.py',167),
  ('for_log -> decl_variavel exp PONTO_VIRG exp','for_log',4,'p_for_log','sintatico.py',168),
  ('for_log -> decl_variavel PONTO_VIRG exp','for_log',3,'p_for_log','sintatico.py',169),
  ('for_log -> PONTO_VIRG exp PONTO_VIRG exp','for_log',4,'p_for_log','sintatico.py',170),
  ('for_log -> PONTO_VIRG exp PONTO_VIRG','for_log',3,'p_for_log','sintatico.py',171),
  ('for_log -> PONTO_VIRG PONTO_VIRG exp','for_log',3,'p_for_log','sintatico.py',172),
  ('for_log -> PONTO_VIRG PONTO_VIRG','for_log',2,'p_for_log','sintatico.py',173),
  ('tipo -> INT','tipo',1,'p_tipo','sintatico.py',176),
  ('tipo -> BOOL','tipo',1,'p_tipo','sintatico.py',177),
  ('tipo -> ID','tipo',1,'p_tipo','sintatico.py',178),
  ('tipo -> STRING','tipo',1,'p_tipo','sintatico.py',179),
]

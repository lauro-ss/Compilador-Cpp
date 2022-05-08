
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND BOOL CHAVE_ABRE CHAVE_FECHA CLASS COLCHETE_ABRE COLCHETE_FECHA COMENTARIO DIFERENTE DIV DOIS_PONTOS ELSE ENDERECO FALSE FOR ID IF IGUAL INT INT_V MAIOR_IGUAL MAIOR_Q MAIS_MAIS MENOR_IGUAL MENOR_Q MENOS_MENOS MODULO MULT NAMESPACE NEW NOT OP_E OP_NOT OP_OU OP_OU_EX OR PARENT_ABRE PARENT_FECHA PONTO PONTO_VIRG PUBLIC RECEBER RETURN SETA SIZEOF SOMA STATIC STRING STRUCT SUB THIS TRUE TRY TYPEDEF TYPEID USING VIRGULA VOID WHILE XORcpp : decl_classe\n         | decl_funcao\n         | decl_variavel\n         | decl_classe  cpp\n         | decl_funcao  cpp\n         | decl_variavel cppdecl_classe : CLASS ID body_class PONTO_VIRGbody_class : CHAVE_ABRE PUBLIC DOIS_PONTOS content_class CHAVE_FECHAcontent_class : decl_variavel content_class\n                   | decl_funcao content_class\n                   | decl_variavel\n                   | decl_funcaodecl_funcao : tipo ID PARENT_ABRE parametros PARENT_FECHA body\n                 | tipo ID PARENT_ABRE PARENT_FECHA body\n                 | tipo ID PARENT_ABRE VOID PARENT_FECHA body\n                 | VOID ID PARENT_ABRE parametros PARENT_FECHA body\n                 | VOID ID PARENT_ABRE PARENT_FECHA body\n                 | VOID ID PARENT_ABRE VOID PARENT_FECHA bodyparametros : tipo ID\n                | tipo ID VIRGULA parametrosdecl_variavel : tipo ID PONTO_VIRG \n                   | tipo ID RECEBER exp PONTO_VIRG\n                   | tipo ID decl_variavel_n PONTO_VIRG \n                   | tipo ID RECEBER exp decl_variavel_n PONTO_VIRG\n                   | TYPEDEF tipo ID PONTO_VIRG\n                   | TYPEDEF tipo ID decl_variavel_ndecl_variavel_n : VIRGULA ID decl_variavel_n\n                     | VIRGULA ID RECEBER exp decl_variavel_n\n                     | VIRGULA ID \n                     body : CHAVE_ABRE comandos CHAVE_FECHA\n            | CHAVE_ABRE CHAVE_FECHA comandos : comando \n               | comando comandoscomando : condicional_1\n               | condicional_2exp : exp RECEBER exp_1\n         | exp_1exp_1 : exp_1 OP_OU exp_2 \n           | exp_1 OR exp_2\n           | exp_2exp_2 : exp_2 OP_E exp_3\n           | exp_2 AND exp_3\n           | exp_3exp_3 : exp_3 OP_OU_EX exp_4\n           | exp_3 XOR exp_4\n           | exp_4exp_4 : exp_4 IGUAL exp_5\n           | exp_4 DIFERENTE exp_5\n           | exp_5exp_5 : exp_5 MENOR_Q exp_6\n           | exp_5 MAIOR_Q exp_6\n           | exp_5 MAIOR_IGUAL exp_6\n           | exp_5 MENOR_IGUAL exp_6\n           | exp_6exp_6 : exp_6 SOMA exp_7\n           | exp_6 SUB exp_7\n           | exp_7exp_7 : exp_7 MULT exp_8\n           | exp_7 DIV exp_8\n           | exp_7 MODULO exp_8\n           | exp_8exp_8 : OP_NOT exp_9\n           | NOT exp_9\n           | exp_9 MAIS_MAIS\n           | exp_9 MENOS_MENOS\n           | SIZEOF PARENT_ABRE exp_9 PARENT_FECHA\n           | exp_9exp_9 : ID\n           | INT_V\n           | TRUE\n           | FALSE\n           | chamada_funcao\n           | STRING\n           | PARENT_ABRE exp PARENT_FECHAchamada_funcao : ID PARENT_ABRE parametros PARENT_FECHA\n                    | ID PARENT_ABRE PARENT_FECHA\n                    | TYPEID PARENT_ABRE exp PARENT_FECHAcondicional_1 : IF PARENT_ABRE exp PARENT_FECHA rest_if\n                     | exp PONTO_VIRG \n                     | decl_variavel\n                     | WHILE PARENT_ABRE exp PARENT_FECHA body\n                     | FOR PARENT_ABRE for_log PARENT_FECHA body\n                     | RETURN exp PONTO_VIRG\n                     | RETURN PONTO_VIRGcondicional_2 : IF PARENT_ABRE exp PARENT_FECHA body\n                     | IF PARENT_ABRE exp PARENT_FECHA condicional_1rest_if : condicional_1 ELSE condicional_1\n               | condicional_1 ELSE body\n               | body ELSE body\n               | body ELSE condicional_1for_log : decl_variavel PONTO_VIRG\n             | decl_variavel exp PONTO_VIRG\n             | decl_variavel exp PONTO_VIRG exp\n             | decl_variavel PONTO_VIRG exp\n             | PONTO_VIRG exp PONTO_VIRG exp\n             | PONTO_VIRG exp PONTO_VIRG\n             | PONTO_VIRG PONTO_VIRG exp\n             | PONTO_VIRG PONTO_VIRGtipo : INT \n          | BOOL \n          | ID\n          | STRING'
    
_lr_action_items = {'CLASS':([0,2,3,4,23,29,56,57,61,62,66,71,97,101,107,109,122,126,148,149,155,167,],[5,5,5,5,-21,-7,-23,-29,-25,-26,-14,-22,-27,-17,-13,-31,-15,-24,-18,-16,-30,-28,]),'VOID':([0,2,3,4,22,23,27,29,56,57,61,62,63,66,71,97,101,103,104,107,109,122,126,148,149,155,167,],[8,8,8,8,34,-21,58,-7,-23,-29,-25,-26,8,-14,-22,-27,-17,8,8,-13,-31,-15,-24,-18,-16,-30,-28,]),'TYPEDEF':([0,2,3,4,23,29,56,57,61,62,63,66,67,71,97,101,103,104,107,109,110,111,112,115,122,126,148,149,155,158,160,162,167,173,174,182,183,184,185,186,192,193,197,198,199,200,201,],[9,9,9,9,-21,-7,-23,-29,-25,-26,9,-14,9,-22,-27,-17,9,9,-13,-31,9,-34,-35,-80,-15,-24,-18,-16,-30,-79,9,-84,-28,-83,9,-78,-85,-86,-81,-82,9,9,-89,-90,-87,-88,9,]),'INT':([0,2,3,4,9,22,23,27,29,56,57,61,62,63,66,67,69,71,97,101,103,104,106,107,109,110,111,112,115,122,126,148,149,155,158,160,162,167,173,174,182,183,184,185,186,192,193,197,198,199,200,201,],[10,10,10,10,10,10,-21,10,-7,-23,-29,-25,-26,10,-14,10,10,-22,-27,-17,10,10,10,-13,-31,10,-34,-35,-80,-15,-24,-18,-16,-30,-79,10,-84,-28,-83,10,-78,-85,-86,-81,-82,10,10,-89,-90,-87,-88,10,]),'BOOL':([0,2,3,4,9,22,23,27,29,56,57,61,62,63,66,67,69,71,97,101,103,104,106,107,109,110,111,112,115,122,126,148,149,155,158,160,162,167,173,174,182,183,184,185,186,192,193,197,198,199,200,201,],[11,11,11,11,11,11,-21,11,-7,-23,-29,-25,-26,11,-14,11,11,-22,-27,-17,11,11,11,-13,-31,11,-34,-35,-80,-15,-24,-18,-16,-30,-79,11,-84,-28,-83,11,-78,-85,-86,-81,-82,11,11,-89,-90,-87,-88,11,]),'ID':([0,2,3,4,5,6,7,8,9,10,11,12,19,22,23,24,26,27,29,31,45,47,49,56,57,61,62,63,66,67,69,70,71,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,94,96,97,98,101,103,104,105,106,107,109,110,111,112,115,118,119,120,121,122,126,148,149,155,157,158,159,160,162,167,171,172,173,174,177,179,182,183,184,185,186,188,190,191,192,193,197,198,199,200,201,],[6,6,6,6,16,-101,17,18,6,-99,-100,-102,28,6,-21,35,57,6,-7,64,35,35,35,-23,-29,-25,-26,6,-14,120,6,35,-22,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,-27,35,-17,6,6,153,6,-13,-31,120,-34,-35,-80,35,163,-101,-102,-15,-24,-18,-16,-30,35,-79,35,6,-84,-28,35,35,-83,120,35,35,-78,-85,-86,-81,-82,35,35,35,120,120,-89,-90,-87,-88,120,]),'STRING':([0,2,3,4,9,22,23,24,27,29,45,47,49,56,57,61,62,63,66,67,69,70,71,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,94,96,97,98,101,103,104,106,107,109,110,111,112,115,118,122,126,148,149,155,157,158,159,160,162,167,171,172,173,174,177,179,182,183,184,185,186,188,190,191,192,193,197,198,199,200,201,],[12,12,12,12,12,12,-21,54,12,-7,54,54,54,-23,-29,-25,-26,12,-14,121,12,54,-22,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,-27,54,-17,12,12,12,-13,-31,121,-34,-35,-80,54,-15,-24,-18,-16,-30,54,-79,54,12,-84,-28,54,54,-83,121,54,54,-78,-85,-86,-81,-82,54,54,54,121,121,-89,-90,-87,-88,121,]),'$end':([1,2,3,4,13,14,15,23,29,56,57,61,62,66,71,97,101,107,109,122,126,148,149,155,167,],[0,-1,-2,-3,-4,-5,-6,-21,-7,-23,-29,-25,-26,-14,-22,-27,-17,-13,-31,-15,-24,-18,-16,-30,-28,]),'CHAVE_ABRE':([16,33,60,65,68,99,100,174,175,176,192,193,201,],[21,67,67,67,67,67,67,67,67,67,67,67,67,]),'PARENT_ABRE':([17,18,23,24,35,45,47,48,49,55,56,57,61,62,67,70,71,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,94,96,97,98,109,110,111,112,113,115,116,117,118,120,126,153,155,157,158,159,162,167,171,172,173,174,177,179,181,182,183,184,185,186,188,190,191,192,193,197,198,199,200,201,],[22,27,-21,49,69,49,49,94,49,96,-23,-29,-25,-26,49,49,-22,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,-27,49,-31,49,-34,-35,157,-80,159,160,49,69,-24,22,-30,49,-79,49,-84,-28,49,49,-83,49,49,49,191,-78,-85,-86,-81,-82,49,49,49,49,49,-89,-90,-87,-88,49,]),'PONTO_VIRG':([17,20,23,25,28,35,36,37,38,39,40,41,42,43,44,46,50,51,52,53,54,56,57,61,62,71,72,90,91,92,93,97,114,118,120,121,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,145,150,153,160,161,163,164,165,166,167,171,172,178,180,],[23,29,-21,56,61,-68,71,-37,-40,-43,-46,-49,-54,-57,-61,-67,-69,-70,-71,-72,-73,-23,-29,-25,-26,-22,126,-62,-64,-65,-63,-27,158,162,-68,-73,-76,-36,-24,-38,-39,-41,-42,-44,-45,-47,-48,-50,-51,-52,-53,-55,-56,-58,-59,-60,-74,-8,23,172,173,23,-75,-66,-77,-28,177,179,188,190,]),'RECEBER':([17,35,36,37,38,39,40,41,42,43,44,46,50,51,52,53,54,57,90,91,92,93,95,114,120,121,124,125,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,145,146,147,153,161,163,164,165,166,168,169,178,180,187,189,194,195,196,],[24,-68,70,-37,-40,-43,-46,-49,-54,-57,-61,-67,-69,-70,-71,-72,-73,98,-62,-64,-65,-63,70,70,-68,-73,-76,-36,-38,-39,-41,-42,-44,-45,-47,-48,-50,-51,-52,-53,-55,-56,-58,-59,-60,-74,70,70,24,70,24,-75,-66,-77,70,70,70,70,70,70,70,70,70,]),'VIRGULA':([17,28,35,36,37,38,39,40,41,42,43,44,46,50,51,52,53,54,57,64,90,91,92,93,124,125,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,145,147,153,163,164,165,166,],[26,26,-68,26,-37,-40,-43,-46,-49,-54,-57,-61,-67,-69,-70,-71,-72,-73,26,106,-62,-64,-65,-63,-76,-36,-38,-39,-41,-42,-44,-45,-47,-48,-50,-51,-52,-53,-55,-56,-58,-59,-60,-74,26,26,26,-75,-66,-77,]),'PUBLIC':([21,],[30,]),'PARENT_FECHA':([22,27,32,34,35,37,38,39,40,41,42,43,44,46,50,51,52,53,54,58,59,64,69,90,91,92,93,95,123,124,125,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,154,164,165,166,168,169,170,177,179,187,188,189,190,194,195,196,],[33,60,65,68,-68,-37,-40,-43,-46,-49,-54,-57,-61,-67,-69,-70,-71,-72,-73,99,100,-19,124,-62,-64,-65,-63,145,164,-76,-36,-38,-39,-41,-42,-44,-45,-47,-48,-50,-51,-52,-53,-55,-56,-58,-59,-60,165,-74,166,-20,-75,-66,-77,174,175,176,-91,-98,-94,-92,-97,-96,-93,-95,201,]),'CHAVE_FECHA':([23,56,57,61,62,66,67,71,97,101,102,103,104,107,108,109,110,111,112,115,122,126,148,149,151,152,155,156,158,162,167,173,182,183,184,185,186,197,198,199,200,],[-21,-23,-29,-25,-26,-14,109,-22,-27,-17,150,-11,-12,-13,155,-31,-32,-34,-35,-80,-15,-24,-18,-16,-9,-10,-30,-33,-79,-84,-28,-83,-78,-85,-86,-81,-82,-89,-90,-87,-88,]),'IF':([23,56,57,61,62,67,71,97,109,110,111,112,115,126,155,158,162,167,173,174,182,183,184,185,186,192,193,197,198,199,200,201,],[-21,-23,-29,-25,-26,113,-22,-27,-31,113,-34,-35,-80,-24,-30,-79,-84,-28,-83,181,-78,-85,-86,-81,-82,181,181,-89,-90,-87,-88,181,]),'WHILE':([23,56,57,61,62,67,71,97,109,110,111,112,115,126,155,158,162,167,173,174,182,183,184,185,186,192,193,197,198,199,200,201,],[-21,-23,-29,-25,-26,116,-22,-27,-31,116,-34,-35,-80,-24,-30,-79,-84,-28,-83,116,-78,-85,-86,-81,-82,116,116,-89,-90,-87,-88,116,]),'FOR':([23,56,57,61,62,67,71,97,109,110,111,112,115,126,155,158,162,167,173,174,182,183,184,185,186,192,193,197,198,199,200,201,],[-21,-23,-29,-25,-26,117,-22,-27,-31,117,-34,-35,-80,-24,-30,-79,-84,-28,-83,117,-78,-85,-86,-81,-82,117,117,-89,-90,-87,-88,117,]),'RETURN':([23,56,57,61,62,67,71,97,109,110,111,112,115,126,155,158,162,167,173,174,182,183,184,185,186,192,193,197,198,199,200,201,],[-21,-23,-29,-25,-26,118,-22,-27,-31,118,-34,-35,-80,-24,-30,-79,-84,-28,-83,118,-78,-85,-86,-81,-82,118,118,-89,-90,-87,-88,118,]),'OP_NOT':([23,24,49,56,57,61,62,67,70,71,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,96,97,98,109,110,111,112,115,118,126,155,157,158,159,162,167,171,172,173,174,177,179,182,183,184,185,186,188,190,191,192,193,197,198,199,200,201,],[-21,45,45,-23,-29,-25,-26,45,45,-22,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,-27,45,-31,45,-34,-35,-80,45,-24,-30,45,-79,45,-84,-28,45,45,-83,45,45,45,-78,-85,-86,-81,-82,45,45,45,45,45,-89,-90,-87,-88,45,]),'NOT':([23,24,49,56,57,61,62,67,70,71,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,96,97,98,109,110,111,112,115,118,126,155,157,158,159,162,167,171,172,173,174,177,179,182,183,184,185,186,188,190,191,192,193,197,198,199,200,201,],[-21,47,47,-23,-29,-25,-26,47,47,-22,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,-27,47,-31,47,-34,-35,-80,47,-24,-30,47,-79,47,-84,-28,47,47,-83,47,47,47,-78,-85,-86,-81,-82,47,47,47,47,47,-89,-90,-87,-88,47,]),'SIZEOF':([23,24,49,56,57,61,62,67,70,71,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,96,97,98,109,110,111,112,115,118,126,155,157,158,159,162,167,171,172,173,174,177,179,182,183,184,185,186,188,190,191,192,193,197,198,199,200,201,],[-21,48,48,-23,-29,-25,-26,48,48,-22,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,-27,48,-31,48,-34,-35,-80,48,-24,-30,48,-79,48,-84,-28,48,48,-83,48,48,48,-78,-85,-86,-81,-82,48,48,48,48,48,-89,-90,-87,-88,48,]),'INT_V':([23,24,45,47,49,56,57,61,62,67,70,71,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,94,96,97,98,109,110,111,112,115,118,126,155,157,158,159,162,167,171,172,173,174,177,179,182,183,184,185,186,188,190,191,192,193,197,198,199,200,201,],[-21,50,50,50,50,-23,-29,-25,-26,50,50,-22,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,-27,50,-31,50,-34,-35,-80,50,-24,-30,50,-79,50,-84,-28,50,50,-83,50,50,50,-78,-85,-86,-81,-82,50,50,50,50,50,-89,-90,-87,-88,50,]),'TRUE':([23,24,45,47,49,56,57,61,62,67,70,71,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,94,96,97,98,109,110,111,112,115,118,126,155,157,158,159,162,167,171,172,173,174,177,179,182,183,184,185,186,188,190,191,192,193,197,198,199,200,201,],[-21,51,51,51,51,-23,-29,-25,-26,51,51,-22,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,-27,51,-31,51,-34,-35,-80,51,-24,-30,51,-79,51,-84,-28,51,51,-83,51,51,51,-78,-85,-86,-81,-82,51,51,51,51,51,-89,-90,-87,-88,51,]),'FALSE':([23,24,45,47,49,56,57,61,62,67,70,71,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,94,96,97,98,109,110,111,112,115,118,126,155,157,158,159,162,167,171,172,173,174,177,179,182,183,184,185,186,188,190,191,192,193,197,198,199,200,201,],[-21,52,52,52,52,-23,-29,-25,-26,52,52,-22,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,-27,52,-31,52,-34,-35,-80,52,-24,-30,52,-79,52,-84,-28,52,52,-83,52,52,52,-78,-85,-86,-81,-82,52,52,52,52,52,-89,-90,-87,-88,52,]),'TYPEID':([23,24,45,47,49,56,57,61,62,67,70,71,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,94,96,97,98,109,110,111,112,115,118,126,155,157,158,159,162,167,171,172,173,174,177,179,182,183,184,185,186,188,190,191,192,193,197,198,199,200,201,],[-21,55,55,55,55,-23,-29,-25,-26,55,55,-22,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,-27,55,-31,55,-34,-35,-80,55,-24,-30,55,-79,55,-84,-28,55,55,-83,55,55,55,-78,-85,-86,-81,-82,55,55,55,55,55,-89,-90,-87,-88,55,]),'ELSE':([23,56,57,61,62,71,97,109,115,126,155,158,162,167,173,182,183,184,185,186,197,198,199,200,202,203,],[-21,-23,-29,-25,-26,-22,-27,-31,-80,-24,-30,-79,-84,-28,-83,-78,192,193,-81,-82,-89,-90,-87,-88,193,192,]),'DOIS_PONTOS':([30,],[63,]),'MAIS_MAIS':([35,46,50,51,52,53,54,120,121,124,145,164,166,],[-68,91,-69,-70,-71,-72,-73,-68,-73,-76,-74,-75,-77,]),'MENOS_MENOS':([35,46,50,51,52,53,54,120,121,124,145,164,166,],[-68,92,-69,-70,-71,-72,-73,-68,-73,-76,-74,-75,-77,]),'MULT':([35,43,44,46,50,51,52,53,54,90,91,92,93,120,121,124,139,140,141,142,143,145,164,165,166,],[-68,87,-61,-67,-69,-70,-71,-72,-73,-62,-64,-65,-63,-68,-73,-76,87,87,-58,-59,-60,-74,-75,-66,-77,]),'DIV':([35,43,44,46,50,51,52,53,54,90,91,92,93,120,121,124,139,140,141,142,143,145,164,165,166,],[-68,88,-61,-67,-69,-70,-71,-72,-73,-62,-64,-65,-63,-68,-73,-76,88,88,-58,-59,-60,-74,-75,-66,-77,]),'MODULO':([35,43,44,46,50,51,52,53,54,90,91,92,93,120,121,124,139,140,141,142,143,145,164,165,166,],[-68,89,-61,-67,-69,-70,-71,-72,-73,-62,-64,-65,-63,-68,-73,-76,89,89,-58,-59,-60,-74,-75,-66,-77,]),'SOMA':([35,42,43,44,46,50,51,52,53,54,90,91,92,93,120,121,124,135,136,137,138,139,140,141,142,143,145,164,165,166,],[-68,85,-57,-61,-67,-69,-70,-71,-72,-73,-62,-64,-65,-63,-68,-73,-76,85,85,85,85,-55,-56,-58,-59,-60,-74,-75,-66,-77,]),'SUB':([35,42,43,44,46,50,51,52,53,54,90,91,92,93,120,121,124,135,136,137,138,139,140,141,142,143,145,164,165,166,],[-68,86,-57,-61,-67,-69,-70,-71,-72,-73,-62,-64,-65,-63,-68,-73,-76,86,86,86,86,-55,-56,-58,-59,-60,-74,-75,-66,-77,]),'MENOR_Q':([35,41,42,43,44,46,50,51,52,53,54,90,91,92,93,120,121,124,133,134,135,136,137,138,139,140,141,142,143,145,164,165,166,],[-68,81,-54,-57,-61,-67,-69,-70,-71,-72,-73,-62,-64,-65,-63,-68,-73,-76,81,81,-50,-51,-52,-53,-55,-56,-58,-59,-60,-74,-75,-66,-77,]),'MAIOR_Q':([35,41,42,43,44,46,50,51,52,53,54,90,91,92,93,120,121,124,133,134,135,136,137,138,139,140,141,142,143,145,164,165,166,],[-68,82,-54,-57,-61,-67,-69,-70,-71,-72,-73,-62,-64,-65,-63,-68,-73,-76,82,82,-50,-51,-52,-53,-55,-56,-58,-59,-60,-74,-75,-66,-77,]),'MAIOR_IGUAL':([35,41,42,43,44,46,50,51,52,53,54,90,91,92,93,120,121,124,133,134,135,136,137,138,139,140,141,142,143,145,164,165,166,],[-68,83,-54,-57,-61,-67,-69,-70,-71,-72,-73,-62,-64,-65,-63,-68,-73,-76,83,83,-50,-51,-52,-53,-55,-56,-58,-59,-60,-74,-75,-66,-77,]),'MENOR_IGUAL':([35,41,42,43,44,46,50,51,52,53,54,90,91,92,93,120,121,124,133,134,135,136,137,138,139,140,141,142,143,145,164,165,166,],[-68,84,-54,-57,-61,-67,-69,-70,-71,-72,-73,-62,-64,-65,-63,-68,-73,-76,84,84,-50,-51,-52,-53,-55,-56,-58,-59,-60,-74,-75,-66,-77,]),'IGUAL':([35,40,41,42,43,44,46,50,51,52,53,54,90,91,92,93,120,121,124,131,132,133,134,135,136,137,138,139,140,141,142,143,145,164,165,166,],[-68,79,-49,-54,-57,-61,-67,-69,-70,-71,-72,-73,-62,-64,-65,-63,-68,-73,-76,79,79,-47,-48,-50,-51,-52,-53,-55,-56,-58,-59,-60,-74,-75,-66,-77,]),'DIFERENTE':([35,40,41,42,43,44,46,50,51,52,53,54,90,91,92,93,120,121,124,131,132,133,134,135,136,137,138,139,140,141,142,143,145,164,165,166,],[-68,80,-49,-54,-57,-61,-67,-69,-70,-71,-72,-73,-62,-64,-65,-63,-68,-73,-76,80,80,-47,-48,-50,-51,-52,-53,-55,-56,-58,-59,-60,-74,-75,-66,-77,]),'OP_OU_EX':([35,39,40,41,42,43,44,46,50,51,52,53,54,90,91,92,93,120,121,124,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,145,164,165,166,],[-68,77,-46,-49,-54,-57,-61,-67,-69,-70,-71,-72,-73,-62,-64,-65,-63,-68,-73,-76,77,77,-44,-45,-47,-48,-50,-51,-52,-53,-55,-56,-58,-59,-60,-74,-75,-66,-77,]),'XOR':([35,39,40,41,42,43,44,46,50,51,52,53,54,90,91,92,93,120,121,124,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,145,164,165,166,],[-68,78,-46,-49,-54,-57,-61,-67,-69,-70,-71,-72,-73,-62,-64,-65,-63,-68,-73,-76,78,78,-44,-45,-47,-48,-50,-51,-52,-53,-55,-56,-58,-59,-60,-74,-75,-66,-77,]),'OP_E':([35,38,39,40,41,42,43,44,46,50,51,52,53,54,90,91,92,93,120,121,124,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,145,164,165,166,],[-68,75,-43,-46,-49,-54,-57,-61,-67,-69,-70,-71,-72,-73,-62,-64,-65,-63,-68,-73,-76,75,75,-41,-42,-44,-45,-47,-48,-50,-51,-52,-53,-55,-56,-58,-59,-60,-74,-75,-66,-77,]),'AND':([35,38,39,40,41,42,43,44,46,50,51,52,53,54,90,91,92,93,120,121,124,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,145,164,165,166,],[-68,76,-43,-46,-49,-54,-57,-61,-67,-69,-70,-71,-72,-73,-62,-64,-65,-63,-68,-73,-76,76,76,-41,-42,-44,-45,-47,-48,-50,-51,-52,-53,-55,-56,-58,-59,-60,-74,-75,-66,-77,]),'OP_OU':([35,37,38,39,40,41,42,43,44,46,50,51,52,53,54,90,91,92,93,120,121,124,125,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,145,164,165,166,],[-68,73,-40,-43,-46,-49,-54,-57,-61,-67,-69,-70,-71,-72,-73,-62,-64,-65,-63,-68,-73,-76,73,-38,-39,-41,-42,-44,-45,-47,-48,-50,-51,-52,-53,-55,-56,-58,-59,-60,-74,-75,-66,-77,]),'OR':([35,37,38,39,40,41,42,43,44,46,50,51,52,53,54,90,91,92,93,120,121,124,125,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,145,164,165,166,],[-68,74,-40,-43,-46,-49,-54,-57,-61,-67,-69,-70,-71,-72,-73,-62,-64,-65,-63,-68,-73,-76,74,-38,-39,-41,-42,-44,-45,-47,-48,-50,-51,-52,-53,-55,-56,-58,-59,-60,-74,-75,-66,-77,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'cpp':([0,2,3,4,],[1,13,14,15,]),'decl_classe':([0,2,3,4,],[2,2,2,2,]),'decl_funcao':([0,2,3,4,63,103,104,],[3,3,3,3,104,104,104,]),'decl_variavel':([0,2,3,4,63,67,103,104,110,160,174,192,193,201,],[4,4,4,4,103,115,103,103,115,171,115,115,115,115,]),'tipo':([0,2,3,4,9,22,27,63,67,69,103,104,106,110,160,174,192,193,201,],[7,7,7,7,19,31,31,105,119,31,105,105,31,119,119,119,119,119,119,]),'body_class':([16,],[20,]),'decl_variavel_n':([17,28,36,57,147,153,163,],[25,62,72,97,167,25,25,]),'parametros':([22,27,69,106,],[32,59,123,154,]),'exp':([24,49,67,96,98,110,118,157,159,171,172,174,177,179,188,190,191,192,193,201,],[36,95,114,146,147,114,161,168,169,178,180,114,187,189,194,195,196,114,114,114,]),'exp_1':([24,49,67,70,96,98,110,118,157,159,171,172,174,177,179,188,190,191,192,193,201,],[37,37,37,125,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,]),'exp_2':([24,49,67,70,73,74,96,98,110,118,157,159,171,172,174,177,179,188,190,191,192,193,201,],[38,38,38,38,127,128,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,]),'exp_3':([24,49,67,70,73,74,75,76,96,98,110,118,157,159,171,172,174,177,179,188,190,191,192,193,201,],[39,39,39,39,39,39,129,130,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,]),'exp_4':([24,49,67,70,73,74,75,76,77,78,96,98,110,118,157,159,171,172,174,177,179,188,190,191,192,193,201,],[40,40,40,40,40,40,40,40,131,132,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,]),'exp_5':([24,49,67,70,73,74,75,76,77,78,79,80,96,98,110,118,157,159,171,172,174,177,179,188,190,191,192,193,201,],[41,41,41,41,41,41,41,41,41,41,133,134,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,]),'exp_6':([24,49,67,70,73,74,75,76,77,78,79,80,81,82,83,84,96,98,110,118,157,159,171,172,174,177,179,188,190,191,192,193,201,],[42,42,42,42,42,42,42,42,42,42,42,42,135,136,137,138,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,]),'exp_7':([24,49,67,70,73,74,75,76,77,78,79,80,81,82,83,84,85,86,96,98,110,118,157,159,171,172,174,177,179,188,190,191,192,193,201,],[43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,139,140,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,]),'exp_8':([24,49,67,70,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,96,98,110,118,157,159,171,172,174,177,179,188,190,191,192,193,201,],[44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,141,142,143,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,]),'exp_9':([24,45,47,49,67,70,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,94,96,98,110,118,157,159,171,172,174,177,179,188,190,191,192,193,201,],[46,90,93,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,144,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,]),'chamada_funcao':([24,45,47,49,67,70,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,94,96,98,110,118,157,159,171,172,174,177,179,188,190,191,192,193,201,],[53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,]),'body':([33,60,65,68,99,100,174,175,176,192,193,201,],[66,101,107,122,148,149,183,185,186,197,200,203,]),'content_class':([63,103,104,],[102,151,152,]),'comandos':([67,110,],[108,156,]),'comando':([67,110,],[110,110,]),'condicional_1':([67,110,174,192,193,201,],[111,111,184,198,199,202,]),'condicional_2':([67,110,],[112,112,]),'for_log':([160,],[170,]),'rest_if':([174,201,],[182,182,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> cpp","S'",1,None,None,None),
  ('cpp -> decl_classe','cpp',1,'p_cpp','sintatico.py',26),
  ('cpp -> decl_funcao','cpp',1,'p_cpp','sintatico.py',27),
  ('cpp -> decl_variavel','cpp',1,'p_cpp','sintatico.py',28),
  ('cpp -> decl_classe cpp','cpp',2,'p_cpp','sintatico.py',29),
  ('cpp -> decl_funcao cpp','cpp',2,'p_cpp','sintatico.py',30),
  ('cpp -> decl_variavel cpp','cpp',2,'p_cpp','sintatico.py',31),
  ('decl_classe -> CLASS ID body_class PONTO_VIRG','decl_classe',4,'p_decl_classe','sintatico.py',35),
  ('body_class -> CHAVE_ABRE PUBLIC DOIS_PONTOS content_class CHAVE_FECHA','body_class',5,'p_body_class','sintatico.py',39),
  ('content_class -> decl_variavel content_class','content_class',2,'p_content_class','sintatico.py',43),
  ('content_class -> decl_funcao content_class','content_class',2,'p_content_class','sintatico.py',44),
  ('content_class -> decl_variavel','content_class',1,'p_content_class','sintatico.py',45),
  ('content_class -> decl_funcao','content_class',1,'p_content_class','sintatico.py',46),
  ('decl_funcao -> tipo ID PARENT_ABRE parametros PARENT_FECHA body','decl_funcao',6,'p_decl_funcao','sintatico.py',50),
  ('decl_funcao -> tipo ID PARENT_ABRE PARENT_FECHA body','decl_funcao',5,'p_decl_funcao','sintatico.py',51),
  ('decl_funcao -> tipo ID PARENT_ABRE VOID PARENT_FECHA body','decl_funcao',6,'p_decl_funcao','sintatico.py',52),
  ('decl_funcao -> VOID ID PARENT_ABRE parametros PARENT_FECHA body','decl_funcao',6,'p_decl_funcao','sintatico.py',53),
  ('decl_funcao -> VOID ID PARENT_ABRE PARENT_FECHA body','decl_funcao',5,'p_decl_funcao','sintatico.py',54),
  ('decl_funcao -> VOID ID PARENT_ABRE VOID PARENT_FECHA body','decl_funcao',6,'p_decl_funcao','sintatico.py',55),
  ('parametros -> tipo ID','parametros',2,'p_parametros','sintatico.py',59),
  ('parametros -> tipo ID VIRGULA parametros','parametros',4,'p_parametros','sintatico.py',60),
  ('decl_variavel -> tipo ID PONTO_VIRG','decl_variavel',3,'p_decl_variavel','sintatico.py',64),
  ('decl_variavel -> tipo ID RECEBER exp PONTO_VIRG','decl_variavel',5,'p_decl_variavel','sintatico.py',65),
  ('decl_variavel -> tipo ID decl_variavel_n PONTO_VIRG','decl_variavel',4,'p_decl_variavel','sintatico.py',66),
  ('decl_variavel -> tipo ID RECEBER exp decl_variavel_n PONTO_VIRG','decl_variavel',6,'p_decl_variavel','sintatico.py',67),
  ('decl_variavel -> TYPEDEF tipo ID PONTO_VIRG','decl_variavel',4,'p_decl_variavel','sintatico.py',68),
  ('decl_variavel -> TYPEDEF tipo ID decl_variavel_n','decl_variavel',4,'p_decl_variavel','sintatico.py',69),
  ('decl_variavel_n -> VIRGULA ID decl_variavel_n','decl_variavel_n',3,'p_decl_variavel_n','sintatico.py',73),
  ('decl_variavel_n -> VIRGULA ID RECEBER exp decl_variavel_n','decl_variavel_n',5,'p_decl_variavel_n','sintatico.py',74),
  ('decl_variavel_n -> VIRGULA ID','decl_variavel_n',2,'p_decl_variavel_n','sintatico.py',75),
  ('body -> CHAVE_ABRE comandos CHAVE_FECHA','body',3,'p_body','sintatico.py',80),
  ('body -> CHAVE_ABRE CHAVE_FECHA','body',2,'p_body','sintatico.py',81),
  ('comandos -> comando','comandos',1,'p_comandos','sintatico.py',85),
  ('comandos -> comando comandos','comandos',2,'p_comandos','sintatico.py',86),
  ('comando -> condicional_1','comando',1,'p_comando','sintatico.py',90),
  ('comando -> condicional_2','comando',1,'p_comando','sintatico.py',91),
  ('exp -> exp RECEBER exp_1','exp',3,'p_exp','sintatico.py',95),
  ('exp -> exp_1','exp',1,'p_exp','sintatico.py',96),
  ('exp_1 -> exp_1 OP_OU exp_2','exp_1',3,'p_exp_1','sintatico.py',100),
  ('exp_1 -> exp_1 OR exp_2','exp_1',3,'p_exp_1','sintatico.py',101),
  ('exp_1 -> exp_2','exp_1',1,'p_exp_1','sintatico.py',102),
  ('exp_2 -> exp_2 OP_E exp_3','exp_2',3,'p_exp_2','sintatico.py',106),
  ('exp_2 -> exp_2 AND exp_3','exp_2',3,'p_exp_2','sintatico.py',107),
  ('exp_2 -> exp_3','exp_2',1,'p_exp_2','sintatico.py',108),
  ('exp_3 -> exp_3 OP_OU_EX exp_4','exp_3',3,'p_exp_3','sintatico.py',112),
  ('exp_3 -> exp_3 XOR exp_4','exp_3',3,'p_exp_3','sintatico.py',113),
  ('exp_3 -> exp_4','exp_3',1,'p_exp_3','sintatico.py',114),
  ('exp_4 -> exp_4 IGUAL exp_5','exp_4',3,'p_exp_4','sintatico.py',118),
  ('exp_4 -> exp_4 DIFERENTE exp_5','exp_4',3,'p_exp_4','sintatico.py',119),
  ('exp_4 -> exp_5','exp_4',1,'p_exp_4','sintatico.py',120),
  ('exp_5 -> exp_5 MENOR_Q exp_6','exp_5',3,'p_exp_5','sintatico.py',124),
  ('exp_5 -> exp_5 MAIOR_Q exp_6','exp_5',3,'p_exp_5','sintatico.py',125),
  ('exp_5 -> exp_5 MAIOR_IGUAL exp_6','exp_5',3,'p_exp_5','sintatico.py',126),
  ('exp_5 -> exp_5 MENOR_IGUAL exp_6','exp_5',3,'p_exp_5','sintatico.py',127),
  ('exp_5 -> exp_6','exp_5',1,'p_exp_5','sintatico.py',128),
  ('exp_6 -> exp_6 SOMA exp_7','exp_6',3,'p_exp_6','sintatico.py',132),
  ('exp_6 -> exp_6 SUB exp_7','exp_6',3,'p_exp_6','sintatico.py',133),
  ('exp_6 -> exp_7','exp_6',1,'p_exp_6','sintatico.py',134),
  ('exp_7 -> exp_7 MULT exp_8','exp_7',3,'p_exp_7','sintatico.py',138),
  ('exp_7 -> exp_7 DIV exp_8','exp_7',3,'p_exp_7','sintatico.py',139),
  ('exp_7 -> exp_7 MODULO exp_8','exp_7',3,'p_exp_7','sintatico.py',140),
  ('exp_7 -> exp_8','exp_7',1,'p_exp_7','sintatico.py',141),
  ('exp_8 -> OP_NOT exp_9','exp_8',2,'p_exp_8','sintatico.py',145),
  ('exp_8 -> NOT exp_9','exp_8',2,'p_exp_8','sintatico.py',146),
  ('exp_8 -> exp_9 MAIS_MAIS','exp_8',2,'p_exp_8','sintatico.py',147),
  ('exp_8 -> exp_9 MENOS_MENOS','exp_8',2,'p_exp_8','sintatico.py',148),
  ('exp_8 -> SIZEOF PARENT_ABRE exp_9 PARENT_FECHA','exp_8',4,'p_exp_8','sintatico.py',149),
  ('exp_8 -> exp_9','exp_8',1,'p_exp_8','sintatico.py',150),
  ('exp_9 -> ID','exp_9',1,'p_exp_9','sintatico.py',154),
  ('exp_9 -> INT_V','exp_9',1,'p_exp_9','sintatico.py',155),
  ('exp_9 -> TRUE','exp_9',1,'p_exp_9','sintatico.py',156),
  ('exp_9 -> FALSE','exp_9',1,'p_exp_9','sintatico.py',157),
  ('exp_9 -> chamada_funcao','exp_9',1,'p_exp_9','sintatico.py',158),
  ('exp_9 -> STRING','exp_9',1,'p_exp_9','sintatico.py',159),
  ('exp_9 -> PARENT_ABRE exp PARENT_FECHA','exp_9',3,'p_exp_9','sintatico.py',160),
  ('chamada_funcao -> ID PARENT_ABRE parametros PARENT_FECHA','chamada_funcao',4,'p_chamada_funcao','sintatico.py',164),
  ('chamada_funcao -> ID PARENT_ABRE PARENT_FECHA','chamada_funcao',3,'p_chamada_funcao','sintatico.py',165),
  ('chamada_funcao -> TYPEID PARENT_ABRE exp PARENT_FECHA','chamada_funcao',4,'p_chamada_funcao','sintatico.py',166),
  ('condicional_1 -> IF PARENT_ABRE exp PARENT_FECHA rest_if','condicional_1',5,'p_condicional_1','sintatico.py',169),
  ('condicional_1 -> exp PONTO_VIRG','condicional_1',2,'p_condicional_1','sintatico.py',170),
  ('condicional_1 -> decl_variavel','condicional_1',1,'p_condicional_1','sintatico.py',171),
  ('condicional_1 -> WHILE PARENT_ABRE exp PARENT_FECHA body','condicional_1',5,'p_condicional_1','sintatico.py',172),
  ('condicional_1 -> FOR PARENT_ABRE for_log PARENT_FECHA body','condicional_1',5,'p_condicional_1','sintatico.py',173),
  ('condicional_1 -> RETURN exp PONTO_VIRG','condicional_1',3,'p_condicional_1','sintatico.py',174),
  ('condicional_1 -> RETURN PONTO_VIRG','condicional_1',2,'p_condicional_1','sintatico.py',175),
  ('condicional_2 -> IF PARENT_ABRE exp PARENT_FECHA body','condicional_2',5,'p_condicional_2','sintatico.py',179),
  ('condicional_2 -> IF PARENT_ABRE exp PARENT_FECHA condicional_1','condicional_2',5,'p_condicional_2','sintatico.py',180),
  ('rest_if -> condicional_1 ELSE condicional_1','rest_if',3,'p_rest_if','sintatico.py',183),
  ('rest_if -> condicional_1 ELSE body','rest_if',3,'p_rest_if','sintatico.py',184),
  ('rest_if -> body ELSE body','rest_if',3,'p_rest_if','sintatico.py',185),
  ('rest_if -> body ELSE condicional_1','rest_if',3,'p_rest_if','sintatico.py',186),
  ('for_log -> decl_variavel PONTO_VIRG','for_log',2,'p_for_log','sintatico.py',190),
  ('for_log -> decl_variavel exp PONTO_VIRG','for_log',3,'p_for_log','sintatico.py',191),
  ('for_log -> decl_variavel exp PONTO_VIRG exp','for_log',4,'p_for_log','sintatico.py',192),
  ('for_log -> decl_variavel PONTO_VIRG exp','for_log',3,'p_for_log','sintatico.py',193),
  ('for_log -> PONTO_VIRG exp PONTO_VIRG exp','for_log',4,'p_for_log','sintatico.py',194),
  ('for_log -> PONTO_VIRG exp PONTO_VIRG','for_log',3,'p_for_log','sintatico.py',195),
  ('for_log -> PONTO_VIRG PONTO_VIRG exp','for_log',3,'p_for_log','sintatico.py',196),
  ('for_log -> PONTO_VIRG PONTO_VIRG','for_log',2,'p_for_log','sintatico.py',197),
  ('tipo -> INT','tipo',1,'p_tipo','sintatico.py',201),
  ('tipo -> BOOL','tipo',1,'p_tipo','sintatico.py',202),
  ('tipo -> ID','tipo',1,'p_tipo','sintatico.py',203),
  ('tipo -> STRING','tipo',1,'p_tipo','sintatico.py',204),
]

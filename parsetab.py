
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ABSTRACT ADMIRATION AND ARROWFUNCTION AS BOOLEAN BREAK CASE CATCH CHAINCHAR CLASS COMMA CONST DATAATTRIBUTE DEF DEFAULT DIVIDE DOLLAR DOT DOTCOMMA DOUBLE DYNAMIC ELIF ELSE ENUM EQUALS EXTENDS FALSE FINAL FINALLY FLOAT FOR FUNCTION IF IN INT INTEGERDIVISION INTERFACE INTERNDATATYPE IS LANGLE LBRACE LBRACKET LIST LPAREN MAIN MAP METHOD MINUS MOD MODULE NEQ NEW NEWDATATYPE NULL NUMBER NUMBERINT OR PLUS PRINT PRIVATE PROTECTED PUBLIC RANGLE RBRACE RBRACKET RETURN RPAREN SET STATIC STRING SUPER SWITCH THIS TIMES TRUE TRY TWODOTS TYPEDEF VAR VARIABLE VOID WHILE commentBlock commentLinecuerpo : impresion\n              | tupla\n              | declaracion\n              | sentenciaIf\n              | estructuraList\n              | funcionVoid\n              | switch\n              | operacion\n              | flecha\n              | RETURN VARIABLE \n              | funcion\n              | funcionData \n              | crearConjunto\n            impresion : PRINT LPAREN valores RPAREN DOTCOMMA\n                 | PRINT LPAREN operacion RPAREN DOTCOMMA\n     sentenciaIf : IF LPAREN condicion RPAREN LBRACE cuerpo RBRACE else\n                        | IF LPAREN condicion RPAREN LBRACE cuerpo RBRACE DOTCOMMA\n    condicion : valor operadorComp valor\n    else : ELSE LBRACE cuerpo RBRACE DOTCOMMA\n    estructuraList : LIST LANGLE type RANGLE VARIABLE EQUALS LBRACKET valores RBRACKET DOTCOMMAfuncionVoid : VOID VARIABLE LPAREN valores RPAREN LBRACE cuerpo RBRACE DOTCOMMAoperadorComp : EQUALS \n                    | LANGLE\n                    | RANGLE\n                    | NEQtupla : LPAREN valores RPARENimpresion : PRINT LPAREN RPAREN DOTCOMMA\n    impresion : valores : valor\n               | valor COMMA valoresBool : TRUE\n        | FALSE valor : VARIABLE\n             | FLOAT\n             | Bool\n             | operacion\n             | NUMBER\n             | CHAINCHAR\n    type : MAP\n            | DOUBLE\n            | STRING\n            | INT\n            | SET\n            | LIST\n            | BOOLEAN\n    tipoVariable : type  \n                    | FINAL\n                    | CONST\n                    | VAR\n                    | DYNAMIC declaracion : tipoVariable VARIABLE EQUALS valoroperacion : valor operador numeroSiguientenumeroSiguiente : LPAREN valor operador numeroSiguiente RPAREN\n                    | valor funcion : VARIABLE LPAREN valores RPARENfuncionData : VARIABLE DOT VARIABLE LPAREN valores RPARENswitch : SWITCH LPAREN valor RPAREN LBRACE caso RBRACEcaso : CASE valor TWODOTS cuerpo BREAK caso \n            | CASE valor TWODOTS cuerpo BREAKflecha : type VARIABLE LPAREN valores RPAREN ARROWFUNCTION cuerpocrearConjunto : SET VARIABLE EQUALS conjunto\n                    | SET LANGLE type RANGLE VARIABLE EQUALS conjuntoconjunto : LBRACE valores RBRACE\n                | LBRACE RBRACE operador : PLUS\n                | MINUS\n                | TIMES\n                | DIVIDE '
    
_lr_action_items = {'RETURN':([0,108,121,122,140,141,],[11,11,11,11,11,11,]),'PRINT':([0,108,121,122,140,141,],[16,16,16,16,16,16,]),'$end':([0,1,2,3,4,5,6,7,8,9,10,13,14,15,30,31,32,33,39,40,41,47,48,67,70,71,83,86,89,101,105,106,115,117,121,125,127,130,132,134,135,136,143,146,150,],[-28,0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-11,-12,-13,-34,-35,-37,-38,-31,-32,-10,-33,-36,-26,-54,-52,-55,-27,-51,-61,-14,-15,-64,-56,-28,-63,-53,-60,-57,-62,-16,-17,-21,-20,-19,]),'LPAREN':([0,12,16,20,24,50,51,52,53,54,57,58,63,107,108,121,122,140,141,],[17,42,44,55,59,72,-65,-66,-67,-68,78,79,84,72,17,17,17,17,17,]),'IF':([0,108,121,122,140,141,],[20,20,20,20,20,20,]),'LIST':([0,56,61,108,121,122,140,141,],[21,75,75,21,21,21,21,21,]),'VOID':([0,108,121,122,140,141,],[23,23,23,23,23,23,]),'SWITCH':([0,108,121,122,140,141,],[24,24,24,24,24,24,]),'VARIABLE':([0,11,17,18,21,22,23,25,26,27,28,29,34,35,36,37,38,42,43,44,50,51,52,53,54,55,59,68,69,72,78,79,84,92,93,94,95,96,97,102,103,107,108,121,122,124,129,140,141,],[12,41,47,49,-44,57,58,60,-47,-48,-49,-50,-39,-40,-41,-42,-45,47,63,47,47,-65,-66,-67,-68,47,47,47,47,47,47,47,47,47,-22,-23,-24,-25,110,47,116,47,12,12,12,47,47,12,12,]),'SET':([0,56,61,108,121,122,140,141,],[25,77,77,25,25,25,25,25,]),'FINAL':([0,108,121,122,140,141,],[26,26,26,26,26,26,]),'CONST':([0,108,121,122,140,141,],[27,27,27,27,27,27,]),'VAR':([0,108,121,122,140,141,],[28,28,28,28,28,28,]),'DYNAMIC':([0,108,121,122,140,141,],[29,29,29,29,29,29,]),'FLOAT':([0,17,42,44,50,51,52,53,54,55,59,68,69,72,78,79,84,92,93,94,95,96,102,107,108,121,122,124,129,140,141,],[30,30,30,30,30,-65,-66,-67,-68,30,30,30,30,30,30,30,30,30,-22,-23,-24,-25,30,30,30,30,30,30,30,30,30,]),'NUMBER':([0,17,42,44,50,51,52,53,54,55,59,68,69,72,78,79,84,92,93,94,95,96,102,107,108,121,122,124,129,140,141,],[32,32,32,32,32,-65,-66,-67,-68,32,32,32,32,32,32,32,32,32,-22,-23,-24,-25,32,32,32,32,32,32,32,32,32,]),'CHAINCHAR':([0,17,42,44,50,51,52,53,54,55,59,68,69,72,78,79,84,92,93,94,95,96,102,107,108,121,122,124,129,140,141,],[33,33,33,33,33,-65,-66,-67,-68,33,33,33,33,33,33,33,33,33,-22,-23,-24,-25,33,33,33,33,33,33,33,33,33,]),'MAP':([0,56,61,108,121,122,140,141,],[34,34,34,34,34,34,34,34,]),'DOUBLE':([0,56,61,108,121,122,140,141,],[35,35,35,35,35,35,35,35,]),'STRING':([0,56,61,108,121,122,140,141,],[36,36,36,36,36,36,36,36,]),'INT':([0,56,61,108,121,122,140,141,],[37,37,37,37,37,37,37,37,]),'BOOLEAN':([0,56,61,108,121,122,140,141,],[38,38,38,38,38,38,38,38,]),'TRUE':([0,17,42,44,50,51,52,53,54,55,59,68,69,72,78,79,84,92,93,94,95,96,102,107,108,121,122,124,129,140,141,],[39,39,39,39,39,-65,-66,-67,-68,39,39,39,39,39,39,39,39,39,-22,-23,-24,-25,39,39,39,39,39,39,39,39,39,]),'FALSE':([0,17,42,44,50,51,52,53,54,55,59,68,69,72,78,79,84,92,93,94,95,96,102,107,108,121,122,124,129,140,141,],[40,40,40,40,40,-65,-66,-67,-68,40,40,40,40,40,40,40,40,40,-22,-23,-24,-25,40,40,40,40,40,40,40,40,40,]),'RBRACE':([2,3,4,5,6,7,8,9,10,13,14,15,30,31,32,33,39,40,41,46,47,48,67,70,71,83,86,88,89,101,102,105,106,108,114,115,117,119,121,122,123,125,127,130,131,132,134,135,136,141,143,145,146,147,149,150,],[-1,-2,-3,-4,-5,-6,-7,-8,-9,-11,-12,-13,-34,-35,-37,-38,-31,-32,-10,-29,-33,-36,-26,-54,-52,-55,-27,-30,-51,-61,115,-14,-15,-28,125,-64,-56,128,-28,-28,132,-63,-53,-60,139,-57,-62,-16,-17,-28,-21,148,-20,-59,-58,-19,]),'BREAK':([2,3,4,5,6,7,8,9,10,13,14,15,30,31,32,33,39,40,41,47,48,67,70,71,83,86,89,101,105,106,115,117,121,125,127,130,132,134,135,136,140,143,144,146,150,],[-1,-2,-3,-4,-5,-6,-7,-8,-9,-11,-12,-13,-34,-35,-37,-38,-31,-32,-10,-33,-36,-26,-54,-52,-55,-27,-51,-61,-14,-15,-64,-56,-28,-63,-53,-60,-57,-62,-16,-17,-28,-21,147,-20,-19,]),'PLUS':([9,12,19,30,31,32,33,39,40,46,47,48,66,70,71,74,80,89,90,109,118,127,133,],[-36,-33,51,-34,-35,-37,-38,-31,-32,51,-33,-36,-36,51,-52,51,51,51,51,51,-52,-53,51,]),'MINUS':([9,12,19,30,31,32,33,39,40,46,47,48,66,70,71,74,80,89,90,109,118,127,133,],[-36,-33,52,-34,-35,-37,-38,-31,-32,52,-33,-36,-36,52,-52,52,52,52,52,52,-52,-53,52,]),'TIMES':([9,12,19,30,31,32,33,39,40,46,47,48,66,70,71,74,80,89,90,109,118,127,133,],[-36,-33,53,-34,-35,-37,-38,-31,-32,53,-33,-36,-36,53,-52,53,53,53,53,53,-52,-53,53,]),'DIVIDE':([9,12,19,30,31,32,33,39,40,46,47,48,66,70,71,74,80,89,90,109,118,127,133,],[-36,-33,54,-34,-35,-37,-38,-31,-32,54,-33,-36,-36,54,-52,54,54,54,54,54,-52,-53,54,]),'DOT':([12,],[43,]),'LANGLE':([21,25,30,31,32,33,39,40,47,48,70,71,74,127,],[56,61,-34,-35,-37,-38,-31,-32,-33,-36,-54,-52,94,-53,]),'COMMA':([30,31,32,33,39,40,46,47,48,66,70,71,127,],[-34,-35,-37,-38,-31,-32,68,-33,-36,-36,-54,-52,-53,]),'RPAREN':([30,31,32,33,39,40,44,45,46,47,48,62,64,66,70,71,73,80,88,98,99,104,109,118,127,],[-34,-35,-37,-38,-31,-32,65,67,-29,-33,-36,83,85,87,-54,-52,91,100,-30,111,112,117,-18,127,-53,]),'EQUALS':([30,31,32,33,39,40,47,48,49,60,70,71,74,110,116,127,],[-34,-35,-37,-38,-31,-32,-33,-36,69,81,-54,-52,93,120,126,-53,]),'RANGLE':([30,31,32,33,34,35,36,37,38,39,40,47,48,70,71,74,75,76,77,82,127,],[-34,-35,-37,-38,-39,-40,-41,-42,-45,-31,-32,-33,-36,-54,-52,95,-44,97,-43,103,-53,]),'NEQ':([30,31,32,33,39,40,47,48,70,71,74,127,],[-34,-35,-37,-38,-31,-32,-33,-36,-54,-52,96,-53,]),'RBRACKET':([30,31,32,33,39,40,46,47,48,70,71,88,127,138,],[-34,-35,-37,-38,-31,-32,-29,-33,-36,-54,-52,-30,-53,142,]),'TWODOTS':([30,31,32,33,39,40,47,48,70,71,127,133,],[-34,-35,-37,-38,-31,-32,-33,-36,-54,-52,-53,140,]),'DOTCOMMA':([65,85,87,128,139,142,148,],[86,105,106,136,143,146,150,]),'LBRACE':([81,91,100,112,126,137,],[102,108,113,122,102,141,]),'ARROWFUNCTION':([111,],[121,]),'CASE':([113,147,],[124,124,]),'LBRACKET':([120,],[129,]),'ELSE':([128,],[137,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'cuerpo':([0,108,121,122,140,141,],[1,119,130,131,144,145,]),'impresion':([0,108,121,122,140,141,],[2,2,2,2,2,2,]),'tupla':([0,108,121,122,140,141,],[3,3,3,3,3,3,]),'declaracion':([0,108,121,122,140,141,],[4,4,4,4,4,4,]),'sentenciaIf':([0,108,121,122,140,141,],[5,5,5,5,5,5,]),'estructuraList':([0,108,121,122,140,141,],[6,6,6,6,6,6,]),'funcionVoid':([0,108,121,122,140,141,],[7,7,7,7,7,7,]),'switch':([0,108,121,122,140,141,],[8,8,8,8,8,8,]),'operacion':([0,17,42,44,50,55,59,68,69,72,78,79,84,92,102,107,108,121,122,124,129,140,141,],[9,48,48,66,48,48,48,48,48,48,48,48,48,48,48,48,9,9,9,48,48,9,9,]),'flecha':([0,108,121,122,140,141,],[10,10,10,10,10,10,]),'funcion':([0,108,121,122,140,141,],[13,13,13,13,13,13,]),'funcionData':([0,108,121,122,140,141,],[14,14,14,14,14,14,]),'crearConjunto':([0,108,121,122,140,141,],[15,15,15,15,15,15,]),'tipoVariable':([0,108,121,122,140,141,],[18,18,18,18,18,18,]),'valor':([0,17,42,44,50,55,59,68,69,72,78,79,84,92,102,107,108,121,122,124,129,140,141,],[19,46,46,46,70,74,80,46,89,90,46,46,46,109,46,70,19,19,19,133,46,19,19,]),'type':([0,56,61,108,121,122,140,141,],[22,76,82,22,22,22,22,22,]),'Bool':([0,17,42,44,50,55,59,68,69,72,78,79,84,92,102,107,108,121,122,124,129,140,141,],[31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,]),'valores':([17,42,44,68,78,79,84,102,129,],[45,62,64,88,98,99,104,114,138,]),'operador':([19,46,70,74,80,89,90,109,133,],[50,50,50,50,50,50,107,50,50,]),'numeroSiguiente':([50,107,],[71,118,]),'condicion':([55,],[73,]),'operadorComp':([74,],[92,]),'conjunto':([81,126,],[101,134,]),'caso':([113,147,],[123,149,]),'else':([128,],[135,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> cuerpo","S'",1,None,None,None),
  ('cuerpo -> impresion','cuerpo',1,'p_cuerpo','main.py',9),
  ('cuerpo -> tupla','cuerpo',1,'p_cuerpo','main.py',10),
  ('cuerpo -> declaracion','cuerpo',1,'p_cuerpo','main.py',11),
  ('cuerpo -> sentenciaIf','cuerpo',1,'p_cuerpo','main.py',12),
  ('cuerpo -> estructuraList','cuerpo',1,'p_cuerpo','main.py',13),
  ('cuerpo -> funcionVoid','cuerpo',1,'p_cuerpo','main.py',14),
  ('cuerpo -> switch','cuerpo',1,'p_cuerpo','main.py',15),
  ('cuerpo -> operacion','cuerpo',1,'p_cuerpo','main.py',16),
  ('cuerpo -> flecha','cuerpo',1,'p_cuerpo','main.py',17),
  ('cuerpo -> RETURN VARIABLE','cuerpo',2,'p_cuerpo','main.py',18),
  ('cuerpo -> funcion','cuerpo',1,'p_cuerpo','main.py',19),
  ('cuerpo -> funcionData','cuerpo',1,'p_cuerpo','main.py',20),
  ('cuerpo -> crearConjunto','cuerpo',1,'p_cuerpo','main.py',21),
  ('impresion -> PRINT LPAREN valores RPAREN DOTCOMMA','impresion',5,'p_impresion','main.py',25),
  ('impresion -> PRINT LPAREN operacion RPAREN DOTCOMMA','impresion',5,'p_impresion','main.py',26),
  ('sentenciaIf -> IF LPAREN condicion RPAREN LBRACE cuerpo RBRACE else','sentenciaIf',8,'p_sentenciaIf','main.py',31),
  ('sentenciaIf -> IF LPAREN condicion RPAREN LBRACE cuerpo RBRACE DOTCOMMA','sentenciaIf',8,'p_sentenciaIf','main.py',32),
  ('condicion -> valor operadorComp valor','condicion',3,'p_condicion','main.py',35),
  ('else -> ELSE LBRACE cuerpo RBRACE DOTCOMMA','else',5,'p_else','main.py',39),
  ('estructuraList -> LIST LANGLE type RANGLE VARIABLE EQUALS LBRACKET valores RBRACKET DOTCOMMA','estructuraList',10,'p_estructuraList','main.py',43),
  ('funcionVoid -> VOID VARIABLE LPAREN valores RPAREN LBRACE cuerpo RBRACE DOTCOMMA','funcionVoid',9,'p_funcionVoid','main.py',47),
  ('operadorComp -> EQUALS','operadorComp',1,'p_operadorComp','main.py',50),
  ('operadorComp -> LANGLE','operadorComp',1,'p_operadorComp','main.py',51),
  ('operadorComp -> RANGLE','operadorComp',1,'p_operadorComp','main.py',52),
  ('operadorComp -> NEQ','operadorComp',1,'p_operadorComp','main.py',53),
  ('tupla -> LPAREN valores RPAREN','tupla',3,'p_tupla','main.py',56),
  ('impresion -> PRINT LPAREN RPAREN DOTCOMMA','impresion',4,'p_impresion_vacia','main.py',59),
  ('impresion -> <empty>','impresion',0,'p_impresion_varias','main.py',62),
  ('valores -> valor','valores',1,'p_valores','main.py',65),
  ('valores -> valor COMMA valores','valores',3,'p_valores','main.py',66),
  ('Bool -> TRUE','Bool',1,'p_Bool','main.py',69),
  ('Bool -> FALSE','Bool',1,'p_Bool','main.py',70),
  ('valor -> VARIABLE','valor',1,'p_valor','main.py',73),
  ('valor -> FLOAT','valor',1,'p_valor','main.py',74),
  ('valor -> Bool','valor',1,'p_valor','main.py',75),
  ('valor -> operacion','valor',1,'p_valor','main.py',76),
  ('valor -> NUMBER','valor',1,'p_valor','main.py',77),
  ('valor -> CHAINCHAR','valor',1,'p_valor','main.py',78),
  ('type -> MAP','type',1,'p_type','main.py',81),
  ('type -> DOUBLE','type',1,'p_type','main.py',82),
  ('type -> STRING','type',1,'p_type','main.py',83),
  ('type -> INT','type',1,'p_type','main.py',84),
  ('type -> SET','type',1,'p_type','main.py',85),
  ('type -> LIST','type',1,'p_type','main.py',86),
  ('type -> BOOLEAN','type',1,'p_type','main.py',87),
  ('tipoVariable -> type','tipoVariable',1,'p_tipoVariable','main.py',93),
  ('tipoVariable -> FINAL','tipoVariable',1,'p_tipoVariable','main.py',94),
  ('tipoVariable -> CONST','tipoVariable',1,'p_tipoVariable','main.py',95),
  ('tipoVariable -> VAR','tipoVariable',1,'p_tipoVariable','main.py',96),
  ('tipoVariable -> DYNAMIC','tipoVariable',1,'p_tipoVariable','main.py',97),
  ('declaracion -> tipoVariable VARIABLE EQUALS valor','declaracion',4,'p_declaracion','main.py',101),
  ('operacion -> valor operador numeroSiguiente','operacion',3,'p_operacion','main.py',104),
  ('numeroSiguiente -> LPAREN valor operador numeroSiguiente RPAREN','numeroSiguiente',5,'p_numeroSiguiente','main.py',107),
  ('numeroSiguiente -> valor','numeroSiguiente',1,'p_numeroSiguiente','main.py',108),
  ('funcion -> VARIABLE LPAREN valores RPAREN','funcion',4,'p_funcion','main.py',111),
  ('funcionData -> VARIABLE DOT VARIABLE LPAREN valores RPAREN','funcionData',6,'p_funcionData','main.py',114),
  ('switch -> SWITCH LPAREN valor RPAREN LBRACE caso RBRACE','switch',7,'p_sentenciaSwitch','main.py',118),
  ('caso -> CASE valor TWODOTS cuerpo BREAK caso','caso',6,'p_casos','main.py',121),
  ('caso -> CASE valor TWODOTS cuerpo BREAK','caso',5,'p_casos','main.py',122),
  ('flecha -> type VARIABLE LPAREN valores RPAREN ARROWFUNCTION cuerpo','flecha',7,'p_funcionflecha','main.py',128),
  ('crearConjunto -> SET VARIABLE EQUALS conjunto','crearConjunto',4,'p_crearConjunto','main.py',134),
  ('crearConjunto -> SET LANGLE type RANGLE VARIABLE EQUALS conjunto','crearConjunto',7,'p_crearConjunto','main.py',135),
  ('conjunto -> LBRACE valores RBRACE','conjunto',3,'p_conjunto','main.py',138),
  ('conjunto -> LBRACE RBRACE','conjunto',2,'p_conjunto','main.py',139),
  ('operador -> PLUS','operador',1,'p_operador','main.py',143),
  ('operador -> MINUS','operador',1,'p_operador','main.py',144),
  ('operador -> TIMES','operador',1,'p_operador','main.py',145),
  ('operador -> DIVIDE','operador',1,'p_operador','main.py',146),
]

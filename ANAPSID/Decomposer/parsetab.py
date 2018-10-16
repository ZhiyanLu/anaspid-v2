
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = '\x96>\x04t\xfa?\tuk\x81F3\xd1N*\xbe'
    
_lr_action_items = {'LPAR':([29,],[41,]),'CONSTANT':([7,16,17,38,39,40,41,65,66,67,68,70,71,],[-8,-6,-7,53,-36,-37,57,57,57,57,57,57,57,]),'LESS':([57,58,59,75,76,77,78,79,80,],[-29,-30,66,66,66,66,66,66,66,]),'NEQUALS':([57,58,59,75,76,77,78,79,80,],[-29,-30,67,67,67,67,67,67,67,]),'RPAR':([57,58,59,75,76,77,78,79,80,],[-29,-30,69,-33,-31,-35,-28,-34,-32,]),'PREFIX':([0,3,6,7,16,17,],[1,1,-5,-8,-6,-7,]),'SELECT':([0,3,4,5,6,7,9,16,17,],[-4,-4,11,-3,-5,-8,-2,-6,-7,]),'POINT':([7,16,17,27,36,50,53,54,55,56,61,63,69,73,],[-8,-6,-7,-21,49,49,-42,-27,-40,-41,-24,49,-22,-23,]),'DISTINCT':([11,],[14,]),'OPTIONAL':([7,16,17,24,25,27,32,36,43,47,49,50,53,54,55,56,61,63,69,73,],[-8,-6,-7,34,34,-21,34,34,34,34,34,34,-42,-27,-40,-41,-24,34,-22,-23,]),'GREATEREQ':([57,58,59,75,76,77,78,79,80,],[-29,-30,70,70,70,70,70,70,70,]),'COLON':([8,],[12,]),'$end':([2,10,45,52,],[0,-1,-10,-9,]),'LKEY':([7,16,17,21,23,24,25,27,32,34,36,43,47,49,50,53,54,55,56,61,63,69,73,],[-8,-6,-7,24,25,32,32,-21,32,47,32,32,32,32,32,-42,-27,-40,-41,-24,32,-22,-23,]),'UNION':([7,16,17,27,30,36,48,50,51,53,54,55,56,60,61,63,64,69,73,74,],[-8,-6,-7,-21,43,-4,-17,-4,-18,-42,-27,-40,-41,43,-24,-4,-20,-22,-23,-19,]),'RKEY':([7,16,17,26,27,30,31,36,37,42,44,46,48,50,51,53,54,55,56,60,61,62,63,64,69,72,73,74,],[-8,-6,-7,-13,-21,-4,45,-4,52,-14,-15,61,-17,-4,-18,-42,-27,-40,-41,-4,-24,73,-4,-20,-22,-16,-23,-19,]),'URI':([1,7,12,16,17,24,25,27,28,32,33,35,36,38,39,40,43,47,49,50,53,54,55,56,61,63,69,73,],[7,-8,17,-6,-7,7,7,-21,7,7,-39,-38,7,7,-36,-37,7,7,7,7,-42,-27,-40,-41,-24,7,-22,-23,]),'EQUALS':([57,58,59,75,76,77,78,79,80,],[-29,-30,68,68,68,68,68,68,68,]),'VARIABLE':([7,11,13,14,15,16,17,19,20,22,24,25,27,28,32,33,35,36,38,39,40,41,43,47,49,50,53,54,55,56,61,63,65,66,67,68,69,70,71,73,],[-8,-4,19,-11,-12,-6,-7,-26,22,-25,33,33,-21,40,33,-39,-38,33,56,-36,-37,58,33,33,33,33,-42,-27,-40,-41,-24,33,58,58,58,58,-22,58,58,-23,]),'WHERE':([18,19,20,22,],[21,-26,23,-25,]),'ID':([1,7,12,16,17,24,25,27,28,32,33,35,36,38,39,40,43,47,49,50,53,54,55,56,61,63,69,73,],[8,-8,16,-6,-7,8,8,-21,8,8,-39,-38,8,8,-36,-37,8,8,8,8,-42,-27,-40,-41,-24,8,-22,-23,]),'ALL':([11,13,14,15,],[-4,18,-11,-12,]),'GREATER':([57,58,59,75,76,77,78,79,80,],[-29,-30,65,65,65,65,65,65,65,]),'FILTER':([7,16,17,24,25,27,32,36,43,47,49,50,53,54,55,56,61,63,69,73,],[-8,-6,-7,29,29,-21,29,29,29,29,29,29,-42,-27,-40,-41,-24,29,-22,-23,]),'LESSEQ':([57,58,59,75,76,77,78,79,80,],[-29,-30,71,71,71,71,71,71,71,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'bgp':([24,25,32,36,43,47,49,50,63,],[36,36,36,50,36,36,63,50,50,]),'predicate':([28,],[38,]),'join_block':([24,25,32,43,47,],[30,30,30,60,30,]),'distinct':([11,],[13,]),'expression':([41,65,66,67,68,70,71,],[59,75,76,77,78,79,80,]),'object':([38,],[54,]),'rest_join_block':([36,50,63,],[48,64,74,]),'uri':([1,24,25,28,32,36,38,43,47,49,50,63,],[6,35,35,39,35,35,55,35,35,35,35,35,]),'parse_sparql':([0,],[2,]),'group_graph_pattern':([24,25,32,47,],[31,37,46,62,]),'rest_union_block':([30,60,],[42,72,]),'prefix':([0,3,],[3,3,]),'triple':([24,25,32,36,43,47,49,50,63,],[27,27,27,27,27,27,27,27,27,]),'union_block':([24,25,32,47,],[26,26,26,26,]),'query':([4,],[10,]),'var_list':([13,],[20,]),'prefix_list':([0,3,],[4,9,]),'empty':([0,3,11,30,36,50,60,63,],[5,5,15,44,51,51,44,51,]),'subject':([24,25,32,36,43,47,49,50,63,],[28,28,28,28,28,28,28,28,28,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> parse_sparql","S'",1,None,None,None),
  ('parse_sparql -> prefix_list query','parse_sparql',2,'p_parse_sparql','/home/gabriela/Anapsid/ANAPSID/Decomposer/parseQuery.py',96),
  ('prefix_list -> prefix prefix_list','prefix_list',2,'p_prefix_list','/home/gabriela/Anapsid/ANAPSID/Decomposer/parseQuery.py',103),
  ('prefix_list -> empty','prefix_list',1,'p_empty_prefix_list','/home/gabriela/Anapsid/ANAPSID/Decomposer/parseQuery.py',109),
  ('empty -> <empty>','empty',0,'p_empty','/home/gabriela/Anapsid/ANAPSID/Decomposer/parseQuery.py',115),
  ('prefix -> PREFIX uri','prefix',2,'p_prefix','/home/gabriela/Anapsid/ANAPSID/Decomposer/parseQuery.py',121),
  ('uri -> ID COLON ID','uri',3,'p_uri_0','/home/gabriela/Anapsid/ANAPSID/Decomposer/parseQuery.py',133),
  ('uri -> ID COLON URI','uri',3,'p_uri_1','/home/gabriela/Anapsid/ANAPSID/Decomposer/parseQuery.py',139),
  ('uri -> URI','uri',1,'p_uri_2','/home/gabriela/Anapsid/ANAPSID/Decomposer/parseQuery.py',145),
  ('query -> SELECT distinct var_list WHERE LKEY group_graph_pattern RKEY','query',7,'p_query_0','/home/gabriela/Anapsid/ANAPSID/Decomposer/parseQuery.py',151),
  ('query -> SELECT distinct ALL WHERE LKEY group_graph_pattern RKEY','query',7,'p_query_1','/home/gabriela/Anapsid/ANAPSID/Decomposer/parseQuery.py',157),
  ('distinct -> DISTINCT','distinct',1,'p_distinct_0','/home/gabriela/Anapsid/ANAPSID/Decomposer/parseQuery.py',163),
  ('distinct -> empty','distinct',1,'p_distinct_1','/home/gabriela/Anapsid/ANAPSID/Decomposer/parseQuery.py',169),
  ('group_graph_pattern -> union_block','group_graph_pattern',1,'p_ggp_0','/home/gabriela/Anapsid/ANAPSID/Decomposer/parseQuery.py',175),
  ('union_block -> join_block rest_union_block','union_block',2,'p_union_block_0','/home/gabriela/Anapsid/ANAPSID/Decomposer/parseQuery.py',181),
  ('rest_union_block -> empty','rest_union_block',1,'p_rest_union_block_0','/home/gabriela/Anapsid/ANAPSID/Decomposer/parseQuery.py',187),
  ('rest_union_block -> UNION join_block rest_union_block','rest_union_block',3,'p_rest_union_block_1','/home/gabriela/Anapsid/ANAPSID/Decomposer/parseQuery.py',193),
  ('join_block -> bgp rest_join_block','join_block',2,'p_join_block','/home/gabriela/Anapsid/ANAPSID/Decomposer/parseQuery.py',199),
  ('rest_join_block -> empty','rest_join_block',1,'p_rest_join_block_0','/home/gabriela/Anapsid/ANAPSID/Decomposer/parseQuery.py',205),
  ('rest_join_block -> POINT bgp rest_join_block','rest_join_block',3,'p_rest_join_block_1','/home/gabriela/Anapsid/ANAPSID/Decomposer/parseQuery.py',211),
  ('rest_join_block -> bgp rest_join_block','rest_join_block',2,'p_rest_join_block_2','/home/gabriela/Anapsid/ANAPSID/Decomposer/parseQuery.py',217),
  ('bgp -> triple','bgp',1,'p_bgp_0','/home/gabriela/Anapsid/ANAPSID/Decomposer/parseQuery.py',224),
  ('bgp -> FILTER LPAR expression RPAR','bgp',4,'p_bgp_1','/home/gabriela/Anapsid/ANAPSID/Decomposer/parseQuery.py',230),
  ('bgp -> OPTIONAL LKEY group_graph_pattern RKEY','bgp',4,'p_bgp_2','/home/gabriela/Anapsid/ANAPSID/Decomposer/parseQuery.py',236),
  ('bgp -> LKEY group_graph_pattern RKEY','bgp',3,'p_bgp_3','/home/gabriela/Anapsid/ANAPSID/Decomposer/parseQuery.py',242),
  ('var_list -> var_list VARIABLE','var_list',2,'p_var_list','/home/gabriela/Anapsid/ANAPSID/Decomposer/parseQuery.py',248),
  ('var_list -> VARIABLE','var_list',1,'p_single_var_list','/home/gabriela/Anapsid/ANAPSID/Decomposer/parseQuery.py',254),
  ('triple -> subject predicate object','triple',3,'p_triple_0','/home/gabriela/Anapsid/ANAPSID/Decomposer/parseQuery.py',272),
  ('expression -> expression EQUALS expression','expression',3,'p_expression_0','/home/gabriela/Anapsid/ANAPSID/Decomposer/parseQuery.py',278),
  ('expression -> CONSTANT','expression',1,'p_expression_1','/home/gabriela/Anapsid/ANAPSID/Decomposer/parseQuery.py',284),
  ('expression -> VARIABLE','expression',1,'p_expression_2','/home/gabriela/Anapsid/ANAPSID/Decomposer/parseQuery.py',290),
  ('expression -> expression LESS expression','expression',3,'p_expression_3','/home/gabriela/Anapsid/ANAPSID/Decomposer/parseQuery.py',296),
  ('expression -> expression LESSEQ expression','expression',3,'p_expression_4','/home/gabriela/Anapsid/ANAPSID/Decomposer/parseQuery.py',302),
  ('expression -> expression GREATER expression','expression',3,'p_expression_5','/home/gabriela/Anapsid/ANAPSID/Decomposer/parseQuery.py',308),
  ('expression -> expression GREATEREQ expression','expression',3,'p_expression_6','/home/gabriela/Anapsid/ANAPSID/Decomposer/parseQuery.py',314),
  ('expression -> expression NEQUALS expression','expression',3,'p_expression_7','/home/gabriela/Anapsid/ANAPSID/Decomposer/parseQuery.py',320),
  ('predicate -> uri','predicate',1,'p_predicate_uri','/home/gabriela/Anapsid/ANAPSID/Decomposer/parseQuery.py',338),
  ('predicate -> VARIABLE','predicate',1,'p_predicate_var','/home/gabriela/Anapsid/ANAPSID/Decomposer/parseQuery.py',344),
  ('subject -> uri','subject',1,'p_subject_uri','/home/gabriela/Anapsid/ANAPSID/Decomposer/parseQuery.py',350),
  ('subject -> VARIABLE','subject',1,'p_subject_variable','/home/gabriela/Anapsid/ANAPSID/Decomposer/parseQuery.py',356),
  ('object -> uri','object',1,'p_object_uri','/home/gabriela/Anapsid/ANAPSID/Decomposer/parseQuery.py',362),
  ('object -> VARIABLE','object',1,'p_object_variable','/home/gabriela/Anapsid/ANAPSID/Decomposer/parseQuery.py',368),
  ('object -> CONSTANT','object',1,'p_object_constant','/home/gabriela/Anapsid/ANAPSID/Decomposer/parseQuery.py',374),
]
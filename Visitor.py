from visitor_abstract import visitor_abstract

tab = 0

def blank():
    p = ''
    for x in range(tab):
        p = p + ' '
    return p

class Visitor(visitor_abstract):

    def visit_decl_classeConcrete(self, decl_classeConcrete):
       print(blank(), decl_classeConcrete.Class,' ' ,decl_classeConcrete.id, '{', end='', sep='')
       decl_classeConcrete.Class.accept(self)
       decl_classeConcrete.id.accept(self)
       if(decl_classeConcrete.body_class):
          decl_classeConcrete.body_class.accept(self)
       print('}',';', end='', sep='')
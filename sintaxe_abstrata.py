from abc import abstractmethod
from abc import ABCMeta
from Visitor import Visitor

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
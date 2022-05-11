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
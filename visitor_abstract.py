from abc import abstractmethod
from abc import ABCMeta

class visitor_abstract(metaclass=ABCMeta):

    @abstractmethod
    def visit_decl_classeConcrete(self, decl_classeConcrete):
        pass
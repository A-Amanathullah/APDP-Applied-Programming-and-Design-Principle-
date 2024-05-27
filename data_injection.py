from abc import ABC, abstractmethod

class IData_injection(ABC):
  @abstractmethod
  
  def data_inject(self,path):
    pass

class CSV_data_injector(IData_injection):
  def data_inject(self, path):
    with open (path,"r") as csv:
      
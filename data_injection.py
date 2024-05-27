from abc import ABC, abstractmethod
import JSON as json

class IData_injection(ABC):
  @abstractmethod
  
  def data_inject(self,path):
    pass

class JSON_data_injector(IData_injection):
  def data_inject(self, path):
    with open (path,"r") as j:
      json_data = json.load(j)
      return json_data
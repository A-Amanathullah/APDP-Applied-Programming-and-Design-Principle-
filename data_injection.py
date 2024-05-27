from abc import ABC, abstractmethod
import JSON as json

class IData_injection(ABC):
  @abstractmethod
  
  def data_inject(self,path):
    pass

class IJSON_data_injector(IData_injection):
  def data_inject(self, path):
    with open (path,"r") as j:
      json_data = json.load(j)
      return json_data
    
class ICSV_data_injector(IData_injection):
  def data_inject(self, path):
    with open (path,"r") as c:
      csv_data = json.load(c)
      return csv_data
import pandas as pd
from abc import ABC, abstractmethod
import csv as c

class Idata(ABC):
    @abstractmethod
    def data_inject(self):
        pass

    @abstractmethod    
    def data_preprocess(self):
        pass

class Idata_inject(Idata):
    @abstractmethod
    def data_inject(self,path):
        pass
        
class Idata_preprocess(Idata):
    @abstractmethod
    def data_preprocess(self,path):
        pass

class Csv(Idata_inject):
    def __init__(self,path):
        self.path = path

    def data_inject(self, path):
        with open (path ,"r") as file:
            reader = c.DictReader(file)
            data = list(reader)
            return data
        
class Graph(Idata_inject):
    def __init__(self,path):
        pass
    def data_inject(self, path):
        pass


file_path = r'D:\HND\sem-4\APDP\Class Activites\data\new_sales.csv'
csv = Csv(file_path)
csv.data_inject(file_path)
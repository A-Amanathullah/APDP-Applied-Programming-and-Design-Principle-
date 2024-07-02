from abc import ABC, abstractmethod
import json
import pandas as pd
import xml.etree.ElementTree as ET


class ImportFactory(ABC):
    @abstractmethod
    def create_importer(self):
        pass

class Importer(ABC):
    @abstractmethod
    def import_data(self,file_path):
        pass


class JsonImporter(Importer):
    def import_data(self, file_path):
        with open (file_path, 'r') as file:
            data = json.load(file)
        return data
    
class CsvImporter(Importer):
    def import_data(self, file_path):
        with open (file_path, 'r') as file:
            data = pd.read_csv(file)
        return data
    

class XmlImporter(Importer):
    def import_data(self, file_path):
        with open (file_path, 'r') as file:
            tree = ET.parse(file_path)
            root = tree.getroot()
            data = [{elem.tag: elem.text for elem in child} for child in root]
        return data
    

class JsonImportFactory(ImportFactory):
    def create_importer(self):
        return JsonImporter()
    
class CsvImportFactory(ImportFactory):
    def create_importer(self):
        return CsvImporter()
    
class XmlImportFactory(ImportFactory):
    def create_importer(self):
        return XmlImporter()
    

def import_data(factory: ImportFactory,file_path : str):
    importer = factory.create_importer()
    data = importer.import_data(file_path)
    return data


if __name__ == "__main__":
    json_factory = JsonImportFactory()
    csv_factory = CsvImportFactory()
    xml_factory = XmlImportFactory()

   # json_data = import_data(json_factory, 'data.json')
    csv_data = import_data(csv_factory, 'data/sales_orders_sheet.csv')
   # xml_data = import_data(xml_factory, 'data.xml')

   # print("JSON DATA : ", json_data)
    print("CSV DATA : ", csv_data)
   # print("XML DATA : ", xml_data)
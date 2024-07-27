import pandas as pd
from data_import import JsonImporter, CsvImporter, XmlImporter
import pytest

def test_json_importer():
    importer = JsonImporter()
    data = importer.import_data('tests/data/test_data.json')
    assert isinstance(data, dict)
    assert 'sales' in data

def test_csv_importer():
    importer = CsvImporter()
    data = importer.import_data('tests/data/test_data.csv')
    assert isinstance(data, pd.DataFrame)
    assert 'productid' in data.columns

def test_xml_importer():
    importer = XmlImporter()
    data = importer.import_data('tests/data/test_data.xml')
    assert isinstance(data, list)
    assert 'customerid' in data[0]

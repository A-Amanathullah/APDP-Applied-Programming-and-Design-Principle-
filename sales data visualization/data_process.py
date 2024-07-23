from data_import import *

class DataImporter:
    def __init__(self, factory, file_path):
        self.factory = factory
        self.file_path = file_path

    def import_data(self):
        return import_data(self.factory, self.file_path)

class DataMerger:
    def __init__(self, order_data, product_data, customer_data):
        self.order_data = order_data
        self.product_data = product_data
        self.customer_data = customer_data

    def merge_data(self):
        with_product_data = self.order_data.merge(self.product_data, how='inner', on='productid')
        all_data = with_product_data.merge(self.customer_data, how='inner', on='customerid')
        return all_data

class DataProcessor:
    def __init__(self, data):
        self.data = data

    def process_data(self):
        final_data = self.data.drop(
            ['productid', 'customerid', 'warehousecode', 'orderdate', 'shipdate',
             'procureddate', 'salesteamid', 'storeid'], axis=1)

        final_data['discount_amount'] = final_data['unit_price'] * final_data['discount_applied']
        final_data['net_price'] = (final_data['unit_price'] - final_data['discount_amount']) * final_data['order_quantity']
        final_data['profit'] = final_data['net_price'] - (final_data['unit_cost'] * final_data['order_quantity'])

        return final_data

# Factory instantiation
csv_factory = CsvImportFactory()

# Import data
order_importer = DataImporter(csv_factory, 'data/sales_orders_sheet.csv')
product_importer = DataImporter(csv_factory, 'data/products_sheet.csv')
customer_importer = DataImporter(csv_factory, 'data/customers_sheet.csv')

order_data = order_importer.import_data()
product_data = product_importer.import_data()
customer_data = customer_importer.import_data()

# Merge data
merger = DataMerger(order_data, product_data, customer_data)
all_data = merger.merge_data()

# Process data
processor = DataProcessor(all_data)
final_data = processor.process_data()

data = final_data
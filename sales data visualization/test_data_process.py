from data_process import DataMerger, DataProcessor
import pandas as pd

def test_data_merger():
    order_data = pd.DataFrame({'productid': [1, 2], 'customerid': [1, 2]})
    product_data = pd.DataFrame({'productid': [1, 2], 'product_name': ['Product A', 'Product B']})
    customer_data = pd.DataFrame({'customerid': [1, 2], 'customer_names': ['Customer A', 'Customer B']})
    
    merger = DataMerger(order_data, product_data, customer_data)
    merged_data = merger.merge_data()
    
    assert 'product_name' in merged_data.columns
    assert 'customer_names' in merged_data.columns

def test_data_processor():
    data = pd.DataFrame({
        'unit_price': [100, 200],
        'discount_applied': [0.1, 0.2],
        'order_quantity': [10, 20],
        'unit_cost': [50, 150]
    })
    
    processor = DataProcessor(data)
    processed_data = processor.process_data()
    
    assert 'discount_amount' in processed_data.columns
    assert 'net_price' in processed_data.columns
    assert 'profit' in processed_data.columns

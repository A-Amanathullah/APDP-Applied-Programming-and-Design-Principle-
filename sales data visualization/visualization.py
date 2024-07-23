from abc import ABC, abstractmethod
import pandas as pd
import streamlit as st
import plotly.express as px
from data_process import *
from datetime import datetime

class VisualizationStrategy(ABC):
    @abstractmethod
    def visualize(self, data, mask):
        pass

class ChannelBasedVisualization(VisualizationStrategy):
    def visualize(self, data, mask):
        filtered_data = data[mask].groupby('sales_channel').agg({
            'customer_names': 'first',
            'profit': 'sum',
            'deliverydate': 'first',
            'discount_amount': 'sum'
        }).reset_index()

        bar_chart = px.bar(filtered_data,
                           title='Profits for channels in bar chart',
                           x='sales_channel',
                           y='profit',
                           color_discrete_sequence=['#F63366']*len(filtered_data),
                           template='plotly_white')

        pie_chart = px.pie(filtered_data,
                           title="Profits for channels in pie chart",
                           values='profit',
                           names='sales_channel')

        funnel_chart = px.funnel(filtered_data,
                                 x='discount_amount',
                                 y='sales_channel',
                                 title="Discount based")

        col1, col2, col3 = st.columns(3)
        col1.plotly_chart(pie_chart)
        col2.plotly_chart(bar_chart)
        col3.plotly_chart(funnel_chart)

class CustomerBasedVisualization(VisualizationStrategy):
    def visualize(self, data, mask):
        filtered_data = data[mask].groupby('customer_names').agg({
            'discount_amount': 'sum',
            'order_quantity': 'sum',
            'profit': 'sum'
        }).reset_index()

        bar_chart = px.bar(filtered_data,
                           title='Profits by customer in bar chart',
                           x='customer_names',
                           y='profit',
                           color_discrete_sequence=['#F63366']*len(filtered_data),
                           template='plotly_white')

        scatter_chart = px.scatter(filtered_data,
                                   x='customer_names',
                                   y='discount_amount',
                                   title="Discounts")

        col4, col5 = st.columns(2)
        col4.plotly_chart(bar_chart)
        col5.plotly_chart(scatter_chart)

class ProductBasedVisualization(VisualizationStrategy):
    def visualize(self, data, mask):
        filtered_data = data[mask].groupby('product_name').agg({
            'customer_names': 'count',
            'order_quantity': 'sum',
            'profit': 'sum',
            'discount_amount': 'sum'
        }).reset_index()

        line_chart = px.line(filtered_data,
                             title="Customer highly liked products",
                             x='product_name',
                             y='customer_names')

        bar_chart = px.bar(filtered_data,
                           title='Profits product vise',
                           x='profit',
                           y='product_name',
                           color_discrete_sequence=['#F63366']*len(filtered_data),
                           template='plotly_white')

        st.plotly_chart(bar_chart)
        st.plotly_chart(line_chart)

class Visualizer:
    def __init__(self, strategy: VisualizationStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: VisualizationStrategy):
        self.strategy = strategy

    def visualize(self, data, mask):
        self.strategy.visualize(data, mask)

# visulalization part / main part

st.set_page_config(page_title="Visualization")
st.header("Data Visualization")
st.subheader("Sales Data in Table")

# Display the whole data
st.dataframe(data)

# Option menu
options = ['Channel based', 'Customer based', 'Product based']
selected_option = st.selectbox('Select an option:', options)

# Date slider
data['deliverydate'] = pd.to_datetime(data['deliverydate'])
start_date = data['deliverydate'].min().date()
end_date = data['deliverydate'].max().date()

date_selection = st.slider("Select date range",
                           min_value=start_date,
                           max_value=end_date,
                           value=(start_date, end_date),
                           format="DD/MM/YYYY")

start_date_selected = pd.to_datetime(date_selection[0])
end_date_selected = pd.to_datetime(date_selection[1])

mask = (data['deliverydate'] >= start_date_selected) & (data['deliverydate'] <= end_date_selected)

# Visualization based on the selected option
if selected_option == "Channel based":
    strategy = ChannelBasedVisualization()
elif selected_option == "Customer based":
    strategy = CustomerBasedVisualization()
elif selected_option == "Product based":
    strategy = ProductBasedVisualization()

visualizer = Visualizer(strategy)
visualizer.visualize(data, mask)
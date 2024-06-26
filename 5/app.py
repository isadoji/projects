import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import streamlit as st

car_data = pd.read_csv('vehicles_us_filtered.csv')

st.markdown('<p style="font-size: 40px;">Model and average price of vehicles.</p>', unsafe_allow_html=True)

st.markdown('<p style="font-size: 30px;">The dataset information:</p>', unsafe_allow_html=True)

st.markdown('<style>body { font-size: 20px; }</style>', unsafe_allow_html=True)
st.write('''

* price — price of the vehicle.
* model_year — vehicle model year.
* model — vehicle model.
* condition — condition or state in which the vehicle is found.
* cylinders — cylinders that the vehicle has.
* fuel — gasoline, diesel, etc.
* odometer — the vehicle's mileage when the ad was published
* transmission — type of transmission the vehicle has.
* paint_color — vehicle color.
* is_4wd — if the vehicle has 4-wheel drive (False=0, True=1)
* date_posted — the date the ad was posted.
* days_listed — from publication until it is deleted.
''')
st.markdown('<p style="font-size: 30px;">Models of vehicles.</p>', unsafe_allow_html=True)
counts = car_data['brand'].value_counts()
fig = px.histogram(car_data, x='brand', category_orders={'brand': counts.index.tolist()})
fig.update_xaxes(title_text='Brand',tickangle=45)
fig.update_yaxes(title_text='Counts',)
fig.update_traces(marker_color='blue',marker=dict(opacity=0.7))
fig.update_layout(title='Number of cars per model')
st.plotly_chart(fig, use_container_width=True)

st.markdown('<p style="font-size: 20px;">Average price (USD) per model.</p>', unsafe_allow_html=True)

mean_price = car_data.groupby('brand')['price'].mean().sort_values(ascending=True).round()

if st.checkbox('Table of average price per model'):
    st.write(mean_price)

hist_button = st.button('Bar chart display of average price per model') 
if hist_button: 
        fig = px.bar(mean_price, x=mean_price.index, y=mean_price.values, labels={'x':'Brand', 'y':'Mean Price'})
        fig.update_xaxes(title_text='Brand',tickangle=45)
        fig.update_yaxes(title_text='Average price (USD)',)
        fig.update_traces(marker_color='green',marker=dict(opacity=0.7))
        fig.update_layout(title='Average price per model')
        st.plotly_chart(fig, use_container_width=True)

st.markdown('<p style="font-size: 30px;">Year of vehicles.</p>', unsafe_allow_html=True)
fig = make_subplots(rows=1, cols=2,subplot_titles=('Cars Per Year',  'Price (USD) by Model Year'))
hist = px.histogram(car_data[car_data['model_year'] > 0], y='model_year')
fig.add_trace(
    go.Histogram(x=hist.data[0].x, y=hist.data[0].y, marker_color='lightpink'),
    row=1, col=1
)
scatter = px.scatter(car_data[car_data['model_year'] > 0], y='model_year', x='price')
fig.add_trace(
    go.Scatter(x=scatter.data[0].x, y=scatter.data[0].y, marker=dict(opacity=0.7),mode='markers'),
    row=1, col=2
)
fig.update_yaxes(title_text='Model year', row=1, col=1)
fig.update_xaxes(title_text='Counts', row=1, col=1)
fig.update_xaxes(title_text='Price (USD)', row=1, col=2)
st.plotly_chart(fig, use_container_width=True)



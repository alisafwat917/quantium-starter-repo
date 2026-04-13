import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

# 1. Load the data you generated in the previous step
df = pd.read_csv('formatted_sales_data.csv')

# Ensure the 'date' column is a proper datetime object, then sort the dataframe
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values(by='date')

# Initialize the Dash app
app = dash.Dash(__name__)

# 2. Create the line chart using Plotly Express
fig = px.line(df, x='date', y='sales', color='region', title='Pink Morsel Sales (By Region)')

# Update axis labels as requested
fig.update_layout(xaxis_title='Date', yaxis_title='Sales ($)')

# FIXED: Add a vertical line to mark the price increase on Jan 15, 2021
# (The text annotation has been removed to prevent the date string math error)
fig.add_vline(x='2021-01-15', line_dash="dash", line_color="red")

# 3. Define the layout of the app
app.layout = html.Div(children=[
    # The Header
    html.H1(children='Pink Morsel Sales Visualizer', style={'textAlign': 'center'}),
    
    # The Line Chart
    dcc.Graph(
        id='sales-line-chart',
        figure=fig
    )
])

# Run the server
if __name__ == '__main__':
    app.run(debug=True)
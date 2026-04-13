import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# 1. Load and sort the data
df = pd.read_csv('formatted_sales_data.csv')
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values(by='date')

# Initialize the Dash app
app = dash.Dash(__name__)

# 2. Define a custom color palette for styling
colors = {
    'background': '#F4F4F9',
    'text': '#2C3E50',
    'accent': '#E74C3C', # A nice red for the price increase line
    'card': '#FFFFFF'
}

# 3. Define the layout with CSS styling
app.layout = html.Div(
    style={
        'backgroundColor': colors['background'], 
        'padding': '40px', 
        'fontFamily': 'Helvetica, Arial, sans-serif',
        'minHeight': '100vh'
    }, 
    children=[
    
        # Header Container
        html.Div(
            style={
                'backgroundColor': colors['card'],
                'padding': '20px',
                'borderRadius': '10px',
                'boxShadow': '0 4px 6px rgba(0,0,0,0.1)',
                'marginBottom': '30px'
            },
            children=[
                html.H1(
                    children='Soul Foods: Pink Morsel Sales', 
                    style={'textAlign': 'center', 'color': colors['text'], 'margin': '0'}
                ),
            ]
        ),
        
        # Radio Buttons Container
        html.Div(
            style={
                'textAlign': 'center', 
                'marginBottom': '30px',
                'padding': '15px',
                'backgroundColor': colors['card'],
                'borderRadius': '10px',
                'boxShadow': '0 2px 4px rgba(0,0,0,0.05)'
            },
            children=[
                dcc.RadioItems(
                    id='region-filter',
                    options=[
                        {'label': ' North', 'value': 'north'},
                        {'label': ' East', 'value': 'east'},
                        {'label': ' South', 'value': 'south'},
                        {'label': ' West', 'value': 'west'},
                        {'label': ' All Regions', 'value': 'all'}
                    ],
                    value='all', # Set default value
                    inline=True, # Display horizontally
                    style={'fontSize': '18px', 'color': colors['text'], 'cursor': 'pointer'}
                )
            ]
        ),
        
        # Graph Container
        html.Div(
            style={
                'backgroundColor': colors['card'],
                'padding': '20px',
                'borderRadius': '10px',
                'boxShadow': '0 4px 6px rgba(0,0,0,0.1)'
            },
            children=[
                dcc.Graph(id='sales-line-chart')
            ]
        )
])

# 4. Define the Callback to make the app interactive
@app.callback(
    Output('sales-line-chart', 'figure'),
    Input('region-filter', 'value')
)
def update_graph(selected_region):
    # Filter the dataframe based on the radio button selection
    if selected_region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'] == selected_region]
        
    # Generate the new figure
    fig = px.line(
        filtered_df, 
        x='date', 
        y='sales', 
        color='region' if selected_region == 'all' else None,
    )
    
    # Style the interior of the Plotly graph to match our app
    fig.update_layout(
        plot_bgcolor=colors['card'],
        paper_bgcolor=colors['card'],
        font_color=colors['text'],
        xaxis_title='Date',
        yaxis_title='Sales ($)',
        margin={'l': 40, 'b': 40, 't': 40, 'r': 40}
    )
    
    # Keep the vertical line for the price increase
    fig.add_vline(x='2021-01-15', line_dash="dash", line_color=colors['accent'])
    
    return fig

# Run the server
if __name__ == '__main__':
    app.run(debug=True)
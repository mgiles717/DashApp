"""

Dash Application built to explore the Flexbility dispatches (18/04/2024) dataset from the 
UK Power Network Open Data Portal as of 21/04/2024. The dataset will not be provided alongside 
this repository.

"""

# Imports
from dash import Dash, html, dash_table, dcc

import plotly.express as px
import pandas as pd
import dash_design_kit as ddk

# DataFrame
df = pd.read_csv('../data/ukpn-flexibility-dispatches.csv')

# Initialize app
app = Dash(__name__)

# App layout
app.layout = html.Div([
    html.H1(children='Flexibility Dispatches', style={'textAlign':'center'}),
    dash_table.DataTable(data=df.to_dict('records'), page_size=10),
    dcc.Graph(figure=px.histogram(df, x='company_name', y='mwh_requested', histfunc='avg'))
])

# Main method
def main():
    app.run(debug=True) 
    
if __name__ == '__main__':
    main()
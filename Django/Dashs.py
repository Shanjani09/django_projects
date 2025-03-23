import dash
from dash import html, dcc
app = dash.Dash(__name__) 
app.layout = html.Div([ 
    html.H3("Very First Dash Application"),
        dcc.Input(placeholder='Enter text here in lowerCase...') 
])
if __name__== '__main__':
    app.run_server(debug=True)
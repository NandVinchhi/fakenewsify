import predict
import dash
from dash.dependencies import Input, Output, State
import dash_html_components as html
import dash_core_components as dcc

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


app.layout = html.Div([
	html.H3("Fake News Classifier", style = {'color':'#696969'}),
	html.P("This is an open source fake news classifier, made with python scikit-learn library and plotly dash front-end. It takes the title and text content of a news article as its inputs and classifies it into fake or real. This project was made for the purpose of RookieHacks 2020. check the github repo for more info: ", style = {'color':'#696969'}),
	html.A("GitHub repo", href='https://github.com/NandVinchhi/FakeNewsClassifier', target="_blank"),
	
	
	html.Div([dcc.Textarea(
        id='title',
        value='',
        style={'width': '100%', 'height': 20},
        placeholder = 'Enter URL of Article',
    )], style={'marginTop': 25}),
    
    html.Div([html.Button('Submit', id='button', n_clicks=0)]),
    html.Div(id='output', style={'whiteSpace': 'pre-line'})
], style={'marginBottom': 25, 'marginTop': 25, 'marginLeft':25, 'marginRight':400})

@app.callback(
    Output('output', 'children'),
    [Input('button', 'n_clicks')],
    [State('title', 'value')],
    
    
)
def update_output(n_clicks, value):
    

    if n_clicks > 0:
        k = predict.predict(value)
        return k[0] + "\n" + "This article is " + k[1] + " and " + k[2] + ".\nSummary:\n" + k[3] 

if __name__ == '__main__':
    app.run_server(debug=True)

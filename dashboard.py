import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
app = dash.Dash("Covid Dashboard")
server = app.server
app.title  = "COVID Dashboard"
df = pd.read_excel("jaisalmer.xlsx")
df = df.drop(['S.No.','Name of positive','Contact No.','SampleID/\nCOVID ID'],axis = 1)
df['Age'] = df['Age'].str.replace('Years', '')
df['Age'] = df['Age'].str.replace('Days','').astype(int)
df['Sample Collection Date'] = pd.to_datetime(df['Sample Collection Date'])
df['Date of Positive'] = pd.to_datetime(df['Date of Positive'])
df['Time for result'] = df['Date of Positive'] - df['Sample Collection Date']
# for covid cases according to gender
fig_1 = px.histogram(df, x='Age',color = 'Sex')
fig_1.update_layout(
    title_text='COVID Patients Distribution : Age and Sex', # title of plot
    xaxis_title_text='Age', # xaxis label
    yaxis_title_text='Count', # yaxis label
    bargap=0.3, # gap between bars of adjacent location coordinates
    bargroupgap=0.2 # gap between bars of the same location coordinates
)
# Contact Type
pie_2 = df['Contact Type'].value_counts()
pie_2 = pd.DataFrame(pie_2)
pie_2.reset_index(inplace=True)
pie_2.loc[pie_2['Contact Type'] < 10, 'index'] = 'Other contact'
fig_2 = px.pie(pie_2, names = 'index' , values = 'Contact Type', title = 'Contact Type')
fig_2.update_layout(
    title="Contact Type",
    xaxis_title="",
    yaxis_title="",
    legend_title="",
    font=dict(
        family="Courier New, monospace",
        size=15,
        color="RebeccaPurple"))

# home isolation or hospitalised
fig_3 = px.pie(df, names = 'Status')
fig_3.update_layout(
    title="Status of Isolation",
    xaxis_title="Place",
    yaxis_title="Number of cases",
    legend_title="",
    font=dict(
        family="Courier New, monospace",
        size=15,
        color="RebeccaPurple"))

# Covid cases according to location
pie_3 = df.Address.value_counts()
pie_3 = pd.DataFrame(pie_3)
pie_3.reset_index(inplace=True)
pie_3 = pie_3[pie_3.Address > 10]
fig_4 = px.bar(pie_3, x='index', y='Address', title = 'Regions with more than 10 covid cases on the day')
fig_4.update_layout(
    title="Regions with more than 10 COVID cases",
    xaxis_title="Place",
    yaxis_title="Number of cases",
    legend_title="",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="RebeccaPurple"))
# Name of hospital Admission
pie_chart = df['Name of  Hospital Admission'].value_counts()
pie_chart = pd.DataFrame(pie_chart)
pie_chart.reset_index(inplace=True)
pie_chart.loc[pie_chart['Name of  Hospital Admission'] < 10, 'index'] = 'Other contact'
fig_5 = px.pie(pie_chart, names = 'index' , values = 'Name of  Hospital Admission',title = 'Name of Hospital Admission')
app.layout = html.Div(style = {
  'backgroundColor': '#F6F3F2'
}, children = [
    html.H1(
    children = 'Hello Jaisalmer',
    style = {
      'textAlign': 'center',
      'color': '#000000'
    }
  ),

    html.Div(children = 'One stop destination for all COVID relation information.', style = {
    'textAlign': 'center',
    'color': '#F0360F'
  }),
    html.Div(children=['The number of covid cases reported on the 8th May are ',len(df)], style={
        'textAlign': 'center',
        'color': '#F0360F'
    }),

    dcc.Graph(
    id = 'example-graph-1',
    figure = fig_1
  ),
    dcc.Graph(
        id='example-graph-2',
        figure=fig_2
    ),
    dcc.Graph(
        id='example-graph-3',
        figure=fig_3
    ),
    dcc.Graph(
        id='example-graph-4',
        figure=fig_4
    ),
    dcc.Graph(
        id='example-graph-5',
        figure=fig_5
    ),
html.Div(children = 'Built by Vineet Tripathi', style = {
    'textAlign': 'center',
    'color': '#F0360F'
  })
])
if __name__ == '__main__':
  app.run_server(debug = True)



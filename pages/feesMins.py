
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

from utils import Header, make_dash_table
import pandas as pd
import pathlib

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()

df_expenses = pd.read_csv(DATA_PATH.joinpath("df_expenses.csv"))
df_minimums = pd.read_csv(DATA_PATH.joinpath("df_minimums.csv"))


def create_layout(app):
    return html.Div(
        [
            Header(app),
            # page 4
            html.Div(
                [
                    # Row 1
                    html.Div(
                        [
                            html.Div(
                                [html.H6(["Gastos"], className="subtitle padded")],
                                className="twelve columns",
                            )
                        ],
                        className="row ",
                    ),
                    # Row 2
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.Strong(),
                                    html.Table(make_dash_table(df_expenses)),
                                    html.H6(["Minimos"], className="subtitle padded"),
                                    html.Table(make_dash_table(df_minimums)),
                                ],
                                className="six columns",
                            ),
                            html.Div(
                                [
                                    html.Br([]),
                                    html.Strong(
                                        "Tarifas de $10,000 invertidos en 10 años",
                                        style={"color": "#3a3a3a"},
                                    ),
                                    dcc.Graph(
                                        id="graph-6",
                                        figure={
                                            "data": [
                                                go.Bar(
                                                    x=["Category Average", "This fund"],
                                                    y=["2242", "329"],
                                                    marker={"color": "#97151c"},
                                                    name="A",
                                                ),
                                                go.Bar(
                                                    x=["This fund"],
                                                    y=["1913"],
                                                    marker={"color": " #dddddd"},
                                                    name="B",
                                                ),
                                            ],
                                            "layout": go.Layout(
                                                annotations=[
                                                    {
                                                        "x": -0.0111111111111,
                                                        "y": 2381.92771084,
                                                        "font": {
                                                            "color": "#7a7a7a",
                                                            "family": "Arial sans serif",
                                                            "size": 8,
                                                        },
                                                        "showarrow": False,
                                                        "text": "$2,242",
                                                        "xref": "x",
                                                        "yref": "y",
                                                    },
                                                    {
                                                        "x": 0.995555555556,
                                                        "y": 509.638554217,
                                                        "font": {
                                                            "color": "#7a7a7a",
                                                            "family": "Arial sans serif",
                                                            "size": 8,
                                                        },
                                                        "showarrow": False,
                                                        "text": "$329",
                                                        "xref": "x",
                                                        "yref": "y",
                                                    },
                                                    {
                                                        "x": 0.995551020408,
                                                        "y": 1730.32432432,
                                                        "font": {
                                                            "color": "#7a7a7a",
                                                            "family": "Arial sans serif",
                                                            "size": 8,
                                                        },
                                                        "showarrow": False,
                                                        "text": "You save<br><b>$1,913</b>",
                                                        "xref": "x",
                                                        "yref": "y",
                                                    },
                                                ],
                                                autosize=False,
                                                height=260,
                                                width=320,
                                                bargap=0.4,
                                                barmode="stack",
                                                hovermode="closest",
                                                margin={
                                                    "r": 40,
                                                    "t": 20,
                                                    "b": 20,
                                                    "l": 40,
                                                },
                                                showlegend=False,
                                                title="",
                                                xaxis={
                                                    "autorange": True,
                                                    "range": [-0.5, 1.5],
                                                    "showline": True,
                                                    "tickfont": {
                                                        "family": "Arial sans serif",
                                                        "size": 8,
                                                    },
                                                    "title": "",
                                                    "type": "category",
                                                    "zeroline": False,
                                                },
                                                yaxis={
                                                    "autorange": False,
                                                    "mirror": False,
                                                    "nticks": 3,
                                                    "range": [0, 3000],
                                                    "showgrid": True,
                                                    "showline": True,
                                                    "tickfont": {
                                                        "family": "Arial sans serif",
                                                        "size": 10,
                                                    },
                                                    "tickprefix": "$",
                                                    "title": "",
                                                    "type": "linear",
                                                    "zeroline": False,
                                                },
                                            ),
                                        },
                                        config={"displayModeBar": False},
                                    ),
                                ],
                                className="six columns",
                            ),
                        ],
                        className="row ",
                    ),
                    # Row 3
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(["Tarifas"], className="subtitle"),
                                    html.Br([]),
                                    html.Div(
                                        [
                                            html.Div(
                                                [
                                                    html.Div(
                                                        [
                                                            html.Strong(
                                                                ["Purchase fee"],
                                                                style={
                                                                    "color": "#515151"
                                                                },
                                                            )
                                                        ],
                                                        className="three columns right-aligned",
                                                    ),
                                                    html.Div(
                                                        [
                                                            html.P(
                                                                ["None"],
                                                                style={
                                                                    "color": "#7a7a7a"
                                                                },
                                                            )
                                                        ],
                                                        className="nine columns",
                                                    ),
                                                ],
                                                className="row",
                                                style={
                                                    "background-color": "#f9f9f9",
                                                    "padding-top": "20px",
                                                },
                                            ),
                                            html.Div(
                                                [
                                                    html.Div(
                                                        [
                                                            html.Strong(
                                                                ["Redemption fee"],
                                                                style={
                                                                    "color": "#515151"
                                                                },
                                                            )
                                                        ],
                                                        className="three columns right-aligned",
                                                    ),
                                                    html.Div(
                                                        [
                                                            html.P(
                                                                ["None"],
                                                                style={
                                                                    "color": "#7a7a7a"
                                                                },
                                                            )
                                                        ],
                                                        className="nine columns",
                                                    ),
                                                ],
                                                className="row",
                                                style={"background-color": "#f9f9f9"},
                                            ),
                                            html.Div(
                                                [
                                                    html.Div(
                                                        [
                                                            html.Strong(
                                                                ["12b-1 fee"],
                                                                style={
                                                                    "color": "#515151"
                                                                },
                                                            )
                                                        ],
                                                        className="three columns right-aligned",
                                                    ),
                                                    html.Div(
                                                        [
                                                            html.P(
                                                                ["None"],
                                                                style={
                                                                    "color": "#7a7a7a"
                                                                },
                                                            )
                                                        ],
                                                        className="nine columns",
                                                    ),
                                                ],
                                                className="row",
                                                style={"background-color": "#f9f9f9"},
                                            ),
                                        ],
                                        className="fees",
                                    ),
                                    html.Div(
                                        [
                                            html.Div(
                                                [
                                                    html.Strong(
                                                        ["Account service fee"],
                                                        style={"color": "#515151"},
                                                    )
                                                ],
                                                className="three columns right-aligned",
                                            ),
                                            html.Div(
                                                [
                                                    html.Strong(
                                                        [
                                                            "Cuentas de compras"
                                                        ],
                                                        style={"color": "#515151"},
                                                    ),
                                                    html.P(
                                                        [
                                                            "Costos"
                                                        ],
                                                        style={"color": "#7a7a7a"},
                                                    ),
                                                    html.Br([]),
                                                    html.Strong(
                                                        ["SIMPLE IRAs"],
                                                        style={"color": "#515151"},
                                                    ),
                                                    html.P(
                                                        [
                                                            "Gastos de Compras"
                                                        ],
                                                        style={"color": "#7a7a7a"},
                                                    ),
                                                    html.Br([]),
                                                    html.Strong(
                                                        ["403(b)(7) plans"],
                                                        style={"color": "#515151"},
                                                    ),
                                                    html.P(
                                                        [
                                                    "Cobros"
                                                        ],
                                                        style={"color": "#7a7a7a"},
                                                    ),
                                                    html.Br([]),
                                                    html.Strong(
                                                        ["Individual 401(k) plans"],
                                                        style={"color": "#515151"},
                                                    ),
                                                    html.P(
                                                        [
                                                        " Gastos Cuadernos"
                                                        ],
                                                        style={"color": "#7a7a7a"},
                                                    ),
                                                    html.Br([]),
                                                ],
                                                className="nine columns",
                                            ),
                                        ],
                                        className="row",
                                        style={
                                            "background-color": "#f9f9f9",
                                            "padding-bottom": "30px",
                                        },
                                    ),
                                ],
                                className="twelve columns",
                            )
                        ],
                        className="row",
                    ),
                ],
                className="sub_page",
            ),
        ],
        className="page",
    )
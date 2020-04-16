
import dash_core_components as dcc
import dash_html_components as html

from controls import WELL_STATUSES, WELL_TYPES

def layout_app(app, well_status_options, well_type_options):

    # Create app layout
    the_layout = html.Div(
        [
            dcc.Store(id='aggregate_data'),
            html.Div(
                [
                    html.Div(
                        [
                            html.H2(
                                'New York Oil and Gas',

                            ),
                            html.H4(
                                'Production Overview',
                            )
                        ],

                        className='eight columns'
                    ),
                    html.Img(
                        src="https://s3-us-west-1.amazonaws.com/plotly-tutorials/logo/new-branding/dash-logo-by-plotly-stripe.png",
                        className='two columns',
                    ),
                    html.A(
                        html.Button(
                            "Learn More",
                            id="learnMore"

                        ),
                        href="https://plot.ly/dash/pricing/",
                        className="two columns"
                    )
                ],
                id="header",
                className='row',
            ),
            html.Div(
                [
                    html.Div(
                        [
                            html.P(
                                'Filter by construction date (or select range in histogram):',
                                className="control_label"
                            ),
                            dcc.RangeSlider(
                                id='year_slider',
                                min=1960,
                                max=2017,
                                value=[1990, 2010],
                                className="dcc_control"
                            ),
                            html.P(
                                'Filter by well status:',
                                className="control_label"
                            ),
                            dcc.RadioItems(
                                id='well_status_selector',
                                options=[
                                    {'label': 'All ', 'value': 'all'},
                                    {'label': 'Active only ', 'value': 'active'},
                                    {'label': 'Customize ', 'value': 'custom'}
                                ],
                                value='active',
                                labelStyle={'display': 'inline-block'},
                                className="dcc_control"
                            ),
                            dcc.Dropdown(
                                id='well_statuses',
                                options=well_status_options,
                                multi=True,
                                value=list(WELL_STATUSES.keys()),
                                className="dcc_control"
                            ),
                            dcc.Checklist(
                                id='lock_selector',
                                options=[
                                    {'label': 'Lock camera', 'value': 'locked'}
                                ],
                                values=[],
                                className="dcc_control"
                            ),
                            html.P(
                                'Filter by well type:',
                                className="control_label"
                            ),
                            dcc.RadioItems(
                                id='well_type_selector',
                                options=[
                                    {'label': 'All ', 'value': 'all'},
                                    {'label': 'Productive only ',
                                        'value': 'productive'},
                                    {'label': 'Customize ', 'value': 'custom'}
                                ],
                                value='productive',
                                labelStyle={'display': 'inline-block'},
                                className="dcc_control"
                            ),
                            dcc.Dropdown(
                                id='well_types',
                                options=well_type_options,
                                multi=True,
                                value=list(WELL_TYPES.keys()),
                                className="dcc_control"
                            ),
                        ],
                        className="pretty_container four columns"
                    ),
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.Div(
                                        [
                                            html.P("No. of Wells"),
                                            html.H6(
                                                id="well_text",
                                                className="info_text"
                                            )
                                        ],
                                        id="wells",
                                        className="pretty_container"
                                    ),

                                    html.Div(
                                        [
                                            html.Div(
                                                [
                                                    html.P("Gas"),
                                                    html.H6(
                                                        id="gasText",
                                                        className="info_text"
                                                    )
                                                ],
                                                id="gas",
                                                className="pretty_container"
                                            ),
                                            html.Div(
                                                [
                                                    html.P("Oil"),
                                                    html.H6(
                                                        id="oilText",
                                                        className="info_text"
                                                    )
                                                ],
                                                id="oil",
                                                className="pretty_container"
                                            ),
                                            html.Div(
                                                [
                                                    html.P("Water"),
                                                    html.H6(
                                                        id="waterText",
                                                        className="info_text"
                                                    )
                                                ],
                                                id="water",
                                                className="pretty_container"
                                            ),
                                        ],
                                        id="tripleContainer",
                                    )

                                ],
                                id="infoContainer",
                                className="row"
                            ),
                            html.Div(
                                [
                                    dcc.Graph(
                                        id='count_graph',
                                    )
                                ],
                                id="countGraphContainer",
                                className="pretty_container"
                            )
                        ],
                        id="rightCol",
                        className="eight columns"
                    )
                ],
                className="row"
            ),
            html.Div(
                [
                    html.Div(
                        [
                            dcc.Graph(id='main_graph')
                        ],
                        className='pretty_container eight columns',
                    ),
                    html.Div(
                        [
                            dcc.Graph(id='individual_graph')
                        ],
                        className='pretty_container four columns',
                    ),
                ],
                className='row'
            ),
            html.Div(
                [
                    html.Div(
                        [
                            dcc.Graph(id='pie_graph')
                        ],
                        className='pretty_container seven columns',
                    ),
                    html.Div(
                        [
                            dcc.Graph(id='aggregate_graph')
                        ],
                        className='pretty_container five columns',
                    ),
                ],
                className='row'
            ),
        ],
        id="mainContainer",
        style={
            "display": "flex",
            "flex-direction": "column"
        }
    )
    return the_layout

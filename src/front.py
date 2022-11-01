
from typing import Any, Optional
from dash import html, dcc, Dash
from dash.dependencies import Input, Output

import src.styles as s
from src.stream import StreamAdapter


class AppFront:

    def __init__(self) -> None:
        self.figure: dict = {}
        self.app = Dash(__name__)

        self.app.layout = html.Div(
            id='main_div',
            className='Row',
            children=[
                html.Br(),
                html.H1(s.TITLE, className='headerClass'),
                html.Div(id='plotter', className='plotterClass'),
                dcc.Interval(id='timer_update_bar',
                             interval=s.TIMER_UPDATE_BAR_MS),
                dcc.Interval(id='timer_update_message',
                             interval=s.TIMER_SHOW_MESSAGE_MS),
                html.Table(className='tableCLass', children=[
                    html.Tr([
                        html.Td([
                            dcc.Slider(s.SLIDER_RESOLUTION_MIN_VALUE,
                                       s.SLIDER_RESOLUTION_MAX_VALUE,
                                       s.SLIDER_RESOLUTION_STEP,
                                       value=s.SLIDER_RESOLUTION_CURRENT_VALUE,
                                       id='slider_resolution'),
                            html.Div(id='slider_resolution_container')]),
                        html.Td([
                            dcc.Slider(s.SLIDER_SENSITIVITY_MIN_VALUE,
                                       s.SLIDER_SENSITIVITY_MAX_VALUE,
                                       s.SLIDER_SENSITIVITY_STEP,
                                       value=s.SLIDER_SENSITIVITY_CURRENT_VALUE,
                                       id='slider_level'),
                            html.Div(id='slider_level_container')]),
                    ])
                ]),
                html.Label(id='message_label', className='messageClass'),
            ])

        app_callback = self.app.callback(
            Output('plotter', 'children'),
            [Input('timer_update_bar', 'n_intervals')],
        )
        self.update_bar = app_callback(self.update_bar)  # type: ignore

        app_callback_slider_res = self.app.callback(
            Output('slider_resolution_container', 'children'),
            Input('slider_resolution', 'value'))

        self.update_resolution = app_callback_slider_res(  # type: ignore
            self.update_resolution
        )

        app_callback_slider_level = self.app.callback(
            Output('slider_level_container', 'children'),
            Input('slider_level', 'value'))

        self.update_level = app_callback_slider_level(  # type: ignore
            self.update_level
        )

        app_callback_msg = self.app.callback(
            Output('message_label', 'children'),
            [
                Input('slider_resolution', 'value'),
                Input('slider_level', 'value'),
                Input('timer_update_message', 'n_intervals')
            ])
        self.update_message_label = app_callback_msg(  # type: ignore
            self.update_message_label
        )

    @staticmethod
    def update_resolution(value: int) -> None:
        StreamAdapter.DECIMATION = 2 ** value
        return None

    @staticmethod
    def update_level(value: int) -> None:
        StreamAdapter.LEVEL = value / 10
        return None

    def update_message_label(self, slider_resolution: int,
                             slider_level: int, *args: Any) -> str:
        if slider_level != getattr(self, 'prev_level', 1):
            setattr(self, 'prev_level', slider_level)
            return f"Sensitivity: {slider_level}"

        if slider_resolution != getattr(self, 'prev_res', 1):
            setattr(self, 'prev_res', slider_resolution)
            return f"Decimation: x{2**slider_resolution}"

        if not StreamAdapter.IS_ALIVE:
            return s.LABEL_EXCEPTION_TEXT

        return ""

    def update_bar(self, n: Any) -> Optional[dcc.Graph]:
        if StreamAdapter.IS_ALIVE:
            x_res, x_data, y_data = StreamAdapter.get_data_ready_to_plot()
            self.figure['data'] = [
                {'dx': x_res, 'x': x_data, 'y': y_data} | s.BAR_DATA_PARAMS
            ]
            self.figure['layout'] = s.DASH_FIGURE_BAR_LAYOUT
            return dcc.Graph(id='bar_plot', figure=self.figure,
                             className='bargraphClass')
        return None

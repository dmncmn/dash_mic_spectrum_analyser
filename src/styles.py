
TITLE: str = "Dash Microphone Spectrum Analyser"

WINDOW_WIDTH: int = 640
WINDOW_HEIGHT: int = 480

TIMER_SHOW_MESSAGE_MS: int = 5000
TIMER_UPDATE_BAR_MS: int = 50
TIMER_LISTEN_MIC_MS: int = 25

SLIDER_RESOLUTION_TEXT_TOOLTIP: str = "Decimation"
SLIDER_RESOLUTION_LABEL_TEXT: str = "Decimation"
SLIDER_RESOLUTION_STEP: int = 1
SLIDER_RESOLUTION_MIN_VALUE: int = 0
SLIDER_RESOLUTION_MAX_VALUE: int = 6
SLIDER_RESOLUTION_CURRENT_VALUE: int = 0

SLIDER_SENSITIVITY_TEXT_TOOLTIP: str = "Sensitivity"
SLIDER_SENSITIVITY_LABEL_TEXT: str = "Sensitivity"
SLIDER_SENSITIVITY_STEP: int = 1
SLIDER_SENSITIVITY_MIN_VALUE: int = 1
SLIDER_SENSITIVITY_MAX_VALUE: int = 100
SLIDER_SENSITIVITY_CURRENT_VALUE: int = 1

CLOSE_BUTTON_TEXT_TOOLTIP: str = "Quit"

PLOT_X_MIN_VALUE: int = 0
PLOT_X_MAX_VALUE: int = 22050
PLOT_Y_MIN_VALUE: int = 0
PLOT_Y_MAX_VALUE: int = 100
PLOT_LEFT_LABEL: str = "Amplitude"
PLOT_BOTTOM_LABEL: str = "Frequency, Hz"
PLOT_BAR_WIDTH: float = 0.8
PLOT_BAR_COLOR: str = 'blue'
PLOT_BAR_COLOR_OVERLOAD: str = 'red'
PLOT_THRESHOLD_OVERLOAD: int = 1000
PLOT_HIDE_AXIS_X: bool = True
PLOT_HIDE_AXIS_Y: bool = True
PLOT_SHOW_GRID_X: bool = True
PLOT_SHOW_GRID_Y: bool = True

LABEL_INIT_TEXT: str = TITLE
LABEL_FULLSCREEN_TEXT: str = "Fullscreen"
LABEL_OVERLOAD_TEXT: str = "Overload"
LABEL_EXCEPTION_TEXT: str = "Microphone is disconnected"
LABEL_OPACITY_TEXT: str = "Opacity"

DEFAULT_OPACITY: int = 10
OPACITY_MIN_VALUE: int = 2
OPACITY_MAX_VALUE: int = 10
OPACITY_STEP_VALUE: int = 1
OPACITY_DIV_FACTOR: int = 10

DASH_FIGURE_BAR_LAYOUT = {
    'xaxis': {
        'autorange': False,
        'range': [PLOT_X_MIN_VALUE, PLOT_X_MAX_VALUE],
        'showgrid': not PLOT_SHOW_GRID_X,
        'showticklabels': not PLOT_HIDE_AXIS_X,
    },
    'yaxis': {
        'autorange': False,
        'range': [PLOT_Y_MIN_VALUE, PLOT_Y_MAX_VALUE],
        'showgrid': not PLOT_SHOW_GRID_Y,
        'showticklabels': not PLOT_HIDE_AXIS_Y,
    },
    'paper_bgcolor': 'black',
    'plot_bgcolor': 'black',
}

BAR_DATA_PARAMS = {
    'offset': 1,
    'type': 'bar',
}

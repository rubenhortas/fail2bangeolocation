from presentation.color import Color
from crosscutting import strings


class Tag:
    debug = '>>'
    error = f'[{Color.bold_red}{strings.ERROR}{Color.end}]'
    exception = f'[{Color.bold_red}{strings.EXCEPTION}{Color.end}]'
    info = f'[{Color.green}*{Color.end}]'
    warning = f'[{Color.bold_orange}{strings.WARNING}{Color.end}]'

from presentation.color import Color


class Tag:
    debug = ">>"
    error = "[{0}ERROR{1}]".format(Color.bold_red, Color.end)
    exception = "[{0}EXCEPTION{1}]".format(Color.bold_red, Color.end)
    info = "[{0}*{1}]".format(Color.green, Color.end)
    warning = "[{0}Warning{1}]".format(Color.bold_orange, Color.end)

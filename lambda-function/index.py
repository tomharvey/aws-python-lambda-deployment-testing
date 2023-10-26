from datetime import date
from pyxirr import xirr


def handler(event, context):

    dates = [date(2020, 1, 1), date(2021, 1, 1), date(2022, 1, 1)]
    amounts = [-1000, 750, 500]

    return xirr(dates, amounts)


from django import template
from datetime import datetime, date, timedelta
#from .models import NotaCalendario

register = template.Library()

def get_last_day_of_month(year, month):
    if (month == 12):
        year += 1
        month = 1
    else:
        month += 1
    return date(year, month, 1) - timedelta(1)


def cal_mes(year=date.today().year, month=date.today().month):
    event_list = NotaCalendario.objects.filter(dateField__year=year, dateField__month=month)
    first_day_of_month = date(year, month, 1)
    last_day_of_month = get_last_day_of_month(year, month)
    first_day_of_calendar = first_day_of_month - timedelta(first_day_of_month.weekday())
    last_day_of_calendar = last_day_of_month + timedelta(7 - last_day_of_month.weekday())

    cal_mes = []
    week = []
    week_headers = []

    i = 0
    day = first_day_of_calendar
    while day <= last_day_of_calendar:
        if i < 7:
            week_headers.append(day)
        cal_day = {}
        cal_day['day'] = day
        cal_day['event'] = False
        for event in event_list:
            if day >= event.fecha.date() and day <= event.fecha.date():
                cal_day['event'] = True
        if day.month == month:
            cal_day['in_month'] = True
        else:
            cal_day['in_month'] = False
        week.append(cal_day)
        if day.weekday() == 6:
            cal_mes.append(week)
            week = []
        i += 1
        day += timedelta(1)

    return {'calendar': cal_mes, 'headers': week_headers}

register.inclusion_tag('tags/cal_mes.html')(cal_mes)
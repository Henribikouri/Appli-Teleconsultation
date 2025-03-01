
from django import template
import pytz

register = template.Library()

CET = pytz.timezone('CET')

@register.filter
def cet(datetime):
    if datetime:
        return datetime.astimezone(CET).strftime('%Y-%m-%d %H:%M:%S %Z')
    return ''

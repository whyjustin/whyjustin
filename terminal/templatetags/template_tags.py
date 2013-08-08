from time import strptime, strftime
from django import template
from django.utils.safestring import mark_safe
from django.template.defaultfilters import stringfilter
from django.utils.text import normalize_newlines

register = template.Library()

def format_for_js(text):
    """
    Removes all newline characters from a block of text.
    """
    # First normalize the newlines using Django's nifty utility
    normalized_text = normalize_newlines(text)
    # Then simply remove the newlines like so.
    return mark_safe(normalized_text.replace('\n', ' ').replace("'", "\\'"))
format_for_js = stringfilter(format_for_js)
register.filter(format_for_js, is_safe=True)

def format_date(text):
	datetime = strptime(text, '%Y-%m-%d %H:%M:%S')
	return strftime('%Y-%m-%dT%H:%M:%S', datetime)

format_date = stringfilter(format_date)
register.filter(format_date, is_safe=True)
from django import template
from hurry.filesize import size



register = template.Library()

@register.filter
def converter(value):
	return size(value)
from django import template

register = template.Library()


@register.filter(name='percentage')
def calculate_percentage(value, arg):
    return 0 if arg == 0 else int(100 * float(value) / float(arg))

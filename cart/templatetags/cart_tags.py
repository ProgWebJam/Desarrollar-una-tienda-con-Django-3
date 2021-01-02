from django import template

register = template.Library()

# Filtro para multiplicar
@register.filter()
def multiply(value, arg):
    return float(value) * arg

# Filtro para colocar valor monetario(simbolo de euro)
@register.filter()
def money_format(value, arg):
    return f"{value}{arg}"
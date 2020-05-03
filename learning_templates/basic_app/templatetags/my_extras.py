from django import template

register = template.Library()
@reister.filter(name='cut')
def cut(value,arg):
    """
    this cuts out all values of "arg" from the string!
    """
    return value.replace(arg,'')


# register.filter('cut',cut)

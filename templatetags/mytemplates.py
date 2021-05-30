from django import template
register = template.Library()
# This is a Custom Template  tags Library...
# This to Make Custom Template Tags
# which Will Attributes to the Html Elemnets


@register.filter(name='add_attr')
def add_attr(field, css):
    attrs = {}
    definition = css.split(',')
    for d in definition:
        if '=' not in d:
            attrs['class'] = d
        else:
            key, val = d.split('=')
            attrs[key] = val
    return field.as_widget(attrs=attrs)

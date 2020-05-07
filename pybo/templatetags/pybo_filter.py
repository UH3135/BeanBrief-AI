import markdown
from django import template
from django.utils.safestring import mark_safe


register = template.Library()


@register.filter
def sub(value, arg):
    return value - arg


@register.filter
def mark(value):
    """입력 값을 HTML 문자열로 변환하는 함수"""
    extentions = ["nl2br", "fenced_code"]
    return mark_safe(markdown.markdown(value, extensions=extentions))

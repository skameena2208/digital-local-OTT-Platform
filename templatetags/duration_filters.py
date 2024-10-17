from django import template

register = template.Library()


@register.filter
def duration_to_time(duration):
    if duration:
        total_seconds = int(duration.total_seconds())
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{hours:02}:{minutes:02}:{seconds:02}"
    return "00:00:00"

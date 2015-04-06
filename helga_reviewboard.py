from helga import settings
from helga.plugins import match

REVIEWBOARD_MATCH = r'\bcr(\d+)\b'

@match(REVIEWBOARD_MATCH)
def reviewboard(client, channel, nick, message, matches):
    """
    Automatically responds to reviewboard urls if a user mentions a pattern
    like cr####. Requires REVIEWBOARD_URL to exist in settings with formattable
    substring '{review}'
    """
    url_fmt = getattr(settings, 'REVIEWBOARD_URL', 'http://localhost/{review}')
    reviews = [url_fmt.format(review=cr) for cr in matches]
    return '{0} might be talking about codereview: {1}'.format(nick, ', '.join(reviews))

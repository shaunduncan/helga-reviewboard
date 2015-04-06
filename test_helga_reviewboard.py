from mock import patch
import re

import helga_reviewboard as reviewboard


@patch('helga_reviewboard.settings')
def test_reviewboard(settings):
    settings.REVIEWBOARD_URL = 'http://example.com/{review}'
    expected = 'me might be talking about codereview: http://example.com/1234'
    assert reviewboard.reviewboard(None, '#bots', 'me', 'cr1234', ['1234']) == expected


@patch('helga_reviewboard.settings')
def test_reviewboard_handles_many(settings):
    settings.REVIEWBOARD_URL = 'http://example.com/{review}'
    expected = 'me might be talking about codereview: http://example.com/123, http://example.com/456'
    assert reviewboard.reviewboard(None, '#bots', 'me', 'cr123 cr456', ['123', '456']) == expected


def test_reviewboard_regex():
    pattern = re.compile(reviewboard.REVIEWBOARD_MATCH)
    test_map = {'cr1':True, 'asd cr1':True, 'asd cr1 asd':True,
                'cr1a':False, 'asdcr1':False, 'asdcr1asd':False}
    for string, result in test_map.iteritems():
        assert (re.search(pattern, string) is not None) == result

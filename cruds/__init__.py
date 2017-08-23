from flask import abort
import settings
import validators


def get_paginated_list(results, url, start, page_size=settings.PAGINATION_SIZE):
    # check if page exists
    count = len(results)
    # make response
    obj = {}
    obj['start'] = start
    obj['page_size'] = page_size
    obj['count'] = count
    # make URLs
    # make previous url
    if start == 1:
        obj['previous'] = ''
    else:
        start_copy = max(1, start - page_size)
        page_size_copy = start - 1
        obj['previous'] = url + '?start=%d' % (start_copy)
    # make next url
    if start + page_size > count:
        obj['next'] = ''
    else:
        start_copy = start + page_size
        obj['next'] = url + '?start=%d' % (start_copy)
    # finally extract result according to bounds
    obj['results'] = results[(start - 1):(start - 1 + page_size)]
    return obj


def format_urls_in_text(text):
    new_text = []

    for word in str(text).split():
        new_word = word
        new_word.replace('http://', '')
        new_word = 'http://{0}'.format(new_word)

        if validators.url(new_word)==True:
            new_word = '<a href="{0}">{1}</a>'.format(new_word, word)
        else:
            new_word = word

        new_text.append(new_word)
    return ' '.join(new_text)

#!/usr/bin/python
# encoding: utf-8

import sys
from workflow import Workflow3, web


def main(wf):
    list_articles(wf)


def get_articles():
    """docstring for get_articles"""
    return web.get('https://dev.to/api/articles?top=1&per_page=10').json()


def list_articles(wf):
    """docstring for list_articles"""
    data = wf.cached_data('dev.to', get_articles, max_age=600)
    for datum in data:
        wf.add_item(
            title=datum['title'],
            arg=datum['url'],
            valid=True)
    wf.send_feedback()


def update_settings():
    return {
        'github_slug': 'mijailr/alfred-devto'
    }


if __name__ == "__main__":
    wf = Workflow3(update_settings=update_settings())

    if wf.update_available:
        wf.start_update()

    sys.exit(wf.run(main))

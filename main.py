# -*- coding: utf-8 -*-
import json

import benedict
import wikitextparser as wtp

TEMPLATE_NAMES = ['l1', 'lx', 'l2', 'l']


def extract_data(filename):
    # parse the xml
    pages = benedict.benedict(filename, format='xml')['mediawiki']['page']

    # filter out unnecessary pages
    pages = list(filter(lambda x: 'Category:' not in x['title'], pages))
    pages = list(
        filter(lambda x: 'text' in x['revision'] and "==Links to other series==" in x['revision']['text']['#text'],
               pages))

    # transform - we only need the title and page text (categories will be parsed later)
    pages = [dict({'title': i['title'], 'text': i['revision']['text']['#text']}) for i in pages]

    output = []

    for serie in pages:
        parsed = wtp.parse(serie['text'])
        # dig for our data
        _wanted_section = list(filter(lambda x: x.title == 'Links to other series', parsed.sections))
        if len(_wanted_section) != 1:
            continue
        wanted_section = _wanted_section[0]
        _templates = list(filter(lambda x: x.name in TEMPLATE_NAMES, wanted_section.templates))
        _links = list(filter(lambda x: x.arguments[2].value in ['1', '1a', '1b', '2'], _templates))
        toadd = {
            'title': serie['title'],
            'categories': [i.title.replace('Category:', '') for i in
                           list(filter(lambda x: x.title.startswith('Category:'), parsed.wikilinks))],
            'links': [{
                'with': i.arguments[0].value,
                'how': i.arguments[7].value
            } for i in _links]
        }

        output.append(toadd)

    return output


if __name__ == '__main__':
    out = extract_data('CrossoverWiki.xml')
    print(json.dumps(out))

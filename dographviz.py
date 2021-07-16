import json

from main import extract_data
import graphviz

already_pulled = []
already_done_combos = []

def getsafe(txt):
    return ''.join([i if ord(i) < 128 else ' ' for i in txt])

if __name__ == '__main__':
    print("parsing...")
    out = extract_data('CrossoverWiki.xml')
    print("parsed")
    dot = graphviz.Digraph(comment='Fortnite multiverse')

    def dopulls(title):
        if title in already_pulled:
            return
        print(f"pulling {title}")
        already_pulled.append(title)
        _wants = list(filter(lambda x: x['title'] == title, out))
        if len(_wants) != 1:
            # some titles don't have a dedicated page and thus no child relationships, so we don't pull any more via them
            return
        want = _wants[0]
        for link in want['links']:
            slug = '_X_'.join(sorted([link['with'], want['title']]))
            if slug in already_done_combos:
                continue
            already_done_combos.append(slug)
            dot.edge(getsafe(link['with']), getsafe(want['title']))
            dopulls(link['with'])

    dopulls('Fortnite')
    with open("Output.txt", "w") as text_file:
        text_file.write(dot.source)

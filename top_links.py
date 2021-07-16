from main import extract_data

if __name__ == '__main__':
    top = {}
    out = extract_data('CrossoverWiki.xml')
    for name in out:
        for link in name['links']:
            w = link['with']
            top[w] = top[w] + 1 if w in top else 1
    top = dict(reversed(sorted(top.items(), key=lambda item: item[1])))
    print(top)

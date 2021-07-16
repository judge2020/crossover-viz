
## crossover-viz

Parses the [Crossover Wiki](https://fictionalcrossover.fandom.com/) to generate cool visualizations. This is mostly a weekend toy project and will likely not ever be fully-featured.

To use:


1. go to https://fictionalcrossover.fandom.com/wiki/Special:Export

2. In the 'add pages from category' box, enter `Series` and click 'add'

3. download them (without revision history), rename the file to `CrossoverWiki.xml`, and place in this folder

4. Either install the requirements listed in [Pipfile](Pipfile) or run `pipenv install` to use pipenv

5. run `python main.py` (python 3)


Current issues:

- without constraints, graphs are generated nearly instantly, however these provide no use (all edges overlap each other)
- with constraints, the dot program takes an extremely long time to generate the svg

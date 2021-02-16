#!/usr/bin/env python3

import networkx as nx
from re import sub
from xml.dom import minidom
from zipfile import ZipFile

def load_xml(deck, path):
  xml = deck.read(path)
  return minidom.parseString(xml)


def get_slide_count(deck):
  presentation = load_xml(deck, 'ppt/presentation.xml')
  slides = presentation.getElementsByTagName('p:sldId')
  return slides.length


def get_solution_path(deck, start_slide, end_slide):
  xref = {}
  graph = nx.DiGraph()
  is_slide = lambda rel: rel.attributes['Type'].value.endswith('slide')

  for i in range(1, get_slide_count(deck) + 1):
    relationships = load_xml(deck, f'ppt/slides/_rels/slide{i}.xml.rels')
    relationships = relationships.getElementsByTagName('Relationship')
    slide_references = {}

    for relationship in filter(is_slide, relationships):
      j = int(sub('\D', '', relationship.attributes['Target'].value))
      slide_references[j] = relationship.attributes['Id'].value
      graph.add_edge(i, j)

    xref[i] = slide_references

  path = nx.shortest_path(graph, start_slide, end_slide)
  xref = {slide: xref[slide] for slide in path}
  return path, xref


def main():
  with ZipFile('./extra/safe.pptx') as deck:
    path, xref = get_solution_path(deck, start_slide=1, end_slide=14)
    flag = ''

    for i, j in zip(path, path[1:]):
      slide = load_xml(deck, f'ppt/slides/slide{i}.xml')
      buttons = slide.getElementsByTagName('p:sp')
      button_id = xref[i][j]

      for button in buttons:
        if link := button.getElementsByTagName('a:hlinkClick'):
          if link[0].attributes['r:id'].value == button_id:
            key = button.getElementsByTagName('a:t')[0].firstChild
            key = key.nodeValue.strip()
            if key.isnumeric():
              flag += key

    print('CTFlearn{%s}' % flag)


if __name__ == '__main__':
  main()

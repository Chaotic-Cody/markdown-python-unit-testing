"""
 Markdown.py
 0. just print whatever is passed in to stdin
 0. if filename passed in as a command line parameter, 
    then print file instead of stdin
 1. wrap input in paragraph tags
 2. convert single asterisk or underscore pairs to em tags
 3. convert double asterisk or underscore pairs to strong tags

"""

import fileinput
import re

def convertStrong(line):
  line = re.sub(r'\*\*(.*)\*\*', r'<strong>\1</strong>', line)
  line = re.sub(r'__(.*)__', r'<strong>\1</strong>', line)
  return line

def convertEm(line):
  line = re.sub(r'\*(.*)\*', r'<em>\1</em>', line)
  line = re.sub(r'_(.*)_', r'<em>\1</em>', line)
  return line

def convertHead1(line):
  line = re.sub(r'\# (.*)', r'<h1>\1</h1>', line)
  return line

def convertHead2(line):
  line = re.sub(r'\#\# (.*)', r'<h2>\1</h2>', line)
  return line

def convertHead3(line):
  line = re.sub(r'\#\#\# (.*)', r'<h3>\1</h3>', line)
  return line

def findBlockQuote(line):
  return re.search(r'> ', line)

def convertBlockQuote(line):
  currentBlock = False
  if findBlockQuote(line):
    currentBlock = True
  line = re.sub(r'> (.*)', r'<blockquote>\1', line)
  return line, currentBlock

prevBlock = False
currentBlock = False

for line in fileinput.input():
  line = line.rstrip() 
  line = convertStrong(line)
  line = convertEm(line)
  line = convertHead3(line)
  line = convertHead2(line)
  line = convertHead1(line)
  line, currentBlock = convertBlockQuote(line)

  if prevBlock and not currentBlock:
    print line + '</blockquote></p>'
  elif prevBlock and currentBlock:
    print re.sub(r'<blockquote>', '', line)
  elif currentBlock and not prevBlock:
    print('<p>' + line),
  else:
    print '<p>' + line + '</p>'
    
  prevBlock = currentBlock


#! /usr/bin/env python3

import os
import sys

import json
from json import JSONEncoder

class PaperReview(object):
   def __init__(self):
      self.title = 'TITLE'
      self.description = ['DESCRIPTION', 'PARAGRAPH']
      self.review = ['REVIEW', 'PARAGRAPH']
      self.rating = -1

class PaperReviewJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, PaperReview):
            return obj.__dict__
        return JSONEncoder.default(self, obj)

def main():
   review = PaperReview()
   print(json.dumps(review, indent = '    ', sort_keys=True, cls=PaperReviewJSONEncoder))
   return 0

if __name__ == '__main__':
   sys.exit(main())


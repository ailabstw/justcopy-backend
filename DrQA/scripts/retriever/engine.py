#!/usr/bin/env python3
# Copyright 2017-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
"""Interactive mode for the tfidf DrQA retriever module."""

import argparse
import code
import prettytable
import logging
from drqa import retriever


class SearchEngine:
    def __init__(self, db_path, model):
        '''
        Args:
            model: tfidf model path
        '''
        self.doc_db = retriever.DocDB(db_path=db_path)
        self.ranker = retriever.get_class('tfidf')(tfidf_path=model)


    def process(self, query, k=1):
        doc_names, doc_scores = self.ranker.closest_docs(query, k)
        table = prettytable.PrettyTable(
            ['Rank', 'Doc Id', 'Doc Score']
        )
        texts = []
        for i in range(len(doc_names)):
            texts.append(self.doc_db.get_doc_raw(doc_names[i]))
            table.add_row([i + 1, doc_names[i], '%.5g' % doc_scores[i]])
        #print(table)
        return doc_names, texts


if __name__ == '__main__':
    ''' test '''
    model = '/data/alex/db_tfidf/db-tfidf-ngram=2-hash=16777216-tokenizer=simple.npz'
    engine = SearchEngine(model = model)
    engine.process('館長', k=5)

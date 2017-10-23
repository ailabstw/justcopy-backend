import torch
import argparse
import code
import prettytable
import os

from termcolor import colored
from drqa import pipeline
from drqa.retriever import utils

class Agent:
    def __init__(self, reader, retriever, doc_db):
        self.DrQA = pipeline.DrQA(
            cuda=True,
            fixed_candidates=None,
            reader_model=reader,
            ranker_config={'options': {'tfidf_path': retriever}},
            db_config={'options': {'db_path': doc_db}},
            tokenizer=None
        )
    def process(self, question, candidates=None, top_n=1, n_docs=5):
        predictions = self.DrQA.process(
            question, candidates, top_n, n_docs, return_context=True
        )
        table = prettytable.PrettyTable(
            ['Rank', 'Answer', 'Doc', 'Answer Score', 'Doc Score']
        )
        for i, p in enumerate(predictions, 1):
            table.add_row([i, p['span'], p['doc_id'],
                        '%.5g' % p['span_score'],
                        '%.5g' % p['doc_score']])
        print('Top Predictions:')
        print(table)
        print('\nContexts:')
        for p in predictions:
            text = p['context']['text']
            start = p['context']['start']
            end = p['context']['end']
            output = (text[:start] +
                    colored(text[start: end], 'green', attrs=['bold']) +
                    text[end:])
            print('[ Doc = %s ]' % p['doc_id'])
            print(output + '\n')
        return predictions


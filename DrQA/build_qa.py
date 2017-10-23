'''
Process Web QA dataset into SQuAD format
'''
import json
import sys
from multiprocessing import Pool as ProcessPool
from tqdm import tqdm
import multiprocessing

def parse_sample(raw_sample):
    squad_paragraphs = []

    sample = json.loads(raw_sample)
    question = ' '.join(sample['question_tokens'])
    for evidence in sample['evidences']:
        if evidence['type'] == 'positive':
            e_key = evidence['e_key']
            context = ' '.join(evidence['evidence_tokens'])
            answer = ' '.join(evidence['golden_answers'][0])
            
            squad_context = {'context': context,  'qas': []}
            
            answers = [{'text': answer, 'answer_start': context.find(answer)}]
            squad_context['qas'].append({'id': e_key,
                                      'question': question,
                                      'answers': answers })
            squad_paragraphs.append(squad_context)
    return squad_paragraphs

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        samples = f.readlines()
    
    paragraphs = []
    for sample in tqdm(samples):
        paragraphs += parse_sample(sample)
    
    squad_data = {'data': [{'paragraphs': paragraphs}]}
    json.dump(squad_data, open(sys.argv[2], 'w'))

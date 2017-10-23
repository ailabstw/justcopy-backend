'''
Prepare the data for retriver from processed.json
'''
import os
import random
import jieba
from util.analyzier import Analyzier
from util.ptt_filter import ArticleFilter
from multiprocessing import Pool as ProcessPool
import multiprocessing
import json
import pickle
import re
from tqdm import tqdm
dict_path = os.path.join(os.getenv("JIEBA_DATA"), "dict.txt.big") 
jieba.set_dictionary(dict_path)
jieba.initialize() 

def get_article(article):
    if len(article['Title'].strip()) == 0 or len(article['Content'].strip()) == 0:
        return None

    title_cut = jieba.cut(article['Title'], cut_all=False)
    title_cut = ' '.join(title_cut).strip()
    
    content = re.sub('\n', ' ', article['Content'])
    content = re.sub('\ +', ' ', content)
    content_cut = jieba.cut(content, cut_all=False)
    content_cut = ' '.join(content_cut).strip()

    article = {'id' : title_cut, 'text': content_cut, 'raw': article['Raw']}
    return article
  
if __name__ == '__main__':
    data_path = os.getenv('DBDATA')
    
    ptt_filter = ArticleFilter()
    analyzier = Analyzier()
    
    articles = []
    filenames = [os.path.join(data_path, name) for name in os.listdir(data_path) if not name.startswith(".")]
    print(filenames)
    for file in filenames:
        with open(file, 'r', encoding='utf-8') as data:
            articles += json.load(data)
    print(len(articles))
    articles = ptt_filter.generate_corpus(articles)

    response_counter = {}
    f = open('gossiping_articles', 'w')
    '''for i, article in tqdm(enumerate(articles),desc='Ptt articles: '):
        #print(article['Tag'])
        if len(article['Title'].strip()) == 0 or len(article['Content'].strip()) == 0:
            continue

        title_cut = jieba.cut(article['Title'], cut_all=False)
        title_cut = ' '.join(title_cut).strip()
        
        content = re.sub('\n', ' ', article['Content'])
        content = re.sub('\ +', ' ', content)
        content_cut = jieba.cut(content, cut_all=False)
        content_cut = ' '.join(content_cut).strip()

        article = {'id' : title_cut, 'text': content_cut}
        f.write(json.dumps(article) + '\n')
    '''
    cpus = multiprocessing.cpu_count()
    workers = ProcessPool(cpus)
    for article in tqdm(workers.imap_unordered(get_article, articles)):
        if article == None:
            continue
        f.write(json.dumps(article) + '\n')
  
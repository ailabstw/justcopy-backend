'''
dump new crawled pages to one file
'''

import os
import json
import re
import datetime

    
def get_articles( board, index=1):
    '''
    Get the crawled page by the modified time
    Args:
        board: string, specify the board
        index: get index(st) page from the directory
    Return:
        articles
    '''
    def get_pagenum(filename):
        return int(re.findall(r'\d+', filename)[0])
    def get_modified(filename):
        return os.path.getctime(filename)
    data_path = os.path.join(os.getenv("DATA"), "raw" ) 
    path = os.path.join(data_path, board)
    filenames = [os.path.join(path, name) for name in os.listdir(path) if not name.startswith(".")]
    filenames = sorted(filenames, key=get_modified)
    files = filenames[index:]
    articles = []
    for file in files:
        if os.path.exists(file):
            with open(file, 'r', encoding='utf-8') as f:
                articles += json.load(f)
        else:
            print('No such file!')
            return []
    return articles 



if __name__ == '__main__':
    articles = get_articles('Gossiping', -100) # get the latest 100 pages
    
    target_dir = os.getenv('DBDATA')
    filename = datetime.datetime.now().strftime('%m_%d_%H_%M_%S')
    with open(os.path.join(target_dir, filename + '.json'), 'w') as f:
        json.dump(articles, f)
    

    



    
#!/bin/bash

source /home/alex/setup.sh
source /home/alex/DrQA/setup.sh

src=/home/alex/DrQA
python3 $src/merge_pages.py
python3 $src/prepare_ptt.py
python3 $src/scripts/retriever/build_db.py $src/gossiping_articles $src/db.db
python3 $src/scripts/retriever/build_tfidf.py $src/db.db $src/


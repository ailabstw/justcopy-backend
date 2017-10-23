
CUDA_VISIBLE_DEVICES='1' python3 scripts/reader/train.py --fix-embedding=True --embedding-dim=300 --embed-dir=/home/alex/DeepQA/data/embeddings/ --embedding-file=wiki.zh_classical.vec --tune-partial 5000 --model-dir=models --data-dir=data/tw_datasets --train-file=training-processed-corenlp.txt --dev-file=validation-processed-corenlp.txt --dev-json=validation.json 

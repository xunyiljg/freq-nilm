#!bin/bash

# svm gpu1

CUDA_VISIBLE_DEVICES=1 python rnn-tree-greedy.py GRU 50 2 True 1 200 0
CUDA_VISIBLE_DEVICES=1 python rnn-tree-greedy.py GRU 50 2 True 1 400 0
CUDA_VISIBLE_DEVICES=1 python rnn-tree-greedy.py GRU 50 2 True 1 600 0
CUDA_VISIBLE_DEVICES=1 python rnn-tree-greedy.py GRU 50 2 True 1 800 0

CUDA_VISIBLE_DEVICES=1 python rnn-tree-greedy.py GRU 50 4 True 1 200 0
CUDA_VISIBLE_DEVICES=1 python rnn-tree-greedy.py GRU 50 4 True 1 400 0
CUDA_VISIBLE_DEVICES=1 python rnn-tree-greedy.py GRU 50 4 True 1 600 0
CUDA_VISIBLE_DEVICES=1 python rnn-tree-greedy.py GRU 50 4 True 1 800 0
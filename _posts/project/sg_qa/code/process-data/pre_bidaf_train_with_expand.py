# coding:utf-8
import re
import json
import sys
import codecs
from prepro import all_pro,my_ch2digits,my_digits2ch,contains_d
import pdb
from fuzzy_find import fuzzy_answer
import os
import argparse
#pdb.set_trace()

parser = argparse.ArgumentParser()
parser.add_argument('--in_dir')
parser.add_argument('--in_type')
parser.add_argument('--out_dir')
parser.add_argument('--out_fname')
args = parser.parse_args()
new_data = {}
new_data['version'] = args.out_fname
new_data['data'] = []

def get_answer(answer,context):
    qa_answers = []
    start = 0
    while True:
        p = context.find(answer,start)
        if p != -1:
            qa_answers.append({"text":answer,'answer_start':p})
            start = p + 1
        else:
            break
    return qa_answers 

answer_expand={}
with open(os.path.join(args.in_dir,'qid_answer_expand'),'r') as f:
    for line in f.readlines():
        v = line.strip('\n').split('\t')
        answer_expand[int(v[0])] = v[2].split('|')

fw = open(os.path.join(args.out_dir,args.out_fname),"w",encoding="utf-8")
total = 0
for file in os.listdir(args.in_dir):
    if file.startswith(args.in_type+'_factoid'):
        with open(os.path.join(args.in_dir,file),"r",encoding='utf-8') as fr:    
            for line in fr.readlines():
                inf = json.loads(line.strip("\n").strip("\r"))
                d1 = {}
                d1['paragraphs'] = []
                q= all_pro(inf["query"],True)
                passages = []
                for inx,passage in enumerate(inf['passages']):
                    if passage['passage_text']:
                         tmp = all_pro(passage['passage_text'],True)
                         if tmp not in passages:
                             passages.append(tmp)
                context = "".join(passages)
                qas = []
                for answer in answer_expand[int(inf['query_id'])]:
                    if answer!= '':
                        qa = {}
                        qa['question'] = q
                        qa['id'] = str(inf["query_id"]) + '_' + str(answer_expand[int(inf['query_id'])].index(answer))
                        qa['answers'] = get_answer(answer=all_pro(answer,True),context=context)
                        if len(qa['answers']) != 0:
                            qas.append(qa)
                d2 = {}
                d2["context"] = passages
                d2['qas'] = qas
                d1['paragraphs'].append(d2)
                new_data['data'].append(d1)
                total += 1
new_data['version'] = str(total) + '_' + args.out_fname
fw.write(json.dumps(new_data,ensure_ascii=False,indent=3))
fw.close()

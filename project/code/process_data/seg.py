# coding:utf-8
LTP_DATA_DIR = '/data2/yndeng/GAME/ltp_data'  # ltp模型目录的路径
import os
import pdb
cws_model_path = os.path.join(LTP_DATA_DIR, 'cws.model')  # 分词模型路径，模型名称为`cws.model`
from pyltp import Segmentor
import json
segmentor = Segmentor()  # 初始化实例
segmentor.load(cws_model_path)  # 加载模型
def word_tokenize(sent):
    sent = sent.replace(' ','XXXX')
    tmp = segmentor.segment(sent)  # 分词
    words = []
    for w in tmp:
        if 'XXXX' in w:
            words.append(w.replace('XXXX',' '))
        else:
            words.append(w)
    return words

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
#pdb.set_trace()
with open('train.json','r') as fr,open('seg_train.json','w') as fw:
    inf = json.load(fr)
    new_inf = inf
    for i in range(len(inf['data'])):
        d = inf['data'][i]['paragraphs'][0]['context']
        new_d = []
        for c in d:
            c = word_tokenize(c)
            c = "".join(c[:100])
            new_d.append(c)
        context = "".join(new_d)
        new_inf['data'][i]['paragraphs'][0]['context'] = new_d
        for j in range(len(inf['data'][i]['paragraphs'][0]['qas'])):
            m_id = str(inf['data'][i]['paragraphs'][0]['qas'][j]['id'])
            if len(inf['data'][i]['paragraphs'][0]['qas'][j]['answers']) > 0:
                a = inf['data'][i]['paragraphs'][0]['qas'][j]['answers'][0]['text']
                qa_answers = get_answer(answer=a,context=context)
                new_inf['data'][i]['paragraphs'][0]['qas'][j]['answers'] = qa_answers
            else:
                print(m_id,a)
    fw.write(json.dumps(new_inf,ensure_ascii=False,indent=3))
segmentor.release()  # 释放模

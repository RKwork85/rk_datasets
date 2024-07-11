import json

with open ('/home/rkwork/work_place/project/rk_datasets/rk_experiment/4_gz_company/result/v3.jsonl', mode='r') as f:
    data = [json.loads(line) for line in f]


with open('./ttt.jsonl', mode='w', encoding='utf-8') as f :
    for dataset in data:
        dataset['instruction']= dataset['input']
        dataset['input'] = ''
        f.write(json.dumps(dataset, ensure_ascii =False) + '\n')
import json

with open ('/home/rkwork/work_place/project/rk_datasets/rk_experiment/3_gz_baiyunshan/daiding.json', mode='r') as f:
    data = json.load(f)

with open('./daiding.jsonl', mode='a+', encoding='utf-8') as f :
    for dataset in data:
        f.write(json.dumps(dataset, ensure_ascii =False) + '\n')
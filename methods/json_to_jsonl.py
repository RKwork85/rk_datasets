import json

with open ('temp.json', mode='r') as f:
    data = json.load(f)

with open('./temp.jsonl', mode='a+', encoding='utf-8') as f :
    for dataset in data:
        f.write(json.dumps(dataset, ensure_ascii =False) + '\n')
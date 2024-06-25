import json

with open ('temp.jsonl', mode='r') as f:
    data = [json.loads(line) for line in f]


with open('./temp.json', mode='w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
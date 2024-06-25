# 关于数据集工作的总结

### Dir Introduce

目录包含三部分: 

- 数据集文件：json 和 jsonl格式

- 互转脚本：method， 根目录下的文件是测试脚本用的 

- 试验记录： rk_experiment

├── datasets
│   ├── advertisement
│   │   ├── advertisement.json
│   │   └── advertisement.jsonl
│   ├── company
│   │   └── company.jsonl
│   ├── contract
│   │   └── contract.jsonl
│   ├── other_diseases
│   │   ├── 癫痫.csv
│   │   ├── 癫痫.jsonl
│   │   ├── 高血压.csv
│   │   ├── 高血压.jsonl
│   │   ├── 胃炎.csv
│   │   ├── 胃炎.jsonl
│   │   └── Pulmonology
│   │       ├── 肺炎.csv
│   │       ├── 感冒.csv
│   │       ├── 哮喘.csv
│   │       ├── 支气管炎.csv
│   │       └── breath.csv
│   ├── self_recognition
│   │   └── self_recognition.jsonl
│   └── sentiment
│       ├── sentiment.json
│       └── sentiment.jsonl
├── medical
│   └── pediatric_consultation.jsonl
├── methods
│   ├── jsonl_to_json.py
│   └── json_to_jsonl.py
├── REDME.md
├── rk_experiment
│   ├── 1_gz_traval
│   │   ├── traval2_eval.jsonl
│   │   ├── traval2.jsonl
│   │   ├── traval_eval.jsonl
│   │   └── traval.jsonl
│   ├── 2_cloud_traval
│   │   ├── traval6_eval.jsonl
│   │   ├── traval6.json
│   │   └── traval6.jsonl
│   ├── prompt.md
│   └── REDME.md
├── temp.json
└── temp.jsonl

- 

## Notes

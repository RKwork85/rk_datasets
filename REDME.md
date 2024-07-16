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
│   │   ├── company2.jsonl
│   │   └── company.jsonl
│   ├── contract
│   │   └── contract.jsonl
│   ├── general
│   │   ├── alpaca_data_cn.json
│   │   ├── Belle_open_source.json
│   │   ├── counterfactural_correction_multi_round_chat.json
│   │   ├── firefly.json
│   │   └── RedGPT-Dataset-V1-CN.json
│   ├── law
│   │   └── consultation.jsonl
│   ├── ms_agent
│   │   └── dev.jsonl
│   ├── multiturn
│   │   └── multiturn_chat_0.8M.json
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
│   ├── poem
│   │   └── chinese_poems.txt
│   ├── rlhf
│   │   └── 1ec8bf999c56541a0b00d3dd6e56eb2e.csv
│   ├── self_recognition
│   │   └── self_recognition.jsonl
│   └── sentiment
│       ├── sentiment.json
│       └── sentiment.jsonl
├── docs
│   ├── dataset_format.md
│   └── Training_documentation.md
├── medical
│   └── pediatric_consultation.jsonl
├── methods
│   ├── jsonl_to_json.py
│   ├── json_to_jsonl.py
│   └── random_eval.py
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
│   ├── 3_gz_baiyunshan
│   │   ├── baiyunshan.json
│   │   ├── baiyunshan.jsonl
│   │   ├── human_eval.md
│   │   ├── jingquziliao.md
│   │   └── rknotes.md
│   ├── 4_gz_company
│   │   ├── company.jsonl
│   │   ├── json_to_jsonl.py
│   │   ├── modify.py
│   │   ├── refer_data
│   │   │   ├── gzzca_0.txt
│   │   │   ├── gzzca_1.txt
│   │   │   ├── gzzca_2.txt
│   │   │   ├── gzzca_3.txt
│   │   │   ├── gzzca_4.txt
│   │   │   ├── gzzca_5.txt
│   │   │   ├── gzzca_6.txt
│   │   │   ├── gzzca.txt
│   │   │   ├── q0q3.txt
│   │   │   └── question.md
│   │   ├── result
│   │   │   ├── input_compare
│   │   │   │   ├── m00m33.jsonl
│   │   │   │   ├── m0m3.jsonl
│   │   │   │   ├── v00.jsonl
│   │   │   │   ├── v0.jsonl
│   │   │   │   ├── v11.jsonl
│   │   │   │   ├── v1.jsonl
│   │   │   │   ├── v22.jsonl
│   │   │   │   ├── v2.jsonl
│   │   │   │   ├── v33.jsonl
│   │   │   │   └── v3.jsonl
│   │   │   └── question
│   │   │       ├── q1.jsonl
│   │   │       ├── q2.jsonl
│   │   │       ├── q3.jsonl
│   │   │       └── q4.jsonl
│   │   ├── rknotes.md
│   │   ├── temp.json
│   │   └── tempp.json
│   ├── 5_position
│   │   ├── muzi.jsonl
│   │   └── position.jsonl
│   ├── 提示词.md
│   ├── prompt.md
│   └── REDME.md
├── temp.json
├── ttt copy.jsonl
└── ttt.jsonl

- 

## Notes

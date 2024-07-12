## 关于4_gz_company的训练记录

```
文件夹目录结构：
├── company.jsonl                       // 最终结果数据集
├── json_to_jsonl.py                    // 如文件名
├── modify.py                           // 对数据集字段 进行修改：v0 ——> v00的 改变： 目的是探究input字段是否为空的 训练效果 区别
├── refer_data                          // 数据集参考资料
│   ├── gzzca_0.txt                 
│   ├── gzzca_1.txt
│   ├── gzzca_2.txt
│   ├── gzzca_3.txt
│   ├── gzzca_4.txt
│   ├── gzzca_5.txt
│   ├── gzzca.txt                       //gzzca_* 是gzzca.txt的分块子文件
│   └── question.md                     // question.md 是 创建数据集文件的方式
├── result
│   ├── m00m33.jsonl
│   ├── m0m3.jsonl
│   ├── v00.jsonl
│   ├── v0.jsonl
│   ├── v11.jsonl
│   ├── v1.jsonl
│   ├── v22.jsonl
│   ├── v2.jsonl
│   ├── v33.jsonl
│   └── v3.jsonl
├── rknotes.md
├── temp.json
└── tempp.json
```

一、 数据集制作方面

- 数据集组成

```
v1: 200 

80（自我认知） + 30(who is CEO)  + 90( Introduction about CEO)

/home/rkwork/work_place/project/platform/gzcai/output/qwen1half-7b-chat/v81-20240711-194024
8:2 20epoch 200step

```











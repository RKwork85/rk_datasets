##  培训方案

目标：

通过制作数据集，微调一个大模型

**数据集**： 用于训练的文本数据

- 数据集分类： 训练集，测试集，验证集    （AI上一般来说）

- 比例：2：8 、3：7

- 数据集格式： 
    - 文件格式：json, jsonl, csv
    - 内容格式：单轮对话，多轮对话

- 数据集条数： 

    - 对于一个问题 3——4条数据集

- 数据集评价标准：

1 文本数据多样性

2 符合真实场景


**大模型**

以Transformer为代表的模型架构，一堆参数

BERT（Bidirectional Encoder Representations from Transformers）、
GPT（Generative Pre-trained Transformer）、
T5（Text-to-Text Transfer Transformer）等

**微调**： 在预训练模型的基础上进行监督微调

```
全量微调（Full Fine-Tuning, FFT）：

这种方法涉及对预训练模型的所有参数进行调整，以适应新的下游任务。它可能会导致计算成本较高，并有可能引起灾难性遗忘，即在提高特定任务性能的同时，可能会损害模型在原始任务上的表现 。
参数高效微调（Parameter-Efficient Fine-Tuning, PEFT）：

这类方法旨在减少需要更新的参数数量，以降低训练成本和时间。PEFT包括多种技术，如Prefix Tuning、Prompt Tuning、Adapter Tuning和LoRA等 。
前缀调整（Prefix Tuning）：

通过在输入前添加可学习的virtual tokens作为Prefix，并只更新这些Prefix参数，而保持Transformer其他部分固定 。
Prompt Tuning：

一种简化版的Prefix Tuning，通过在输入层加入prompt tokens，而无需额外的MLP调整 。
适配器调整（Adapter Tuning）：

在模型的每个层或选定层之间插入小型神经网络模块，称为“适配器”，这些适配器是可训练的，而原始模型的参数则保持不变 。
LoRA（Low-Rank Adaptation）：

引入两个低秩矩阵来对原始权重矩阵进行低秩近似调整，从而实现对模型的微调 。
监督式微调（Supervised Fine-Tuning, SFT）：

使用人工标注的数据，通过监督学习的方法对大模型进行微调 。
基于人类反馈的强化学习微调（RLHF, Reinforcement Learning with Human Feedback）：

结合人类反馈通过强化学习的方式进行微调，以提升模型生成文本等内容的质量 。
基于AI反馈的强化学习微调（RLAIF, Reinforcement Learning with AI Feedback）：

类似于RLHF，但是反馈的来源是AI，旨在解决反馈系统的效率问题 。
ReFT（Representation Finetuning）：

```
**训练参数**

1 train_epoch: 训练轮数, 数据集文件训练多少遍

2 batch_size: 批处理大小，每一步训练多少条数据，数据集划分

3 gradient_accumulation_steps: 梯度累计，多久更新一次梯度：理论上每经过一次前向传播和反向传播就会更新一次梯度

4 step: 步长

5 交叉验证步数： 每隔多少步验证一次

6 LR： 学习率： 一般为1e4 或 1e5 ， 学习率 预热 衰减 前 0.1% ~ 0.5%

7 loss: 模型求解过程中理论和实际的差异

评估：

以验证集为准：

eval_loss：不断走低

eval_acc: 不断走高

**量化**

- 使用：显存不足时，选择

- 模式： int 4 in8


**部署**

quantization_bit 4

2 
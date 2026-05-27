# biocarp

`biocarp` 是面向生物医学、肿瘤生信和转化研究的 Codex 技能体系。它用于研究设计、数据评估、工具选择、流程执行、图表质控、结果解读、文献依据整理和项目状态记录。

## 功能范围

- bulk RNA-seq、芯片、临床队列、生存分析、预测模型和功能推断
- 单细胞 RNA、CITE-seq、VDJ、scATAC、多组学、扰动组学、空间组学和邻域分析
- ATAC-seq、ChIP-seq、CUT&Tag、CUT&Run、甲基化、Hi-C、motif 和 footprinting
- WGS、WES、panel、RNA variant、CNV、SV、HLA、抗原肽、neoantigen 和免疫肽组学
- 宏基因组、16S、ITS、宏转录组、virome、MAG 和宿主-微生物联合分析
- 蛋白质组、磷酸化组、PTM、靶向蛋白质组、代谢组、脂质组、同位素示踪和代谢流
- small RNA、splicing、long-read isoform、CLIP-seq、Ribo-seq、RNA modification、RNA editing、cfDNA、ctDNA、CTC 和 exosome
- 蛋白结构预测、分子对接、分子动力学、虚拟筛选、ADMET 和药物预测
- 影像组学、病理图像、自动分割、自动勾画、多重组织成像、虚拟染色和虚拟空间组学
- 临床研究方案设计、样本量估计、真实世界证据、临床数据标准化和数据质量检查
- 系统综述、meta 分析、网状 meta、MR、药物警戒、GWAS、PRS、fine mapping、colocalization、QTL、TWAS 和 biobank 分析

## 调用场景

- 从原始 FASTQ、BAM、VCF、mzML、DICOM、WSI 或表达矩阵开始完成分析
- 判断一个数据集能支持哪些研究问题
- 为论文设计完整图表流程和验证路线
- 复现或扩展公共数据研究
- 比较工具路线并选择适合当前数据的流程
- 进行临床研究方案、样本量、真实世界证据或结局分析
- 检查工具版本、GitHub issue、论坛问题和常见错误

## 使用方法

在 Codex 中直接说明任务和数据位置，例如：

```text
使用 biocarp 分析这个单细胞数据，完成 QC、注释、差异分析、细胞通讯、拟时序、完整图表输出和中文阶段报告。
```

```text
使用 biocarp 评估这个临床研究问题，给出研究方案、样本量估计、结局分析和报告框架。
```

```text
使用 biocarp 为这个蛋白质组和代谢组项目设计分析流程，并输出完整图表和中文说明。
```

## 核心特性

- 先确认研究问题、数据结构、关键实验信息、参数和终点，再执行分析
- 按任务读取 `references/` 中的专项流程，避免一次加载无关内容
- 支持子任务代理协作和目标追踪
- 每个分析模块输出该方法应有的诊断图、特色图和最终解释图
- 每张图都检查尺寸、比例、分辨率、标签、图例、配色和数据一致性
- 缺少工具时优先配置，并记录版本、命令、数据库、模型和环境
- 阶段完成后生成中文说明文件，包含结果、解读、方法学、参考文献、限制和工具问题
- 保存 `分析状态.md`，方便项目在对话中断后继续
- 用 `method-updates.md`、`bug-log.md` 和 `tool-issues.md` 记录新流程、新问题和处理方法

## 目录结构

```text
.
├── SKILL.md
├── agents/
├── references/
└── scripts/
```

`SKILL.md` 保存核心规则。`references/` 保存按任务调用的流程、工具、参数、文献和问题记录。`scripts/` 保存文献检索和代码风格摘要等辅助脚本。

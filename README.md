# biocarp

`biocarp` 是面向肿瘤生物信息学和转化医学研究的 Codex 技能体系。它用于把研究问题、数据结构、分析流程、图表输出、结果解释、工具部署、文献依据和问题记录整合为完整分析过程。

该技能强调从生物学问题出发，先确认数据、分组、终点和可实现的分析目标，再选择工具和流程。对于新手用户，它会直接指出不合理假设，给出修正方案，并主动补充合适的公共数据、分析工具和验证路线。

## 核心能力

- 研究问题拆解和数据可行性评估
- 公共数据库检索、文献梳理和近年方法对齐
- bulk RNA-seq、芯片、临床队列和生存分析
- 单细胞转录组、单细胞 ATAC、多组学联合和空间转录组
- 细胞通讯、拟时序、RNA velocity、CNV、克隆性和免疫组库
- 转录因子活性、通路活性、激酶活性、反卷积和功能评分
- WGS、WES、panel、RNA variant、HLA 分型、抗原肽、neoantigen 和免疫肽组学
- ATAC-seq、ChIP-seq、CUT&Tag、CUT&Run、甲基化和染色质分析
- 宏基因组、16S、ITS、宏转录组、MAG 和宿主-微生物联合分析
- 蛋白质组、磷酸化组、PTM、靶向蛋白质组、代谢组、脂质组、同位素示踪和代谢流
- 蛋白结构预测、分子对接、分子动力学模拟、虚拟药物筛选和 ADMET
- 药物预测、扰动组学、Perturb-seq、CROP-seq 和单细胞扰动分析
- 影像组学、病理图像、自动分割、自动勾画、虚拟多重免疫荧光和虚拟空间组学
- 流式、CyTOF、多重组织成像、蛋白组、代谢组和其他专项组学
- 工具版本检查、GitHub issue、论坛问题和已知 bug 记录
- 子任务代理协作、目标追踪、阶段报告和项目状态恢复

## 数据类型

`biocarp` 支持常见和前沿生物医学数据，包括：

- FASTQ、BAM、CRAM、VCF、BED、GTF、GFF、peak、fragment、count matrix
- bulk 表达矩阵、芯片矩阵、临床表、随访表、药物响应表
- VCF、MAF、CNV segment、SV、HLA、抗原肽候选表和免疫肽组学结果
- Seurat、SingleCellExperiment、AnnData、h5ad、h5Seurat、10x 数据
- Visium、Slide-seq、Stereo-seq、MERFISH、Xenium、CosMx 等空间数据
- TCR、BCR、CyTOF、流式、mIF、IMC、CODEX、MIBI 和 CyCIF 数据
- 16S、ITS、shotgun metagenomics、metatranscriptomics、MAG 和 virome 数据
- mzML、raw MS、proteinGroups、peptide、PTM site、metabolite feature、lipid feature、isotopologue 和 flux 表
- PDB、mmCIF、FASTA、SDF、SMILES、分子库和药物筛选结果
- WSI、H&E、IHC、IF、DICOM、NIfTI、病理切片和放疗勾画数据

## 工作方式

一次真实分析通常按以下顺序执行：

1. 通览项目状态、数据目录、已有输出和环境。
2. 明确研究问题、分组、样本来源、终点和限制。
3. 读取任务相关的参考文件，必要时检索近期文献、工具文档和 issue。
4. 选择最短的完整分析路线，避免过度工程化。
5. 部署缺失工具，记录版本、命令、数据库、模型权重和环境路径。
6. 编写脚本并运行分析，保留原始文件和关键中间结果。
7. 输出该方法应有的完整图表集合。
8. 检查每张图的尺寸、比例、分辨率、标签、配色、图例和数据一致性。
9. 对每张图写出方法、结果、可靠性、异常检查和后续验证。
10. 生成中文阶段报告，写明结果、解读、方法学、参考文献、限制和工具问题。

## 图表标准

该技能要求每个分析模块输出方法应有的完整图表集合，不能只输出最低限度的展示图。

示例：

- 拟时序分析需要输出轨迹结构、根节点和分支设定、拟时序分布、分支相关基因趋势和工具诊断图。
- RNA velocity 需要输出速度箭头或流线图、latent time、速度置信度、phase portrait 和关键驱动基因视图。
- 细胞通讯需要输出全局互作、通路网络、配体-受体气泡图或热图、信号角色、贡献图和工具支持的 chord、circle、hierarchy 等特色图。
- ATAC 和 ChIP 类分析需要输出 QC、峰注释、信号热图、metaplot、motif、footprint 和关键位点浏览器轨道。
- 空间组学需要输出组织空间图、空间 marker、邻域、共定位、空间通讯和组织图像对齐结果。
- 结构和药物筛选需要输出置信度、结构视图、对接姿势、相互作用图、评分分布、RMSD、RMSF、SASA、氢键和自由能相关图。
- 抗原肽和免疫肽组学需要输出 HLA 支持、候选肽过滤流程、MHC 结合分布、肽长度、motif、MS 证据和多层证据矩阵。
- 蛋白质组、代谢组和代谢流需要输出 raw MS QC、鉴定数量、缺失率、标准化、PCA、差异图、PTM 位点、激酶活性、代谢物注释、脂质类别、同位素分布、flux map 和模型拟合图。
- 影像和虚拟染色需要输出原始图、配准和分割 QC、真实值与预测叠加、Dice、Hausdorff、边界误差、表型图和不确定性图。

如果数据缺少必需输入，技能会记录具体阻断原因。它不会用简单图替代完整方法输出。

## 输出文件

分析结果默认使用 UTF-8 中文命名。常见输出包括：

- `分析状态.md`
- `图表清单.md`
- `图表解读.md`
- `方法学说明.md`
- `参考文献与依据.md`
- `工具部署记录.md`
- `工具问题记录.md`
- `阶段报告.md`
- `限制说明.md`
- 分析脚本、结果表、RDS、AnnData、模型输出和完整图片目录

当工具或外部软件存在编码问题时，才使用 ASCII 文件名，并记录中文名和 ASCII 名的对应关系。

## 文献和知识更新

`biocarp` 使用真实存在的数据集、工具文档、软件 issue 和已发表文献。涉及新方法、近期工具、疾病特异分析、公共数据复现或研究设计时，技能会先进行文献和工具检查，再给出方法判断。

技能维护以下记录：

- `references/method-updates.md`：新工具、新流程、新版本和新文献用法。
- `references/bug-log.md`：分析过程中遇到的错误、原因和处理方法。
- `references/user-profile.md`：用户水平和使用习惯的临时参考。
- `references/tool-issues.md`：常用工具的已知问题、版本冲突和处理方法。

用户水平和使用习惯只作为临时参考。更换使用者或任务背景变化时，技能会重新判断。

## 仓库结构

```text
.
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── index.md
│   ├── workflows.md
│   ├── execution.md
│   ├── learning.md
│   ├── methods.md
│   ├── tools.md
│   ├── single-cell-advanced.md
│   ├── bulk-inference.md
│   ├── metagenomics.md
│   ├── structural.md
│   ├── imaging.md
│   ├── tool-issues.md
│   ├── literature.md
│   ├── public-data.md
│   └── data-assessment.md
└── scripts/
    ├── build_literature_landscape.py
    └── summarize_code_style.py
```

`SKILL.md` 保存核心执行规则。`references/` 保存按任务按需读取的方法、工具、流程、问题和知识更新。`scripts/` 保存稳定的辅助脚本。

## 使用方式

在 Codex 中调用：

```text
使用 biocarp 分析这个单细胞数据，完成 QC、注释、差异分析、细胞通讯、拟时序和完整图表解读。
```

也可以指定具体任务：

```text
使用 biocarp 评估这个 bulk RNA-seq 队列能否做免疫反卷积、TF 活性预测和药物预测，并给出完整分析路线。
```

## 基本原则

- 先确认问题和数据，再执行分析。
- 保留原始文件和关键输出。
- 缺少必要工具时尽量直接部署，并记录部署内容。
- 需要多线程或 GPU 时优先使用。
- 阶段完成后必须写中文说明文件。
- 每张图必须检查并解释。
- 结论必须来自真实数据、真实文献和真实工具结果。
- 不输出占位结果、半成品或无依据结论。

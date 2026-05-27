# 方法更新记录

## 记录规则

每条记录包含：

- 日期
- 工具、流程、数据集或文献名称
- 来源链接
- 更新内容
- 输入要求
- 输出结果
- 局限性
- 已更新的本地参考文件

## 已记录更新

### 2026-05-28

- 工具、流程、数据集或文献名称：ROGUE、LISI、scIB、kBET、ASW、graph connectivity、NMI、ARI、clustree
- 来源链接：
  - https://github.com/PaulingLiu/ROGUE
  - https://pmc.ncbi.nlm.nih.gov/articles/PMC7308400/
  - https://github.com/immunogenomics/LISI
  - https://scib.readthedocs.io/
  - https://www.nature.com/articles/s41592-021-01336-8
- 更新内容：将单细胞聚类纯度、异质性、整合效果和批次混合评估纳入常规单细胞 QC 与处理流程。ROGUE 用于聚类纯度和异质性评估。LISI、iLISI、cLISI、kBET、ASW、graph connectivity 等用于整合质量和生物结构保留检查。
- 输入要求：单细胞表达矩阵或降维坐标、聚类标签、批次标签、样本或患者标签、细胞类型标签。ROGUE 需要表达矩阵和待评估分群。LISI 和 scIB 类指标需要嵌入、邻接图或标签信息。
- 输出结果：ROGUE 分数、聚类纯度或异质性图、silhouette 或 ASW 图、iLISI、cLISI、kBET rejection rate、graph connectivity、NMI、ARI、整合前后批次与生物标签对照图。
- 局限性：这些指标不能替代 marker 证据、样本结构和疾病背景判断。高批次混合分数可能伴随真实生物差异减弱，需同时检查 cLISI、marker 保留和细胞类型分离。
- 已更新的本地参考文件：`references/single-cell-advanced.md`、`references/workflows.md`

### 2026-05-28

- 工具、流程、数据集或文献名称：上游处理、变异、HLA、抗原肽、免疫肽组学、蛋白质组、磷酸化组、代谢组、脂质组、代谢流、多组学整合、表观组、通用统计可视化
- 来源链接：
  - https://nf-co.re/docs
  - https://gatk.broadinstitute.org/
  - https://pvactools.readthedocs.io/
  - https://openvax.github.io/mhcflurry/
  - https://nf-co.re/quantms
  - https://fragpipe.nesvilab.org/
  - https://msstats.org/
  - https://www.metaboanalyst.ca/
  - https://bioconductor.org/packages/release/bioc/html/xcms.html
  - https://cobrapy.readthedocs.io/
  - https://docs.scvi-tools.org/en/latest/user_guide/models/multivi.html
  - https://scglue.readthedocs.io/
  - https://macs3-project.github.io/MACS/
  - https://bioconductor.org/packages/release/bioc/html/ComplexHeatmap.html
- 更新内容：新增并接入 `upstream.md`、`variants.md`、`immunopeptidomics.md`、`proteomics.md`、`metabolomics.md`、`multiomics.md`、`epigenomics.md`、`statistics.md`。补齐 FASTQ 到矩阵、raw MS 到定量矩阵、VCF/MAF 到抗原肽、蛋白和 PTM 差异分析、代谢物注释、同位素示踪、13C 代谢流、FBA、CITE-seq、多组学整合、Hi-C、motif、footprinting、通用统计建模和出版级图表工具。
- 输入要求：按模块检查原始文件、样本表、参考版本、HLA、VCF、MAF、raw MS、mzML、搜索数据库、FDR、代谢物注释证据、同位素 tracer、空间坐标、单细胞对象、峰文件、甲基化文件、Hi-C 矩阵和临床标签。
- 输出结果：MultiQC、alignment QC、variant QC、oncoplot、HLA 支持、抗原肽候选表、MHC binding 图、免疫肽组 motif、蛋白质组 QC、差异蛋白图、PTM 位点图、激酶活性图、代谢物注释图、脂质类别图、同位素分布、flux map、FBA 结果、多组学因子、modality weight、motif 和 footprint 图、统计诊断和最终图表清单。
- 局限性：这些工具族依赖输入质量、数据库版本、样本匹配、批次设计、HLA 准确性、肽段证据、代谢物注释等级、同位素实验设计和模型假设。每次真实分析仍需读取官方文档、近期论文和 issue 后再执行。
- 已更新的本地参考文件：`SKILL.md`、`README.md`、`references/index.md`、`references/coverage.md`、`references/routing.md`、`references/methods.md`、`references/tools.md`、`references/workflows.md`、`references/tool-issues.md`、`references/public-data.md`、`references/data-assessment.md`、`references/single-cell-advanced.md`、`references/metagenomics.md`、`references/structural.md`、`references/imaging.md`、`references/upstream.md`、`references/variants.md`、`references/immunopeptidomics.md`、`references/proteomics.md`、`references/metabolomics.md`、`references/multiomics.md`、`references/epigenomics.md`、`references/statistics.md`

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

- 工具、流程、数据集或文献名称：SLOPER、scDecorr、PSGRN、TotalX、seismicGWAS、TrendCatcher、scSurv、scSurvival、SPARK、SPARK-X、phenoptr、RegDiffusion 及相邻工具族
- 来源链接：
  - https://chitra-lab.github.io/2025/12/01/sloper/
  - https://www.nature.com/articles/s41598-026-50586-z
  - https://github.com/GuanLab/PSGRN
  - https://www.nature.com/articles/s41587-026-03068-6
  - https://ylaboratory.github.io/seismic/
  - https://www.nature.com/articles/s41467-025-63753-z
  - https://jaleesr.github.io/TrendCatcher/
  - https://pmc.ncbi.nlm.nih.gov/articles/PMC12797213/
  - https://aacrjournals.org/cancerdiscovery/article/16/5/931/784405/scSurvival-Single-Cell-Survival-Analysis-of
  - https://www.nature.com/articles/s41592-019-0701-7
  - https://github.com/xzhoulab/SPARK
  - https://akoyabio.github.io/phenoptr/
  - https://akoyabio.github.io/phenoptrReports/
  - https://github.com/TuftsBCB/RegDiffusion
- 更新内容：将用户点名工具全部归入对应模块。空间转录组补入空间变异基因、梯度、结构和高分辨率空间探索工具。单细胞补入自监督整合、GRN、扰动 GRN、趋势分析、单细胞生存关联、单细胞与 GWAS 整合。专项 RNA 补入单细胞总 RNA 和非 poly(A) RNA 流程。多重成像补入 phenoptr、phenoptrReports、rtree 和 inForm 导出表路线。
- 输入要求：空间坐标、组织图像、单细胞表达矩阵、扰动标签、时间点、患者生存数据、GWAS summary statistics、LD reference、单细胞注释、mIF 图像、inForm 导出表、TotalX 或相关总 RNA 原始输出。
- 输出结果：空间变异基因图、梯度图、组织结构图、整合质量图、GRN 网络和边置信度图、扰动恢复图、趋势类别图、单细胞生存风险图、空间风险图、细胞类型遗传关联图、driver gene 证据表、mIF 表型和邻域图、总 RNA 生物类型和非编码 RNA QC 图。
- 局限性：这些工具更新较快，部分工具文档和安装方式仍需在每次真实分析前核对。涉及生存、遗传和空间梯度的结论需要患者层面、LD reference、组织结构和外部证据支持。
- 已更新的本地参考文件：`references/single-cell-advanced.md`、`references/tools.md`、`references/index.md`、`references/workflows.md`、`references/imaging.md`、`references/genetic-epidemiology.md`、`references/specialized-omics.md`、`references/coverage.md`、`references/tool-issues.md`、`references/method-updates.md`

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

### 2026-05-28

- 工具、流程、数据集或文献名称：临床研究设计、目标试验模拟、临床数据标准、证据合成、遗传流行病学、专项 RNA 与液体活检、组学平台差异、参数影响
- 来源链接：
  - https://www.bmj.com/content/389/bmj-2024-081123
  - https://jamanetwork.com/journals/jama/fullarticle/2833408
  - https://www.fda.gov/regulatory-information/search-fda-guidance-documents/e9r1-statistical-principles-clinical-trials-addendum-estimands-and-sensitivity-analysis-clinical
  - https://www.rpact.org/
  - https://causal-lda.r-universe.dev/TrialEmulation/TrialEmulation.pdf
  - https://www.hl7.org/fhir/
  - https://www.ohdsi.org/data-standardization/the-common-data-model/
  - https://www.cdisc.org/standards
  - https://www.prisma-statement.org/
  - https://www.metafor-project.org/
  - https://gwas.mrcieu.ac.uk/
  - https://www.cog-genomics.org/plink/2.0/
  - https://www.10xgenomics.com/support/software/cell-ranger
  - https://bd-rhapsody-bioinfo-docs.genomics.bd.com/
  - https://scalebio.github.io/ScaleRna-docs/
  - https://mzmine.github.io/mzmine_documentation/workflows/lcmsworkflow/lcms-workflow.html
- 更新内容：新增并接入 `clinical-research.md`、`causal-inference.md`、`clinical-data.md`、`evidence-synthesis.md`、`genetic-epidemiology.md`、`specialized-omics.md`、`platforms.md`、`parameters.md`。补齐单臂和双臂研究、样本量、SAP、目标试验模拟、真实世界研究、EHR、REDCap、OMOP、FHIR、CDISC、meta 分析、MR、药物警戒、GWAS、PRS、fine mapping、colocalization、small RNA、splicing、long-read isoform、CLIP、Ribo-seq、RNA modification、RNA editing、cfDNA、ctDNA、CTC、exosome、10x、BD、MGI、BGI、Singleron/新格元、Parse、ScaleBio、Fluent、SMART-seq、空间平台、质谱平台、影像平台和关键参数影响。
- 输入要求：按任务检查临床问题、PICO 或目标试验元素、数据字典、终点、时间零点、随访、样本量假设、平台、化学版本、仪器、采集模式、原始 pipeline、参数、公共数据库、summary statistics、LD reference、raw MS、mzML、junction、isoform、fragment、ctDNA、图像和分割标签。
- 输出结果：研究设计表、样本量和 power 曲线、目标试验协议表、平衡图、权重图、临床数据质量表、meta 分析 forest、funnel、network 图、GWAS Manhattan 和 QQ 图、PRS 校准图、colocalization 图、small RNA、splicing、isoform、CLIP、Ribo-seq、RNA modification、RNA editing、fragmentomics 和 ctDNA 图、平台表、参数决策表、before-after 计数表和参数敏感性图。
- 局限性：临床设计依赖真实终点和假设；真实世界研究依赖时间零点、处理过程、测量过程和缺失数据；遗传流行病学依赖祖源、LD reference 和等位基因匹配；平台比较依赖厂商文档和原始 QC；参数敏感性不能替代实验验证。
- 已更新的本地参考文件：`SKILL.md`、`README.md`、`references/index.md`、`references/coverage.md`、`references/routing.md`、`references/methods.md`、`references/tools.md`、`references/workflows.md`、`references/upstream.md`、`references/single-cell-advanced.md`、`references/proteomics.md`、`references/metabolomics.md`、`references/metagenomics.md`、`references/imaging.md`、`references/statistics.md`、`references/public-data.md`、`references/data-assessment.md`、`references/clinical-research.md`、`references/causal-inference.md`、`references/clinical-data.md`、`references/evidence-synthesis.md`、`references/genetic-epidemiology.md`、`references/specialized-omics.md`、`references/platforms.md`、`references/parameters.md`

### 2026-05-28

- 工具、流程、数据集或文献名称：临床研究设计分类扩展与 README 精简
- 来源链接：
  - https://www.consort-spirit.org/extensions
  - https://www.ideal-collaboration.net/the-ideal-framework/recommendations/
  - https://pmc.ncbi.nlm.nih.gov/articles/PMC5963278/
  - https://pmc.ncbi.nlm.nih.gov/articles/PMC4732571/
  - https://pmc.ncbi.nlm.nih.gov/articles/PMC3731143/
  - https://www.equator-network.org/reporting-guidelines/tidier/
  - https://www.equator-network.org/reporting-guidelines/stari-statement/
  - https://pmc.ncbi.nlm.nih.gov/articles/PMC4625997/
  - https://www.bmj.com/content/376/bmj-2021-067975
- 更新内容：扩展 `clinical-research.md` 的研究设计分类，覆盖药物、生物制品、器械、手术、行为、数字健康、随机、非随机、观察性、诊断、预后、预测、实施科学、质量改进、卫生经济学、转化研究、动态治疗策略、SMART、MOST、micro-randomized、master protocol、真实世界和注册登记研究。同步更新 `SKILL.md`、`references/index.md`、`references/coverage.md`、`references/routing.md`、`references/workflows.md`、`references/methods.md`。精简 `README.md`，去掉平台差异条目，将临床能力改为概括性表述。
- 输入要求：临床问题、设计家族、研究目的、目标人群、干预或暴露、对照、终点、随访、随机或抽样规则、样本量假设、实施场景、经济学视角、数据来源、报告规范。
- 输出结果：设计分类选择、假设表、样本量或模拟结果、研究流程图、分析集定义、报告规范清单、阶段报告。
- 局限性：临床设计分类不能替代具体方案论证。罕见或监管用途研究仍需结合真实方案、伦理要求、统计分析计划和主管部门要求核对。
- 已更新的本地参考文件：`README.md`、`SKILL.md`、`references/clinical-research.md`、`references/index.md`、`references/coverage.md`、`references/routing.md`、`references/workflows.md`、`references/methods.md`、`references/method-updates.md`

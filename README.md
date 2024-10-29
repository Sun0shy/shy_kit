# 单细胞测序生物信息学分析流程

## 一、数据读取和创建Seurat对象

### 1. 读取10x数据

下载的数据中有三个压缩文件保存在一个文件夹

* barcodes.tsv.gz
* features.tsv.gz
* matrix.mtx.gz

```r
# 读取单细胞数据集并创建Seurat对象

library(Seurat)

GSE_Seurat <- CreateSeuratObject(
    project = "GSExxxxx",  # 在orig.ident中设置项目名称，可以使用GSE编号来标识数据集
    counts = Read10X("包含上述三个压缩文件的文件夹地址"),  # 读取10x Genomics格式的数据。该函数会自动读取指定文件夹中的压缩文件（.gz），并返回计数矩阵。
    min.cells = 3,  # 限定基因的条件：每个基因至少在3个细胞中被检测到，以过滤掉低表达的基因
    min.features = 200,  # 限定细胞的条件：每个细胞至少要有200个基因被检测到，以确保细胞具有足够的表达信息
    assay = "RNA"  # 指定该Seurat对象所用的测序实验类型为RNA测序
)
```

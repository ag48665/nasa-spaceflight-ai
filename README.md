# NASA Spaceflight AI – RNA-seq Transcriptomics Analysis

## Project Overview

This project analyzes NASA GeneLab RNA-seq transcriptomics datasets using Python, bioinformatics workflows, data visualization, and machine learning techniques.

The analysis focuses on gene expression patterns observed in biological samples exposed to spaceflight-related conditions.

By combining transcriptomics, exploratory data analysis, and machine learning, this project investigates how biological systems may respond to environmental stressors associated with spaceflight.

---

## Project Highlights

✔ NASA GeneLab RNA-seq analysis

✔ PCA transcriptomic exploration

✔ Gene expression profiling

✔ Heatmap visualization

✔ Comparative transcriptomics

✔ Machine learning clustering

✔ Reproducible Python workflow

✔ Space biology data analysis

---

## Main Findings

### Spaceflight samples exhibit distinct transcriptomic patterns

Principal Component Analysis (PCA) revealed substantial variability between biological samples exposed to spaceflight-related conditions.

### Highly expressed genes dominate transcriptomic signatures

Several genes showed consistently elevated expression levels across analyzed datasets and contributed strongly to overall expression patterns.

### Machine learning identifies transcriptomic clusters

K-Means clustering grouped genes into distinct expression profiles, suggesting underlying biological programs and expression states.

### Transcriptomics can support space biology research

Gene expression analysis provides insight into molecular adaptations potentially associated with microgravity, radiation exposure, and physiological stress.

---

## Results

### NASA OSD-245 Expression Profiles

![OSD245 Expression Profiles](figures/osd245_expression_profiles.png)

Gene expression distributions across RNA-seq samples.

---

### PCA of RNA-seq Expression Data

![PCA](figures/pca_spaceflight.png)

PCA visualization of transcriptomic variability across samples.

---

### Top Expressed Genes Heatmap

![Heatmap](figures/top_genes_heatmap.png)

Heatmap showing expression patterns of highly expressed genes.

---

### Top Highly Expressed Genes

![Top Genes](figures/top10_genes_osd245.png)

Most highly expressed genes identified within the OSD-245 dataset.

---

### Top Expressed Genes in NASA Spaceflight Samples

![Top Spaceflight Genes](figures/top10_spaceflight_genes.png)

Comparison of highly expressed genes across analyzed spaceflight datasets.

---

## Datasets

NASA GeneLab RNA-seq datasets:

* GLDS-168
* GLDS-245

Sources:

https://osdr.nasa.gov/bio/repo/data/studies/OSD-168

https://osdr.nasa.gov/bio/repo/data/studies/OSD-245

These datasets contain transcriptomic measurements from mouse biological samples exposed to spaceflight-related environments.

---

## Technologies Used

### Bioinformatics

* RNA-seq transcriptomics
* Gene expression analysis
* Comparative transcriptomics

### Data Science

* Principal Component Analysis (PCA)
* Machine Learning
* Clustering
* Exploratory Data Analysis (EDA)

### Tools

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Jupyter Notebook

---

## Project Structure

```text
nasa-spaceflight-ai/
│
├── figures/
│   ├── osd245_expression_profiles.png
│   ├── pca_spaceflight.png
│   ├── top_genes_heatmap.png
│   ├── top10_genes_osd245.png
│   └── top10_spaceflight_genes.png
│
├── nasa_spaceflight_ai.ipynb
├── nasa_comparative_transcriptomics.ipynb
├── quick_analysis.py
├── README.md
```

---

## RNA-seq Analysis Workflow

### 1. Data Loading

RNA-seq transcriptomics datasets were loaded into Pandas DataFrames and prepared for downstream analysis.

### 2. Gene Expression Analysis

Gene expression distributions were explored to identify highly expressed genes and transcriptomic trends.

### 3. Principal Component Analysis (PCA)

PCA was applied to reduce dimensionality and visualize sample-to-sample variability.

### 4. Heatmap Visualization

Heatmaps were generated to visualize expression patterns and identify dominant transcriptional programs.

### 5. Machine Learning Clustering

K-Means clustering was used to identify transcriptomic groups and expression patterns within the data.

---

## Example Machine Learning Code

```python
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

X = df[['TPM', 'FPKM', 'expected_count']]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

kmeans = KMeans(n_clusters=3, random_state=42)

df['cluster'] = kmeans.fit_predict(X_scaled)
```

---

## Biological Interpretation

The RNA-seq analysis revealed substantial variability in gene expression profiles across NASA spaceflight-related biological samples.

Principal Component Analysis identified transcriptomic differences between samples, suggesting potential biological responses to environmental stressors associated with spaceflight.

Highly expressed genes may be involved in:

* cellular stress responses
* metabolic adaptation
* mitochondrial function
* immune regulation
* tissue remodeling
* radiation response pathways

The clustering analysis further demonstrated that transcriptomic profiles can be grouped into distinct expression states, highlighting the usefulness of machine learning approaches for exploring complex biological datasets.

---

## Potential Applications

### Space Biology

* astronaut health monitoring research
* biological stress response analysis
* radiation response studies
* molecular adaptation research

### Precision Medicine

* biomarker discovery
* disease transcriptomics
* cancer genomics research
* personalized medicine research

### Computational Biology

* transcriptomic pattern discovery
* machine learning for genomics
* biological data exploration
* large-scale omics analysis

---

## Skills Demonstrated

### Bioinformatics

* RNA-seq analysis
* Transcriptomics
* Gene expression profiling
* Biological interpretation

### Data Science

* Principal Component Analysis (PCA)
* Machine learning clustering
* Data visualization
* Exploratory data analysis

### Tools

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* Jupyter Notebook

---

## Future Improvements

* Differential gene expression analysis
* Pathway enrichment analysis
* Gene set enrichment analysis (GSEA)
* Deep learning approaches for transcriptomics
* Multi-omics integration
* Interactive dashboards
* Explainable AI methods for biological interpretation

---

## Installation

Clone the repository:

```bash
git clone https://github.com/ag48665/nasa-spaceflight-ai.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Launch Jupyter Notebook:

```bash
jupyter notebook
```

---

## License

This repository is provided for educational and portfolio purposes.

---

## Author

**Agata Gabara**

MSc Bioinformatics Student

Research Interests:

* Transcriptomics
* Space Biology
* Cancer Genomics
* Computational Biology
* Machine Learning for Life Sciences

GitHub: https://github.com/ag48665

LinkedIn: https://www.linkedin.com/in/agatha-gabara-06494a37/

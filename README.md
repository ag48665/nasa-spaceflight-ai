# NASA Spaceflight AI – RNA-seq Transcriptomics Analysis

## Overview

This project analyzes NASA spaceflight RNA-seq transcriptomics datasets using Python, bioinformatics workflows, data visualization, and machine learning techniques.

The analysis focuses on gene expression patterns observed in biological samples exposed to spaceflight conditions.

The project includes:

- RNA-seq preprocessing
- Exploratory transcriptomics analysis
- PCA dimensionality reduction
- Heatmap visualization
- Highly expressed gene detection
- Comparative transcriptomics
- AI/ML clustering methods

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook

---

## Datasets

NASA GeneLab RNA-seq datasets:

- GLDS-168
- GLDS-245

These datasets contain transcriptomics measurements from mouse biological samples exposed to spaceflight-related conditions.

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

RNA-seq transcriptomics datasets were loaded into Pandas DataFrames and preprocessed for downstream analysis.

### 2. Gene Expression Analysis

The project identifies highly expressed genes using normalized transcriptomics counts and TPM values.

### 3. PCA Analysis

Principal Component Analysis (PCA) was applied to reduce dimensionality and visualize transcriptomic variability across samples.

### 4. Heatmap Visualization

Heatmaps were generated to visualize top expressed genes and expression intensity patterns.

### 5. Machine Learning

K-Means clustering was used to identify gene expression clusters and transcriptomic patterns.

---

## Results

### NASA OSD-245 Expression Profiles

![OSD245 Expression Profiles](figures/osd245_expression_profiles.png)

---

### PCA of RNA-seq Expression Data

![PCA](figures/pca_spaceflight.png)

---

### Top Expressed Genes Heatmap

![Heatmap](figures/top_genes_heatmap.png)

---

### Top Highly Expressed Genes

![Top Genes](figures/top10_genes_osd245.png)

---

### Top Expressed Genes in NASA Spaceflight Sample

![Top Spaceflight Genes](figures/top10_spaceflight_genes.png)

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
## Key Findings

- Identified highly expressed genes across NASA spaceflight samples
- Detected transcriptomic outliers using PCA
- Visualized expression variability using heatmaps
- Applied machine learning clustering to RNA-seq data
- Generated comparative transcriptomics visualizations
  
---

## Biological Interpretation of Results

The RNA-seq transcriptomics analysis revealed significant variability in gene expression profiles across NASA spaceflight-related biological samples.

Principal Component Analysis (PCA) demonstrated distinct transcriptomic variability between samples, suggesting that spaceflight conditions may influence biological regulation and gene activity. Several samples appeared as strong outliers, indicating potentially unique molecular responses to environmental stressors such as microgravity, radiation exposure, oxidative stress, or altered immune regulation.

The heatmap and highly expressed gene analysis identified subsets of genes with exceptionally high transcriptional activity. These genes may play important roles in:

- cellular stress response
- mitochondrial activity
- immune system regulation
- tissue remodeling
- metabolic adaptation
- radiation response pathways

The clustering analysis using machine learning methods further demonstrated that transcriptomic profiles can be grouped into biologically distinct expression patterns. This suggests the possibility of identifying molecular signatures associated with physiological adaptation to spaceflight conditions.

---

## Potential Medical and Clinical Applications

This type of transcriptomics and AI analysis could potentially support biomedical research and future clinical applications in several areas:

### Space Medicine

- monitoring astronaut health during long-duration missions
- detecting early biological stress responses
- studying radiation-induced molecular damage
- identifying biomarkers associated with spaceflight adaptation

### Precision Medicine

Doctors and biomedical researchers could potentially use similar RNA-seq + AI pipelines to:

- detect abnormal gene expression patterns
- identify disease biomarkers
- support cancer transcriptomics analysis
- monitor immune dysfunction
- study neurodegenerative disorders
- personalize treatment strategies

### Early Disease Detection

Machine learning models trained on transcriptomics data may help identify:

- early-stage cancer signatures
- inflammatory disorders
- metabolic dysfunction
- rare molecular abnormalities
- immune system dysregulation

---

## Example Future AI Extensions

### Classification Models

Future versions of this project could include supervised machine learning models such as:

- Random Forest
- XGBoost
- Support Vector Machines (SVM)
- Neural Networks

These models could classify biological samples into categories such as:

- healthy vs diseased
- control vs spaceflight-exposed
- low-risk vs high-risk molecular profiles

---

## Anomaly Detection

AI anomaly detection models could identify unusual transcriptomic patterns that may represent:

- rare molecular responses
- disease-associated abnormalities
- radiation damage
- immune overactivation
- unknown biological events

Potential methods include:

- Isolation Forest
- Autoencoders
- DBSCAN
- One-Class SVM

---

## Scientific Value

This project demonstrates how bioinformatics, transcriptomics, and artificial intelligence can be integrated to analyze complex biological systems and support future biomedical discovery.

---

## Future Improvements

- Deep learning models for transcriptomics
- Differential gene expression analysis
- Biological pathway enrichment analysis
- Outlier and anomaly detection
- Multi-omics integration
- Interactive dashboards

---

## Future AI Development

Planned future improvements include:

- Deep learning for transcriptomics
- Cancer biomarker prediction
- Gene expression classification
- Autoencoder anomaly detection
- Multi-omics integration
- Explainable AI for bioinformatics

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

Run Jupyter Notebook:

```bash
jupyter notebook
```
---

  
## Author

Agata Gabara

GitHub Repository:
https://github.com/ag48665/nasa-spaceflight-ai

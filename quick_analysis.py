import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs("figures", exist_ok=True)

df = pd.read_csv("GLDS-245_rna_seq_Normalized_Counts_GLbulkRNAseq.csv", nrows=20)

print(df.shape)
print(df.head())

sample_data = df.iloc[:, 1:11].T

plt.figure(figsize=(10, 6))
plt.plot(sample_data)
plt.title("NASA OSD-245 RNA-seq expression profiles")
plt.xlabel("Samples")
plt.ylabel("Normalized expression")
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig("figures/osd245_expression_profiles.png", dpi=300)
plt.show()


mean_expression = df.iloc[:,1:].mean(axis=1)

# top 10 genów
top10 = mean_expression.sort_values(ascending=False).head(10)

plt.figure(figsize=(10,6))
top10.plot(kind="bar")

plt.title("Top 10 highly expressed genes")
plt.ylabel("Mean normalized expression")
plt.tight_layout()

plt.savefig("figures/top10_genes_osd245.png", dpi=300)
plt.show()
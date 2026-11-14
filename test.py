import anndata as ad

files = ["data/tabula_muris/all.h5ad"]

for filename in files:
    adata = ad.read_h5ad(filename)

    print(f"\n{'=' * 60}")
    print(f"File: {filename}")
    print(f"Shape: {adata.shape}")
    print(f"Number of cells: {adata.n_obs:,}")
    print(f"Number of genes: {adata.n_vars:,}")

    print("\nObservation metadata:")
    print(adata.obs.columns.tolist())

    print("\nVariable metadata:")
    print(adata.var.columns.tolist())

    print("\nOther stored information:")
    print("Layers:", list(adata.layers.keys()))
    print("Embeddings:", list(adata.obsm.keys()))
    print("Unstructured metadata:", list(adata.uns.keys()))

    print("\nFirst 5 cell metadata rows:")
    print(adata.obs.head())

    print(adata.obs['celltype'].unique())
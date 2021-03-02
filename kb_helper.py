import anndata
import pandas as pd

adata = anndata.read_loom("./kb_outs/counts_unfiltered/adata.loom")
adata.var["gene_id"] = adata.var.index.values
t2g = pd.read_csv("/cvmfs/soft.galaxy/v2.1/server/tools/single_cell_tools/refs/kb_python/Index/Mouse/t2g.txt", sep = "\t", header = None, names=["tid", "gene_id", "gene_name"])
t2g.index = t2g.gene_id
t2g = t2g.loc[~t2g.index.duplicated(keep='first')]
#adata.var["Accession"] = list(adata.var.index) #added to try to conform with loom validation
adata.var["Gene"] = adata.var.gene_id.map(t2g["gene_name"])
adata.var.index = adata.var["Gene"]
adata.var_names_make_unique()
adata.obs["CellID"] = list(adata.obs.index)
#adata.obs["ClusterID"] = [0] * adata.obs['CellID'].shape[0] #added to try to conform with loom validation
adata.write("./kb_outs/counts_unfiltered/adata.h5ad")

# Validating QTLs using molecular assays
***
This repository contains data inspection, cleaning, exploratory analysis, and integration of eQTL and co-eQTL data with experimental high-throughput datasets, specifically MPRA (Massively Parallel Reporter Assay) and CRISPR-Cas9 interference scRNA-seq screens. <br>
The aim of this work is to address the challenges in identifying potential causal variants for disease risk by combining association studies (eQTL and co-eQTL) with experimental perturbation-based approaches.

## Project descriptions
**eQTL and MPRA Integration** <br>
In this part of the project, we focus on analyzing the relationship between eQTLs and regulatory active DNA regions using MPRA. The aim is to identify whether eQTLs are enriched in regulatory elements and whether these elements are active in the same cell type. This analysis contributes to understanding how genetic variation impacts gene expression through regulatory mechanisms. <br>
**co-eQTL and CRISPRi Integration** <br>
This analysis investigates co-eQTLs and their potential direct regulatory effects on gene expression using CRISPR-Cas9 interference scRNA-seq screens. By leveraging CRISPRi data, we aim to identify regulatory interactions between co-eGenes and their associated eGenes, offering deeper insights into the regulatory mechanisms of gene expression. <br>


## Notebooks & scripts
**MPRA notebooks** <br>
Notebooks for preprocessing, statistical analysis, enrichment testing, and integration of MPRA data with eQTLs. <br>
Main analysis notebooks: <br>
- sc_eqtls_data_preparation.ipynb <br>
- mpra_plasmid_kurtis_grch_buildconversion.ipynb <br>
- lcl_mpra_inspection_conversion_analysis.ipynb <br>
- enrichment_scores_mpra_new.ipynb <br>

Process data inspection, prepartion & analysis MPRA datasets: <br>
- plasmid_coverage_kurtis.ipynb <br>
- data_inspection_kurtis.ipynb <br>
- data_inspection_tewhey_lcl_mpra.ipynb <br>
- starr_mpra_plasmid_kurtis.ipynb <br><br>

**CRISPRi notebooks** <br>
Notebooks for preprocessing, analysis, and integration of CRISPRi data with co-eQTLs. <br>
Main analysis notebook and script: <br>
- annotate_egene_coegene.py
- assign_crispr_score_to_coeqtls.ipynb <br><br>
Process data inspection, prepartion & analysis co-eqtl and cripsr datasets: <br>
- crispr_gene_coexpression_analysis.ipynb <br>
- gasperini_crispr_analyse.ipynb <br> <br>
Library versions needed to run the notebook are in library_packages.txt

## License:
Distributed under MIT license. See the file LICENSE for more information.

## Contact Information:
For questions feel free to reach out to me at a.h.van.den.broek@st.hanze.nl or anna.vandenbroek@hotmail.com .


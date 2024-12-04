"""
Script for correctly annotating egene and co-egene of co-eqtls
Needed a reference file with snp and annotated egene &
co-eqtl data containing feature_id with gene_gene annotation

"""
import time
import pandas as pd

def filter(ref, file):
    file['co_gene'] = [0 for i in range(len(file['snp_id']))]
    file['egene'] = [0 for i in range(len(file['snp_id']))]
    for i in range(len(file['snp_id'])):
        print(round(i/len(file['snp_id']),3),end='\r')
        temp = ref[ref['snp']==file['snp_id'].iloc[i]]
        if len(temp['gene']) == 1:
            file['egene'].iloc[i] = temp['gene'].iloc[0]
        elif len(temp['gene']) > 1:
            geneA, geneB = file['feature_id'].iloc[i].split('_')
            if geneA in temp['gene'].values:
                file['egene'].iloc[i] = geneA
                file['co_gene'].iloc[i] = geneB
            elif geneB in temp['gene'].values:
                file['egene'].iloc[i] = geneB
                file['co_gene'].iloc[i] = geneA

def filter_egene(file, ref):
    file=file.sort_values(by='snp_id')
    snp_id = [i for i in file['snp_id']]
    now=time.time()
    checkpoint = 0
    temp_snp = 0
    egenes = []
    for i in range(len(snp_id)):
        if time.time()-now > 1:
            now = time.time()
            print(i,end='\r')
        if snp_id[i] != temp_snp:
            checkpoint = 0
            temp_snp = snp_id[i]
        if checkpoint ==2:
            geneA,geneB=file.iloc[i]['feature_id'].split('_')
            if geneA in temp_gene.values:
                gene = geneA
            elif geneB in temp_gene.values:
                gene = geneB
            else:
                'something is wrong'
                break
        if checkpoint == 0:
            temp_gene = ref[ref['snp']==snp_id[i]]['gene']
            if len(temp_gene) == 1:
                checkpoint = 1
                gene = temp_gene.iloc[0]
            else:
                checkpoint = 2
                geneA,geneB=file.iloc[i]['feature_id'].split('_')
                if geneA in temp_gene.values:
                    gene = geneA
                elif geneB in temp_gene.values:
                    gene = geneB
                else:
                    'something is wrong'
                    break
        egenes.append(gene)


    file['egene'] = egenes

    coegene = []
    gene_pair = [i for i in file['feature_id']]
    egene = [i for i in file['egene']]
    for i in range(len(gene_pair)):
        if time.time()-now > 1:
            now = time.time()
            print(i,end='\r')
        geneA,geneB = gene_pair[i].split('_')
        if geneA == egene[i]:
            coegene.append(geneB)
        else:
            coegene.append(geneA)
    file['coegene'] = coegene
    print(file.head())
    return file

if __name__ == '__main__':
    ref=pd.read_csv('gene_snp_ref.tsv',sep='\t')
    file=pd.read_csv('filtered_coeqtl_results_CD4T.tsv.gz',sep='\t')


    file1 =filter_egene(file, ref)
    file1.to_csv('egene_coegene_filtered_CD4T.tsv', sep='\t', index=False)
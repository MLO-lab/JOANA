from joanapy.enrichment_obj import ENRICHMENT_OBJ
from joanapy.joana import JOANA
import os


#varPath='Original/single/prot'
#varPath='kegg/data'
varPath='prot'
#£varPath='GO'
typeInput='qval'

#path='/home/samerifar/joana/lungTumData/papil_solid/'+varPath
#path='/home/samerifar/joana/lymphoma/Julius/R_ABC_GCB/'+varPath
path='/home/samerifar/joana/lymphoma/Julius/Original/single/'+varPath
#path='/home/samerifar/joana/lymphoma/Julius/Original2/'+varPath


filename_output_single_species = path+'/results/singleResult'+typeInput+'.csv'
filename_output_cooperative = path+'/results/coopResult'+typeInput+'.csv'
filename_assignment_matrix = path+'/assignmentmatrixProt.txt'
filename_terms = path+'/terms.txt'
filename_qvalues_first= path+'/Trimmed'+typeInput+'Prot.txt'
filename_qvalues_second = path+'/Trimmed'+typeInput+'Prot.txt'
filename_missing_first = path+'/TrimmedmissingRNA.txt'
filename_missing_second = path+'/TrimmedmissingProt.txt'

"""
filename_output_single_species = '/home/samerifar/joana/HGU_133/CNS_vs_COLON/results/singleResultpval.csv'
filename_output_cooperative = '/home/samerifar/joana/HGU_133/CNS_vs_COLON/results/coopResultpval.csv'
filename_assignment_matrix = '/home/samerifar/joana/HGU_133/CNS_vs_COLON/data/assignmentMatrix.txt'
filename_terms = '/home/samerifar/joana/HGU_133/CNS_vs_COLON/data/terms.txt'
filename_qvalues_first= '/home/samerifar/joana/HGU_133/CNS_vs_COLON/data/pvalues_rna_1.txt'
#filename_qvalues_first = '/home/samerifar/joana/lungTumData/papil_solid/kegg/data/TrimmedpvalProt.txt'
filename_missing_first = '/home/samerifar/joana/lungTumData/papil_solid/GO/data/TrimmedmissingRNA.txt'
#filename_missing_first = '/home/samerifar/joana/lungTumData/papil_solid/kegg/data/TrimmedmissingProt.txt'
"""

min_term_size = 1
max_term_size = 300000
prior_pA = 1
goodness_of_fit = True
plot_components = True
signif_threshold=0.1
quantile=0.95

# run single species model
#"""
enrichment_obj_single_species = ENRICHMENT_OBJ(filename_assignment_matrix, filename_terms, filename_qvalues_first)
joana_single_species = JOANA(enrichment_obj_single_species)
joana_single_species.run(filename_output_single_species, goodness_of_fit=goodness_of_fit, plot_components=plot_components, prior_pA=prior_pA, min_term_size=min_term_size, max_term_size=max_term_size)
joana_single_species.plot_hidden_significant_genes(os.path.dirname(filename_output_single_species), signif_threshold=signif_threshold, quantile=quantile)

print(enrichment_obj_single_species.joana_output.sort_values(by='Single-Species', ascending=False).head())
#joana_single_species.plot(filename_output_single_species.replace('.csv', '.pdf'))



"""
# run cooperative model

enrichment_obj_cooperative = ENRICHMENT_OBJ(filename_assignment_matrix, filename_terms,

                                            filename_qvalues_first,
                                            filename_qvalues_second=filename_qvalues_second,
                                            filename_missing_first=filename_missing_first,
                                            filename_missing_second=filename_missing_second)
joana_cooperative = JOANA(enrichment_obj_cooperative)
joana_cooperative.run(filename_output_cooperative, goodness_of_fit=goodness_of_fit, plot_components=plot_components, prior_pA=prior_pA, min_term_size=min_term_size, max_term_size=max_term_size)
joana_cooperative.plot_hidden_significant_genes(os.path.dirname(filename_output_cooperative), signif_threshold=signif_threshold, quantile=quantile)

#joana_single_species.plot(filename_output_cooperative.replace('.csv', '.pdf'))
joana_cooperative.plot(filename_output_cooperative.replace('.csv', '.pdf'))

print(enrichment_obj_cooperative.joana_output.sort_values(by='Cooperative', ascending=False).head())

"""

# load objects
enrichment_obj_single_species_reloaded = ENRICHMENT_OBJ.load(filename_output_single_species.replace('.csv', '.pickle'))
joana_single_species_plotting = JOANA(enrichment_obj_single_species_reloaded)
joana_single_species_plotting.plot(filename_output_single_species.replace('.csv', '1.pdf'))
joana_single_species_plotting.plot_barplot(filename_output_single_species.replace('.csv', '_barplot.pdf'))
"""
enrichment_obj_cooperative_reloaded = ENRICHMENT_OBJ.load(filename_output_cooperative.replace('.csv', '.pickle'))

joana_cooperative_plotting = JOANA(enrichment_obj_cooperative_reloaded)
joana_cooperative_plotting.plot(filename_output_cooperative.replace('.csv', '.pdf'), top_percentile_edges=0.9, n_top_terms=10)
joana_cooperative_plotting.plot_barplot(filename_output_cooperative.replace('.csv', '_barplot.pdf'))
#"""
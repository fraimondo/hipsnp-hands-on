"""
Obtain risk scores and alleles
==============================

This example uses a mock dataset file with genotic information hosted in GIN.
The alleles and risk scores will be extracted from the BGEN files

"""

from tempfile import mkdtemp
import shutil
from hipsnp.hipsnp import genotype_from_datalad
from hipsnp.utils import configure_logging
import numpy as np
import os

###############################################################################
# Set the logging level to info to see extra information
configure_logging(level='INFO')

###############################################################################
# Get a temporary directory to work. Use another directory if you want to
# keep the data.
workdir = mkdtemp()

###############################################################################
# localion of the datalad dataset
source = 'https://gin.g-node.org/juaml/datalad-example-bgen'

os.environ['QCTOOL_PATH'] = '/home/oportoles/Apps/qctool_v2.0.6-Ubuntu16.04-x86_64/qctool'

###############################################################################
# list of the rsids (with thier corresponding chromosome numbers) that we want
# to analyse. If the machine is connected to internet, the chromosomes do not
# need to be spcified. Due to the nature of the mock dataset, here we need the 
# chromosome number
rsids_of_interest = ['RSID_3', 'RSID_5', 'RSID_6', 'RSID_8']
chromosomes = ['1'] * len(rsids_of_interest)

###############################################################################
# Get the gneotype
genotype = genotype_from_datalad(
    rsids=rsids_of_interest, chromosomes=chromosomes,
    datalad_source=source, workdir=workdir, datadir=workdir)

###############################################################################
# Visualize the information available in the gennotype for a given RSID

genotype.metadata.loc['RSID_5']

print(f'Number of samples in RSID_5: \
       {len(genotype.probabilities["RSID_5"][0])} ')

print((f'Allele probabilities for the first 3 samples of RSID_5\
        \nREFREF, ALTREF, ALTALT\
        \n{np.round(genotype.probabilities["RSID_5"][1][:3,:], 3)} '))


###############################################################################
# Now we are ready to obtain the alleles of each rsid and sample in the data. 
# Here we will compute the allele of only one RSID
gen_allele, gen_012 = genotype.alleles(rsids='RSID_5')

###############################################################################
# Visualize the information of the computed alleles

print(f'alleles of the first 3 samples:\n {gen_allele.iloc[0,:3]}')

print(f'most probale allele combination in the first 3 samples:\n \
      \n0:REFREF, 1:ALTREF, 2:ALTALT\
      \n{gen_012.iloc[0,:3]}')


##############################################################################
# To compute a poligenetic risk score we need a file or a pandas dataframe with
# the weights associated to each allele and RSID. We can retrieve one from
# https://www.pgscatalog.org/.

# In this case we use a weights file generated for this mock datasets.
path_to_weights = './data/weights_all.csv'

##############################################################################
# For this example will obtain the risk scores of two groups of subjects presnt 
# in the genotype

samples_of_interest_A = ['sample_001', 'sample_002', 'sample_003', 'sample_004']
samples_of_interest_B = ['sample_011', 'sample_012', 'sample_013', 'sample_014']

# Now we can obtain the risk score and the dosage (amount of the effect allele) 
# for each rsids given the samples on the groups A and B

dosage_A, risk_A = genotype.riskscores(weights=path_to_weights,
                                       samples=samples_of_interest_A)

dosage_B, risk_B = genotype.riskscores(weights=path_to_weights,
                                       samples=samples_of_interest_B)

###############################################################################
# Visualize the dosage in groupe A
print(f'Dosages in group A: \n {dosage_A}')

###############################################################################
# difference on risk score between groups
print(f'average risk scores\n\
        Group A: {np.round(np.mean(risk_A), 3)}\n\
        Group B: {np.round(np.mean(risk_B), 3)}')


###############################################################################
# Since we used a temporary directory, we need to delete it
shutil.rmtree(workdir)

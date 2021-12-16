# https://www.snpedia.com/index.php/APOE
from hipsnp import genotype_from_datalad
from hipsnp.utils import configure_logging

configure_logging(level='INFO')

rsids = ['rs429358', 'rs7412']

workdir = '/data/project/ukb_rls/tmp/genetic'

# Get the genotype, might take some time to clone the datalad dataset
genotype = genotype_from_datalad(
    rsids=rsids, workdir=workdir, datadir=workdir)


# Get the alleles
gen_allele, gen_012 = genotype.alleles(rsids=rsids)

# Convert columns (samples) to rows.
gen_allele = gen_allele.transpose()

# Remove the samples with negative values
good_samples = [x for x in gen_allele.index if not x.startswith('-')]
gen_allele = gen_allele.loc[good_samples]

# Count the pairs
print(gen_allele.reset_index().groupby(rsids).count())

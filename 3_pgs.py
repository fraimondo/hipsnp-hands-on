from hipsnp import genotype_from_datalad, read_weights
from hipsnp.utils import configure_logging

configure_logging(level='INFO')

weights = read_weights('data/PGS000034.txt')

rsids = weights.index.tolist()

workdir = '/data/project/ukb_rls/tmp/genetic'

# Get the genotype, might take some time to clone the datalad dataset
genotype = genotype_from_datalad(
    rsids=rsids, workdir=workdir, datadir=workdir)

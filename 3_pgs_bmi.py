from hipsnp import genotype_from_datalad, read_weights
from hipsnp.utils import configure_logging

configure_logging(level='INFO')

weights = read_weights('data/PGS000034.txt')

rsids = weights.index.tolist()
chromosomes = weights['chr'].tolist()

# Where the datalad dataset is/will be
datadir = '/data/project/deleted_every_sunday/hipsnphandson/datalad'

# Where the intermediate files / results are/will be
workdir = '/data/project/deleted_every_sunday/hipsnphandson/workdir_bmi'

# Get the genotype, might take some time to clone the datalad dataset
genotype = genotype_from_datalad(
    rsids=rsids, chromosomes=chromosomes, workdir=workdir, datadir=datadir,
    datalad_drop=False)

dosage, riskscores = genotype.riskscores(weights=weights)
riskscores.to_csv(
    '/data/project/deleted_every_sunday/hipsnphandson/test-bmi.csv',
    sep=';')

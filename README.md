# hipsnp-hands-on

## Requriements

* anaconda or minconda
* account in juseless
* access to the UKBB data

## Preparing

1. Create a conda environment with Python 3.8 and activate it

```
conda create -n ukbsnp python=3.8
conda activate ukbsnp
```

2. Install the following packages

```
conda install ipython flake8
conda install -c conda-forge seaborn datalad bgen-reader
```

3. Check that you have the right datalad:

```
which datalad
```

Should output datalad in the path of the conda environment:

```
/Users/fraimondo/anaconda3/envs/ukbsnp/bin/datalad
```

4. Install _QCTOOL_, required for `hipsnp` (check https://www.well.ox.ac.uk/~gav/qctool/documentation/download.html)

```
wget https://www.well.ox.ac.uk/~gav/resources/qctool_v2.2.0-CentOS_Linux7.8.2003-x86_64.tgz
tar -xvzf qctool_v2.2.0-CentOS_Linux7.8.2003-x86_64.tgz
TODO: Continue
```

5. Install `hipsnp` and `ukbb_parser`:

```
pip install hipsnp
pip install https://github.com/kaurao/ukbb_parser.git
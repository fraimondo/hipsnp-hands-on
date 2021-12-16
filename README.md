# hipsnp-hands-on

## Requriements

* anaconda or minconda
* account in juseless
* access to the UKBB data

## Preparing

### 1. Create a conda environment with Python 3.8 and activate it

```
conda create -n ukbsnp python=3.8
conda activate ukbsnp
```

### 2. Install the following packages

```
conda install ipython flake8
conda install -c conda-forge seaborn datalad bgen-reader
```

### 3. Check that you have the right datalad:

```
which datalad
```

Should output datalad in the path of the conda environment:

```
/home/fraimondo/anaconda3/envs/ukbsnp/bin/datalad
```

### 4. Install _QCTOOL_, required for `hipsnp` (check https://www.well.ox.ac.uk/~gav/qctool/documentation/download.html)

#### 4.1. Download and extract _QCTOOL_

```
wget https://www.well.ox.ac.uk/~gav/resources/qctool_v2.2.0-CentOS_Linux7.8.2003-x86_64.tgz
tar -xvzf qctool_v2.2.0-CentOS_Linux7.8.2003-x86_64.tgz
```

#### 4.2 Install _QCTOOL_

Option A) Install in the environment:

A.1 Check where your environment path is:

```
conda info --envs | grep ukbsnp | awk -F '  +' '{print $3}'
```

Output should be something like this:

```
/home/fraimondo/anaconda3/envs/ukbsnp
```

A.2 Copy `qctool` to the `bin` directory inside the environment path

```
cp qctool_v2.2.0-CentOS\ Linux7.8.2003-x86_64/qctool /home/fraimondo/anaconda3/envs/ukbsnp/bin/
```

#### 4.3 Test the command:

```
qctool
```

Output should be something like this:

```
!! Error (OptionProcessingException): Option "-g" must be supplied..
!! Run qctool -help for usage information.
```


5. Install `hipsnp` and `ukbb_parser`:

```
pip install hipsnp
pip install https://github.com/kaurao/ukbb_parser.git
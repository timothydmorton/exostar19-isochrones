# Stellar property analysis with **isochrones**

Make sure you are running latest master branch of **isochrones**.  Then, run

    python write_ini.py

This will generate all the directories and `star.ini` files for all stars in the
`k2_input_isochrones.csv` data table into the `results/isochrones` directory of this repo.
For each of these directories, you can run

    starfit EPICxxxxxxxxx

and that will fit a single-star model.  To fit a binary star model, run

    starfit --binary EPICxxxxxxxxx


## Running batch on slurm

If you are on an slurm-queued HPC system and want to run all of them as a job array, you can use my
handy `batch-serial` tool if you wish:

    git clone https://github.com/timothydmorton/batch-serial
    cd batch-serial
    python setup.py install

Then, go back to the `results/isochrones` directory, and do the following:

    ls -d EPIC* > all.list
    batch-serial -n 200 -t 15 all.list starfit   # runs with a job array of 200

And if you want to run binaries, do (e.g.):

    batch-serial -n 200 -t 60 all.list starfit --binary


## Creating results table

To make a summary table of results (single and binary), run:

    starfit-summarize -f all.list -p 12 -o single_summary.h5  # -p is number of processes to use
    starfit-summarize -f all.list -p 12 -o binary_summary.h5  --modelname mist_starmodel_binary

## Loading results

```python
import pandas as pd
df = pd.read_hdf('single_summary.h5')
```




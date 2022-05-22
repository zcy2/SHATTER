

# SHATTER: Searching Heterogeneous Network Attack Sequences Through Network Embedding and Reinforcement Learning

This repository is the official implementation of [SHATTER: Searching Heterogeneous Network Attack Sequences Through Network Embedding and Reinforcement Learning](). 

## Dataset
The heterogeneous network training dataset, test dataset, and validation dataset can be found on URL: https://github.com/zcy2/SHATTER
## Training

To train the SHATTER in the paper, run this command:

```train
python train.py
python train_cost.py
```

>📋  Running train.py is to train the SHATTER model without considering the cost. Run train_cost.py for SHATTER model training with cost.

## Evaluation

To evaluate SHATTER on network_scalefree_60-90, run:

```eval
python eval.py 
python eval_cost.py
```

>📋  Run eval.py to test the SHATTER model without cost on the test data set network_scalefree_60-90. Running eval_cost.py is to run the SHATTER model with cost considered on the test data set network_scalefree_60-90_cost.

## Pre-trained Models

You can download pretrained models here:

- My awesome model(./models_sage2) trained on SHATTER without considering the cost.
- My awesome model(./models_sage_cost) trained on SHATTER considering the cost.

>📋  BATCH_SIZE = 32,LR=0.0001, EPSILON = 0.9 # greedy policy, GAMMA = 0.99 # reward discount, TARGET_REPLACE_ITER = 1000   # target update frequency, MEMORY_CAPACITY = 50000
## Results

- Run Convergence curve.py to get the convergence curve of SHATTER on the test set.
- HDSA_OODA.py, HDDA_OODA.py, HDIA_OODA.py, HDA_OODA.py, HPA_OODA.py, FINDER_OODA.py, and SHATTER_OODA.py are the validation of SHATTER and its baseline algorithm on multiple validation sets without considering the cost, respectively.
- HDSA_OODA_cost.py, HDDA_OODA_cost.py, HDIA_OODA_cost.py, HDA_OODA_cost.py, HPA_OODA_cost.py, FINDER_OODA_cost.py, and SHATTER_OODA_cost.py respectively are the validation of SHATTER and its baseline algorithm on multiple validation sets considering the cost case.
- data_cat.py and data_cat_cost.py are the data processing of the validation results on the validation set considering the cost or not, respectively, running Algorithm Comparison_boxplot.py and Algorithm Comparison_boxplot_cost.py box plots showing results.
- The data for all algorithm comparisons and the generated plots can be found in the folder [save]().
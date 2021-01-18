'''
kfoldを想定して試してみる
'''

import wandb
import numpy as np

config = {
        'model': {
            'name': 'model1',
            'params': 2},
        'loss': {
            'name': 'bce'}
        }

wandb.init(
        project='sandpit_028_kfold',
        name='01'
        )
wandb.config = config

for i_fold in range(5):
    for epoch in range(10):
        loss = np.exp(-epoch)
        wandb.log({'epoch': epoch, 'loss': loss})

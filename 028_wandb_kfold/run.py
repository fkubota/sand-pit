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


# wandb.config.all_config = config
# wandb.config.debug = True
for i_fold in range(5):
    run = wandb.init(project='sandpit_028_kfold',
                     group='exp01',
                     name=f'fold{i_fold}')
    run.config.dropout = 0.2
    run.config.debug = True
    for epoch in range(50):
        loss = np.exp(-0.1*epoch) + np.random.randint(-500, 500)/5000
        wandb.log({'epoch': epoch, 'loss': loss})
    run.finish()

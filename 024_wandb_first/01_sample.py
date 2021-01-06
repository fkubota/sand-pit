```
このサイトわかりやすい
https://github.com/MLHPC/wandb_tutorial
```

import wandb
import numpy as np

wandb.init(
        project='sandpit_024_01',
        name='01_sample.py',
        )
print('wandb start')

wandb.config.dropout = 0.2
wandb.config.hidden_layer_size = 128

for epoch in range(10):
    loss = np.exp(-epoch)  # change as appropriate :)
    wandb.log({'epoch': epoch, 'loss': loss})

print('wnadb end')

# Copyright (c) OpenMMLab. All rights reserved.
import random
import warnings

import numpy as np
import torch
# from mmcv.parallel import MMDataParallel, MMDistributedDataParallel
# from mmcv.runner import HOOKS, build_optimizer, build_runner
# from mmcv.utils import build_from_cfg
#
# from mmseg.core import DistEvalHook, EvalHook
# from mmseg.datasets import build_dataloader, build_dataset
# from mmseg.utils import get_root_logger


def set_random_seed(seed, deterministic=False):
    """Set random seed.

    Args:
        seed (int): Seed to be used.
        deterministic (bool): Whether to set the deterministic option for
            CUDNN backend, i.e., set `torch.backends.cudnn.deterministic`
            to True and `torch.backends.cudnn.benchmark` to False.
            Default: False.
    """
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    if deterministic:
        torch.backends.cudnn.deterministic = True
        torch.backends.cudnn.benchmark = False



import torch
import numpy as np

def describe(x) :
    print(f"type={x.type()}, shape={x.shape}, value=\n{x}")

# 생성
describe(torch.Tensor(2, 3))
describe(torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.int64))
describe(torch.rand(2, 3))
describe(torch.randn(2, 3))
describe(torch.zeros(2, 3))
describe(torch.ones(2, 3))
describe(torch.ones(2, 3).fill_(5))
describe(torch.from_numpy(np.random.rand(2, 3)))
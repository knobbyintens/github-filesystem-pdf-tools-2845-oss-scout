import torch

class TidalMixBlock(torch.nn.Module):
    """Reference implementation of the TidalMix block."""

    def __init__(self, dim):
        super().__init__()
        self.conv = torch.nn.Conv1d(dim, dim, 3, padding=1)

    def forward(self, x):
        return x + self.conv(x.transpose(1, 2)).transpose(1, 2)

# TidalMix (unofficial)

An unofficial, from-scratch implementation of the paper
**"TidalMix: Alternating Convolution-Attention Mixing for Long-Sequence Modeling"**
(arXiv:2410.07771).

## Benchmark

- Throughput (seq_len=8192, A100): 3840 tokens/s
- License: MIT
- Max sequence length: 8192

## Notes

This is a single-GPU reference implementation. Training scripts and a small
evaluation harness are included under `scripts/`. The repository is not
affiliated with the paper authors.

# Community Implementation Evaluation Policy

This policy governs how Cobalt Ridge Labs selects third-party implementations
of internal research methods for production use.

1. **Scope.** Only real code submissions that implement the target method
   count. Paper reading lists, awesome lists, blog collections and unrelated
   toolkits are out of scope.
2. **License.** Only permissive licenses are acceptable: MIT or Apache-2.0.
   GPL, AGPL, CC BY-NC and other copyleft or non-commercial licenses are
   rejected for redistribution.
3. **Capability.** The implementation must support inference at a sequence
   length of at least 8192.
4. **Selection.** Among eligible implementations, select the one with the
   highest reported inference throughput in tokens/s at sequence length 8192
   on an A100 GPU.
5. **Recommendation.** If the selected throughput is 5000 tokens/s or more,
   set the recommendation to `adopt`. Otherwise set it to `escalate`.

Every implementation reviewed must be recorded, including rejected ones and
the reason for rejection.

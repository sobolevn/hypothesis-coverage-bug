# hypothesis bug with entrypoints

## Points of interest

1. Entrypoint for `hypothesis` we define: https://github.com/sobolevn/hypothesis-coverage-bug/blob/master/setup.py#L8
2. Our coverage settings: https://github.com/sobolevn/hypothesis-coverage-bug/blob/master/setup.cfg
3. Our tests: https://github.com/sobolevn/hypothesis-coverage-bug/blob/master/tests/test_my_type.py
4. Output demo: https://github.com/sobolevn/hypothesis-coverage-bug/runs/1104300186

It should ideally have `100%` coverage. But it has `0%` instead.
Try to comment everything inside `to_cover/entrypoint.py`.
It show the correct coverage, but one of the logical tests will fail.

## Full reproduction

Follow these steps: https://github.com/sobolevn/hypothesis-coverage-bug/blob/master/.github/workflows/test.yml

## Links

- https://github.com/HypothesisWorks/hypothesis/pull/2567
- https://github.com/dry-python/returns/issues/594

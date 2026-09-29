# dsa

My DSA problems. The tooling lives in [dsa-kit](https://github.com/ahrazarfi/dsa-kit);
this repo holds only the problems.

## Use it on a new machine

```
curl -LsSf https://raw.githubusercontent.com/ahrazarfi/dsa-kit/main/install.sh | sh
#   Windows: irm https://raw.githubusercontent.com/ahrazarfi/dsa-kit/main/install.ps1 | iex
git clone git@github.com:ahrazarfi/dsa.git && cd dsa/PROBLEMS/Arrays
new two-sum            # scaffold a problem here
dsa check ..           # re-run every problem that has an expected.txt
```

Each problem is a folder with `solution.py`, `input.txt`, `expected.txt` and `output.txt`
(the last one is git-ignored). See the dsa-kit README for the file formats and `run()` options.

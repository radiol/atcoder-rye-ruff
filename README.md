# atcoder-rye-ruff

AtCoder environment by Rye + Ruff

## Install Rye

https://rye-up.com/

```bash
curl -sSf https://rye-up.com/get | bash
```

### Install Libraries

Run in the atcoder-rye-ruff directory

```bash
rye sync
```

## Install AtCoder-CLI

https://github.com/Tatamo/atcoder-cli

```bash
npm install -g atcoder-cli
```

## Login AtCoder-CLI

```bash
acc login
```

## Login Online-Judge-Tools

Activate virtual environment

```bash
sourve .venv/bin/activate
```

Login

```bash
oj login https://atcoder.jp/
```

## Copy templates

Copy atcoder-cli-templates to acc config-dir.
Check acc config-dir

```bash
cp -r atcoder-cli-templates/py `acc config-dir`
```

### Edit acc-config

```bash
nvim `acc config-dir`/config.json
-> default-template:"py"
```

# Usage

## Create new directory

```bash
acc new abc001
```

## Check test case

```bash
rye run oj t -c 'python3 main.py' -d ./tests/
```

## Check test case after Format and Lint.

```bash
rye run black main.py && rye run ruff --fix main.py && rye run oj t -c 'python3 main.py' -d ./tests/
```

## Submit

PyPy

```bash
acc s main.py -- --guess-python-interpreter pypy
```

Python

```bash
acc s main.py -- -l 5055
```

## Run code

```bash
rye run python main.py
```

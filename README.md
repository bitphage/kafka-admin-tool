# kafka-admin-tool

Cli tool to automate some kafka admin actions.

Installation via poetry
-----------------------

1. Make sure you have installed required packages: `apt-get install gcc make libssl-dev`
2. Install [poetry](https://python-poetry.org/docs/)
3. Run `poetry install` to install the dependencies
4. Copy `config.yml.example` to `config.yml` and change variables according to your needs
5. Now you're ready to run scripts:


```
poetry shell
./admin.py
```

Running tests
-------------

Use `pytest -v tests/`.

Testsuite is run against real kafka cluster launched in docker automatically.

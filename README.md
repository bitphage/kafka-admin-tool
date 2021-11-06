# kafka-admin-tool

Cli tool to automate some kafka admin actions.

Features
--------

Rationale to have such a tool is that current cli tools like `kafka-topics.sh` are too poor in terms of accessing only subset of topics. For example, you just cannot delete some topics matching a substring.

Currently, the tool support just a small number of commands:

```
% ./admin.py --help
Usage: admin.py [OPTIONS] COMMAND [ARGS]...

Options:
  -d, --debug            enable debug output
  -c, --config FILENAME  specify custom path for config file
  --help                 Show this message and exit.

Commands:
  alter-topic-config     Alter topic config.
  delete-topics          Delete all topics starting with prefix.
  describe-topic         Describe a TOPIC.
  describe-topic-config  Show topic config.
  describe-topics        Describe multiple topics using prefix.
  generate-topics-move   Generates topics-to-move.json file for later use...
  list-topics            Display topics, all or matched a prefix.
```

Example usages
--------------

List topics matching a substring:
```
% ./admin.py list-topics --prefix foo
['foo-1',
 'foo-2',
 'foo-3'
]
```

Alter retention for multiple topics:

```
./admin.py --config config-amazon3.yml alter-topics --prefix prod-demo retention.ms 86400001
```


Installation via poetry
-----------------------

1. Install [poetry](https://python-poetry.org/docs/)
1. Run `poetry install` to install the dependencies
1. Copy `config.yml.example` to `config.yml` and change variables according to your needs
1. Now you're ready to run scripts:


```
poetry shell
./admin.py
```

Running tests
-------------

Use `pytest -v tests/`.

Testsuite is run against real kafka cluster launched in docker automatically.

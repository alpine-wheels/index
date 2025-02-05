> [!CAUTION]
> The [alpine-wheels organization](https://github.com/alpine-wheels/) is currently unmaintained.

# alpine-wheels/index

This is a [PEP 503][a]-compliant Python package index specifically providing wheels built for Alpine Linux.

[a]: https://www.python.org/dev/peps/pep-0503/

If you want to use [`python:alpine` Docker containers][b] but you don&#x02bc;t want to build Python packages yourself, you may find this index useful.

[b]: https://hub.docker.com/_/python

## Usage examples

### Pip

```shell
$ pip install --extra-index-url https://alpine-wheels.github.io/index pandas
```

### Pip with a requirements file

```shell
# contents of requirements.txt

--extra-index-url https://alpine-wheels.github.io/index

pandas
```

```shell
$ pip install -r requirements.txt
```
### pip-tools

```shell
# add this to the top of requirements.in

--extra-index-url https://alpine-wheels.github.io/index
```

```shell
$ pip-compile
```

### Poetry

```toml
# add this section to pyproject.toml

[[tool.poetry.source]]
name = "alpine-wheels"
url = "https://alpine-wheels.github.io/index"
```

```shell
$ poetry add pandas
```

### Pipenv

```toml
# add this section to Pipfile

[[source]]
name = "alpine-wheels"
url = "https://alpine-wheels.github.io/index"
verify_ssl = true
```

```shell
$ pipenv install pandas
```

## Tools that require `/simple`

Some tools require a simple index URL to end with `/simple`. For this case, the index content is also available at
`https://alpine-wheels.github.io/index/-/simple`.

*   Sonatype Nexus [1][s1] [2][s2]

[s1]: https://community.sonatype.com/t/how-would-i-create-a-proxy-for-a-pypi-that-uses-simple-instead-of-simple/7378/2
[s2]: https://issues.sonatype.org/browse/NEXUS-29223

## Contributing

Is there a package you need that is missing from the index? [Open an issue][c] to suggest it. We only support packages that are available on [PyPI][d] but do not already have a wheel that is compatible with Alpine Linux.

To add a new package, do *not* fork this repository directly; make a new repository for the individual package using https://github.com/alpine-wheels/_template.

[c]: https://github.com/alpine-wheels/index/issues/new/choose
[d]: https://pypi.org/

# alpine-wheels/index

This is a [PEP 503][a]-compliant Python package index specifically providing wheels built for Alpine Linux.

[a]: https://www.python.org/dev/peps/pep-0503/

If you want to use [`python:alpine` Docker containers][b] but you don&#x02bc;t want to build Python packages yourself, you may find this index useful.

[b]: https://hub.docker.com/_/python

## Usage

To search this index, add one line at the top of your `requirements.txt` file:

    --extra-index-url https://alpine-wheels.github.io/index

## Contributing

Is there a package you need that is missing from the index? [Open an issue][c] to request it.

[c]: https://github.com/alpine-wheels/index/issues/new/choose

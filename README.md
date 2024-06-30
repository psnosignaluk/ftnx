<p align="center">
  <a href="https://github.com/psnosignaluk/ftnx">
    <img width="350" src="https://raw.githubusercontent.com/psnosignaluk/ftnx/main/docs/img/FTNX.png" alt="FTNX" />
  </a>
</p>
<p align="center"><em>A next gen Fortanix DSM client and library</em></p>

FTNX will be a fully featured client for interfacing with Fortanix DSM via Python 3. It includes
an **integrated command line client** that can be used to create, modify and delete groups and
security objects, test security object policies and manage users. The library can be used to
integrate `ftnx` into your own projects,

---

Install FTNX using pip:
```shell
pip install ftnx
```

To use `ftnx`:

```pycon
>>> import ftnx
```

Alternatively, to use the command-line tool:

```shell
pip install 'ftnx[cli]'
```

## Features

A list of things `ftnx` is capable of.

## Installation

Install the library using pip:
```shell
pip install ftnx
```

To include the optional command-line client:
```shell
pip install 'ftnx[cli]'
```

`ftnx` requires Python 3.8+.

## Dependencies

`ftnx` relies on the following excellent tools:

* `httpx`: A fully featured HTTP client library for Python 3, and the library that inspired the layout of this one.

---

<p align="center"><i>FTNX is <a href="https://github.com/psnosignaluk/blob/main/LICENSE.md">BSD licensed</a></i></p>
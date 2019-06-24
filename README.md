<h1 align="center">Welcome to LightshotSniffer 👋</h1>
<p>
  <a href="#">
    <img alt="GitHub tag (latest SemVer)" src="https://img.shields.io/github/tag/Airthee/LightshotSniffer.svg?label=version">
  </a>
  <a href="http://www.wtfpl.net/" target="_blank">
    <img alt="GitHub" src="https://img.shields.io/github/license/Airthee/LightshotSniffer.svg">
  </a>
  <a href="https://travis-ci.org/Airthee/LightshotSniffer" target="_blank">
    <img alt="Travis CI" src="https://travis-ci.org/Airthee/LightshotSniffer.svg?branch=master" target="_blank">
  </a>
  <a href='https://coveralls.io/github/Airthee/LightshotSniffer?branch=master' target="_blank">
    <img src='https://coveralls.io/repos/github/Airthee/LightshotSniffer/badge.svg?branch=master' alt='Coverage Status' />
  </a>
  <a href="https://twitter.com/Airthee" target="_blank">
    <img alt="Twitter: Airthee" src="https://img.shields.io/twitter/follow/Airthee.svg?style=social" target="_blank" />
  </a>
</p>

> Project that scan LightShot to find interesting images

### 🏠 [Homepage](https://github.com/Airthee/LightshotSniffer)

## Description

### Usage

1. At the lauch, user has to select download directory.
2. User can choose a start id and end id, by default, it starts from ZZZZZZ to 00000.
3. For each image, user tape "S" to save, "N" for next, "P" for previous.


## Install
This project use python3.6. You may want to create a virtualenv :
```sh
virtualenv -p python3.6 env
source env/bin/activate
```
and then install the requierements.

```sh
pip install -r requirements.txt
```

If you want some docs about virtualenv, go check their [website](https://pypi.org/project/virtualenv/). 

## Usage

```sh
PYTHONPATH=src/ python src/lightshotsniffer.py
```

## Run tests

```sh
PYTHONPATH=$PWD/src pytest --cov=src/ test
```

## Format source files

```sh
black src/ test/
```

## Author

👤 **Airthee**

* Twitter: [@Airthee](https://twitter.com/Airthee)
* Github: [@Airthee](https://github.com/Airthee)

## 🤝 Contributing

Contributions, issues and feature requests are welcome!<br />Feel free to check [issues page](https://github.com/Airthee/LightshotSniffer/issues/new).

## Show your support

Give a ⭐️ if this project helped you!

## 📝 License

Copyright © 2019 [Airthee](https://github.com/Airthee).<br />
This project is [WTFPL](http://www.wtfpl.net/) licensed.

***
_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_

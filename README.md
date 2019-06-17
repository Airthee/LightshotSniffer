<h1 align="center">Welcome to LightshotSniffer 👋</h1>
<p>
  <img src="https://img.shields.io/badge/version-0.0.1-blue.svg?cacheSeconds=2592000" />
  <a href="https://github.com/Airthee/LightshotSniffer">
    <img alt="Documentation" src="https://img.shields.io/badge/documentation-yes-brightgreen.svg" target="_blank" />
  </a>
  <a href="http://www.wtfpl.net/">
    <img alt="License: WTFPL" src="https://img.shields.io/badge/License-WTFPL-yellow.svg" target="_blank" />
  </a>
  <a href="https://twitter.com/Airthee">
    <img alt="Twitter: Airthee" src="https://img.shields.io/twitter/follow/Airthee.svg?style=social" target="_blank" />
  </a>
</p>

> Project that scan LightShot to find interesting images

### 🏠 [Homepage](https://github.com/Airthee/LightshotSniffer)

## Description

### Princip

* Url format : https://prnt.sc/XXXXXX where XXXXXX is the id of the image.
* The real source of the image is stored in src attribute of ".screenshot-image" element (CSS selector).
* If the url is "https://st.prntscr.com/2019/04/03/1355/img/0_173a7b_211be8ff.png", we pass.
* For each valid image, we ask the user to save the image, pass to the next or to the previous.

### Usage

1. At the lauch, user has to select download directory.
2. User can choose a start id and end id, by default, it starts from ZZZZZZ to 00000.
3. For each image, user tape "S" to save, "N" for next, "P" for previous.


## Install

```sh
pip install -r requirements.txt
```

## Usage

```sh
python sample/LightshotSniffer.py
```

## Run tests

```sh
cd src
python3 -m unittest discover ../test/
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
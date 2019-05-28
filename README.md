# LightshotSniffer

## Princip
* Url format : https://prnt.sc/XXXXXX where XXXXXX is the id of the image.
* The real source of the image is stored in src attribute of ".screenshot-image" element (CSS selector).
* If the url is "https://st.prntscr.com/2019/04/03/1355/img/0_173a7b_211be8ff.png", we pass.
* For each valid image, we ask the user to save the image, pass to the next or to the previous.

## Usage
1. At the lauch, user has to select download directory.
2. User can choose a start id and end id, by default, it starts from ZZZZZZ to 00000.
3. For each image, user tape "S" to save, "N" for next, "P" for previous.

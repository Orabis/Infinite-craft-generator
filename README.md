# Infinite-Craft-Generator

## Description

A script with a humorous purpose, spamming requests to find new crafts on the website https://neal.fun/infinite-craft. <br>
Creator of infinite-craft : Neal Agarwal - [His Twitter](https://twitter.com/nealagarwal)

## Installation

- Require Python 3.11
```
git clone https://github.com/Orabis/Infinite-craft-generator.git
pip install -r requirements.txt
python3 infinite.py
```
- Require a `headers.txt` file in the root directory of the folder, looks like :
```
Host: neal.fun
User-Agent: Any users agent
Accept: */*
Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate, br
Referer: https://neal.fun/infinite-craft/
Alt-Used: neal.fun
Connection: keep-alive
Cookie: Nuh Uhh
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
If-Modified-Since: 04/12/1400
TE: trailers
```

## How to retrieve Data 
For retrieving the data-storage of all the crafts, copy the content of `data-storage.json` and remplace it in the `local Storage` of the infinite-craft website. (I use Local Storage Editor) 
## To Do

List any tasks or features that need to be completed or added to the project.

- [x] Add a random pattern
- [x] Implement caching to resume from where it left off
- [x] Enable exporting of completed crafts to be used on the website
- [] Refactor code (Already done function)

## Contact

If you have any questions or suggestions regarding the project, feel free to contact:

- Email: cdf.leo.merkel@gmail.com - Léo MERKEL

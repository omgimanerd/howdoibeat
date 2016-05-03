# How Do I Beat...
This is a repository for Alvin Lin and Alvis Wong's web application for the
Riot Games API Challenge of 2016.
Since this year's theme is champion mastery, this web app allows you to query a
user to determine their mastery. It will approximate your likelihood of beating
the player given their champion history, mastery, and overall experience with
the role. It will also take into account the current matchup if the player
is in game.  
Hosted at ...

# Setup
Virtual Environment and Dependency Setup
```
virtualenv env
. ./activate
pip install -r requirements.txt
```
You will need to set the environment variable RIOT_API_KEY to your Riot Games
API key.
Example Bash script:
```bash
#!/bin/bash

export RIOT_API_KEY="your_key_here"
```

# Contributing
Please follow the [PEP8](http://pep8.org) standard for Python and the Google
JSDoc JavaScript standard if you wish to contribute to any of the code.
Fork this repository and set it up on your own computer.
Send us pull requests from your fork.

# Attribution
Itemify isn't endorsed by Riot Games and doesn't reflect the views or opinions
of Riot Games or anyone officially involved in producing or managing League of
Legends. League of Legends and Riot Games are trademarks or registered
trademarks of Riot Games, Inc. League of Legends &copy; Riot Games, Inc.
We do not own any of the image assets used in this website.

# License
Copyright &copy; Alvin Lin & Alvis Wong 2016

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sub license, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

# Creators
  - omgimanerd
  - wongalvis

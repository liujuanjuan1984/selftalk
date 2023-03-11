# self-talk

Talk to yourself.

Each talk contains some text messages.

All the text messages as talk data will be posted to rum group chain (init with seedurl) with two new eth account, and be saved to your local data dirpath.

### Usage


```sh
pip install quorum_data_py
pip install quorum_mininode_py

```


```python3

from selftalk import SelfTalk

seedurl = 'rum://seed?v=1&e=0&n=0&c=lz5_jMXmS0qcT62vf7OSXLU...TIqTyCSljxYx9KSw'
datadir="/selftalk/data"

bot = SelfTalk(seedurl,datadir)

bot.start()

```
# self-talk

Talk to yourself.

Each talk contains some text messages. All the text messages as talk data will be posted to rum group chain (init with seedurl) with two new eth account, and be saved to your local data dirpath.

### Usage


```sh
pip install quorum_data_py
pip install quorum_mininode_py

```

#### Each message of a selftalk is sent to rum group as a trx. Each selftalk contains many trxs.

```python3
from selftalk import NoodlesTalk

seedurl = "rum://seed?v=1&e=0&n=0&c=lz5_jMXmS0qcT62vf7OSXLU...TIqTyCSljxYx9KSw"
datadir = "/selftalk/data"

bot = NoodlesTalk(seedurl, datadir)

bot.start()

```

#### Messages of a selftalk as a whole is sent to rum group as one trx. Each selftalk is one trx.

```python3
from selftalk import PieTalk

seedurl = "rum://seed?v=1&e=0&n=0&c=lz5_jMXmS0qcT62vf7OSXLU...TIqTyCSljxYx9KSw"
datadir = "/selftalk/data"
pvtkey = "0x45417af0...39caf"

bot = PieTalk(seedurl, datadir, pvtkey)

bot.start()

```

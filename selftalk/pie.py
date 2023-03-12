import datetime
import os

from quorum_data_py import FeedData as feed
from quorum_mininode_py import MiniNode


class PieTalk:
    def __init__(
        self, seedurl: str, datadir: str, pvtkey: str = None, age_pvtkey: str = None
    ):
        """
        each talk contains many messages, and as a whole, posted to rum group as a trx.
        that is, each talk is a trx.
        """

        self.rum = MiniNode(seedurl, pvtkey, age_pvtkey)
        self.datadir = datadir

    def start(self):
        print(datetime.datetime.now(), "Setting up selftalk...")
        talklog = f"{str(datetime.datetime.now())[:19]} Selftalk start.\n\n"

        title = input("Enter the title >>")
        topic = input("Enter the topic >>").replace(" ", "-")
        aname = input("Name talker a >>")
        bname = input("Name talker b >>")

        print(datetime.datetime.now(), "Start talking...Enter 0 to stop selftalk.\n\n")

        talkers = [aname, bname]
        topic = f"{datetime.date.today()}_{topic}"
        fname = os.path.join(self.datadir, f"{topic}.md")

        talklog += "\n\n".join(
            [
                f"Title: {title}",
                f"Talker: {aname}",
                f"Talker: {bname}",
                f"Topic: {topic}",
                "Messages: \n\n------\n\n",
            ]
        )

        flag = True
        i = 0
        while flag:
            for talker in talkers:
                i += 1
                content = input(f" {talker}:\t")
                if content == "0":
                    flag = False
                    break
                try:
                    talklog += f"{talker}:\t{content}\n\n"
                except Exception as err:
                    print(err)
                    flag = False
                    break

        talklog += f"\n\n{str(datetime.datetime.now())[:19]} Selftalk finished.\n\n"

        post = feed.new_post(content=talklog, post_id=topic, name=title)
        resp = self.rum.api.post_content(post)
        print(resp)
        talklog += f"\n\n----Group: {self.rum.api.group_id}\n\nTrx: {resp['trx_id']}\n"

        with open(fname, "w", encoding="utf-8") as f:
            f.write(talklog)

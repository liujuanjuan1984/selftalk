import datetime
import os

from quorum_data_py import FeedData as feed
from quorum_mininode_py import MiniNode


class SelfTalk:
    def __init__(self, seedurl: str, datadir: str):
        # init two new account for selftalk
        self.talker_a = MiniNode(seedurl)
        self.talker_b = MiniNode(seedurl)
        self.datadir = datadir

    def start(self):
        print(datetime.datetime.now(), "Setting up selftalk...")
        title = input("Enter the title >>")
        topic = input("Enter the topic >>").replace(" ", "-")
        aname = input("Name talker a >>")
        bname = input("Name talker b >>")
        print(datetime.datetime.now(), "Start talking...Enter 0 to stop selftalk.\n\n")

        talkers = {aname: self.talker_a, bname: self.talker_a}
        topic = f"{datetime.date.today()}_{topic}"
        fname = os.path.join(self.datadir, f"{topic}.md")
        f = open(fname, "a", encoding="utf-8")

        f.write(f"Title: {title}\n\n")
        f.write(f"Talker: {aname}\n\n```python\n {self.talker_a.account}\n```\n\n")
        f.write(f"Talker: {bname}\n\n```python\n {self.talker_b.account}\n```\n\n")
        f.write(f"Topic: {topic}\n\n")
        f.write("Messages: \n\n")

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
                    post = feed.new_post(content=content, post_id=f"{topic}_{i}")
                    talkers[talker].api.post_content(post)
                    f.write(f"{talker}:\n{content}\n\n")
                except Exception as err:
                    print(err)
                    flag = False
                    break

        f.close()
        print(
            datetime.datetime.now(), f"Selftalk finished. Data is saved to \n{fname}\n"
        )

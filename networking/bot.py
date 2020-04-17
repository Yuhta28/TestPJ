from irc import *
import os
import random

channel = "#testit"
server = "irc.freenode.net"
botnick = "reddity"

irc = IRC()
irc.connect(server, channel, botnick)

while 1:
    text = irc.get_text().decode("utf-8")
    print(text)

    if "PRIVMSG " in text and channel in text and "hello" in text:
        irc.send(channel, "HEllo!")
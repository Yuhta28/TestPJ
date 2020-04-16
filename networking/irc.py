import socket
import sys

class IRC:
    irc = socket.socket()

    def __init__(self):
        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def send(self, chan, msg):
        self.irc._send_raw("PRIVMSG " + chan + " " + msg + "\n")

    def _send_raw(self, line, encoding="utf-8"):
        self.irc._send_raw(line.encode(encoding) + b"\r\n")

    def connect(self, server, channel, botnick):
        # defines the socket
        print("connecting to:" + server)
        self.irc.connect((server, 6667))     # connects to the server
        self.irc._send_raw("USER " + botnick + " " + botnick + " " + botnick + " :This is a fun bot!\n")   # user authentication
        self.irc._send_raw("NICK " + botnick + "\n")
        self.irc._send_raw("JOIN " + channel + "\n")  # join the channel

    def get_text(self):
        text=self.irc.recv(2040)    # receive the text

        if text.find(b'PING') != -1:
            self._send_raw('PONG' + text.split()[1])
        return text
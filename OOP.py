class song(object):

    def __init__(self,lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = song(["Happy birthday to you;"
                   "I dont want to get sued"
                   "So ill stop right there"])

bulls_on_parade = song(["They rally around tha family"
                        "With the pockets full of shell"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

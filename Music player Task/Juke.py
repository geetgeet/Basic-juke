

from tkinter import *
from tkinter import filedialog
from pygame import mixer


class MusicPlayer:
    def __init__(self, window ):
        window.geometry('320x100'); window.title('Basic Juke'); window.configure(background="teal")
        Load_b = Button(window, bg="orange",text = 'Load',  width = 10, command = self.load_song)
        Play_b = Button(window,bg="light blue", text = 'Play',  width = 10, command = self.play)
        Pause_b = Button(window,text = 'Pause',  width = 10,  command = self.pause)
        Stop_b = Button(window ,bg="red",text = 'Stop',  width = 10,  command = self.stop)
        Load_b.grid(row=2,column=1);Play_b.grid(row=2,column=2);Pause_b.grid(row=2,column=3);Stop_b.grid(row=3,column=2)
        self.music_file = False
        self.playing_state = False
    def load_song(self):
        self.music_file = filedialog.askopenfilename()
    def play(self):
        if self.music_file:
            mixer.init()
            mixer.music.load(self.music_file)
            mixer.music.play()
    def pause(self):
        if not self.playing_state:
            mixer.music.pause()
            self.playing_state=True
        else:
            mixer.music.unpause()
            self.playing_state = False
    def stop(self):
        mixer.music.stop()


window = Tk()
app= MusicPlayer(window)
window.mainloop()





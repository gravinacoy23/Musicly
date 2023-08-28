import customtkinter
from PIL import Image, ImageTk
import os



class Window(customtkinter.CTk, customtkinter.CTkImage,):
    def __init__(self):
        super().__init__()
        
        self.title('Musicly')
        self.geometry('400x600')
        self.columnconfigure((0,1,2,3,4,5,6,7,8,9,10), weight=1)
        self.rowconfigure((0,1,2,3,4,5,6,7,8,9,10), weight=1)
        
        self.play_image = customtkinter.CTkImage(Image.open(os.path.join('media', 'images', 'play_button.png')), size=(50,50))
        self.pause_image = customtkinter.CTkImage(Image.open(os.path.join('media', 'images', 'pause_button.png')), size=(50,50))
        self.skipfoward_image = customtkinter.CTkImage(Image.open(os.path.join('media', 'images', 'skip_forward.png')), size=(40,40))
        self.skipbackward_image = customtkinter.CTkImage(Image.open(os.path.join('media', 'images', 'skip_backwards.png')), size=(40,40))
        
        self.music_bar = customtkinter.CTkProgressBar(self, 
                                                      orientation="horizontal",
                                                      width=300)
        self.music_bar.set(0)
        self.volume_level = customtkinter.CTkSlider(self,
                                                    from_=0, 
                                                    to=100, 
                                                    command=self.volume_value, 
                                                    number_of_steps=100,
                                                    orientation='vertical', 
                                                    height=400)
        self.options = customtkinter.CTkOptionMenu(self, 
                                                   values=['Player', 'Playlist'])
        self.options.set('Player')
        self.play_button = customtkinter.CTkButton(self, 
                                                   text=None, 
                                                   command=self.play_button_callback, 
                                                   image=self.play_image,
                                                   width=50,
                                                   height=50)
        self.skipfoward_button = customtkinter.CTkButton(self,
                                                         text=None,
                                                         image=self.skipfoward_image,
                                                         width=50,
                                                         height=50)
        self.skipbackward_button = customtkinter.CTkButton(self,
                                                           text=None,
                                                           image=self.skipbackward_image,
                                                           width=50,
                                                           height=50)
        self.play_button.grid(row=10, column=5,)
        self.skipfoward_button.grid(row=10, column=5, sticky='e')
        self.skipbackward_button.grid(row=10, column=5, sticky='w')
        self.music_bar.grid(row=8, column=5, sticky= 's')
        self.volume_level.grid(row=1, column=0, rowspan=8, sticky='e')
        self.options.grid(row=0,column=5)
        
        
    playing=False
    
    def volume_value(self, value): 
        print(value)

    def play_button_callback(self):
        if not self.playing:
            self.play_button.configure(image=self.pause_image)
            self.music_bar.start()
            self.playing=True
        else: 
            self.play_button.configure(image=self.play_image)
            self.music_bar.stop()
            self.playing=False
if __name__ == '__main__':
    window = Window()
    window.mainloop()
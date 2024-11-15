from tkinter import messagebox
from tkinter import*
from pytube import YouTube 
import os
from tkinter import ttk
import tkinter as tk

class Youtube_vid_aud:
    def __init__(self,root):
        self.root=root
        self.root.title("Calender Question")
        self.root.geometry("1100x2130+0+0")
        self.root.resizable(False,False)
        self.root.configure(bg='cyan')
        self.root.overrideredirect(True)
        
        self.txt_var1=StringVar()
        self.txt_var2=StringVar()
        
        self.lbl=Label(self.root,text='Youtube to Gallery',bg="cyan",fg='blue',font=("Arial",18,'bold','underline'))
        self.lbl.place(x=110,y=100)
        self.lbl=Label(self.root,text='▪︎ URL :- ',bg="cyan",font=("Georgia",7,'bold'))
        self.lbl.place(x=50,y=350)
        self.lbl=Label(self.root,text='▪︎ Path:- ',bg="cyan",font=("Georgia",7,'bold'))
        self.lbl.place(x=50,y=650)
        
        self.entry1=Entry(self.root,bg='yellow',bd=5,textvariable=self.txt_var1)
        self.entry1.place(x=240,y=350,width=800)
        self.entry2=Entry(self.root,bg='yellow',bd=5,textvariable=self.txt_var2)
        self.entry2.place(x=240,y=650,width=800)
        
        self.btn_paste=Button(self.root,text='Paste',bg='Deeppink1',bd=5,font=('Georgia',5,'bold'),command=lambda:self.entry1.event_generate("<<Paste>>"))
        self.btn_paste.place(x=450,y=470,width=300)
        
        self.btn1=Button(self.root,text='.mp3',bg='lime',bd=5,font=('Georgia',5,'bold'),command=self.yt_mp3)
        self.btn1.place(x=120,y=800,width=400)
        self.btn2=Button(self.root,text='.mp4',bg='red',bd=5,font=('Georgia',5,'bold'),command=self.yt_mp4)
        self.btn2.place(x=570,y=800,width=400)
        
        self.lbl=Label(self.root,text='▪︎ Note :- Wait till the popup message for downloading\n be done.',bg="cyan",font=("Georgia",7,'bold'))
        self.lbl.place(x=50,y=1000)
        
        self.lbl=Label(self.root,text='CODING VODING',bg="cyan",fg='indigo',font=("Georgia",15,'bold'))
        self.lbl.place(x=200,y=1150)
        
    def yt_mp3(self):
        yt = YouTube(self.txt_var1.get()) 
        
        # extract only audio 
        video = yt.streams.filter(only_audio=True).first() 
        
        destination = '/storage/emulated/0/music/download/'+self.txt_var2.get()
        
        # download the file 
        out_file = video.download(output_path=destination) 
        
        # save the file 
        
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file) 
        
        msg='Done downloading , You can see\n on given path'
        messagebox.showinfo("Congrats",msg)
        self.txt_var1.set('')
        
    def yt_mp4(self):
        path = '/storage/emulated/0/video/download/'+self.txt_var2.get()
        url = self.txt_var1.get()
        resol = "360p"
        file_type = "mp4"
        
        video = YouTube(url)
        Streams = video.streams
        
        vid = Streams.filter(res = resol, file_extension = file_type).first()
        
        vid.download(path)
        
        msg='Done downloading , You can see\n on given path'
        messagebox.showinfo("Congrats",msg)
        
        
root=tk.Tk()
obj=Youtube_vid_aud(root)
root.mainloop()
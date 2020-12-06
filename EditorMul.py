import tkinter
import os
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from tkinter import simpledialog  
from tkinter import ttk
import threading
import sys
import faulthandler
sys.setrecursionlimit(10**6)

#faulthandler.enable()

class Editor:
	
	__root = Tk()
	
	__thisWidth = 300
	__thisHeight = 300
	
	__thisTextArea = Text(__root,bg="white",font="Arial",fg="black",highlightbackground="red",highlightcolor="green",insertbackground="black",selectbackground="cyan",wrap=WORD)
	"""Theme changed to light, font black"""
	"""Create a text area, menu bar and scroll bar"""
	__thisMenuBar = Menu(__root)
	__thisFileMenu = Menu(__thisMenuBar, tearoff = 0)
	__thisEditMenu = Menu(__thisMenuBar, tearoff = 0)
	__thisHelpMenu = Menu(__thisMenuBar, tearoff = 0)
	
	__thisScrollBar = Scrollbar(__thisTextArea)

	counter = 0

	__file = None 
	
	def __init__(self,**kwargs):
		try:
			self.__root.wm_iconbitmap("Notepad.ico")
		except:
			pass
		
		try:
			self.__thisWidth = kwargs['width']
		except KeyError:
			pass
			
		try:
			self.__thisHeight = kwargs['height']
		except KeyError:
			pass
			
		self.__root.title("Untitled - Editor")

		"""Do not uncomment this part"""
		"""Removing bindings also removes binding with keyboard and mouse i.e. user cannot interact with the text area"""	
#		bindtags = list(self.__thisTextArea.bindtags())
#		bindtags.remove("Text")
#		self.__thisTextArea.bindtags(tuple(bindtags))
		
		"""If the height is not specified in the keyword arguments given, then use default values specified"""
		
		screenWidth = self.__root.winfo_screenwidth() 
		screenHeight = self.__root.winfo_screenheight() 
	
		left = (screenWidth / 2) - (self.__thisWidth / 2) 
		
		top = (screenHeight / 2) - (self.__thisHeight /2) 
		
		self.__root.geometry('%dx%d+%d+%d' % (self.__thisWidth,self.__thisHeight,left,top))
		
		self.__root.grid_rowconfigure(0,weight = 1)
		self.__root.grid_columnconfigure(0,weight = 1)
		
		self.__thisTextArea.grid(sticky = N + E + S + W) 
		
		self.__thisFileMenu.add_command(label = "New",command = self.__newFile, accelerator = "Ctrl + N")
		
		self.__thisFileMenu.add_command(label = "Open",command = self.__openFile, accelerator = "Ctrl + O")
		
		self.__thisFileMenu.add_command(label = "Save",command = self.__saveFile, accelerator = "Ctrl + S")
		
		self.__thisFileMenu.add_command(label = "Save As",command = self.__saveFileas, accelerator = "Ctrl + Shift + V")
		
		self.__thisFileMenu.add_command(label = "Switch Theme",command = self.__theme)
		
		self.__thisFileMenu.add_separator()
		self.__thisFileMenu.add_command(label = "Exit",command = self.__quitApplication, accelerator = "Ctrl + Q")
		
		self.__thisMenuBar.add_cascade(label = "File",menu = self.__thisFileMenu)
		
		
		self.__thisEditMenu.add_command(label = "Select All",command = self.__selectALL, accelerator = "Ctrl + A")
		
		self.__thisEditMenu.add_command(label = "Search",command = self.__find, accelerator = "Ctrl + F")
		
		self.__thisEditMenu.add_command(label = "Search and Replace",command = self.__findNReplace, accelerator = "Ctrl + H")
		
		self.__thisEditMenu.add_command(label = "Cut", command = self.__cut, accelerator = "Ctrl + X")

		self.__thisEditMenu.add_command(label = "Copy", command = self.__copy, accelerator = "Ctrl + C")
	
		self.__thisEditMenu.add_command(label = "Paste", command = self.__paste, accelerator = "Ctrl + V")
		
		self.__thisEditMenu.add_command(label = "Clear", command = self.__clear, accelerator = "Ctrl + D")
		
		self.__thisEditMenu.add_command(label = "Spell check", command = self.__SpellCheck, accelerator = "Ctrl + J")
		
		self.__thisMenuBar.add_cascade(label = "Edit",menu = self.__thisEditMenu)
		
		
		self.__thisHelpMenu.add_command(label = "About",command = self.__showAbout)
		
		self.__thisHelpMenu.add_command(label = "Team",command = self.__showTeam)
		
		self.__thisHelpMenu.add_command(label = "Shortcuts",command = self.__showShortcuts)
		
		self.__thisMenuBar.add_cascade(label = "Help",menu = self.__thisHelpMenu)
		
		
		self.__root.config(menu = self.__thisMenuBar)
		
		self.__thisScrollBar.pack(side = RIGHT,fill = Y)
		
		self.__thisScrollBar.config(command = self.__thisTextArea.yview)
		
		self.__thisTextArea.config(yscrollcommand = self.__thisScrollBar.set)
		
		"""
		Remove all existing keybinds that exist by default in Tkinter to avoid overlap of functions
		"""
		"""Removing all the shortcuts that may exist with the alphabet keys so that overlap of functions is removed"""
		self.__thisTextArea.bind('<Control-A>',lambda event:"break")
		self.__thisTextArea.bind('<Control-a>',lambda event:"break")

		self.__thisTextArea.bind('<Control-B>',lambda event:"break")
		self.__thisTextArea.bind('<Control-b>',lambda event:"break")
		
		self.__thisTextArea.bind('<Control-C>',lambda event:"break")
		self.__thisTextArea.bind('<Control-c>',lambda event:"break")
		
		self.__thisTextArea.bind('<Control-D>',lambda event:"break")
		self.__thisTextArea.bind('<Control-d>',lambda event:"break")
	
		self.__thisTextArea.bind('<Control-E>',lambda event:"break")
		self.__thisTextArea.bind('<Control-e>',lambda event:"break")
		
		self.__thisTextArea.bind('<Control-F>',lambda event:"break")
		self.__thisTextArea.bind('<Control-f>',lambda event:"break")
		
		self.__thisTextArea.bind('<Control-G>',lambda event:"break")
		self.__thisTextArea.bind('<Control-g>',lambda event:"break")
		
		self.__thisTextArea.bind('<Control-H>',lambda event:"break")
		self.__thisTextArea.bind('<Control-h>',lambda event:"break")
		
		self.__thisTextArea.bind('<Control-I>',lambda event:"break")
		self.__thisTextArea.bind('<Control-i>',lambda event:"break")
		
		self.__thisTextArea.bind('<Control-J>',lambda event:"break")
		self.__thisTextArea.bind('<Control-j>',lambda event:"break")
		
		self.__thisTextArea.bind('<Control-K>',lambda event:"break")
		self.__thisTextArea.bind('<Control-k>',lambda event:"break")
		
		self.__thisTextArea.bind('<Control-L>',lambda event:"break")
		self.__thisTextArea.bind('<Control-l>',lambda event:"break")
		
		self.__thisTextArea.bind('<Control-M>',lambda event:"break")
		self.__thisTextArea.bind('<Control-m>',lambda event:"break")
		
		self.__thisTextArea.bind('<Control-N>',lambda event:"break")
		self.__thisTextArea.bind('<Control-n>',lambda event:"break")
		
		self.__thisTextArea.bind('<Control-O>',lambda event:"break")
		self.__thisTextArea.bind('<Control-o>',lambda event:"break")
		
		self.__thisTextArea.bind('<Control-P>',lambda event:"break")
		self.__thisTextArea.bind('<Control-p>',lambda event:"break")
		
		self.__thisTextArea.bind('<Control-Q>',lambda event:"break")
		self.__thisTextArea.bind('<Control-q>',lambda event:"break")
		
		self.__thisTextArea.bind('<Control-R>',lambda event:"break")
		self.__thisTextArea.bind('<Control-r>',lambda event:"break")
		
		self.__thisTextArea.bind('<Control-S>',lambda event:"break")
		self.__thisTextArea.bind('<Control-s>',lambda event:"break")
		
		self.__thisTextArea.bind('<Control-T>',lambda event:"break")
		self.__thisTextArea.bind('<Control-t>',lambda event:"break")
		
		self.__thisTextArea.bind('<Control-U>',lambda event:"break")
		self.__thisTextArea.bind('<Control-u>',lambda event:"break")
		
#		self.__thisTextArea.bind('<Control-V>',lambda event:"break")
#		self.__thisTextArea.bind('<Control-v>',lambda event:"break")
		
		self.__thisTextArea.bind('<Control-W>',lambda event:"break")
		self.__thisTextArea.bind('<Control-w>',lambda event:"break")
		
		self.__thisTextArea.bind('<Control-X>',lambda event:"break")
		self.__thisTextArea.bind('<Control-x>',lambda event:"break")
		
		self.__thisTextArea.bind('<Control-Y>',lambda event:"break")
		self.__thisTextArea.bind('<Control-y>',lambda event:"break")
		
		self.__thisTextArea.bind('<Control-Z>',lambda event:"break")
		self.__thisTextArea.bind('<Control-z>',lambda event:"break")
		
		self.__thisTextArea.bind('<Control-slash>',lambda event:"break")
		
		"""
		Bind the shortcuts to the their respective functions
		"""
		
		self.__thisTextArea.bind('<Control-N>',self.__newFile)
		self.__thisTextArea.bind('<Control-n>',self.__newFile)
		
		self.__thisTextArea.bind('<Control-S>',self.__saveFile)
		self.__thisTextArea.bind('<Control-s>',self.__saveFile)
		
		self.__thisTextArea.bind('<Control-Shift-S>',self.__saveFileas)
		self.__thisTextArea.bind('<Control-Shift-s>',self.__saveFileas)
		
		self.__thisTextArea.bind('<Control-O>',self.__openFile)
		self.__thisTextArea.bind('<Control-o>',self.__openFile)

		self.__thisTextArea.bind('<Control-Q>',self.__quitApplication)
		self.__thisTextArea.bind('<Control-q>',self.__quitApplication)
		
		self.__thisTextArea.bind('<Control-A>',self.__selectALL)
		self.__thisTextArea.bind('<Control-a>',self.__selectALL)
		
		self.__thisTextArea.bind('<Control-F>',self.__find)
		self.__thisTextArea.bind('<Control-f>',self.__find)
		
		self.__thisTextArea.bind('<Control-H>',self.__findNReplace)
		self.__thisTextArea.bind('<Control-h>',self.__findNReplace)
		
		self.__thisTextArea.bind('<Control-D>',self.__clear)
		self.__thisTextArea.bind('<Control-d>',self.__clear)
		
		self.__thisTextArea.bind('<Control-X>',self.__cut)
		self.__thisTextArea.bind('<Control-x>',self.__cut)
		
		self.__thisTextArea.bind('<Control-C>',self.__copy)
		self.__thisTextArea.bind('<Control-c>',self.__copy)
		
		self.__thisTextArea.bind('<Control-J>',self.__SpellCheck)
		self.__thisTextArea.bind('<Control-j>',self.__SpellCheck)
		
		self.__words = open("/usr/share/dict/words").read().split("\n")
		
#		self.__thisTextArea.bind('<Control-V>',self.__paste)
#		self.__thisTextArea.bind('<Control-v>',self.__paste)
		
	def __quitApplication(self,event = None):
		if messagebox.askokcancel("Quit","Do you wish to exit the Editor?"):
			self.__root.destroy()
		
	def __showAbout(self):
		showinfo("Editor","Made by Team 2")
		
	def __showTeam(self):
		showinfo("Team Members","COE18B018 - G V Anurag\nCOE18B029 - Katte Prahlad Gowtham\nCOE18B056 - Thigulla Vamsi Krishna\nCOE18B065 - Srinivasan R Sharma\nCED18I039 - Paleti Krishnasai\nCED18I056 - Darshan VSS\n")
		
	def __showShortcuts(self):
		showinfo("Editor Shortcuts","New File - Ctrl + N\nOpen File - Ctrl + O\nSave File - Ctrl + S\nSave As - Ctrl + Shift + S\nExit - Ctrl + Q\nCut - Ctrl + X\nCopy - Ctrl + C\nPaste - Ctrl + P\n\nFind - Ctrl + F\nFind and Replace - Ctrl + H\nSelect All - Ctrl + A\nSelect - Shift + <Arrow Key>\nBeginning of line - Home\nEnd of line - End\nBeginning of File - Ctrl + Home\nEnd of File - Ctrl + End\n Next Paragraph - Ctrl + <Down>\nPrevious Paragraph - Ctrl + <Up>\nToggle between , . ; - Ctrl + <Left/Right>\n")
	
	def __openFile(self,event = None):
		self.__file = askopenfilename(defaultextension =".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
		
		if self.__file == "":
			self.__file = None
		else:
			self.__root.title(os.path.basename(self.__file)+" - Editor")
			
			self.__thisTextArea.delete(1.0,END)
			file = open(self.__file,"r")
			self.__thisTextArea.insert(1.0,file.read())
			file.close()
	
	def __newFile(self, event = None):
		self.__root.title("Untitled - Editor")
		self.__file = None
		self.__thisTextArea.delete(1.0,END)	
		"""Clears the text area window"""	
		
	def __saveFile(self,event = None):
		if self.__file == None:
			self.__file = asksaveasfilename(initialfile = 'Untitled.txt',defaultextension = ".txt",filetypes = [("All Files","*.*"),("Text Documents","*.txt")])
			if self.__file == "":
				self.__file = None
			else:
				file = open(self.__file,"w")
				file.write(self.__thisTextArea.get(1.0,END))
				file.close()
				self.__root.title(os.path.basename(self.__file)+ " - Editor")	
				"""This line changes the title of the window"""
		
		else:
			file = open(self.__file,"w")
			file.write(self.__thisTextArea.get(1.0,END))
			file.close()
	
	def __saveFileas(self, event = None):
		self.__file = asksaveasfilename(initialfile = 'Untitled.txt',defaultextension = ".txt",filetypes = [("All Files","*.*"),("Text Documents","*.txt")])
		if self.__file != "":
			file = open(self.__file,"w")
			file.write(self.__thisTextArea.get(1.0,END))
			file.close()
			self.__root.title(os.path.basename(self.__file)+ " - Editor")
			"""This line changes the title of the window"""
	def __clear(self, event = None):
		self.__thisTextArea.delete(1.0,END)	
		
	def __cut(self, event = None):
		self.__thisTextArea.event_generate("<<Cut>>")
	
	def __copy(self, event = None):
		self.__thisTextArea.event_generate("<<Copy>>")
		
	def __paste(self, event = None):
		self.__thisTextArea.event_generate("<<Paste>>")
		
	def __selectALL(self,event=None):
		self.__thisTextArea.tag_add('sel','1.0',END)
		return "break"
	"""Add multithreading for find and findNReplace"""	
	def __finder(self,event=None):
		self.__thisTextArea.tag_remove('found','1.0',END)
		s = simpledialog.askstring("Find","Enter the string to be found")
		if(s):
			index = '1.0'
			while 1:
				index = self.__thisTextArea.search(s,index,nocase = 1,stopindex = END)
				
				if not index:
					break
				lastindex = '%s+%dc'%(index,len(s))
				
				self.__thisTextArea.tag_add('found',index,lastindex)
				index = lastindex
				
			self.__thisTextArea.tag_config('found',foreground="red")
		
	
	def __find(self,event=None):
		t1=threading.Thread(target=self.__finder());
		t1.start()
		t1.join()
		
	def __findNReplaceF(self,event=None):
		self.__thisTextArea.tag_remove('found','1.0',END)
		
		s = simpledialog.askstring("Find","Enter the string to be replaced")
		r = simpledialog.askstring("Replace","Enter the string to be replaced with")
		
		if(s and r):
			index = '1.0'
			while 1:
				index = self.__thisTextArea.search(s, index, nocase = 1,stopindex = END)
				#print(index)
				
				if not index:
					break
				lastindex = '%s+%dc'%(index,len(s))
				
				self.__thisTextArea.delete(index,lastindex)
				self.__thisTextArea.insert(index,r)
				
				lastindex = '%s+%dc'%(index,len(r))
		
				self.__thisTextArea.tag_add('found',index,lastindex)
				index = lastindex
			if self.counter == 1:
				self.__thisTextArea.tag_config('found',foreground="yellow")
			else:
				self.__thisTextArea.tag_config('found',foreground="blue")
		
		
	def __findNReplace(self,event=None):
		t1=threading.Thread(target=self.__findNReplaceF())
		t1.start()
		t1.join()

	def __SpellChecker(self,event = None):
		self.__file = askopenfilename(defaultextension =".txt",filetypes=[("Text Documents","*.txt")])
		cmd = 'aspell -c '+self.__file
		os.system(cmd)
		self.__thisTextArea.delete(1.0,END)
		file = open(self.__file,"r")
		self.__thisTextArea.insert(1.0,file.read())
		file.close()
		return "break"
		
	def __SpellCheck(self,event = None):
		t1=threading.Thread(target=self.__SpellChecker())
		t1.start()
		t1.join()
			
	def __theme(self):
		if self.counter!=0:
			self.__thisTextArea.config(bg="white",font="Arial",fg="black",highlightbackground="red",highlightcolor="green",insertbackground="black",selectbackground="cyan",wrap=WORD)
			self.counter = 0
		else:
			self.__thisTextArea.config(bg="black",font="Arial",fg="white",highlightbackground="red",highlightcolor="green",insertbackground="white",selectbackground="yellow",wrap=WORD)
			self.counter = 1
	
	def run(self):
		self.__root.mainloop()
		
		
Editor1 = Editor(width=600,height=400)
Editor1.run()

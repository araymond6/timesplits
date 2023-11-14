import tkinter as tk
import os
import csv
import xml.etree.ElementTree as ET

#to silence warning
TK_SILENCE_DEPRECATION=1

# opening the files I need for now: cached .lss file and bg
splits = open("Splits/bal5.lss", 'r')
bg = open("../bg.jpeg", 'U')

# Gets the names from the .lss files.
def get_names():
	global root
	global names
	tree = ET.parse('Splits/bal5.lss')
	root = tree.getroot()
	attempt_count = root.find('AttemptCount').text
	print(attempt_count)
	segments = root.find('Segments')
	names = {}
	i = 0
	for y in segments.findall('Segment'):
		names[i]=y.find('Name').text
		i += 1

def removeinfo():
	tree = ET.parse('Splits/bal5.lss')
	root = tree.getroot()

def main():
	#Initiating a window
	root = tk.Tk()
	root.geometry("500x800")
	root.title("TimeSplits")
	label = tk.Label(root, text="Hello World!", font=("Arial", 18))
	label.pack(padx=20, pady=20)
	textbox = tk.Text(root)
	textbox.pack()
	exitbutton = tk.Button(root, text="Quit", command=root.destroy)
	exitbutton.pack()
	#Program Loop
	root.mainloop()

if __name__ == "__main__":
	get_names()
	for x in names:
		print(names[x])
	splits.close()
	bg.close()


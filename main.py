import tkinter as tk
import os
import csv
import xml.etree.ElementTree as ET

#to silence warning
TK_SILENCE_DEPRECATION=1

# opening the files I need for now: cached .lss file and bg
splits = open("Splits/bal5.lss", 'r')
bg = open("../bg.jpeg", 'U')

def parse_XML():
	tree = ET.parse('Splits/bal5.lss')
	root = tree.getroot()
	segments = tree.findall(path = 'Segment')


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
	return root

if __name__ == "__main__":
	root = main()
	print(root)
	#parse_XML()
	splits.close()
	bg.close()



from tkinter import *
import sqlite3
import random
import pickle

conn = sqlite3.connect('clickbait.db')

c = conn.cursor()

def close():
	conn.close()
	window.destroy()
	exit()

def history():
    output.delete(0.0, END)
    c.execute("SELECT * FROM history")
    history = c.fetchall()
    numout = 1.0
    numarr = 0
    for i in history:
        output.insert(numout, f'''{history[numarr]}
			''')
        numout = numout + 1.0
        numarr = numarr + 1

def generate():
    output.delete(0.0, END)
    abbreviations = ["OMG", "LMAO", "LMFAO", "ROFL", "OMFG", "STFU", "VIRAL", "NSFW", "GTFO"]
    begin = ["I", "My Friend", "My GF", "My BF", "Obama", "Trump", "Trudeau", "Biden"]
    mid = ["Contacted The Dead Spirit Of XxxTentacion", "Filled My House With SLIME", "MURDERED ME", "ORDERED HUMAN SLAVES", "Drank Among Us Potion", "Drank MINECRAFT Potion", "Browsed The Dark Web!", "Got High On Skittles!", "Filled A Pool Of Orbeez!", "Blew Up My Toilet!", "Killed My SISTER?!"]
    end = ["ACTUALLY HAPPENED", "COPS CALLED", "GONE WRONG", "GONE SEXUAL?", "GONE DEADLY", "I LITERALLY CAN'T BELIEVE IT HAPPENED", "666", "GONE SPOOKY", "420"]
    whole = f"{random.choice(abbreviations)}!!! {random.choice(begin)} {random.choice(mid)}! ({random.choice(end)}!!!!)"
    pickle.dump( whole, open( "clickbait.p", "wb" ) )
    wholefinal = pickle.load( open( "clickbait.p", "rb" ) )
    sql = ("INSERT INTO history(title) VALUES(?)")
    val = (wholefinal,)
    c.execute(sql, val)
    conn.commit()
    output.insert(1.0, f'''{wholefinal}
        ''')

window = Tk()
window.title('Clickbait 2021 Abridged The Manga')
window.configure(background="black")
window.resizable(0,0)

Label (window, text="Clickbait 2021 Abridged The Manga", bg="black", fg='white', font="none 12") .grid(row=1, column=0, sticky=N)
Button(window, text="Generate", width=6, bg="black", fg="white", command=generate) .grid(row=2, column=0, sticky=N)
Button(window, text="History", width=6, bg="black", fg="white", command=history) .grid(row=3, column=0, sticky=N)
output = Text(window, width=40, height=10, wrap=WORD, fg="white", background="black")
output.grid(row=4, column=0, sticky=N)

window.mainloop()

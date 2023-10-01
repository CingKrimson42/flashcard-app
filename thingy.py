from tkinter import *
from random import randint

root = Tk()
root.geometry("550x410")

words = [
    (("Salve"),("Hello (Singular)")),
    (("Salvete"),("Hello (Plural)")),
    (("-t, -tur"), ("he, she, it")),
    (("-o,-r,-m,-i"),("I, me, myself")),
    (("-s, -ris, isti"),("you")),
    (("cur?"), ("why?")),
    (("ubi?"), ("where?, when?")),
    (("quis?"), ("who?")),
    (("quid?"), ("what?")),
    (("quantus?"), ("how great?")),
    (("quot?"), ("how many?")),
    (("qualis?"), ("what kind of?")),
    (("iuvenis"), ("young man")),
    (("qualis?"), ("what kind of?")),
    (("Habito?"), ("I inhabit")),
    (("Habitas"), ("You inhabit")),
    (("Habitat"), ("he/she/it inhabits")),
    (("Habitamus"), ("We inhabit")),
    (("Habitant"), ("They inhabit")),
    (("Habitasne"), ("Do you inhabit?"))

]

count = len(words)

def next():
    global hinter, hint_count

    answer_label.config(text="")
    my_entry.delete(0, END)
    hint_label.config(text="")

    hinter = ""
    hint_count = 0

    global random_word
    random_word = randint(0,count-1)
    latin_word.config(text=words[random_word][0])

def answer():
    if my_entry.get().capitalize()==words[random_word][1].capitalize():
        answer_label.config(
            text = f"Correct! {words[random_word][0]} is {words[random_word][1]}")
            
    else:
        answer_label.config(
            text=f"Incorrect! {words[random_word][0]} is not {my_entry.get()}")

hinter = ""
hint_count = 0

def hint():
    global hint_count
    global hinter
    if hint_count<len(words[random_word][1]):
        hinter = hinter+words[random_word][1][hint_count]
        hint_label.config(text=hinter)
        hint_count+=1



latin_word = Label(root, text = "", font = ("Times New Roman", 36))
latin_word.pack(pady=50)

answer_label = Label(root, text= "")
answer_label.pack(pady=20)

my_entry = Entry(root, font = ('Times New Roman',18))
my_entry.pack(pady=20)

button_frame = Frame(root)
button_frame.pack(pady=20)

answer_button = Button(button_frame, text = "Answer", command = answer)
answer_button.grid(row=0,column=0,padx=20)

next_button = Button(button_frame, text="Next", command=next)
next_button.grid(row=0, column =1)

hint_button = Button(button_frame, text="Hint", command=hint)
hint_button.grid(row=0,column=2, padx=20 )

hint_label = Label(root, text="")
hint_label.pack(pady=20)

next()

root.mainloop() 

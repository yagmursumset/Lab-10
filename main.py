import tkinter as tk

path = open("C:\\Users\\yagmu\\Documents\\Marvel.txt")
window = tk.Tk()
window.title("CREATE TABLE")

def delete():
    l5.delete("1.0", tk.END)

def read():
    delete()
    while path:
        readtext = path.read()
        if readtext == "":
            break
        l5.insert("1.0", readtext)


def calculate():
    delete()
    list = []
    readtext2 = path.read()
    words = readtext2.split()

    for word in words:
        if word not in list:
            list.append(word)
    print(list)

    for word in range(0, len(list)):
        x = ("Frequency of" + str(list[word]) + "is : " + str(readtext2.count(list[word])))
        l5.insert("1.0", x)
        l5.insert("1.0", "\n")


l5 = tk.Text(width=100, height=25)
l5.pack()
button1 = tk.Button(window, text="READ", width=5, command=read, font=("Helvetica", 10))
button1.pack()
button2 = tk.Button(window, text="CALCULATE", width=10, command=calculate, font=("Helvetica", 10))
button2.pack()

window.mainloop()

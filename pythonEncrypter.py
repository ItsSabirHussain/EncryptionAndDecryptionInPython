import tkinter as Encrypter
import random
import time

fields = ('Message', 'DOB', 'Encrypted Message', 'Encryption Time', 'Decrypted Message', 'Decryption Time')

def encryptMessage(message, dob):
    days = int(dob.split("/")[0])
    months = int(dob.split("/")[1])
    years = int(dob.split("/")[2])
    #split string in months parts
    if int(len(message)/months):
        partSize = int(len(message)/months)
        arr = []
        for i in range(0, len(message) - len(message)%months, partSize):
            arr.append(message[i:i+partSize])

        if len(message) % months:
            arr.append(message[len(message) - len(message) % months:len(message)])
    else:
        arr = [message]
    #replace character with next years character
    nextCharacter = years % 128
    newArr = []
    for i in arr:
        tmpArr = []
        for j in range(len(i)):
            if (ord(i[j]) + nextCharacter) > 127:
                tmpArr.append( chr(32+(nextCharacter - (127 - ord(i[j])))))
            else:
                tmpArr.append(chr(ord(i[j]) + nextCharacter))

        newArr.append(''.join(tmpArr))
    #rotating days time
    newRotatedArr = []
    for i in newArr:
        rotater = days%len(i)
        newRotatedArr.append(
            i[len(i)-rotater:len(i)]+i[0:len(i)-rotater]
        )
    #adding dummy characters
    finalMessage = ''
    dummyNumber = int(years/(days*months))
    for i in ''.join(newRotatedArr):
        finalMessage += i
        for j in range(dummyNumber):
            finalMessage += chr(random.randint(32,127))
    return  finalMessage


def decryptMessage(message, dob):
    days = int(dob.split("/")[0])
    months = int(dob.split("/")[1])
    years = int(dob.split("/")[2])
    #removeDummy Characters
    newMessage = ''
    dummyNumber = int(years/(days*months))
    chk = 0
    while (chk < len(message)):
        newMessage += message[chk]
        chk += 1
        for i in range(dummyNumber):
            chk += 1
    # split string in months parts
    if int(len(newMessage)/months):
        partSize = int(len(newMessage) / months)
        arr = []
        for i in range(0, len(newMessage) - len(newMessage) % months, partSize):

            arr.append(newMessage[i:i + partSize])
        if len(newMessage) % months:
            arr.append(newMessage[len(newMessage) - len(newMessage) % months:len(newMessage)])
    else:
        arr = [newMessage]
    # rotating days time
    newRotatedArr = []
    for i in arr:
        rotater = days % len(i)
        newRotatedArr.append(
            i[rotater:len(i)] + i[0:rotater]
        )
    # replace character with next years character
    nextCharacter = years % 128
    newReplacedMessage = []
    for i in newRotatedArr:
        tmpArr = []
        for j in range(len(i)):
            if (ord(i[j]) - nextCharacter) < 32:

                tmpArr.append(chr(127 - (nextCharacter - (ord(i[j]) - 32))))
            else:
                tmpArr.append(chr(ord(i[j]) - nextCharacter))

        newReplacedMessage.append(''.join(tmpArr))
    return  (''.join(newReplacedMessage))

def compute(entries):
    sTime = time.time()
    eMessage = encryptMessage(entries['Message'].get(), entries["DOB"].get())
    eTime = time.time() - sTime
    sTime = time.time()
    dMessage = decryptMessage(eMessage, entries["DOB"].get())
    dTime = time.time() - sTime
    entries['Encrypted Message'].delete(0, Encrypter.END)
    entries['Encrypted Message'].insert(0, eMessage )
    entries['Decrypted Message'].delete(0, Encrypter.END)
    entries['Decrypted Message'].insert(0, dMessage )
    entries['Encryption Time'].delete(0, Encrypter.END)
    entries['Encryption Time'].insert(0, eTime)
    entries['Decryption Time'].delete(0, Encrypter.END)
    entries['Decryption Time'].insert(0, dTime)
    print("Encrypted Message:", eMessage )
    print("Decrypted Message:", dMessage)
    print("Encrypted Time:",eTime)
    print("Decrypted Time:", dTime)

def gui(r, f):
    entries = {}
    for field in f:
        row = Encrypter.Frame(r)
        lab = Encrypter.Label(row, width=22, text=field + ": ", anchor='w')
        ent = Encrypter.Entry(row)
        ent.insert(0, "0")
        row.pack(side=Encrypter.TOP,
                 fill=Encrypter.X,
                 padx=5,
                 pady=5)
        lab.pack(side=Encrypter.LEFT)
        ent.pack(side=Encrypter.RIGHT,
                 expand=Encrypter.YES,
                 fill=Encrypter.X)
        entries[field] = ent
    return entries

if __name__ == '__main__':
    root = Encrypter.Tk()
    root.title("Encrypter")
    ents = gui(root, fields)
    b1 = Encrypter.Button(root, text='Compute',
                          command=(lambda e=ents: compute(e)))
    b1.pack(side=Encrypter.LEFT, padx=5, pady=5)

    b3 = Encrypter.Button(root, text='Quit', command=root.quit)
    b3.pack(side=Encrypter.LEFT, padx=5, pady=5)
    root.mainloop()
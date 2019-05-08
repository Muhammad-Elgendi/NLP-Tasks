import Stemmer
import mysql.connector
from tkinter import *
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="nlp2"
)
print(mydb)
mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE nlp")
# mycursor.execute("CREATE DATABASE nlp2 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;")
# mycursor.execute("SHOW DATABASES")

# for x in mycursor:
#   print(x)

# mycursor.execute("CREATE TABLE classification (word VARCHAR(255), type VARCHAR(255))")

# mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

sql = "INSERT INTO classification (word, type) VALUES (%s, %s)"
# utf8Name ="SET NAMES 'utf8'"
# utf8Char = "SET CHARACTER SET utf8"
# mycursor.execute(utf8Name)

# mycursor.execute(utf8Char)

# statement = input("Enter statement : ")
# listOfwords = Stemmer.tokenizeArabic(statement)
# Stems = Stemmer.stemArabic(listOfwords)
# for index , stem in enumerate(Stems):    
#     val = (stem, listOfwords[index])
#     mycursor.execute(sql, val)

# mydb.commit()

# mycursor.execute("SELECT * FROM classification")

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)

# print(mycursor.rowcount, "record inserted.")

def show_outputs():
    statement = e1.get()
    listOfwords = Stemmer.tokenizeArabic(statement)
    Stems = Stemmer.stemArabic(listOfwords)
    for index , stem in enumerate(Stems):    
      val = (stem, listOfwords[index])
      mycursor.execute(sql, val)
    mydb.commit()
    mycursor.execute("SELECT * FROM classification")
    myresult = mycursor.fetchall()
    lbl["text"] = str(myresult)
    

if __name__ == "__main__":    
    master = Tk()
    # master.geometry("500x600")
    master.title('DB')
    Label(master, text="Enter your text : ",font=("Helvetica", 16)).grid(row=0)
    Label(master, text="DB output :",font=("Helvetica", 16)).grid(row=1)

    e1 = Entry(master)

    lbl = Label(master, text = '')
    # lbl.config(height=15, width=30)

    e1.grid(row=0, column=1,pady=10)
    lbl.grid(row=1, column=1,pady=10)

    Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
    Button(master, text='Stem and Show DB', command=show_outputs).grid(row=3, column=1, sticky=W, pady=4)

    mainloop()
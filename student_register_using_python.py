import csv  #CSV MODULE IMPORT 
import pandas as pd  #PANDAS MODULE IMPORT

#PANDAS MODULE PROVIDES A VERY EASY TO UNDERSTAND AND HIGHLY EFFICIENT WAY TO MANIPULATE CSV/EXCEL/TXT FILES.

#CODE TO APPEND DATA INTO A CSV
file_to_output = open('my_comp_project.csv',mode = "w",newline = '')

csv_writer = csv.writer(file_to_output, delimiter = ',')
csv_writer.writerow(['NAME','USN','CHEMISTRY','ELECTRONICS','COMPUTER SCIENCE','CIVIL','MATHEMATICS'])

print('''what would you like to do?
1) input a new piece of data
2) break, to exercise different options.
''')

x = input("option selected (1/break): ")
while True:
    if x == "1":
        print('''please enter the data in the given order:-''')
        print("Also, if any field is supposed to be empty, please type in 'not available' or 'na'")
        a = input("please enter the name: ")
        b = input("please enter the USN: ")
        c = input("please enter the chemistry marks: ")
        d = input("please enter the electronics marks: ")
        e = input("please enter the computer science marks: ")
        f = input("please enter the civil marks: ")
        g = input("please enter the mathematics marks: ")
        list1 = [a,b,c,d,e,f,g]
        csv_writer.writerow(list1)
        print("\n")
        print('''what would you like to do?
        1) input a new piece of data
        2) break, to exercise different options.
        ''')
        x = input("option selected (1/break): ")
    elif x=="break":
        break
    elif x != "break" or "1":
        print("invalid input. please try again")        
        x = input("option selected (1/break): ")
file_to_output.close()

#CODE TO REMOVE DATA

df = pd.read_csv('my_comp_project.csv',index_col = 'USN',na_values = ["","not available","na","NA","Not Available","NOT AVAILABLE"])
k = input("do you wish to delete any row from your file?(y/n): ")
while True:
    if k == "y":
        a = int(input("please enter the USN: "))

        if a in (df.index):
            df.drop([a],inplace = True)
            df.to_csv("my_comp_project.csv")  
            print("the desired row has been deleted...")
            print("\n")
            print(df)
            t = input("would you like to delete any more rows?(y/n): ")
            if t == "y":
                a
            elif t == "n":
                print("ok,saving changes...")
                break
            else:
                print("INVALID INPUT.PLESE TRY AGAIN.")
                t 

        elif a not in (df.index):
            print("INVALID INPUT. PLEASE TRY AGAIN.")
            a 

    elif k == "n":
        pass
        break
    
    else: 
        print("INVALID INPUT. PLEASE RECHECK AND TRY AGAIN.")
        k 


#CODE TO UPDATE

df = pd.read_csv("my_comp_project.csv",index_col = 'USN')
k = input("would you like to update any row from your file?(y/n): ")
while True:
    if k == "y":
        p = int(input("please enter the USN: "))
        l = list(df.loc[p].values)
        print('''what would you like to change?
        1) Name
        2) chem marks
        3) electronics marks
        4) comp science marks
        5) civil marks
        6) mathematics marks''')
        m = input("please enter your choice here: ")
        if m == "1":
            s = input("please enter the new name: ")
            l[0] = s
        elif m == "2":
            q = input("please enter the new chem marks: ")
            l[1] = q
        elif m == "3":
            w = input("please enter the new electronics marks: ")
            l[2] = w
        elif m == "4":
            y = input("please enter the new computer science marks: ")
            l[2] = y
        elif m == "5":
            j = input("please enter the new civil marks: ")
            l[2] = j
        elif m == "6":
            o = input("please enter the new mathematics marks: ")
            l[2] = o
        mystr = 'The final values are: '
        print(mystr + ', '.join(str(f) for f in l))
        df.loc[p,:] = l
        f = input("would you like to make more changes?(y/n): ")
        if f == "y":
            pass
        elif f == "n":
            break
    elif k == "n":
        print("Alright")    
        break
    else: 
        print("INVALID INPUT. PLEASE TRY AGAIN.")



df.to_csv("my_comp_project.csv")

#TO GET A PREVIEW OF THE CSV FILE:

df = pd.read_csv("my_comp_project.csv",index_col = 'USN',na_values = ["","not available","na","NA","Not Available","NOT AVAILABLE","nan"])

while True:
    p = input("would you like to have a preview?(y/n): ")
    if p == "y":
        print("\n")
        print(df)
        break
    elif p == "n":
        print("ok. Saving file...")
        break
    else:
        print("INVALID INPUT.PLEASE TRY AGAIN.")
        pass   




    



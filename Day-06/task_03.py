st = {}
while True:
    print("1.View all students and marks")
    print("2.View average marks")
    print("3.View topper")
    print("4.Add new Student")
    print("5.view Lowest scorer")
    print("6.Exit")
    
    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        print("Student data:", st)
    elif choice == "2":
        mars = list(st.values())
        avg = sum(mars) / y
        print("Average:", avg)
    elif choice == "3":
        t= max(st, key=st.get)
        print(f"Topper is {t} with {st[t]} marks.")
    elif choice == "4":
       o = input(f"Enter name of student: ")
       v = int(input("Enter marks: "))
       st[o] = v
    elif choice == "5":
       r= min(st, key=st.get)
       print(f"Lowest scorer is {r} with {st[r]} marks.")
    
    elif choice == "6":
        print("you exited")
        break
    
    


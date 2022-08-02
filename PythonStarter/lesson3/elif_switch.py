print("""Menu:
1. File
2. View
3. Exit
""")
choice = input('Enter your choice: ')
if choice == '1':
    print("you have selected 'File'")
elif choice == '2':
    print("you have selected 'View'")
elif choice == '3':
    print("stopping....")
else:
    print("incorrect choose")

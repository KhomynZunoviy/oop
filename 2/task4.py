phonebook = {  
    "Zunovii" : 938477566,
    "Vlad" : 938377264,
    "Nastya" : 947662781
}  

phonebook["Denys"] = 938273443  
del phonebook["Nastya"]  

if "Denys" in phonebook:  
    print("Денис занесений до телефонної книги.")
    
if "Nastya" not in phonebook:      
    print("Насті немає в телефонній книзі.")  
    print(phonebook)
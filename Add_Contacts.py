from Save_File import save_all_contact
from Duplicate_Numbers import duplicate_numbers

def add_contact(contact_list):
    name = str(input("Enter your name: "))
    email = str(input("Enter your email: "))
    phone_number = int(input("Enter your phone number: "))
    if duplicate_numbers(contact_list, phone_number):
        print("Phone number already exists. Please enter a different number.")
        return contact_list  # Return the list without adding the duplicate contact
    address = str(input("Enter your address: "))
    
    

    contact = {
        "Name": name,
        "Email": email,
        "Phone Number": phone_number,
        "Address": address
    }
    contact_list.append(contact)
    save_all_contact(contact_list)
    print("COntact Added Successfully")
    print()
    
    return contact_list

    

    


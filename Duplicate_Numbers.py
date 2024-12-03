def duplicate_numbers(contact_list,phone_number):
    for contact in contact_list:
        if contact["Phone Number"] == phone_number:
            return True
    return False
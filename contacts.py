# contacts.py
# Author: Alex Jun  
# Date: 02/20/2024
# Purpose: Module for Employee Contact List

def add_contact(contact_dict, / , *, id, first_name, last_name):
    if id in contact_dict:
        return 'error'
    contact_dict[id] = [first_name, last_name]
    return contact_dict[id]

def modify_contact(contact_dict, /, *, id, first_name, last_name):
    if id not in contact_dict:
        return 'error'
    contact_dict[id] = [first_name, last_name]
    return contact_dict[id]

def delete_contact(contact_dict, /, *, id):
    if id not in contact_dict:
        return 'error'
    deleted_value = contact_dict.pop(id)
    return deleted_value

def sort_contacts(contact_dict, /):
    sorted_dict = dict(sorted(contact_dict.items(), key=lambda x: (x[1][1], x[1][0])))
    return sorted_dict

def find_contact(contact_dict, / , * , find):
    found_dict = {}
    find_lower = str(find).lower() 
    for key, value in contact_dict.items():
        if str(find).isdigit() and key == int(find):
            found_dict[key] = value
        elif find_lower in value[0].lower() or find_lower in value[1].lower() or str(find) == str(key):
            found_dict[key] = value
    sorted_found_dict = dict(sorted(found_dict.items(), key=lambda x: (x[1][1], x[1][0])))
    return sorted_found_dict

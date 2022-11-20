import names

def search(gender,types,text):
    Gender = gender.get()
    Type = types.get()

    if Gender == 'Male' and Type == "Full Name":
        name = names.get_full_name(gender="male")
        text.insert('end', name+"\n")
    elif Gender == 'Male' and Type == "First Name":
        name = names.get_first_name()
        text.insert('end', name+"\n")
    elif Gender == 'Male' and Type == "Last Name":
        name = names.get_last_name()
        text.insert('end', name+"\n")

    elif Gender == 'Female' and Type == "Full Name":
        name = names.get_full_name(gender="female")
        text.insert('end', name+"\n")
    elif Gender == 'Female' and Type == "First Name":
        name = names.get_first_name()
        text.insert('end', name+"\n")
    elif Gender == 'Female' and Type == "Last Name":
        name = names.get_last_name()
        text.insert('end', name+"\n")

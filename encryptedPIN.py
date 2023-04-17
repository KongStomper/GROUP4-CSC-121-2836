import bcrypt

def login(id, s_list):
    # Prompt to enter their PIN
    pin = input("Enter your PIN: ")

    # Finds the student with the matching ID
    for s in s_list:
        if s['id'] == id:
            student = s
            break
    else:
        print("Invalid ID or PIN.")
        return False

    # Verify the encrypted PIN using bcrypt
    if bcrypt.checkpw(pin.encode('utf-8'), student['pin'].encode('utf-8')):
        print("Verification successful.")
        return True
    else:
        print("Invalid ID or PIN.")
        return False

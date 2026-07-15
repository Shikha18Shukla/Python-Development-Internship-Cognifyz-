print("========== EMAIL CHECK ==========")

def check_email(address):
    address = address.strip()

    # Checking if there is exactly one '@'
    if address.count("@") != 1:
        return False
    username, domain = address.split("@")
    # Username and domain should not be empty
    if username == "" or domain == "":
        return False
    # Domain should contain a dot
    if "." not in domain:
        return False
    # Dot cannot be the first or last character of the domain
    if domain.startswith(".") or domain.endswith("."):
        return False
    # Reject spaces anywhere in the email
    if " " in address:
        return False
    return True


email_input = input("Enter an email address: ")
if check_email(email_input):
    print("The email address is valid.")
else:
    print("The email address is not valid.")
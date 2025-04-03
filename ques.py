# WILL RETURN PROMPT TO SEND TO AI
def questions():

    prompt = ""
    x = False

    print("\n\n----------QUESTIONS----------")

    # QUESTION 01
    while x == False:
        q = input("QUESTION 01 **Scanning Permission** – Do you grant the AI permission to scan your system, software, and configurations for potential vulnerabilities? (y/n): ").lower()

        if q == "y":
            prompt += "The user gives the tool permission to automatically change settings and execute commands as needed to patch vulnerabilities. Please explain to the user what you're doing as you're doing it."
            break
        
        elif q == "n":
            prompt += "The user does not give the tool permission to automatically change settings and execute commands. Please explain to the user step-by-step what they would need to do as if you were doing it yourself."
            break

        else:
            print("Invalid input, try again")




    # QUESTION 02
    while x == False:
        q = input("QUESTION 02 **Automation Preference** - Do you grant the AI permission to automatically change settings across your PC to patch vulnerabilities as needed? (y/n): ").lower()

        if q == "y":
            prompt += "Q#: y"
            break
        
        elif q == "n":
            prompt += "Q#: n"
            break

        else:
            print("Invalid input, try again")

    # QUESTION 03
    while x == False:
        q = input("QUESTION 03 **Scope of Scan** - Please select a scope that best fits your needs (1, 2, or 3)\n\t1 - Network settings ONLY\n\t2 - Network settings AND application settings ONLY\n\t3 - Network settings AND application settings AND OS settings : ").lower()

        if q == "1":
            prompt += "Q#: 1"
            break
        
        elif q == "2":
            prompt += "Q#: 2"
            break

        if q == "3":
            prompt += "Q#: 3"
            break

        else:
            print("Invalid input, try again")

    # QUESTION 04
    while x == False:
        q = input("QUESTION 04 **Exploitation Permissions** – Do you grant the AI permission to attempt exploitation of identified vulnerabilities to validate their severity? (y/n): ").lower()

        if q == "y":
            prompt += "Q#: y"
            break
        
        elif q == "n":
            prompt += "Q#: n"
            break

        else:
            print("Invalid input, try again")

    # QUESTION 05
    while x == False:
        q = input("QUESTION 05 **Exclusion Rules** – Are there any specific systems, data, or areas of your network that you would prefer to be excluded from the scan for confidentiality reasons? (y/n): ").lower()

        if q == "y":
            prompt += "Q#: y"
            break
        
        elif q == "n":
            prompt += "Q#: n"
            break

        else:
            print("Invalid input, try again")

    return prompt



# BEGINNING PROMPT & DISCLAIMER
print("Welcome, and thank you for using our AI penetration testing tool.\nDue to the nature of generative AI, we are not responsible for any damages done to any systems this tool is used on. \nIt has been designed to give you, the user, as much control over the depth and degree of invasion as possible. \nJust like any other application, it can be manipulated and used for harm. By using this tool, you agree to act morally and ethically while using it.\n\n")

input("Press Enter to continue...")

prompt = questions()

print(prompt)

input("")

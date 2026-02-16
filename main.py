from pyscript import document, display

def signup(e): # e for event handling
    document.getElementById('output1').innerHTML = ' ' 
    username = document.getElementById("user").value
    password = document.getElementById("pass").value

    if username == "" or password == "": # checks if the input is blank or not
        display("Input is blank.", target="output1")
        return

    if len(username) >= 7: # checks if the username has 7 characters
        if password.isalpha(): # checks if the password has at least one letter
            if password.isdigit(): # checks if the password has at least one number
                if len(password) >= 10: # checks if the password has 10 characters 
                    display("You have successfully made an account", target="output1")
                else: 
                    display(f'Please add {10 - len(username)} more characters.', target="output1")
            else:
                display("Password must contain at least one number.", target="output1")
        else:
            display("Password must contain at least one letter.", target="output1")
    else:
        display(f'Please add {7 - len(username)} more characters.', target="output1") 
        # shows how many more characters we need by subracting

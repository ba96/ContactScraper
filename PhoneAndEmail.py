#! python3

import re, pyperclip

# TODO: Created a regex for phone numbers
phoneRegex = re.compile(r'''
#415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345ext. 12345, x12345

(
((\d\d\d)|(\(\d\d\d\)))?    # area code (optional)
(\s|-|.)    #first seperator
\d\d\d    #first 3 digits
(-|.)    #second seperator
\d\d\d\d    #last 4 digits
(((ext(\.)?\s)|x)     #extension word-part + number-part
(\d{2,5}))?
)
''', re.VERBOSE)

# TODO: Create a regex for email addresses
emailRegex = re.compile(r'''
[a-zA-z0-9_.+]+ #name part 
@ # @ symbol
[a-zA-z0-9_.+]+ #domain name part
''',re.VERBOSE)

# TODO: Get the text off the clipboard
text = pyperclip.paste()

# TODO: Extract the email/phone from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])


# TODO: Copy the extracted email/phone to the clipboard

results = "\n".join(allPhoneNumbers) + "\n" + "\n".join(extractedEmail)
pyperclip.copy(results)
#print(extractedEmail)

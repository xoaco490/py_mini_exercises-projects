#! python3
import re
# Regex for phone numbers
phoneRegex = re.compile(r"""
# 415-555-000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345
#Usamos el | para demostrar un or
(
((\d\d\d)| (\(\d\d\d\)))?          #area dode (optional)
(\s|-)                               #first separator
\d\d\d                              #first 3 digits
-                                    #separator
\d\d\d\d                            #last 4 digits
(((ext(\.)?\s) |x)                   #extension word part(optional)
  (\d{2,5}))?                            #extension number part
)""", re.VERBOSE)
# Regex for email adresses
emailRegex = re.compile(r"""
#some.+_thing@something.com(\d{2,5}))?.com
[a-zA-Z0-9_.+]+     #name part
@                    #@ symbol 
[a-zA-Z0-9_.+]+     #domain name part""", re.VERBOSE)
#extract and paste phone and emailsadresses
text = ("""mi number is 123-123-1234 and my email is hellos@sasaf.gob and my other number is 435-145-1672 and my
secondary email is frotw@wtaw.com""")
numbersf = phoneRegex.findall(text)
emailsf = emailRegex.findall(text)
#antes aparecian los numeros mal, por eso se deben encapsular todos los grupos de phoneregex con ()
allPhoneNumbers = []
for phoneNumber in numbersf:
    allPhoneNumbers.append(phoneNumber[0])
print(allPhoneNumbers)
print(allPhoneNumbers, emailsf)

#copy all the numbers and emails in clean
results ='\n'.join(allPhoneNumbers)+ '\n' + '\n'.join(emailsf)
print(results)


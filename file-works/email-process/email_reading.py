fr_emails="file-works\\email-process\\emails.txt"
fw_outlook="file-works\\email-process\\outlook.txt"
fw_gmail="file-works\\email-process\\gmail.txt"
fw_yahoo="file-works\\email-process\\yahoo.txt"

fr=open(fr_emails,"r")
fw_outlook=open(fw_outlook,"w")
fw_gmail=open(fw_gmail,"w")
fw_yahoo=open(fw_yahoo,"w")

for line in fr:
    mail=line.rstrip("\n")
    if mail.endswith("outlook.com"):
        fw_outlook.write(mail + "\n")
    elif mail.endswith("gmail.com"):
        fw_gmail.write(mail+"\n")
    elif mail.endswith("yahoo.com"):
        fw_yahoo.write(mail+"\n")
print("program ends")

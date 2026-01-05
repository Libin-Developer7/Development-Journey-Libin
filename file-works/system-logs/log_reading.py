logs_path="file-works\\system-logs\\logs.txt"
info_path="file-works\\system-logs\\info.txt"
warning_path="file-works\\system-logs\\warning.txt"
error_path="file-works\\system-logs\\error.txt"

fr=open(logs_path,"r")
fw_info=open(info_path,"w")
fw_warning=open(warning_path,"w")
fw_error=open(error_path,"w")

for line in fr:
    logs=line.rstrip("\n")
    if "INFO" in logs:
        fw_info.write(logs+"\n")
    elif "ERROR" in logs:
        fw_error.write(logs+"\n")
    elif "WARNING" in logs:
        fw_warning.write(logs+"\n")
print("program ends")
        
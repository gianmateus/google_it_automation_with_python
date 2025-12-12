import re

# result = re.search(r"aza", "plaza")
# print(result)

# print(re.search(r"^x", "xenon"))

# print(re.search(r"p.ng", "penguin"))

# print(re.search(r"p.ng", "clapping"))
# print(re.search(r"p.ng", "sponge"))
# print(re.search(r"p.ng", "Pangaea", re.IGNORECASE))
# print(re.search(r"Py.*n", "Pygmalion"))
# print(re.search(r"Py.*n", "Python Programming")) #ele pega o maximo possivle de caracterer
# print(re.search(r"o+l+", "goldfish"))
# print(re.search(r"\.com", "google.com"))
# print(re.search(r"\w*", "This is an example"))
# print(re.search(r"\w*", "And_this_is_another"))
# print(re.search(r"A.*a", "Azerbaijan"))
# print(re.search(r"^A.*a$", "Azerbaijan"))
# print(re.search(r"^A.*a$", "Austrailia"))

# print(re.search(r"[a-zA-Z]{5}","a scary ghost appeared"))
# print(re.findall(r"[a-zA-Z]{5}","a scary ghost appeared"))
# print(re.findall(r"\w{5,10}", "I really like strawberries"))
# print(re.findall(r"\w{5,}", "I really like strawberries"))
# print(re.search(r"s\w{,20}", "I really like strawberries"))

import re
log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
result = re.search(regex, "A completely different string that also has numbers [34567]")
result = re.search(regex, "99 elephants in a [cage]")
def extract_pid(log_line):
    regex = r"\[(\d+)\]"
    result = re.search(regex, log_line)
    if result is None:
        return ""
    return result[1]
print(extract_pid(log))
print(extract_pid("99 elephants in a [cage]"))
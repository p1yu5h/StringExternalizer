f_in = open("sample.txt", "r")
f_out = open("output.txt", "w+")
keyword = input("Enter keyword: ")
for line in f_in:
    if (line.strip()):
        text = "<string name=\"" + keyword + "\">" + line.strip().lstrip() + "</string>\n"
        f_out.write(text)
print("Done!")
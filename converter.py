f_in = open("sample.txt", "r")
f_out = open("output.txt", "w+")
keyword = input("Enter keyword: ")
i = 0
for line in f_in:
    if (line.strip()):
        i+=1
        text = "<string name=\"" + keyword + str(i) + "\">" + line.strip().lstrip() + "</string>\n"
        f_out.write(text)
print("Done!")
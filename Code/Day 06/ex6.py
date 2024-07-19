filenames = ['doc.txt', 'report.txt', 'presentation.txt']

for f in filenames:
    file = open(f, "w")
    file.write("Hello")
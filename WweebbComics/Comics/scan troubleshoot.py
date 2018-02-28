
def resultpage(request, job):


    from openpyxl import load_workbook
    file = open("job-name.html")

    wb = load_workbook('Book 2.xlsx')
    sheet_ranges = wb['Sheet1']


    job = ('searchbox')
    n = int(0)
    suffix = 'job'
    row = n

    result = sheet_ranges['B'][row]

    multiple_cells = sheet_ranges['A1':'A294']
    for index, row in enumerate(multiple_cells):

        for zccell in row:

            if job.lower() in [zccell.value.lower()]:
                row = index

                result = sheet_ranges['B'][row]
                output = ("<p>" + job + " has a " + str(result.value) + "% chance to be automated " + "</p>")

                file.write("<!DOCTYPE html>")
                file.write("<style>")
                file.write("body { background-color: rgb(198, 202, 201  );} ")
                file.write("</style>")
                file.write("<head>")
                file.write(" <title> Results page </title>")
                file.write("</head>")
                file.write("<body>")
                file.write("<center> <h1>Your Results are below</h1> </center> ")
                file.write("<center>" + output + "</center>")
                file.write("</body>")
                file.write("</html>")
                file.close()





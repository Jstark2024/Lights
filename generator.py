import os
from glob import iglob
from pathlib import Path
from http.server import HTTPServer, SimpleHTTPRequestHandler
from timeit import default_timer

# If testing, leave blank, otherwise, set to '/' + your GitHub repo name if hosting on GitHub pages
REPO_NAME = ""
start = default_timer()

with open("template.html") as file:
    template = file.read()

# Iterate though every source file
for srcFile in iglob("src/**/*.txt", recursive=True):
    srcFile = Path(srcFile)
    dstPath = str(srcFile.parent).replace("src", "public") + "/" + srcFile.stem + ".html"
    htmlOut = ""
    with open(srcFile) as file:
        # Iterate through every row
        for row in file.readlines():
            # iterate through every column (cell) in row
            htmlOut += "<tr>" + "".join(map(lambda cell: "<td>" + cell.strip() + "</td>", row.split("\t"))) + "</tr>"

    htmlOut += "</table>"
    os.makedirs(os.path.dirname(dstPath), exist_ok=True)
    with open(dstPath, 'w') as file:
        # fill in template information & save
        file.write(template.replace("{{content}}", htmlOut).replace("{{root}}", REPO_NAME))

# with open("public/.nojekyl", 'w'):
#     pass  # Needed so that GitHub pages doesn't interpret website weirdly
#
# with open("public/stylesheet.css", 'w') as file:
#     file.write("table {border-collapse: collapse} td {border: 1px solid black}")

print("Generated files in", default_timer() - start, "seconds")
if not os.getenv('CI'):
    os.chdir("public")
    httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
    print("Testing server listening on http://localhost:8000")
    httpd.serve_forever()

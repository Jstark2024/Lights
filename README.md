# Simple Static Site Generator

Can only generate off of 1 template, `template.html`. Every text file in `/src` will be converted to an HTML table
at every tab character. That means you can copy/paste data from Excel into the text files. Template will fill in
`{{content}}` (no whitespace) with the table, and `{root}` with the `REPO_NAME` variable in `generator.py`

There is no hot reload, so the program must be re-ran every time a change is made. Push to GitHub and change the
`REPO_NAME` variable in `generator.py` to work with GitHub pages.

Licence: Permission is granted to use, modify, and distribute as long as credit is given to [funblaster22]()https://github.com/funblaster22
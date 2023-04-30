abstractFile = open("Abstract.html", "r", encoding="utf8")
textToAdd = abstractFile.read()
abstractFile.close()

mainFile = open("docs/index.html", "w", encoding="utf8")
title = 'Становление человечества' # Enter title
mainFile.write('<!DOCTYPE html>\n<html>\n\t<head>\n\t\t<meta charset="utf-8">\n\t\t<title>Конспект '+title+'</title>\n\t\t<link rel="stylesheet" href="style.css">\n\t</head>\n\t<body>\n\t\t<div class="MyDiv">\n')
mainFile.write(textToAdd)
mainFile.write('\n\t\t</div>\n\t</body>\n</html>')
mainFile.close()

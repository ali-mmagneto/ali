import re

# Metin dosyasını aç
file = open("Disney Plus Captureli.txt",'r')

# Dosyanın içeriğini oku
text = file.read()

# MailPass eşleştirmek için Regex
matches = re.findall(r'(\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}\b:[^"\r\s]*)', text)

# Çıktı dosyasına yaz
file2 = open('output.txt','w+')

# Eşleştir ve göm
for i in matches:
    file2.write(i + '\n')

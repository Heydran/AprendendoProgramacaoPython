import os
msg = input("Qual a mensagem de atualização ")
os.system("git config --global user.name ”André Feuzer”")
os.system("git config --global user.email andre.heydran@gmail.com")
os.system("git add *")
m ="git commit -m " + "\'" + " msg" + "\'"
os.system(m)
os.system("git push")

os.system("git config --global user.name ”FULADO”")
os.system("git config --global user.email FULAON.CICLANO@mail.com")

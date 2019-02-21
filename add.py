import os
msg = input("Qual a mensagem de atualização ")
os.system("git add *")
m ="git commit -m " + "\'" + " msg" + "\'"
os.system(m)
os.system("git push")

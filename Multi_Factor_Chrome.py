import subprocess

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

# Lista de perfis(O range, vai definir a quantidade de perfís que você tem/quer abrir. Sempre altere de acordo com sua necessidade. Por exemplo, se você quer abrir 4 perfís, mude para 1, 5 e assim sucessivamente)

perfis = ["Profile {}".format(i) for i in range(1, 48)]

for perfil in perfis:
    comando = '"{}" --profile-directory="{}"'.format(chrome_path, perfil)
    subprocess.Popen(comando, shell=True)



import subprocess

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

# Lista de perfis
perfis = ["Profile {}".format(i) for i in range(1, 48)]

for perfil in perfis:
    comando = '"{}" --profile-directory="{}"'.format(chrome_path, perfil)
    subprocess.Popen(comando, shell=True)



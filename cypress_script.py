import subprocess
import os

script_directory = os.path.dirname(os.path.abspath(__file__))


def checkIfCypressExist():
    cypress_folder = os.path.join(script_directory, "node_modules", ".bin", "cypress")
    if os.path.isfile(cypress_folder):
        print("Cypress je instaliran u direktoriju skripte.")
        return True
    else:
        print("Cypress nije instaliran u direktoriju skripte.")
        return False


def checkIfYarnExist():
    print("Provjeravamo da li yarn postoji")
    return True


def checkIfPackageJsonExist():
    file_path = os.path.join(script_directory, "package.json")
    if os.path.exists(file_path):
        print("Package.json postoji")
        return True
    else:
        print("Package.json ne postoji.")
        return False


def yarn_init():
    cmd_command = f'cd "{script_directory}" && yarn init -y'
    process = subprocess.Popen(cmd_command, shell=True)
    process.wait()

    if process.returncode == 0:
        print("Yarn inicijalizacija je uspjesno dovrsena.")
    else:
        print("Pogreska prilikom yarn inicijalizacije.")


def cypressRecorderInstall():
    cmd_command = f'cd "{script_directory}" && yarn add @cypress/chrome-recorder'
    process = subprocess.Popen(cmd_command, shell=True)
    process.wait()
    if process.returncode == 0:
        print("Cypress recorder je uspjesno instaliran.")
    else:
        print("Pogreska prilikom instalacije Cypress recordera.")


def convertJsonToCypress(folder, filename):
    print("Prabacujem datoteku " + filename + " u cypress test...")
    cmd_command = f'cd "{folder}" && npx @cypress/chrome-recorder {filename} -o=./'
    print(cmd_command)
    process = subprocess.run(cmd_command, shell=True)
    if process.returncode == 0:
        print(filename + " je uspjesno prebacena u cypress test.")
    else:
        print("Pogreska prilikom prebacivanja " + filename + " u cyperss test.")


def checkIfCypressRecorderExist():
    cypress_folder = os.path.join(
        script_directory, "node_modules", "@cypress", "chrome-recorder"
    )
    if os.path.exists(cypress_folder):
        print("Cypress recorder je instaliran u direktoriju skripte.")
        return True
    else:
        print("Cypress recorder nije instaliran u direktoriju skripte.")
        return False

def checkForIgnoredFolders(path):
    values = ["node_modules", ".vscode"]
    for value in values:
        if value.lower() in path.lower():
            return True
    return False



def findAllFoldersAndFiles():
    print("Dohvacam sve mape..")
    print("--------------------")

    folders = []

    for root, dirnames, _ in os.walk(script_directory):
        for dirname in dirnames:
            folder_path = os.path.join(root, dirname)
            if checkForIgnoredFolders(folder_path) == False:
                folders.append(folder_path)

    if len(folders) == 0:
        print("Nema pronadjenih mapa.")
    else:
        for folder in folders:
            print("Mapa: ", os.path.basename(folder))
            for root, dirnames, filenames in os.walk(folder):
                if len(filenames) != 0:
                    for filename in filenames:
                        file_path = os.path.join(folder, filename)
                        if os.path.exists(file_path) and filename.endswith(".json"):
                            print("Pronadjena datoteka: ", filename)
                            convertJsonToCypress(folder, filename)
                            print("Brisem - " + file_path)
                            os.remove(file_path)
                        else:
                            print("Nema datoteka koje zavrsavaju s .json")
                else:
                    print("U folderu: " + os.path.basename(folder) + " nema datoteka.")
            print("--------------------")


def installCypress():
    if checkIfYarnExist():
        print("Instaliravam cypress...")
        cmd_command = f'cd "{script_directory}" && yarn add cypress'
        process = subprocess.Popen(cmd_command, shell=True)
        process.wait()
        if process.returncode == 0:
            print("Cypress je uspjesno instaliran.")
        else:
            print("Pogreska prilikom instalacije Cypress-a.")
    else:
        print("Instaliravam yarn..")
        yarn_init()


while True:
    if checkIfPackageJsonExist():
        if checkIfCypressExist():
            if checkIfCypressRecorderExist():
                findAllFoldersAndFiles()
                break;
            else:
                while True:
                    answer = input("Instaliram Cypress recorder? (Da/Ne): ")
                    if answer.lower() == "da":
                        print("Instaliravam cypress recorder...")
                        cypressRecorderInstall()
                        break
                    elif answer.lower() == "ne":
                        print("Cypress recorder neće biti instaliran.")
                        break
                    else:
                        print("Nepoznat odgovor. Molimo unesite 'da' ili 'ne'.")
        else:
            while True:
                answer = input("Instaliram Cypress? (Da/Ne): ")
                if answer.lower() == "da":
                    installCypress()
                    break
                elif answer.lower() == "ne":
                    print("Cypress neće biti instaliran.")
                    break
                else:
                    print("Nepoznat odgovor. Molimo unesite 'da' ili 'ne'.")
    else:
        while True:
            answer = input("Inicijaliziram package.json? (Da/Ne): ")
            if answer.lower() == "da":
                print("Inicijaliziram package.json...")
                yarn_init()
                break
            elif answer.lower() == "ne":
                print("Package.json neće biti inicijaliziran.")
                break
            else:
                print("Nepoznat odgovor. Molimo unesite 'da' ili 'ne'.")
    
    while True:
       break;
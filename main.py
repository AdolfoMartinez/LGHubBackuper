import shutil, sys, os, getpass

user = getpass.getuser()
#LGHUB_Path = r"C:\Program Files\LGHUB"
LGHUB_Profile_Path = f"C:\\Users\\{user}\\AppData\\Local\\LGHUB"
restore_data = os.getcwd() + "\\" + "backup_data"

def checkAdminStatus():
    try:
        with open (r"C:\Windows\System32\Drivers\etc\hosts", "w", encoding = "utf-8") as file:
            print("Admin rights granted.")
            return True
    except:
        print("Admin rights didn't granted.\nTry running the script as admin.")
        return False

def copyFiles(checkAdminStatus, src=LGHUB_Profile_Path, dst=restore_data):
    if checkAdminStatus():
        print("Copying data...")
        if os.path.exists(dst):
            shutil.rmtree(dst)
        shutil.copytree(src, dst)
        print("Done")

def restoreFiles(checkAdminStatus, src=restore_data, dst=LGHUB_Profile_Path):
    if checkAdminStatus():
        print("Restoring data...")
        try:
            if os.path.exists(dst):
                shutil.rmtree(dst)
            shutil.copytree(src, dst)
            print("Done")
        except:
            print("Can't write some files... maybe LGHub is runnig?")

if __name__ == "__main__":
    user_input = int(input(f"Hi {user} what do you want to do? \n\t[1] Backup data \n\t[2] Restore data\n\t[9] Exit\nSelection: "))
    if user_input == 1:
        copyFiles(checkAdminStatus)
    elif user_input == 2:
        restoreFiles(checkAdminStatus)
    else:
        pass
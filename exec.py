# This is the code run to create an executable

# to build an executable:
# -----------------------
# distribution mode: splash screen, single file and no console
# pyinstaller --name wezel --clean --onefile --noconsole --additional-hooks-dir=. --noconfirm --splash wezel.jpg exec.py

# debug mode: not single file & no splash screen
# pyinstaller --name wezel --clean --noconsole --additional-hooks-dir=. --noconfirm exec.py

# After this, you should see a dist folder which contains a link to the executable wezel.exe
# Troubleshoot: if pyinstaller throws an error, try deleting "build" and "dist" folders before running this command.


import wezel
import menu

if __name__ == "__main__":

    app = wezel.app()
    #app.set_menu(wezel.menu.menubar.default) # builds default menubar from wezel package
    app.set_menu(menu.default) # builds default menubar from menu.py script (copied from wezel package)
    #app.set_menu(menu.custom) # builds custom (with HelloWorld) menubar from menu.py script
    app.show()

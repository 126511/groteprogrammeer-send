import requests, json, sys

def check_username(username):
    link = "http://127.0.0.1:8000/check_username/" + username
    r = requests.get(link)
    
    if r.status_code != 200:
        print("Username not found")

def get_key():
    r = requests.get("http://127.0.0.1:8000/generate_key/")
    return r.cookies['key']

file = sys.argv[1]
argv = sys.argv[2:]


""" Send a file (argument) to groteprogrammeer.nl """
print(file)
print(argv)

# Open file
f = open(file)
result = str(f.read())

# Establish key
key = get_key()

# Get username
while True:
    username = input("Enter your username on groteprogrammeer.nl: ")
    link = "http://127.0.0.1:8000/check_username/" + username
    r = requests.get(link)

    if r.status_code == 200:
        break
    print("Username not found, try again")

# Make a list of all the files as strings
files = {}

for arg in argv:
    g = open(arg)
    files[arg] = g.read()
    g.close()

# Format data
data = {'key':key, 'username':username, 'result':result, 'files':str(json.dumps(files))}

# Post request to website
r = requests.post("http://127.0.0.1:8000/input/", data=data)

if r.status_code == 200:
    print("Everything went well.")
else:
    print("Something went wrong, please try again.")

# Close file
f.close()

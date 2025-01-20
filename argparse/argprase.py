user_name = 'Sanjay'
password = 'Sanjay@123'
server_name = 'isdad.mydomain.in'

# print(f
#       """
#       The server details login are:
#       user name = {user name}
#       password = {password}
#       server_name = {'isdad.mydomain.in'}
#       """

# #Method 2 - runtime() user can enter their output without changing the main code
# user_name = input("Enter username:")
# password = input("Enter password:")
# server_name = input("Enter server name:") 

#Method 3 - input()-runtime with getpass for password.
# import getpass
# user_name= input('Enter username:')
# password = getpass.getpass("Enter password:")
# server_name = input("Enter server name:") 

#Method 4 -sys.argv#srcipt runs whenever we wants
# import sys
# if len(sys.argv) != 4:
#     print('Help:')
#     print(f"python{help} username password servername")
#     sys.exit(1)
# user_name=sys.argv[1]
# password=sys.argv[2]
# server_name=sys.argv[3]

#Method 5 argparse
import argparse
parser = argparse.ArgumentParser(
    description= "Details to login to Server",# text shown before help
    epilog= "------Please follow help doc----"#text shown after the help text
)
parser.add_argument("-u","- - user_name",help = 'login user name',type=str,required=True)
parser.add_argument("-p",'- - password',help = 'login user password',type=str,required=True)    
parser.add_argument(
                        '-s',
                        "- - servername",
                        help='server_name',
                        type=str,
                        required=False,
                        default="www.google.com"
                    )

args = parser.parse_args()
user_name = args.username
password = args.password
server_name = args.servername                




# Method -1 HardCoding
print(f""" The server details are ,
      user_name = {user_name}
      password = {password}
      server_name = {server_name}""")


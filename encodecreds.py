# -*- coding: utf-8 -*-
import getpass
import base64

def get_credentials():
    user = raw_input("Gmail address: ")
    pwd = getpass.getpass("Gmail password: ")
    return user, pwd


def encode_credentials():
    # Get creds
    user, pwd = get_credentials()

    # Encode to textsafe
    bu = base64.b64encode(user)
    bp = base64.b64encode(pwd)

    # Write out to file
    uf = open("username", "w")
    pf = open("password", "w")

    uf.write(bu)
    pf.write(bp)
    
    uf.close()
    pf.close()

if __name__ == "__main__":
    encode_credentials()
    

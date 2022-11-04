#!/usr/bin/python3
import os

URL="https://templatemo.com/tm-zip-files-2020/templatemo_520_highway.zip"
DIR="templatemo_520_highway"
PACKAGES=["apache2","wget","zip"]

print("\nTASK : Deploy tooplate website on local server\n")
print("\n$ Updating ...\n")
os.system("apt update")
print("\n$ Installing packages ...\n")

for package in PACKAGES:
    print("\n$ Installing {} package ...\n".format(package))
    os.system("apt install {} -y".format(package))

print("\n$ Getting Artifacts fron tooplate.com ...\n")
os.system("wget -O tooplate.zip {}".format(URL))
print("\n$ Unziping ...\n")
os.system("unzip tooplate.zip")
# DIR=cmdline("ls -t | cut -d" " -f1 | grep -v *.zip")
print("\n$ Deploying Artifacts to apache2 Server ...\n")
exitcode=os.system("cp -r ./{}/* /var/www/html/".format(DIR))

if exitcode == 0:
    print("\n$ Congrats Your Artifact Deployed To apache2 server successfully...\n")

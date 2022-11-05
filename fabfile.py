from fabric.api import *

def remote_exec():
    print "System Info"
    run("hostname")
    run("whoami")
    run("uptime")
    run("pwd")
    run("df -h")
    run("free -m")
    sudo("yum install mariadb-server -y")
    sudo("systemctl start mariadb")
    sudo("systemctl enable mariadb")



def websetup(URL,DIR):
    print("\n$ Deployment of web has started ...\n")
    run("hostname")
    local("apt install zip unzip -y")
    print("\n$ Installing Dependency ... \n")
    sudo("yum install httpd wget unzip -y")
    print("\n$ Starting And Enabling httpd service ... \n")
    sudo("systemctl start httpd")
    sudo("systemctl enable httpd")
    print("\n$ Downloading Artifact locally ...\n")
    local("wget -O website.zip {}".format(URL))
    local("unzip -o website.zip")

    print("\n$ Taking Help from helper function to get into the directory ...\n")

    with lcd(DIR):
        print("\n$ Using lcd helper function for getting into local dir and doing tasks...\n")
        local("pwd")
        local("zip -r tooplate.zip *")
        print("\n$ Zipping done ...\n")
        print("\n$ Now Putting [put method] tooplate.zip into remote /var/www/html/ ...\n")
        put("tooplate.zip","/var/www/html/",use_sudo=True)



    with cd("/var/www/html/"):
        print("\n$ Using cd helper function for getting into remote dir and doing tasks...\n")
        sudo("unzip -o tooplate.zip")
        sudo("ls")
        print("\n$ Removing tooplate.zip file ...\n")
        sudo("rm -r tooplate.zip")
        sudo("ls")

    sudo("systemctl restart httpd")

    print("\n $ You Have successfully Deployed Your Website ...\n")

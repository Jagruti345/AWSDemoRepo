import paramiko

HOST = "YOUR_EC2_PUBLIC_IP"
USERNAME = "ubuntu"
KEY = "aws-key.pem"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(
    hostname=HOST,
    username=USERNAME,
    key_filename=KEY
)

commands = [

    "cd /home/ubuntu/aws-nginx-deployment && git pull origin main",

    "sudo cp -r /home/ubuntu/aws-nginx-deployment/* /var/www/html/",

    "sudo systemctl reload nginx"

]

for command in commands:

    print("Running:", command)

    stdin, stdout, stderr = ssh.exec_command(command)

    print(stdout.read().decode())

    print(stderr.read().decode())

ssh.close()

print("Deployment Completed")
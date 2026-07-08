import os
import tempfile
import paramiko

HOST = os.environ["EC2_HOST"]
USERNAME = os.environ["EC2_USERNAME"]
PRIVATE_KEY = os.environ["PRIVATE_KEY"]

with tempfile.NamedTemporaryFile(delete=False, mode="w") as key_file:
    key_file.write(PRIVATE_KEY)
    key_path = key_file.name

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(
    hostname=HOST,
    username=USERNAME,
    key_filename=key_path
)

commands = [
    "cd /home/ubuntu/AWSDemoRepo && git pull origin main",
    "sudo cp -r /home/ubuntu/AWSDemoRepo/* /var/www/html/",
    "sudo systemctl reload nginx"
]

for command in commands:
    print(f"Running: {command}")
    stdin, stdout, stderr = ssh.exec_command(command)
    print(stdout.read().decode())
    print(stderr.read().decode())

ssh.close()

print("Deployment Completed")

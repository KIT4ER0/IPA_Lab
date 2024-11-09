from netmiko import ConnectHandler
import os

devices = [
    {
        'device_type': 'cisco_ios',
        'ip': '172.31.104.4',
        'username': 'admin',
        'password': 'cisco',
    }
]

config_dir = 'config'

for device in devices:
    device_ip = device['ip']
    config_file_path = os.path.join(config_dir, f"{device_ip}-exercise-nat.txt")
    
    if os.path.exists(config_file_path):
        with open(config_file_path) as f:
            config_commands = f.read().splitlines()

        with ConnectHandler(**device) as net_connect:
            net_connect.enable()
            net_connect.send_config_set(config_commands)
            print(f"Configuration applied to {device_ip}")
    else:
        print(f"Configuration file {config_file_path} does not exist.")

print("All configurations have been applied.")

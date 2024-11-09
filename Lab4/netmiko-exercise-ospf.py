from netmiko import ConnectHandler

# Define device parameters
R1 = {
    'device_type': 'cisco_ios',
    'ip': '172.31.104.3',
    'username': 'admin',
    'password': 'cisco',
}

R2 = {
    'device_type': 'cisco_ios',
    'ip': '172.31.104.4',
    'username': 'admin',
    'password': 'cisco',
}

# Connect to R1 and configure OSPF
net_connect_R1 = ConnectHandler(**R1)
net_connect_R1.enable()
config_commands_R1 = [
    'router ospf 1 vrf control-data',
    'network 192.168.1.0 0.0.0.255 area 0',
    'network 192.168.2.0 0.0.0.255 area 0',
]
net_connect_R1.send_config_set(config_commands_R1)

# Connect to R2 and configure OSPF
net_connect_R2 = ConnectHandler(**R2)
net_connect_R2.enable()
config_commands_R2 = [
    'router ospf 1 vrf control-data',
    'network 192.168.2.0 0.0.0.255 area 0',
    'network 192.168.3.0 0.0.0.255 area 0',
    'default-information originate',
]
net_connect_R2.send_config_set(config_commands_R2)

# Disconnect from the devices
net_connect_R1.disconnect()
net_connect_R2.disconnect()

print("OSPF configuration on R1 and R2 is complete.")

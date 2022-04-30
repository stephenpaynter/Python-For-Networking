# Show ip interface brief with Python

from netmiko import ConnectHandler


IOSXE = {
    "device_type": "cisco_xe",
    "host": "sandbox-iosxe-recomm-1.cisco.com",
    "username": "developer",
    "password": "C1sco12345"
}


# Setup SSH conenction
net_connect = ConnectHandler(**IOSXE)

#  Register and send show ip interface brief and print output
output = net_connect.send_command('show ip int brief')
print (output)

# Terminate connection
net_connect.disconnect()

#!/bin/bash

# let jetson nano act as dhcp-server for eth connections
ip_address="192.168.2.1"
netmask="255.255.255.0"
dhcp_range_start="192.168.2.2"
dhcp_range_end="192.168.2.100"
dhcp_time="12h"
eth="eth0"

sudo ifconfig $eth $ip_address netmask $netmask

# remove default route created by dhcpcd
sudo ip route del 0/0 dev $eth &> /dev/null
sudo systemctl stop dnsmasq
sudo rm -rf /etc/dnsmasq.d/* &> /dev/null

echo -e "interface=$eth\n\
bind-interfaces\n\
server=176.103.130.130\n\
domain-needed\n\
bogus-priv\n\
dhcp-range=$dhcp_range_start,$dhcp_range_end,$dhcp_time" > /tmp/custom-dnsmasq.conf

sudo cp /tmp/custom-dnsmasq.conf /etc/dnsmasq.d/custom-dnsmasq.conf
sudo systemctl start dnsmasq

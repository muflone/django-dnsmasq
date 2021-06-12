# DHCP standard options

## Reference:

- [RFC 2939](https://www.iana.org/go/rfc2939)
- [Dynamic Host Configuration Protocol and Bootstrap Protocol Parameters](https://www.iana.org/assignments/bootp-dhcp-parameters/bootp-dhcp-parameters.xhtml) 

## Options
+-----+---------------------------------------------+------+--------------------------------+
| Dec | Name                                        | Type | Description                    |
+-----+---------------------------------------------+------+--------------------------------+
| 001 | Subnet Mask                                 | 4    | Subnet Mask Value
| 002 | Time Offset                                 | 4    | Time Offset in Seconds from UTC
| 003 | Router                                      | N    | N/4 Router addresses
| 004 | Time Servers                                | N    | N/4 Timeserver addresses
| 005 | Name Servers                                | N    | N/4 IEN-116 Server addresses
| 006 | DNS Servers                                 | N    | N/4 DNS Server addresses
| 007 | Log Servers                                 | N    | N/4 Logging Server addresses
| 008 | Quotes Servers                              | N    | N/4 Quotes Server addresses
| 009 | LPR Servers                                 | N    | N/4 Printer Server addresses
| 010 | Impress Servers                             | N    | N/4 Impress Server addresses
| 011 | RLP Servers                                 | N    | N/4 RLP Server addresses
| 012 | Host Name                                   | N    | Hostname string
| 013 | Boot File Size                              | 2    | Size of boot file in 512 byte chunks
| 014 | Merit Dump File                             | N    | Client to dump and name the file to dump it to
| 015 | Domain Name                                 | N    | The DNS domain name of the client
| 016 | Swap Server                                 | N    | Swap Server address
| 017 | Root Path                                   | N    | Path name for root disk
| 018 | Extension File                              | N    | Path name for more BOOTP info
| 019 | IP Layer Forwarding                         | 1    | Enable/Disable IP Forwarding
| 020 | Src route enabler                           | 1    | Enable/Disable Source Routing
| 021 | Policy Filter                               | N    | Routing Policy Filters
| 022 | Max DG Assembly                             | 2    | Max Datagram Reassembly Size
| 023 | Default IP TTL                              | 1    | Default IP Time to Live
| 024 | MTU Timeout                                 | 4    | Path MTU Aging Timeout
| 025 | MTU Plateau                                 | N    | Path MTU Plateau Table
| 026 | MTU Interface size                          | 2    | Interface MTU Size
| 027 | MTU Subnet                                  | 1    | All Subnets are Local
| 028 | Broadcast Address                           | 4    | Broadcast Address
| 029 | Mask Discovery                              | 1    | Perform Mask Discovery
| 030 | Mask Supplier                               | 1    | Provide Mask to Others
| 031 | Router Discovery                            | 1    | Perform Router Discovery
| 032 | Router Request                              | 4    | Router Solicitation Address
| 033 | Static Route                                | N    | Static Routing Table
| 034 | Trailers                                    | 1    | Trailer Encapsulation
| 035 | ARP Timeout                                 | 4    | ARP Cache Timeout
| 036 | Ethernet                                    | 1    | Ethernet Encapsulation
| 037 | Default TCP TTL                             | 1    | Default TCP Time to Live
| 038 | Keepalive Time                              | 4    | TCP Keepalive Interval
| 039 | Keepalive Data                              | 1    | TCP Keepalive Garbage
| 040 | NIS Domain                                  | N    | NIS Domain Name
| 041 | NIS Servers                                 | N    | NIS Server Addresses
| 042 | NTP Servers                                 | N    | NTP Server Addresses
| 044 | NETBIOS Name Servers                        | N    | NETBIOS Name Servers
| 045 | NETBIOS Dist Srv                            | N    | NETBIOS Datagram Distribution
| 046 | NETBIOS Node Type                           | 1    | NETBIOS Node Type
| 047 | NETBIOS Scope                               | N    | NETBIOS Scope
| 048 | X Window Font                               | N    | X Window Font Server
| 049 | X Window Manager                            | N    | X Window Display Manager
| 050 | Address Request                             | 4    | Requested IP Address
| 051 | Address Time                                | 4    | IP Address Lease Time
| 052 | Overload                                    | 1    | Overload "sname" or "file"
| 053 | DHCP Msg Type                               | 1    | DHCP Message Type
| 054 | DHCP Server Id                              | 4    | DHCP Server Identification
| 055 | Parameter List                              | N    | Parameter Request List
| 056 | DHCP Message                                | N    | DHCP Error Message
| 057 | DHCP Max Msg Size                           | 2    | DHCP Maximum Message Size
| 058 | Renewal Time                                | 4    | DHCP Renewal (T1) Time
| 059 | Rebinding Time                              | 4    | DHCP Rebinding (T2) Time
| 060 | Class Id                                    | N    | Class Identifier
| 061 | Client Id                                   | N    | Client Identifier
| 062 | NetWare/IP Domain                           | N    | NetWare/IP Domain Name
| 063 | NetWare/IP Option                           | N    | NetWare/IP sub Options
| 064 | NIS Domain Name                             | N    | NIS+ v3 Client Domain Name
| 065 | NIS Server Address                          | N    | NIS+ v3 Server Addresses
| 066 | TFTP Server Name                            | N    | TFTP Server Name
| 067 | Bootfile-Name                               | N    | Boot File Name
| 068 | Home Agent Addresses                        | N    | Home Agent Addresses
| 069 | SMTP Server                                 | N    | Simple Mail Server Addresses
| 070 | POP3 Server                                 | N    | Post Office Server Addresses
| 071 | NNTP Server                                 | N    | Network News Server Addresses
| 072 | WWW Server                                  | N    | WWW Server Addresses
| 073 | Finger Server                               | N    | Finger Server Addresses
| 074 | IRC Server                                  | N    | Chat Server Addresses
| 075 | StreetTalk Server                           | N    | StreetTalk Server Addresses
| 076 | STDA Server                                 | N    | ST Directory Assist. Addresses
| 077 | User Class                                  | N    | User Class Information
| 078 | SLP Directory Agent                         | N    | Directory agent information
| 079 | SLP Service Scope                           | N    | Service location agent scope
| 080 | Rapid Commit                                | 0    | Rapid Commit
| 081 | Client FQDN                                 | N    | Fully Qualified Domain Name
| 082 | Relay Agent Information                     | N    | Relay Agent Information
| 083 | iSNS                                        | N    | Internet Storage Name Service
| 085 | NDS Servers                                 | N    | Novell Directory Services
| 086 | NDS Tree Name                               | N    | Novell Directory Services
| 087 | NDS Context                                 | N    | Novell Directory Services
| 088 | BCMCS Controller Domain Name list           | S    | 
| 089 | BCMCS Controller IPv4 address option        | S    | 
| 090 | Authentication                              | N    | Authentication
| 093 | Client System                               | N    | Client System Architecture
| 094 | Client NDI                                  | N    | Client Network Device Interface
| 095 | LDAP                                        | N    | Lightweight Directory Access Protocol
| 097 | UUID/GUID                                   | N    | UUID/GUID-based Client Identifier
| 098 | User-Auth                                   | N    | Open Group's User Authentication
| 100 | PCode                                       | N    | IEEE 1003.1 TZ String
| 101 | TCode                                       | N    | Reference to the TZ Database
| 108 | IPv6-Only Preferred                         | 4    | Number of seconds that DHCPv4 should be disabled
| 109 | OPTION_DHCP4O6_S46_SADDR                    | 16   | DHCPv4 over DHCPv6 Softwire Source Address Option
| 112 | Netinfo Address                             | N    | NetInfo Parent Server Address
| 113 | Netinfo Tag                                 | N    | NetInfo Parent Server Tag
| 114 | DHCP Captive-Portal                         | N    | DHCP Captive-Portal
| 116 | Auto-Config                                 | N    | DHCP Auto-Configuration
| 117 | Name Service Search                         | N    | Name Service Search
| 118 | Subnet Selection Option                     | 4    | Subnet Selection Option
| 119 | Domain Search                               | N    | DNS domain search list
| 120 | SIP Servers DHCP Option                     | N    | SIP Servers DHCP Option
| 121 | Classless Static Route Option               | N    | Classless Static Route Option
| 122 | CCC                                         | N    | CableLabs Client Configuration
| 123 | GeoConf Option                              | 16   | GeoConf Option
| 124 | V-I Vendor Class                            | S    | Vendor-Identifying Vendor Class
| 125 | V-I Vendor-Specific Information             | S    | Vendor-Identifying Vendor-Specific Information
| 128 | TFTP Server IP address                      | S    | 
| 129 | Call Server IP address                      | S    | 
| 130 | Discrimination string                       | S    | 
| 131 | Remote statistics server IP address         | S    | 
| 132 | IEEE 802.1Q VLAN ID                         | S    | 
| 133 | IEEE 802.1D/p Layer 2 Priority              | S    | 
| 134 | Diffserv Code Point                         | S    | 
| 135 | HTTP Proxy for phone-specific applications  | S    | 
| 136 | OPTION_PANA_AGENT                           | S    | 
| 137 | OPTION_V4_LOST                              | S    | 
| 138 | OPTION_CAPWAP_AC_V4                         | N    | CAPWAP Access Controller addresses
| 139 | OPTION-IPv4_Address-MoS                     | N    | a series of suboptions
| 140 | OPTION-IPv4_FQDN-MoS                        | N    | a series of suboptions
| 141 | SIP UA Configuration Service Domains        | N    | List of domain names to search for SIP User Agent Configuration
| 142 | OPTION-IPv4_Address-ANDSF                   | N    | ANDSF IPv4 Address Option for DHCPv4
| 143 | OPTION_V4_SZTP_REDIRECT                     | N    | This option provides a list of URIs for SZTP bootstrap servers
| 144 | GeoLoc                                      | 16   | Geospatial Location with Uncertainty
| 145 | FORCERENEW_NONCE_CAPABLE                    | 1    | Forcerenew Nonce Capable
| 146 | RDNSS Selection                             | N    | Information for selecting RDNSS
| 147 | OPTION_V4_DOTS_RI                           | N    | The name of the peer DOTS agent.
| 148 | OPTION_V4_DOTS_ADDRESS                      | N    | N/4 IPv4 addresses of peer DOTS agent(s).
| 150 | TFTP server address                         | S    | 
| 150 | Etherboot                                   | S    | 
| 150 | GRUB configuration path name                | S    | 
| 151 | status-code                                 | N+1  | Status code and optional N byte text message describing status.
| 152 | base-time                                   | 4    | Absolute time (seconds since Jan 1, 1970) message was sent.
| 153 | start-time-of-state                         | 4    | Number of seconds in the past when client entered current state.
| 154 | query-start-time                            | 4    | Absolute time (seconds since Jan 1, 1970) for beginning of query.
| 155 | query-end-time                              | 4    | Absolute time (seconds since Jan 1, 1970) for end of query.
| 156 | dhcp-state                                  | 1    | State of IP address.
| 157 | data-source                                 | 1    | Indicates information came from local or remote server.
| 158 | OPTION_V4_PCP_SERVER                        | S    | Includes one or multiple lists of PCP server IP addresses; each list is treated as a separate PCP server.
| 159 | OPTION_V4_PORTPARAMS                        | 4    | This option is used to configure a set of ports bound to a shared IPv4 address.
| 161 | OPTION_MUD_URL_V4                           | N    | Manufacturer Usage Descriptions
| 208 | PXELINUX Magic                              | 4    | magic string = F1:00:74:7E
| 209 | PXELINUX Configuration File                 | N    | Configuration file
| 210 | PXELINUX Path Prefix                        | N    | Path Prefix Option
| 211 | PXELINUX Reboot Time                        | 4    | Reboot Time
| 213 | OPTION_V4_ACCESS_DOMAIN                     | N    | Access Network Domain Name
| 220 | Subnet Allocation Option                    | N    | Subnet Allocation Option
| 221 | Virtual Subnet Selection (VSS) Option       | S    | 

#!/bin/sh
# Insert into mysql vpn user info
# Create time 2017-03-22 11:34

# vpn user info
name=user
attr=User-Password
pass="vpnuserpassword"

# mysql login info
msbin=/usr/bin/mysql
msuser=radius
msdb=radius
mspass="mysqlpassword"

for ((i=1;i<31;i++));do
    $msbin -u $msuser -p$mspass -e "use radius;insert into radcheck (username,attribute,value) values ('$name$i','$attr','$pass');"
done

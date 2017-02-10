# Ansible hackathon

## Network configuration 


```
                                                 
                     [Ansible][mosquitto]    (          )    DNS
                     [Debian Linux]         (The Internet)-- 8.8.8.8
[Cumulus]            [VirtualBox]            (          )
10.20.0.111/16       10.20.11.1/16                |
    |                      |                      |
    |                      |       10.20.0.254/16 |
    +----------------------+---------------------[R]
```


## Port forwarding

```

                     port:18883        port:1883
 [Cumulus]------------>[VirtualBox]----->[mosquitto/DebianLinux]
                10.20.11.1            
```

## Ansible playbook

Just run "setup.sh" to install agent.py and agent.yaml onto Cumulus Linux.

- [playbook](./playbook.yaml)

Then run "/tmp/agent.py" on Cumulus and "mosquitto_sub -t log" on the Debian VM.

```
arao@debian:~/okinawa$ sudo apt-get install mosquitto-clients 
arao@debian:~/okinawa$ mosquitto_sub -t log
Hello World! I am Cumulus Linux.
Hello World:1486712935.12
Hello World:1486712936.12
Hello World:1486712937.13
Hello World:1486712938.13
Hello World:1486712939.13
Hello World:1486712940.13
    :
```

## TODO

Develop an Ansible module to redirect "tail -f /var/log/syslog" to MQTT server on the Debian VM.


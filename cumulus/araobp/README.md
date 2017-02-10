# Ansible hackathon (2017/2/9-10)

I attended "Ansible hackathon" that took place [here](https://www.google.co.jp/maps?biw=1280&bih=603&q=Okinawa+OpenLab&bav=on.2,or.&bvm=bv.146496531,d.dGc&um=1&ie=UTF-8&sa=X&ved=0ahUKEwjym-DAtIbSAhWBT7wKHXTBAzsQ_AUICCgD) in Okinawa.

## Goal

Just playing with Cumulus Linux is not fun for me.

I make Cumulus Linux speak "Hello World!".

## Network configuration

```
                              [Node-RED ]                                        
                     [Ansible][mosquitto]    (          )    DNS
                     [Debian Linux      ]   (The Internet)-- 8.8.8.8
[Cumulus]            [VirtualBox        ]    (          )
10.20.0.111/16       10.20.11.1/16                |
    |                      |                      |
    |                      |       10.20.0.254/16 |
    +----------------------+---------------------[R]
```

## Port forward setting

"Hello World" message is sent to Node-RED via MQTT server.
```

                     port:11883        port:1883
 [Cumulus]---Hello World--->[VirtualBox]----->[mosquitto/DebianLinux]--->Node-RED
                      10.20.11.1         
```

## Ansible playbook

Just run "setup.sh" to install Python modules, agent.py and agent.yaml onto Cumulus Linux.

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

## Hearing "Hello World" message

I ran Node-RED with "audio node" (Text-to-Speech) to hear the voice from Cumulus.

## TODO

(1) Modify "agent.py" to redirect "tail -f /var/log/syslog" or "tcpdump -i swp1 (netlink/pcap)" to Apache Kafka on the Debian VM. Yet another syslogd. Or just use fluentd.

(2) Develop an agent to redirect "cat /dev/serial/by-id/XXXXXX" to Apache Kafka on the Debian VM. I just want to collect data from sensors (accelerometer, gyroscope etc) attached to small routers.

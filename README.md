patrix is a simple command line client for Matrix written in perl. It can send text messages to rooms. I use it to send Zabbix alertes to a Matrix room, a bit like sendxmpp can do with XMPP.

It requires the following perl modules
  * LWP::UserAgent
  * HTTP::Request
  * Config::Simple
  * File::HomeDir
  * Getopt::Long
  * JSON

For now it's very limited, and can only send messages to a room. Here's the vailable options:

  * --user: specify the user you want to login as
  * --password: the password to auth against the HS
  * --server: the HS you want to connect to. Default is https://matrix.org
  * --access_token: can be used instead of --user and --password
  * --room: the room to which the message must be sent
  * --message: the text message you want to send. If you send something on stdin, it's assumed to be the text to send and this option is ignored
  * --debug: if present, will be verbose
  * --notice: send a notice instead of a message (more or less the same but the client can display it differently. Riot for example will not notify you for notices)
  * --conf: path to a conf file. Default conf file is ~/.patrixrc
  * --action: what to do. Valid actions are
    * send-msg (default): send the text message
    * get-access-token: just login and print the access token

All the available options can be set a the configuration file using a simple ini style format, eg

```
user=alert
password=p@ssw0rd
room=!BWdARvAgNQGgSjgtAG:matrix.domain.com
```

Options given on the command line take precedence over the config file

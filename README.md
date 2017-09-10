patrix is a simple command line client for [Matrix](https://matrix.org) written in perl. It can create and configure rooms, send text messages or files to rooms. I use it to send [Zabbix](https://www.zabbix.com) alerts to a Matrix room, a bit like [sendxmpp](https://github.com/lhost/sendxmpp) can do with XMPP.

It requires the following perl modules
  * LWP::UserAgent
  * HTTP::Request
  * Config::Simple
  * File::HomeDir
  * File::Basename
  * File::MimeInfo
  * Path::Tiny
  * Getopt::Long
  * URI::Escape
  * JSON
  * Term::ReadKey
  * Hash::Merge::Simple
  * Scalar::Util

Here're the vailable options:

  * --user: specify the user you want to login as
  * --password: the password to auth against the HS
  * --server: the HS you want to connect to. Default is https://matrix.org
  * --access_token: can be used instead of --user and --password
  * --room: the room to which the message must be sent. Can be a room ID or a room alias
  * --message: the text message you want to send. If you send something on stdin, it's assumed to be the text to send and this option is ignored
  * --debug: if present, will be verbose
  * --conf: path to a conf file. Default conf file is ~/.patrixrc
  * --file: if action is send-file, specify the path of the file to send
  * --invite: a matrix ID (@user:server.domain.tld) to invite in a room. Can be specified several times. Valid for create-room and modify-room
  * --name: set the name of a room. Valid for create-room and modify-room
  * --topic: set the topic of a room. Valid for create-room and modify-room
  * --alias: set an alias for a room. Valid for create-room and modify-room
  * --join_rules: change joining rules. Can be either public (anyone can join the room) or invite (you must be invited to join the room)
  * --perm: set power levels on the room. Can be specified several times. See examples
  * --perm_user: set user levels on the room. Can be specified several times. See examples
  * --perm_event: set power levels requires to send specific state events. Can be specified several times. See examples
  * --perm_reset: the default behavior of the various --perm args is to add or override specific permissions without changing the others already existing permission. If this flag is set, the previous permissions will be removed, and the one specified with the --perm arg will be applied. The only exception is for user power levels which are at least as high as the operator (including the operator). These user power levels will be kept even is --perm-reset is set
  * --federation: Enable the federation when creating a room. Default is enabled. Can be turned of with --no-federation
  * --action: what to do. Valid actions are
    * send-msg (default): send the text message
    * send-message: an alias for send-msg
    * send-notice: send a notice. Very similar to send-msg but the client may display it differently. Eg Riot will not notify you for notices
    * send-file: send a binary file. --file must be set
    * create-room: create a new room
    * modify-room: change an existing room (add an alias, set name, topic, join_rules, invite)
    * get-access-token: just login and print the access token
    * get-room-list: prints the list of public rooms of this server
    * get-room-id: resolve a room alias to its ID

All the available options can be set a the configuration file using a simple ini style format, eg

```
user=alert
password=p@ssw0rd
room=!BWdARvAgNQGgSjgtAG:matrix.domain.com
```

Options given on the command line take precedence over the config file

Examples:

  * Send the content of /var/log/boot.log to a room (as text)
```
cat /var/log/boot.log | patrix --room='#bootlogs:matrix.domain.com' --action=send-notice
```
  * Send a file (here, the room name must be specified in the config file)
```
patrix --action=send-file --file=/home/dani/archive.tgz --user=dani --password=secret --server=matrix.domain.com
```
  * Send a simple text message, and enable debuging
```
patrix --debug --message="Hello World"
```
  * Create a new room, set its name and invite a Matrix user
```
patrix --action=create-room --name="Human readable room name" --invite="@dani:matrix.example.com"
```
  * Configure an existing room
```
patrix --action=modify-room --join_rules=public --topic='New topic' --room='!uXfknaWNcAnvthnIms:matrix.example.com' --invite='@admin:matrix.example.com'
```
  * Change power level needed for the ban action. Set the default power levels of new users to 10. Set power level for @dani:matrix.example.com to 90
```
patrix --action=modify-room --perm "ban=70" --perm "users_default=10" --perm_user "@dani:matrix.example.com=90"
```
  * Set the required power level to send the m.room.name event to 80 (you can change the room name if you have a power level of at least 80)
```
patrix --action=modify-room --perm_event "m.room.name=80"
```
  * Reset permissions. Only keep user power levels which are at least the same as yours (including yours)
```
patrix --action=modify-room --perm_reset
```

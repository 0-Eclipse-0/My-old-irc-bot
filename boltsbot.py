import re, socket, os

zero      = 0                   # Zero
one       = 1                   # One
false     = 0                   # Boolean False
true      = 1                   # Boolean True

botnick    = "boltsbot"
bufsize    = 2048
channel    = "#QuickChatz"
channel    = "#Leet-Support"
port       = 6667
server     = "irc.freenode.net"
master     = "Bolts114h"
uname      = "boltsbot"
realname   = "boltsbot"

Replies = dict()
Replies ['help'     ] = "Staff will be around soon to help you. Please be patient."
Replies ['bolts'    ] = "Bolts is my Owner/Creator"
Replies ['die'      ] = "No, you"
Replies ['goodbye'  ] = "I'll miss you"
Replies ['sayonara' ] = "I'll miss you"
Replies ['scram'    ] = "No, you"
Replies ['shout'    ] = "NO I WON'T"
Replies ['dance'    ] = botnick + " dances"
Replies ['sing'     ] = "Tra la la"
Replies ['hello'    ] = "Hi"
Replies ['howdy'    ] = "Hi"
Replies ['time'     ] = "It is TIME for a RHYME"
Replies ['master'   ] = master + " is my master"
Replies ['bacon'    ] = "Give me some, please!"
Replies ['botnick'  ] = "What do you want?"

def ping():
    global ircsock
    ircsock.send ("PONG :pingis\n")

def sendmsg (chan, msg):
    global ircsock
    ircsock.send ("PRIVMSG "+ chan +" :"+ msg + "\n")

def JoinChan (chan):
    global ircsock
    ircsock.send ("JOIN "+ chan +"\n")

def on_join(self, connection, event):
        nick = irc.strings.lower(event.source.nick)

        if nick not in self.known_nicks:
            self.do_welcome(connection, nick)
            self.known_nicks.add(nick)

def do_welcome(self, connection, nick):
        logger.info(u'Sending welcome message to {}'.format(nick))
        connection.privmsg(self.channel, u'{}: Test'.format(nick, self.MEETUP_PAGE))

def ProcHello():
    global ircsock
    ircsock.send ("PRIVMSG "+ channel +" :Hello!\n")

def Main():
    global ircsock, Replies
                                
    pattern1 = '.*:(\w+)\W*%s\W*$' % (botnick)
    pattern2 = '.*:%s\W*(\w+)\W*$' % (botnick)

                               
    ircsock = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
                                
    ircsock.connect ((server, port))
                                

    ircsock.send ("USER " + uname + " 2 3 " + realname + "\n")

                                
    ircsock.send ("NICK "+ botnick + "\n")
    
    JoinChan (channel)         

    while true:                 
	
        ircmsg = ircsock.recv (bufsize)
                                
        ircmsg = ircmsg.strip ('\n\r')

        print ircmsg  
		
		
        m1 = re.match (pattern1, ircmsg, re.I)
        m2 = re.match (pattern2, ircmsg, re.I)
        if ((m1 == None) and (m2 != None)): m1 = m2

        if (m1 != None):        
            word = m1.group (1) 
            word = word.lower() 
                                
            if (word in Replies):
                sendmsg (channel, Replies [word])

                                
								
        if ircmsg.find ("PING :") != -1:
            ping()

        if ircmsg.find ("!say ") != -1:
            say_split = ircmsg.split ("!say ")
            sendmsg (channel, say_split [1])
            sendmsg (master, "Message sent: " + say_split [1])         
	      
        if ircmsg.find ("!commands") != -1:
            sendmsg (channel, "Commands:\n")
            sendmsg (channel, "!info : Chat info! \n")		
			
# help
        if ircmsg.find ("help") != -1:
		    sendmsg(channel, "Staff will be here to help you soon. Please be patient! Type !commands to see my commands! \n")
			
# lulz
        if ircmsg.find (";-;") != -1:
            sendmsg(channel, "Quit saying that! \n")
			
#leetinfo 
        if ircmsg.find ("!leetinfo") != -1:
		    sendmsg(channel, "Leet.CC is a simple and cheap MCPE Micro-Server hosting company! \n")

# info
        if ircmsg.find ("!info") != -1:
            sendmsg(channel, "This is the official Leet.CC IRC Support Chat! Staff may idle so be patient when asking for help. \n")
			
# nick
        if ircmsg.find (":!nick ") != -1:
            str_split = ircmsg.split ("!nick ")
            ircsock.send ("NICK "+ str_split [1] + "\n")
            sendmsg (master, "Nick changed to " + str_split [1] + ".")

# notice
        if ircmsg.find (":!sendnotice ") != -1:
            str_split = ircmsg.split ("!sendnotice ")
            ircsock.send ("NOTICE " + channel + " " + str_split [1] + "\n")
            sendmsg (master, "Notice sent! Notice: " + str_split [1])

# op/deop
        if ircmsg.find ("!op") != -1:
            str_split = ircmsg.split ("!op ")
            ircsock.send ("MODE " + channel + " +o " + str_split [1] + "\n")
            sendmsg (master, "Opped " + str_split [1] + ".")

        if ircmsg.find ("!deop") != -1:
            str_split = ircmsg.split ("!deop ")
            ircsock.send ("MODE " + channel + " -o " + str_split [1] + "\n")
            sendmsg (master, "Deopped " + str_split [1] + ".")
# voice
        if ircmsg.find ("!voice") != -1:
            str_split = ircmsg.split ("!voice ")
            ircsock.send ("MODE " + channel + " +v " + str_split [1] + "\n")
            sendmsg (master, "Voiced " + str_split [1] + ".")

        if ircmsg.find ("!devoice") != -1:
            str_split = ircmsg.split ("!devoice ")
            ircsock.send ("MODE " + channel + " -v " + str_split [1] + "\n")
            sendmsg (master, "Removed voice on " + str_split [1] + ".")

# topic
        if ircmsg.find ("!topic") != -1:
            str_split = ircmsg.split ("!topic ")
            ircsock.send ("TOPIC " + channel + " " + str_split [1] + "\n")
            sendmsg (master, "Topic set to: " + str_split [1] + ".")
			

Main()
exit (zero)               

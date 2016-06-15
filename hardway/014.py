from sys import argv

script, user_name = argv
prompt = '>  '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)

##################################################
# <===================OUTPUT===================> #
# $ python 014.py zed                            #
# Hi zed, I'm the 014.py script.                 #
# I'd like to ask you a few questions.           #
# Do you like me zed?                            #
# >  Yes                                         #
# Where do you live zed?                         #
# >  China                                       #
# What kind of computer do you have?             #
# >  Mac                                         #
#                                                #
# Alright, so you said 'Yes' about liking me.    #
# You live in 'China'. Not sure where that is.   #
# And you have a 'Mac' computer. Nice.           #
##################################################

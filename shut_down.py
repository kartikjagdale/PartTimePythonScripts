s = raw_input("shut down?")

def shut_down(s):

    s = s.lower()

    if s == "yes":

        print "Shutting down..."

    elif s == "no":

        #return "Shutdown aborted!"

        print "Shutdown aborted!"

    else :

        #return "Sorry, I didn't understand you."

        print "Sorry, I didn't understand you."


shut_down(s)

# User Instructions
# 
# Implement the function escape_html(s), which replaces
# all instances of:
# > with &gt;
# < with &lt;
# " with &quot;
# & with &amp;
# and returns the escaped string
# Note that your browser will probably automatically 
# render your escaped text as the corresponding symbols, 
# but the grading script will still correctly evaluate it.
# 
def escape_html(s):
    srr = ""
    i = 0
    while i < len(s):
        if(s[i]=='>'):
            srr = srr + '&gt;'
        elif(s[i]=='<'):
            srr = srr + '&lt;'
        elif(s[i]=='"'):
            srr = srr + '&quot;'
        elif(s[i]=='&'):
            srr = srr + '&amp;'
        else:
            srr = srr + s[i]
        i = i+1;
    return srr
    

print escape_html("<b>html!</b>")

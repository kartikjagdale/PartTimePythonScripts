#FileName:Format Method and Escape Sequences
age=20
name='kartik' #string Declaration

print('{0} is {1}years old'.format(name,age))#Format Method i.e Constructing sting from other information
print('{0} is Playing Football'.format(name))

print('What\'s your Name?')#here backslash is called escape sequence to avoid Error so you can print single quote
#output of above is What's your Name?
#Examples
print("\"What's your name?\"")#O/p="What's your name?"
print("\\")#will print \ symbol
print(r'\1')#another method of printing Escape Sequences
print("hey!\nHow are you\n\t I am Fine")#\n for new Line and \t for Tab

#Note:Python is a Case Sensitive Language.
#End of Tutorial


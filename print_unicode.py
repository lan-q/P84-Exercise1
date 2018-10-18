import sys
import unicodedata
def	print_unicode_table(words):
	print("decimal hex chr {0:^40}".format("name"))
	print("…… …… {0:-<40}".format(""))

	code=ord("")
	end= min(0xD800, sys.maxunicode)

	while   code<end:
		c=chr(code)
		name=unicodedata.name(c,"***unknown***")
		b = True
                for word in words:
                    if word.lower() not in name.lower():
                        b = False
                        break
    
			if b:
			   print("{0:7} {0:5X} {0:^3c} {1}".format(code,name.title()))
		code +=1
word = []
if len(sys.argv)>1:
        if sys.argv[1] in ("-h","--help"):
                print("usage:{0}[string]".format(sys.argv[0]))
                word = None
        else:
                words = sys.argv[1:]
        if words is not None:
             print_unicode_table(words)

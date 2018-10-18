import sys
import unicodedata
def	print_unicode_table(words):
	print("decimal hex chr {0:^40}".format("name"))
	print("…… …… {0:-<40}".format(""))

	code=ord("")
	end= min(0xD800,sys.maxunicode)#Stop at surrogate pairs

	while   code<end:
		c=chr(code)
		name=unicodedata.name(c,"***unknown***")
		 ok = True
        for word in words:
            if word not in name.lower():
                ok = False
                break
        if ok:
            print("{0:7}  {0:5X}  {0:^3c}  {1}".format(
                  code, name.title()))
        code += 1


words = []
if len(sys.argv) > 1:
    if sys.argv[1] in ("-h", "--help"):
        print("usage: {0} [string1 [string2 [... stringN]]]".format(
              sys.argv[0]))
        words = None
    else:
        for word in sys.argv[1:]:
            words.append(word.lower())
if words is not None:
    print_unicode_table(words)

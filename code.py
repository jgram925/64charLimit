x = "Knowing how to write a paragraph is incredibly important. It’s a basic aspect of writing, and it is something that everyone should know how to do. There is a specific structure that you have to follow when you’re writing a paragraph. This structure helps make it easier for the reader to understand what is going on. Through writing good paragraphs, a person can communicate a lot better through their writing. When you want to write a paragraph, most of the time you should start off by coming up with an idea. After you have your idea or topic, you can start thinking about different things you can do to expand upon that idea. You should only finish the paragraph when you’ve finished covering everything you want about that idea."
x = x.split(" ")
while x:
  y = ""
  z = False
  while z == False:
    if x:
      if len(y + " " + x[0]) <= 64:
        y = y + " " + x[0]
        x.pop(0)
      else:
        z = True
    else:
      z = True
  print(y + "\n")

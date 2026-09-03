one_word = "request"
one_para = """This is a request with the text explains that users can now edit their username via the mobile app, following the transition to social handles. this is launched via code chnages not any experiments.
Reference material: """

# indexing and slicing
print(one_para[15:])
print(one_word[-1])
print(one_para[20:22])

# manipulation
print(len(one_para))
print(one_para[0:198].replace("chnages","changes").title())
print(one_para[199:].upper())

# exercise
code = "JavaScript"
desc = "cute and fun"
verb = "work"
function = "develop"

message_1 = f"""{code} is a powerful programming language. It's easy to {verb} You  can  use  {code}  for  web  development, data science, and automation. The syntax is {desc}. This makes {code} perfect for beginners and experts alike."""
print(message_1.strip())

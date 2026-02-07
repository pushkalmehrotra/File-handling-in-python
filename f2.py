file_read = open('sample_doc.txt', "r")
print("File in Read Mode -")
print(file_read. read())
file_read.close()

file_write = open ('sample_doc.txt', 'w')
file_write.write(" File in write mode....")
file_write.write("hi I am penguin I am 1 yr old")
file_write.close()

file_append = open ('sample_doc.txt', 'a')
file_append.write("\n file in append mode ......")
file_append.write("Hi! I am Penguin. I am 1 yr. old")
file_append.close()
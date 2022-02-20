import os
#import logging
cwd = os.chdir(r'C:\Users\tcdin\Desktop\New Folder')
#logging.basicConfig(filename='xyz.log', filemode='a+', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.CRITICAL)
#logging.info('--------------------------------------------------------------------------------------------------')
text = open("number.txt", 'r').read().split()
#logging.info('Before opening number.txt')
f = open("number.txt", "w")
#logging.info('After opening number.txt')
for i in range(len(text)):
   print("text[", i,"]",text[i])
   f.write(text[i]+'   '+str(int(text[i])*2)+'\n')
#logging.critical('Before closing number.txt')
f.close()
#logging.warning('After closing number.txt')



import sys
import os

def main():
   filepath = sys.argv[1]

   if not os.path.isfile(filepath):
       print("File path {} does not exist. Exiting...".format(filepath))
       sys.exit()

   with open(filepath) as fp:
       for line in fp:
           # if line == " ":
            # break
           url = line.replace('-160x160','')
           url = url.replace('-160x98','')
           url = url.replace('-98x160','')
           print(url)
           print(url.replace('.jpg','.JPG'))
           print(url.replace('.jpg','.jpeg'))
           print(url.replace('.jpg','.JPEG'))
           # print("line {}".format(url))

if __name__ == '__main__':
   main()

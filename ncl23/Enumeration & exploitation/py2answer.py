import sys

def main():
    password = list('tfzbwlyzljylawhzzdvyk')
    counter = 0
    while counter < len(password):
        x = ord(password[counter]) - 7
        if x < ord('a'):
            x += 26
        counter += 1
        print(chr(x))

if __name__ == '__main__':
    main()
    

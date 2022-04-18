import encryptor


def project_start ():
    print("encryptor")
    power=True

    while power :
        cmd=input("command:")
        if cmd =="encrypt":
        

            text=input("text:")
            key=int(input("key:"))
            resoult=encryptor.encrypt(text,key)
            print(resoult)
        elif cmd=="decrypt":
            text=input("text")
            key=int(input("key:"))
            resoult=encryptor.decrypt(text,key)
            print(resoult)
        elif cmd == "exit":
            power=False
            
        



if __name__=="__main__":
    project_start()
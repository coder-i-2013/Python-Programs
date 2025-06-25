class employee:
    def __init__(self):
        print(('employee created'))
    def __del__(self):
        print("Destructor called")

def Create_obj():
    print('making Object....')
    obj= employee()
    print('function ending.....')
    return obj

print('calling Create-obj() function.....')
obj= Create_obj()
print('Program is now ending ')
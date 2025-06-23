ItemsInCart = 0
# 2 items will be added to cart

if ItemsInCart != 2:  # raise Exception("product cart count not match")
    pass

assert (ItemsInCart == 0)

# try , catch

try:
    with open("test.txt") as reader:
        reader.read()
except Exception as e:
    print(e)
    print("Custom error by sahil salaria>> The file does not exist")

finally:
    print("Cleaning the message")

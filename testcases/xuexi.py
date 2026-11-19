def calc(*args):
    print("输入参数：",args)
calc("zll",30,"man")

with open("C:/Program Files/David/test.txt","w",encoding="utf-8") as f:
    f.write(f"zll\njob\nage")


with open("C:/Program Files/David/test.txt","r",encoding="utf-8") as f:

    print(f.readline())

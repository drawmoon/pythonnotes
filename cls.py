from typing import overload, Union


# 类的声明
class Store:
    name: str

    def __init__(self, name: str):
        print("Store init")
        self.name = name

    def __call__(self, todo: str):
        print("Store call")
        print(todo)

    def __del__(self):
        print("Store del")

    def get_name(self) -> str:
        return self.name


store = Store("Game Store")
store("run")
store_name = store.get_name()
print(store_name)


# 类的继承与函数重写
class PhysicalStore(Store):
    def get_name(self) -> str:
        print("PhysicalStore get_name")
        return super().get_name()


store = PhysicalStore("Game World")
store_name = store.get_name()
print(store_name)


# 类的继承之构造函数
class CloudStore(Store):
    tag: str

    def __init__(self, name: str, tag: str):
        super(CloudStore, self).__init__(name)
        self.tag = tag


store = CloudStore("Steam", "lib")
print(store.tag)


# 函数重载
class UserService:
    @overload
    def get(self, uid: int): ...

    @overload
    def get(self, name: str): ...

    def get(self, u: Union[int, str]):
        if type(u) == int:
            print(f"User id is {u}")
        else:
            print(f"User name is {u}")


user_service = UserService()
user_service.get(1)
user_service.get("admin")


# 判断或获取对象中指定的属性
class SomeClass:
    word = "Hello World!"

    def hi(self):
        print(self.word)

    def __init__(self):
        print(hasattr(self, "word"))
        print(hasattr(self, "hi"))

        print(getattr(self, "word"))
        print(getattr(self, "hi"))


some_class = SomeClass()


# 在父类中调用子类的方法
class Foo:
    def process(self, name: str):
        try:
            getattr(self, name)()
        except AttributeError:
            print(f"Notfound attr {name}")


class Bar(Foo):
    def tell(self):
        print("Call tell fn")


bar = Bar()
bar.process("tell")

def greet(name: str) -> str:
    greeting = "Hello, " + name + "!"
    print(greeting)
    return greeting


if __name__ == "__main__":
    greet("world")

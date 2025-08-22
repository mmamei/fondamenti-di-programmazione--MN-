def f():
    print("Hello from f()")
    return 42

if __name__ == "__main__":
    print("This is the main module.")
    result = f()
    print(f"Result from f(): {result}")
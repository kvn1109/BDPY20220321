def demo35(func1, func2, **kwargs):
    print(f"fix1={func1}, fix2={func2}")
    for k, v in kwargs.items():
        print(f"*variable parameter name={k}, value={v}")


demo35("0", "parameter")
demo35("1", "parameter", name="BDPY")
demo35("2", "parameters", name="BDPY", duration="35HR")
d1 = {"name": "BDPY", "duration": "35hr", "instructor": "MarkHo", "price": 20000}
demo35("put a ", "dictionary", **d1)
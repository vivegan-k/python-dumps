if type("bus") is str: print(True)
if type(10) is int: print(True)
if type(10.5) is float: print(True)
if type(True) is bool: print(True)
if type(["bus", "car"]) is list: print(True)
if type({"a":"cars", "b":"bike"}) is dict: print(True)
if type(("car", "bike")) is tuple: print(True)

if isinstance("bus", str): print(True)
if isinstance(10, int): print(True)
if isinstance(10.5, float): print(True)
if isinstance(True, bool): print(True)
if isinstance(["bus", "car"], list): print(True)
if isinstance({"a":"cars", "b":"bike"}, dict): print(True)
if isinstance(("car", "bike"), tuple): print(True)

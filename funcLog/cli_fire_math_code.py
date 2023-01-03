#!/c/Users/vcoelho/miniconda3/envs/python_sandbox/python
#!/c/Users/savio/miniconda3/envs/python_sandbox/python

"""
Build a command line interface for the math functions using the fire package.
"""
import fire
from math_code import add, sub, mul, div


def main() -> None:
    """Command line interface using the fire package"""
    fire.Fire({"add": add, "sub": sub, "div": div, "mul": mul})


if __name__ == "__main__":
    main()

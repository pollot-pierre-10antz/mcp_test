from mcp.server import FastMCP


mcp = FastMCP("Hello, World!")


@mcp.tool(name="addition")
def addition(a: float, b: float) -> float:
    """2つの数値を加算して結果を返します。
     
    Params:
        a: 一つ目の数値
        b: 二つ目の数値
    """
    return a + b
 
 
@mcp.tool(name="multiplication")
def multiplication(a: float, b: float) -> float:
    """2つの数値を掛け算して結果を返します。
     
    Params:
        a: 一つ目の数値
        b: 二つ目の数値
    """
    return a * b
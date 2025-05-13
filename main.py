from argparse import ArgumentParser, Namespace

from utils import mcp


def parse_arguments() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument("--stdio", action="store_true")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()
    
    if args.stdio:
        mcp.run(transport="stdio")
        exit(0)
        
    mcp.run(transport="streamable-http")

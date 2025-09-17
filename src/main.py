import asyncio

from viam.module.module import Module

try:
    from models.jack import Jack
except ModuleNotFoundError:
    # when running as local module with run.sh
    pass


if __name__ == "__main__":
    asyncio.run(Module.run_from_registry())

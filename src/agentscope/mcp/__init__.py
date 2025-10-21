"""The MCP module in AgentScope, that provides fine-grained control over
the MCP servers."""

from ._client_base import MCPClientBase
from ._http_stateful_client import HttpStatefulClient
from ._mcp_function import MCPToolFunction
from ._stateful_client_base import StatefulClientBase
from ._stdio_stateful_client import StdIOStatefulClient


def __getattr__(name: str):
    if name == "HttpStatelessClient":
        from ._http_stateless_client import HttpStatelessClient

        return HttpStatelessClient
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


__all__ = [
    "HttpStatefulClient",
    "HttpStatelessClient",
    "MCPClientBase",
    "MCPToolFunction",
    "StatefulClientBase",
    "StdIOStatefulClient",
]

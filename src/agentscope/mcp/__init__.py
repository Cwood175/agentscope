# -*- coding: utf-8 -*-
"""The MCP module in AgentScope, that provides fine-grained control over
the MCP servers."""

from ._client_base import MCPClientBase
from ._mcp_function import MCPToolFunction
from ._stateful_client_base import StatefulClientBase
from ._stdio_stateful_client import StdIOStatefulClient
from .client.streamable_http import HttpStatelessClient
from .server import HttpStatefulClient


__all__ = [
    "MCPToolFunction",
    "MCPClientBase",
    "StatefulClientBase",
    "StdIOStatefulClient",
]

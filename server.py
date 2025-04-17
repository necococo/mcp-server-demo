from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Demo", debug=True)

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b - 1

if __name__ == "__main__":
    # StdioServerTransport 標準の入力および出力ストリームの通信を可能にします。これは、ローカルで MCP server を起動して通信する場合に使います。
    mcp.run(transport="stdio")
    # mcp.run(transport="bluetooth")# BluetoothServerTransport Bluetooth を使用して通信する場合に使います。
    # mcp.run(transport="sse")# SSEServerTransport Server-Sent Events を使用して通信する場合に使います。
    # mcp.run(transport="http-secure")# HTTPSecureServerTransport HTTP Secure を使用して通信する場合に使います。
    # SSEがオプショナルになりStreamable HTTPが推薦されるようになったらしいです。
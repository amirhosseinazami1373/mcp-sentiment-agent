from smolagents import MCPClient,ToolCallingAgent
from smolagents import LiteLLMModel

# Connect to your local MCP server
mcp = MCPClient({
    "url": "http://localhost:7860/gradio_api/mcp/sse",
    "transport": "sse"
})
tools = mcp.get_tools()

# Connect to Ollama (make sure deepseek-coder is running)
model = LiteLLMModel(
    model_id="ollama/deepseek-r1:8b",
    api_base="http://localhost:11434",
    num_ctx=8192
)

# Create the agent
agent = ToolCallingAgent(tools=tools, model=model)

# Run it
response = agent.run("Analyze the sentiment of: 'I love this!'")
print(response)

# Day 17 — LangChain Agent with DuckDuckGo Search + Custom Math Tool
 
## What I built / learned
Built a LangChain agent using the modern `create_agent()` API
(LangChain 1.3.10) with two tools: DuckDuckGoSearchRun for real-time
web search and a custom `@tool` decorated math function using Python's
`eval()` with a sanitized regex filter. Ran three test queries covering
search-only, math-only, and combined search+math workflows.
 

## Results
 
### Query 1 — Search only

**Input:** "Who is the current CEO of Anthropic and when was the
company founded?"
 
**Output:** "Dario Amodei was born in 1983."
 
**Analysis:** Partially correct — Dario Amodei is the correct CEO
but the answer is incomplete and oddly phrased. The agent retrieved
his birth year instead of Anthropic's founding year (2021). This is
a retrieval quality issue — the search returned a snippet about Amodei
personally rather than Anthropic as a company. The final answer
generation then hallucinated a response format that didn't match
the question asked.
 
### Query 2 — Math only
**Input:** "A model processes 512 tokens per second. I have a document
with 8192 tokens. How many seconds will it take? What is that in minutes?"
 
**Output:** Error — `tool_use_failed`
 
**Analysis:** Groq's function calling parser rejected the tool call
because the model generated:
```
<function=math>{expression: 8192 / 512}</function>
```
instead of valid JSON:
```json
{"expression": "8192 / 512"}
```
This is a known compatibility issue between certain Groq models and
LangChain's tool-calling format. The fix is either to switch to
`llama-3.3-70b-versatile` (better tool-calling compliance) or to
add an explicit JSON format instruction to the system prompt.
 
### Query 3 — Search + Math combined
**Input:** "What is the current population of India? If 40% of that
population has access to the internet, how many people is that?"
 
**Output:** "The current population of India is approximately 1.476
billion, and 40% of that is approximately 0.59 billion people."
 
**Analysis:** Correct result. The agent successfully chained search
(retrieved population) and math (computed 40%) into a single coherent
answer. However, the reasoning trace was not visible — `create_agent()`
does not expose Thought/Action/Observation steps the way the older
`AgentExecutor(verbose=True)` did. The internal steps are hidden.

 
## Key insights

**Tool-calling format fragility:**
Query 2's failure revealed that not all Groq models reliably produce
valid JSON for tool calls. The model called the math tool but formatted
the arguments incorrectly. This is the exact kind of production failure
that agent frameworks need guardrails against — the agent "decided" to
use the tool correctly but failed at the serialization layer.
 
**Query 1's partial hallucination:**
The agent returned Dario Amodei's birth year instead of Anthropic's
founding year. The search returned a relevant snippet but the LLM
assembled the final answer incorrectly. This is a retrieval-to-answer
gap — the right information was retrieved but the generation step
lost track of the original question. Classic RAG failure mode, even
outside a RAG system.
 

 

 

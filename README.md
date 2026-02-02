# agent-fitness ✨

A minimalist multi-agent reasoning system for fitness coaching — built **without LangChain or LangGraph** to demonstrate how agents *actually think*. Watch agents analyze workout data → debate improvements → synthesize better training plans — all with explicit, debuggable code.

> 🔑 **Core insight**: Frameworks hide *why* agents work. This repo shows *how* — through phased reasoning (Analyze → Think → Summarize → Decide) you can build meaningful agent collaboration with <200 lines of core logic.

![Agent Reasoning Pipeline](https://via.placeholder.com/800x300?text=Phase+1%3A+Per-File+Analysis+%E2%86%92+Phase+2%3A+System+Synthesis+%E2%86%92+Phase+3%3A+Improvement+Proposal+%E2%86%92+Phase+4%3A+Critical+Validation)

*(Visual: Simple pipeline diagram showing data flow between agent phases)*

## Why This Exists

Most "multi-agent" tutorials are just LangChain wrappers that obscure the reasoning process. This project proves you can build **meaningful agent collaboration** with:

✅ **Explicit role separation** — Analyzer, Thinker, Summarizer agents with distinct purposes  
✅ **Phased reasoning** — From per-file insights → system synthesis → critical validation  
✅ **Decision synthesis** — Agents don't just agree/disagree — they *create better hybrid systems*  
✅ **Zero framework bloat** — Pure Python + standard libraries (PyYAML, json)  

Perfect for engineers who want to **understand agent fundamentals** before adopting complex frameworks.

## How It Works: The 4-Phase Pipeline

```mermaid
flowchart TD
    A[Phase 1: Per-File Analysis] --> B[Phase 2: System Synthesis]
    B --> C[Phase 3: Improvement Proposal]
    C --> D[Phase 4: Critical Validation]
    
    subgraph A [Phase 1]
        A1[Analyze notes/config/plans]
        A2[Think about insights]
        A3[Summarize findings]
    end
    
    subgraph B [Phase 2]
        B1[Analyze all summaries]
        B2[Think systemically]
        B3[Synthesize OLD system]
    end
    
    subgraph C [Phase 3]
        C1[Propose improvements]
        C2[Think critically]
        C3[Synthesize NEW system]
    end
    
    subgraph D [Phase 4]
        D1[Compare systems]
        D2[Discover vulnerabilities]
        D3[Make final decision]
    end

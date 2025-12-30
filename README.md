```
  ┌─────────┐
  │  Entry  │
  └────┬────┘
       │
       ▼
 ┌──────────────┐
 │  RAG Agent   │ ← Retrieves relevant chunks from ChromaDB
 │  (retrieve)  │
 └──────┬───────┘
        │
        ▼
 ┌──────────────────┐
 │ Conditional      │
 │ Router           │ ← Routes based on agent_type
 └──────┬───────────┘
        │
        ├─────────┬─────────┐
        ▼         ▼         ▼
     ┌─────┐  ┌──────┐  ┌─────────┐  
     │ Q&A │  │ Quiz │  │Learning │
     └──┬──┘  └───┬──┘  └────┬────┘
        │         │          │
        └─────────┴──────────┘
                  │
                  ▼
               ┌─────┐
               │ END │
               └─────┘
```

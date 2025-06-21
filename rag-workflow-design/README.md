## RAG Workflow Design

Basic Retrieval-Augmented Generation (RAG) workflow diagram that helps answer user questions using internal DevOps documentation.

### Working Model

1. User Prompt + Chat History are used to create a query.
2. Retrieval Stage searches for relevant information using a Vector DB.
3. The user prompt is enhanced with the retrieved content.
4. LLM generates the final response.
5. Chat history for future interactions.

### Data Source
1. DevOps Confluence documents are broken into chunks.
2. Embeddings are created with those and stored in a vector database.

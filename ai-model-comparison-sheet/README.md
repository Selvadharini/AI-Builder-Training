| **Criteria**                        | **GPT-4o**  | **Claude Sonnet** | **Gemini Flash** | **DeepSeek-R1:7B (Ollama)** |
|------------------------------------|-------------|-------------------|------------------|------------------------------|
| **Code Quality**                   | Excellent   | Good              | Good             | Basic or Limited             |
| **Comments**                       | Generates well-structured, production-ready code in multiple languages. Strong at refactoring, testing, and design patterns. | Clean and logical code with good explanations. Misses robustness in some cases; not always production-ready. | Performs well for frontend/web code. Struggles with backend patterns, error handling, and modular structure. | Handles simple code well. Struggles with complex logic, modularity, or error handling. Needs refinement for production. |

| **SQL Generation**                 | Excellent   | Excellent         | Good             | Basic or Limited             |
| **Comments**                       | Generates accurate, optimized SQL queries, even for complex joins, CTEs, window functions, and nested queries. | Strong in schema-aware SQL generation. Great at optimizing and explaining complex queries. | Good for common SQL tasks like joins and aggregations. Falls short on analytics queries or tuning. | Can generate simple SELECTs and basic JOINs. Not reliable for complex SQL or performance-oriented queries. Needs explicit schema. |

| **Infrastructure Automation (Scripts)** | Good    | Good              | Good             | Basic or Limited             |
| **Comments**                       | Great for Bash, Terraform, CI/CD (GitLab, GitHub), Ansible. Needs prompt tuning for advanced edge cases. | Can write usable scripts for DevOps tools. Lacks depth for multi-step workflows or tool-specific syntax. | Good for simple YAML, shell scripts, and Terraform. Limited knowledge of Helm, AWS IAM, etc. | Basic Bash or YAML generation. Poor tool-specific understanding. Needs heavy prompting for usable automation. |

| **Ease of Use**                    | Excellent   | Good              | Good             | Basic or Limited             |
| **Comments**                       | Understands vague, unstructured prompts and adds intelligent assumptions. Few retries needed. | Accepts natural language well but works better with clearly scoped prompts. | Easy to use for short, direct prompts. Needs decomposition for multi-step tasks. | Requires highly specific prompts. Doesn’t handle vague or high-level tasks well. |

| **Speed / Latency**               | Good        | Good              | Excellent         | Excellent                    |
| **Comments**                       | Fast for most tasks. Slight delay for longer code or multi-part queries. | Consistent performance. Slight lag on deeply nested prompts. | Extremely fast, ideal for real-time workflows and quick coding. | Very fast due to local inference. Great for offline/low-latency environments. |

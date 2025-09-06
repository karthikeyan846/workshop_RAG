from litellm import completion


def completion_llm(prompt):
    response = completion(
                model="ollama/llama3.2:latest",
                messages = [
                    { "role": "system", "content": "You are a specialized legal assistant focused on the Motor Vehicle Act of India. Your role is to provide accurate summaries and interpretations of the Motor Vehicle Act provisions, regulations, and related legal content. When given passages from the Act, provide clear, concise explanations while maintaining legal accuracy." },
                    { "role": "user", "content": prompt }
                ],
                api_base="http://localhost:11434",
                stream=True
    )
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            print(chunk.choices[0].delta.content, end="", flush=True)
from openai import OpenAI

client = OpenAI()   # Create an OpenAI instance with your API key => a client object


# STREAMING EXAMPLE:

# Calling the client to create a chat completion
completion = client.chat.completions.create(     
    model="gpt-4o-mini",  # Defining the model, which will be used  
    messages=[            # The messages exchanged between the user and the AI
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Write a haiku about recursion in programming."}],
    stream=True,          # Stream the response (if True) or wait for the response (if False)
)

# Printing the response from the AI
for chunk in completion:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")
    # 'completion.choices'  a list of possible completions; 
    # 'choices[0]'          refering to the first completion = one with the highest probability/relevance;
    # '.message'            contains the assistant's generated response.
    # 'delta.content'       the content of the response.
    # 'end=""'              to print the response in one line


from openai import OpenAI

client = OpenAI()  # Create an OpenAI client

# Create an embedding = a vector (list of numbers);
# Embedding is supposed to enncode the semantic meaning of the text input;
# The embedded text input is identifiable by machine learning models;
response = client.embeddings.create( 
    model="text-embedding-ada-002",                     # Specifying the model used for embeddings generation
    input="The food was delicious and the waiter...",   # Text input to be embedded
    encoding_format="float",                            # Format of the output embedding                    
)

embedding = response.data[0].embedding  # Extracting the embedding from the response
# 'response.data'   a list of results (usually containing only one element if a single text input is provided);
# 'data[0]'         accesses the first result;
# 'embedding'       the embedding vector for the input text = a list of numbers that represents the text in a high-dimensional space.

print(embedding)

from transformers import RagRetriever, RagTokenizer, RagTokenForGeneration

# Define paths
index_name = "legacy"
passages_path = r"C:\Users\Administrator\Desktop\Project\local_dataset\psgs_w100.tsv.pkl"

# Load retriever with the local index path
rag_retriever = RagRetriever.from_pretrained(
    "facebook/rag-token-nq",
    index_name=index_name,
    passages_path=passages_path
)

tokenizer = RagTokenizer.from_pretrained("facebook/rag-token-nq")
rag_model = RagTokenForGeneration.from_pretrained("facebook/rag-token-nq")

def query_rag(question):
    input_ids = tokenizer(question, return_tensors="pt").input_ids
    generated_ids = rag_model.generate(input_ids, num_return_sequences=1, num_beams=2)
    return tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]

import tkinter as tk
fromtkinter import scrolledtext, filedialog
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from transformers import pipeline

class RAGApplication:
  def __init__(self, root):
    self.root = root
    self.root = root
    self.root.title("RAG Application")

    # Initalize models
    self emmbedding_model = sentanceTransformer('all-MiniLM-l6-v2')
    self.generator = pipeline('text-generation' , model= 'gpt2')
    
    # Document storage 
    self.documents = []
    self.documents = None
    
    # Create GUI elements 
    self.create_wigets()

  def create_wigets(self):
    # document input section
    doc-frame = tk.LabelFrame(self.root, text="Documents" , padx=5, pady=5)
    doc_frame.pack(padx=10,pady5, fill="x")

    self.doc_text

    button_frame = tk.Frame(doc_frame(doc_frame)
    button_frame.pack(fill="x")

    load_btn = tk.Button(button_frame, text="Load Documents", command=self.load_documents)
    load_btn.pack(side="left", padx=5)

    clear_btn = tk.Button(button_frsme, text="Clear Documents", command=self.clear_documents)
    clear_btn.pack(side="left", padx=5)

    # Query section
    query_frame= tk.LableFrame(self.root text ="Query", padx=5. pady=5)
    query_frame.pack(padx=10, pady=5, fill="x")

    self.query_entry = tk.Entry(query_frame)
    self.query_entry.pack(padx=10, pady=5, fill="both", expand=True)

  def load_documents(self):
    file_paths = filedialog.askopenfilenames(
      title="Select Documents"
      filetype=(("Text files", "*.txt"), ("All files", "*.*))
    )

    if not file_paths:
        return
    for file_path in file_paths:
      with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        self .documents.append(content)
        self.doc_text.insert(tk.END, f"Loaded: {file_path}\n{content}\n\n")

    # Create emmbeddings for all documents
    if self.docments = []
    self.documents_embeddings = None
    self.doc_text.delete(1.0, tk.END)
    self.answer_text.delete(1.0, tk.END)

 def process_query(self):
   query = self.query_entry.get()(
     if not query:
     return

if not self.documents:
   self.answer_text.delet(1.0, tk.END)
   self.answer_text.insert(tk.END, "No documents loaded. Please load documents first."
   return

    # Embed the query 
    query_emdedding = self.embedding_model.encode([query])

    # Embed the query
    query_embedding = self.embeddiing_model([query])

    # calculate similarity with documents 
    similarities = cosine_similarity(query_embedding, self.document_embedings)
    most_similaritys_idx = np.argmax(similarities)
    most_similar_doc = sself.documents[most_similar_idx]

    # Generate awnserusing the most relevent document as context
    propmt = f'Document: {most_similar_doc}\n\nQuestion: {query}\nAnswer:"

    geneerate_text = self.generator(
    prompt,
    max_lenght=200,
    num_return_sequences=1,
    temratture=0.7,
    truncation=True
    )[0]['generated_text.split("Answeer:")[1].strip()

# Display rsults
self.answer_text.delete(1.0, tk.END)
self.answers-text.insert(tk.END, f"Question: {query}\n\n'")
self.answer_text.insert(tk.END, f"Most relavntdocuments:\n{most_similar_doc}\n\n")
self.answer_text.insert(tk.END, f"Answer:\n{answer}")








  


    
      



        
    
                      
    
                            


                          

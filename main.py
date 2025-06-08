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


                          

from django.shortcuts import render,redirect
from django.http import HttpResponse
from sentence_transformers import SentenceTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from pinecone import Pinecone, PodSpec
import pandas as pd
import numpy as np



def home(request):
    if request.method == "POST":
        query = request.POST.get("query")
        product,mrp,desc=vectordb(query)
        product_details = zip(product, mrp, desc)
        return render(request,'main.html',{'product_details':product_details}) 
    else:
        return render(request,'main.html')
    

def vectordb(querys):    
    pc = Pinecone(api_key='e50d31f7-7118-4b9b-b6d4-add9b44307xx')
    data=pd.read_csv('C:\\Users\\Rajesh\\Documents\\vector\\vector\\vector_db.csv')
    model= TfidfVectorizer()
    index=pc.Index('testing3')
    model=SentenceTransformer('bert-base-nli-mean-tokens')
    xq = model.encode([querys]).tolist()
    product=[]
    mrp=[]
    description=[]
    result = index.query(vector=xq, top_k=10)
    ids = [int(match['id'])for match in result['matches']]
    for i in ids:
        res=data.iloc[i]
        product.append(res['Product Name'])
        mrp.append(res['MRP'])
        description.append(res['Short description'])
    return product,mrp,description
    



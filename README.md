# Vector Database Search Tool -  Adaya.ai

## Objective :

The Vector Database Search Tool is designed to efficiently store and retrieve high-dimensional data, such as image embeddings or word vectors. The primary objective of this tool is to create a basic search tool that enables users to input a product name and retrieve the most similar product names along with their details from the database.

**Project Overview :**
The project involves the following tasks:

1. Generating 512-dimensional vectors for the "Product Name" column using TF-IDF technique.
2. Implementing a vector database using Pinecone, a cloud-based service known for its speed and scalability.
3. Developing a method to add documents and index vectors in the database, including the "Product Name," "MRP" (Maximum Retail Price), and "Short Description."
4. Creating a user interface where users can input a product name query and retrieve the top 10 most similar product names and their details.
5. Documenting the procedure, including the methodology used, and presenting the results obtained.

# Demo Video :


# Youtube Link :  https://youtu.be/8PqlO8kuh_Y

https://github.com/Barathaj/vector_DB_Adaya/assets/130913642/1b6c93a5-79d6-410c-813d-5da0f0ecee07






## Technology Stack :

![Screenshot 2024-05-08 190552](https://github.com/Barathaj/vector_DB_Adaya/assets/130913642/48825f66-84b4-456c-bf2f-a3eb0cd96e5d)

- ***Vectorization:***
  TDFVectorizer with 512 dimensions or Sentence-transformers with 768 dimensions.
- ***Vector Database:***
   Pinecone for efficient storage and retrieval of high-dimensional vectors.
- ***Framework:***
  Django for developing the user interface and handling backend operations.


# Work Flow 



![workflow_vector](https://github.com/Barathaj/vector_DB_Adaya/assets/130913642/3cd37bbe-350a-43b6-be3d-533bf7fdbf7a)

**Advantages of Pinecone:**
- ***Cloud-based Storage:***
   Pinecone stores data in the cloud, providing accessibility from anywhere and ensuring data durability.
- ***Fast and Scalable:***
   Pinecone is known for its fast query processing speed and scalability, making it suitable for real-time applications with large datasets.
- ***Built-in Similarity Search:***
   Pinecone offers built-in similarity search functionality, simplifying the implementation of search operations.

  # Pinecone vector DataBase cloud Storage
  
  ![image](https://github.com/Barathaj/vector_DB_Adaya/assets/130913642/b8faa9c8-f960-4492-8164-9429237d229e)

**Advantages of Django:**
- ***Full-Featured Framework:***
   Django provides a wide range of built-in features for web development, including authentication, admin interface, and ORM (Object-Relational Mapping).
- ***High-Level Abstraction:***
  Django abstracts away many complexities of web development, allowing developers to focus on application logic rather than boilerplate code.
- ***Robust Ecosystem:***
   Django has a vast ecosystem of libraries and packages, making it easy to integrate additional functionality into the application.

  
![Screenshot 2024-05-08 191606](https://github.com/Barathaj/vector_DB_Adaya/assets/130913642/4dd6ebf2-69f3-4021-9b55-0e19b1f76bd0)

**Conclusion:**
The Vector Database Search Tool is a powerful solution for efficiently storing and retrieving high-dimensional data. By leveraging technologies like Pinecone for vector storage and Django for web development, the tool offers fast and scalable search capabilities with a user-friendly interface. With its ability to retrieve the most similar product names based on user queries, the tool facilitates efficient data exploration and decision-making.


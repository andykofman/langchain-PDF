import logging

# Configure logging to write to a file
logging.basicConfig(
    filename='monitor.log',
    filemode='a',
    format='%(asctime)s [%(levelname)s] %(message)s',
    level=logging.INFO
)

class Monitor:
    """
    Educational Monitor for LLM/GenAI pipelines.
    Logs each major step with explanations for new learners.
    """

    def log_pdf_upload(self, filename):
        """
        Logs when a PDF file is uploaded by the user.
        """
        logging.info(
            f"[STEP: PDF Upload]\nExplanation: The user has uploaded a PDF file. This is the entry point for the document Q&A pipeline.\nFilename: {filename}\n"
        )

    def log_text_extraction(self, num_pages, text_sample):
        """
        Logs the extraction of text from the PDF.
        """
        logging.info(
            f"[STEP: Text Extraction]\nExplanation: The text content is extracted from the uploaded PDF. This raw text will be processed further.\nNumber of pages: {num_pages}\nSample text: {text_sample[:200]}...\n"
        )

    def log_text_chunking(self, num_chunks, chunk_sizes):
        """
        Logs the chunking of extracted text into smaller pieces.
        """
        logging.info(
            f"[STEP: Text Chunking]\nExplanation: The extracted text is split into smaller, overlapping chunks. This helps the AI handle large documents and preserve context.\nNumber of chunks: {num_chunks}\nChunk sizes: {chunk_sizes}\n"
        )

    def log_embedding_creation(self, num_embeddings, embedding_dim):
        """
        Logs the creation of embeddings for all text chunks.
        """
        logging.info(
            f"[STEP: Embedding Creation]\nExplanation: Each text chunk is converted into a vector (embedding) using the Gemini embedding model. These vectors capture the meaning of the text.\nNumber of embeddings: {num_embeddings}\nEmbedding dimension: {embedding_dim}\n"
        )

    def log_vector_store_creation(self, num_vectors):
        """
        Logs the creation of the FAISS vector store.
        """
        logging.info(
            f"[STEP: Vector Store Creation]\nExplanation: All embeddings are stored in a FAISS vector database. This enables fast similarity search for relevant information.\nNumber of vectors stored: {num_vectors}\n"
        )

    def log_chain_creation(self, chain_type):
        """
        Logs the creation of the conversational retrieval chain.
        """
        logging.info(
            f"[STEP: Chain Creation]\nExplanation: The ConversationalRetrievalChain is set up. This chain manages the flow from user question to answer, using retrieval and the LLM.\nChain type: {chain_type}\n"
        )

    def log_user_question(self, question):
        """
        Logs when a user submits a question.
        """
        logging.info(
            f"[STEP: User Question]\nExplanation: The user has submitted a question. The system will now process this query through the pipeline.\nQuestion: {question}\n"
        )

    def log_error(self, error_message):
        """
        Logs errors and exceptions that occur during processing.
        """
        logging.error(
            f"[STEP: Error Handling]\nExplanation: An error occurred during processing. This helps with debugging and improving the system.\nError: {error_message}\n"
        )

    def log_query_embedding(self, query, embedding):
        """
        Logs the process of converting a user question into a vector (embedding).
        Embeddings are how LLMs represent text as numbers for semantic understanding.
        """
        logging.info(
            "[STEP: Query Embedding]"
            "\nExplanation: The user's question is converted into a high-dimensional vector (embedding). "
            "This allows the AI to compare the meaning of the question to the document chunks."
            f"\nQuery: {query}"
            f"\nEmbedding (first 100 chars): {str(embedding)[:100]}...\n"
        )

    def log_semantic_search(self, query_embedding, results):
        """
        Logs the semantic search step, where the system finds the most relevant document chunks.
        Semantic search uses embeddings to find text with similar meaning, not just keywords.
        """
        logging.info(
            "[STEP: Semantic Search]"
            "\nExplanation: The system searches the vector database for document chunks whose embeddings are most similar to the query embedding. "
            "This finds the most relevant information, even if the wording is different."
            f"\nQuery Embedding (first 100 chars): {str(query_embedding)[:100]}..."
            f"\nTop Results: {results}\n"
        )

    def log_knowledge_base_search(self, retrieved_chunks):
        """
        Logs the retrieval of relevant chunks from the knowledge base (vector store).
        This step collects the actual text that will be used to answer the question.
        """
        logging.info(
            "[STEP: Knowledge Base Search]"
            "\nExplanation: The most relevant text chunks are retrieved from the knowledge base (vector database). "
            "These chunks will be provided as context to the language model."
            f"\nRetrieved Chunks: {retrieved_chunks}\n"
        )

    def log_ranked_results(self, ranked_chunks):
        """
        Logs the ranking of retrieved chunks by relevance.
        Ranking helps the LLM focus on the most important information first.
        """
        logging.info(
            "[STEP: Ranked Results]"
            "\nExplanation: The retrieved chunks are ranked by how closely they match the user's question. "
            "The top-ranked chunks are most likely to contain the answer."
            f"\nRanked Chunks: {ranked_chunks}\n"
        )

    def log_llm_response(self, answer):
        """
        Logs the final answer generated by the LLM (Generative AI).
        The LLM uses the retrieved context to generate a human-like answer.
        """
        logging.info(
            "[STEP: LLM Generative AI Response]"
            "\nExplanation: The language model (LLM) uses the retrieved context to generate a natural language answer to the user's question. "
            "This is the final step, where the AI responds as if it were a human expert."
            f"\nAnswer: {answer}\n"
        ) 
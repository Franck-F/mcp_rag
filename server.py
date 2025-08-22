import os
from dotenv import load_dotenv
from groundx import GroundX, Document
from mcp.server.fastmcp import FastMCP

load_dotenv()

mcp = FastMCP("mcp-rag")
client = GroundX(api_key=os.getenv("GROUNDX_API_KEY"))

@mcp.tool()
def search_doc_for_rag_context(query: str) -> str:
    """
    Recherche et extrait le contexte pertinent d'une base de connaissances,
    en fonction de la requête de l'utilisateur.
    Args:
        query: La requête de recherche fournie par l'utilisateur.
    Returns:
        str: Contenu textuel pertinent pouvant être utilisé par le LLM pour répondre à la requête.
    """
    response = client.search.content(
        id=17221,
        query=query,
        n=10,
    )

    return response.search.text

@mcp.tool()
def ingest_documents(local_file_path: str) -> str:
    """
    Importez des documents depuis un fichier local dans la base de connaissances.
    Args:
        local_file_path: Chemin d'accès au fichier local contenant les documents à ingérer.
    Returns:
        str: Un message indiquant que les documents ont été ingérés.
    """
    file_name = os.path.basename(local_file_path)
    client.ingest(
        documents=[
            Document(
            bucket_id=17279,
            file_name=file_name,
            file_path=local_file_path,
            file_type="pdf",
            search_data=dict(
                key = "value",
            ),
            )
        ]
    )
    return f"""Ingestion de {file_name} dans la base de connaissances. 
               Il devrait être disponible dans quelques minutes."""

if __name__ == "__main__":
    mcp.run(transport="stdio")
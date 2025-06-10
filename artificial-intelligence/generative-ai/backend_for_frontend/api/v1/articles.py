from domain.article_service import search
from domain.models import ArticleResponse, SearchRequest
from fastapi import APIRouter

router = APIRouter()


# REF-011-HTTP-METHOD, REF-011-RESOURCE-NAMING, REF-011-SYNCHRONICITY, REF-011-DATA-DESERIALIZATION
# REF-011-INPUT-VALIDATION, REF-011-RESPONSE-VALIDATION
@router.post("articles", response_model=ArticleResponse)
async def search_articles(data: SearchRequest) -> ArticleResponse:
    result: ArticleResponse = await search(data)

    return result
    # return "Hello"

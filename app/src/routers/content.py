from fastapi import APIRouter

from src.dependencies import (
    get_response,
    add_tags,
)

router = APIRouter()

@router.get("/recent_posts", 
            tags = ["Posts"], 
            description = "Get the summary of the most recent posts.",
            summary = "Recent posts"
)
def recent_posts( recent: bool | None = True ):
    return get_response("posts", recent)
    
@router.get("/recent_proj", 
            tags = ["Projects"], 
            description = "Get the information related to the projects.",
            summary = "Recent projects"
)
def recent_proj( recent: bool | None = True ):
    data = get_response("projects", recent)
    data = add_tags(data)
    return data

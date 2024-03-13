from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.contrib.admin.views.decorators import staff_member_required

from app.services.upsert import upsert
from app.services.pipelines.cleanup import cleanup_pipeline


@staff_member_required()
@require_http_methods(["GET"])
def upsert_view(request) -> HttpResponse:
    """
    Upserts data from json into database.
    Parameters:
        N/A
    Returns:
        HttpResponse
    """
    data = cleanup_pipeline()
    upsert(data)

    return HttpResponse(status=200)

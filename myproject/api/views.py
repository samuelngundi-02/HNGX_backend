# Create your views here.
from django.http import JsonResponse
from datetime import datetime
import pytz

def get(request):
        slack_name = request.GET.get("slack_name", "Samuel Ngundi")
        track = request.GET.get("track", "backend")
        
        # Get current UTC time
        utc_time = datetime.now(pytz.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

        response_data = {
            "slack_name": slack_name,
            "current_day": datetime.now().strftime("%A"),
            "utc_time": utc_time,
            "track": track,
            "github_file_url": "https://github.com/samuelngundi-02/HNGX_backend/blob/main/myproject/api/views.py",
            "github_repo_url": "https://github.com/samuelngundi-02/HNGX_backend",
            "status_code": 200,
        }

        return JsonResponse(response_data)

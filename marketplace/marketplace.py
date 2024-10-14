import os

from flask import Flask, render_template
import grpc

from recommendations_pb2 import BookCategory, RecommendationRequest
from recommendations_pb2_grpc import RecommendationsStub

app = Flask(__name__)

recommations_host = os.getenv("RECOMMENDATIONS_HOST", "localhost")
recommendations_channel = grpc.insecure_channel(f"{recommations_host}:50051")

recommendations_client = RecommendationsStub(recommendations_channel)

@app.route("/")
def render_homepage():
    recommendations_request = RecommendationRequest(user_id=1, category = BookCategory.SCIENCE_FICTION, max_results=3)
    recommendations_response = recommendations_client.Recommend(recommendations_request)
    return render_template(
        "homepage.html",
        recommendations = recommendations_response.recommendation
    )
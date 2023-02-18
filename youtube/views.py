from django.shortcuts import render, HttpResponse
from youtube_transcript_api import YouTubeTranscriptApi
import json

# Create your views here.
def index(request):
    return HttpResponse("Developed by Surajit Sarkar");

def generate_transcript(id):
	transcript = YouTubeTranscriptApi.get_transcript(id)
	script = ""

	for text in transcript:
		t = text["text"]
		if t != '[Music]':
			script += t + " "
		
	return script, len(script.split())

def youtube(request):
    id = request.GET["id"];
    transcript, no_of_words = generate_transcript(id);
    return HttpResponse(json.dumps(transcript), content_type="application/json")
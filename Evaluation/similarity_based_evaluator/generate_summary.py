import os
import json
from google import genai
from google.genai import types
import sys
def extract_summary(path):
    with open(path, 'rb') as f:
        summary = json.load(f)
    return summary['summary']


def get_summary(model, diagram):
    diagram = diagram.split('.')[0] + ".png"
    with open(f'./evaluate_png/{model}/{diagram}', 'rb') as f:
        image_bytes = f.read()

    client = genai.Client(api_key=key)
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=[
            types.Part.from_bytes(
                data=image_bytes,
                mime_type='image/png',
            ),
            'summary the workflow in digram in three sentences'
        ]
    )
    return response.text

def generate_summary(model):
    summary_input = []
    for f in os.listdir("../Graph Generation/Ground_truth/extracted_text"):
        ground_path = os.path.join("../Graph Generation/Ground_truth/extracted_text", f)
        summary = {"ground_summary": extract_summary(ground_path),"llm_summary": get_summary(model,f)}
        summary_input.append(summary)
    return summary_input

if __name__ == '__main__':
    model = sys.argv[1]
    key = sys.argv[2] # api key for gemini
    with open(f'ground_summary/{model}_test_similarity.json', 'w') as f:
        json.dump(generate_summary(model), f)
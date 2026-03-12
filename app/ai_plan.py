import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_study_plan(topics):

    topic_text = ", ".join(topics)

    study_plan = f"""
1. Review the core concepts of {topic_text} using GRE preparation material.
2. Solve at least 15 practice questions daily focusing on {topic_text}.
3. Take a timed mock test to evaluate your improvement and identify weak areas.
"""

    return study_plan

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"AI generation error: {str(e)}"
import openai
import os

def generate_analysis(data):
    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    prompt = f"""You are a Rocket League coach. Based on the following match data, provide a fun, casual, and constructive analysis.

Match data:
- Touches: {data['touches']}
- Rotations broken: {data['rotations_broken']}
- Boost usage: {data['boost_usage']}
- Positioning rating: {data['positioning_rating']}
- Double commits: {data['double_commits']}
- Game mode: {data['game_mode']}

Explain what the player did well, what they can improve, and suggest specific training drills."""

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

import json


def call_claude(system_prompt: str, user_message: str) -> str:
    """
    Mock Claude response for development/testing.
    Returns structured JSON in the same shape expected by the UI.
    """

    topic = user_message.strip()

    mock_report = {
        "topic": topic,
        "summary": f"This report identifies SEO opportunities for '{topic}', including keyword clusters, content angles, content gaps, and article ideas to improve visibility and search coverage.",
        "seo_intelligence": {
            "keyword_clusters": [
                {
                    "cluster_name": "Beginner Intent",
                    "keywords": [
                        f"what is {topic}",
                        f"{topic} basics",
                        f"{topic} for beginners"
                    ]
                },
                {
                    "cluster_name": "Commercial Intent",
                    "keywords": [
                        f"best tools for {topic}",
                        f"{topic} software",
                        f"{topic} platform comparison"
                    ]
                },
                {
                    "cluster_name": "Problem-Solving Intent",
                    "keywords": [
                        f"common mistakes in {topic}",
                        f"how to improve {topic}",
                        f"{topic} strategy tips"
                    ]
                }
            ],
            "content_angles": [
                f"Complete beginner's guide to {topic}",
                f"Top mistakes to avoid in {topic}",
                f"Best tools and platforms for {topic}",
                f"How businesses use {topic} to grow faster"
            ],
            "gap_analysis": [
                "Competitor content explains basics but lacks actionable workflows.",
                "There is little content focused on real business use cases.",
                "Most articles do not compare tools or platforms clearly.",
                "Few resources target beginner and advanced users separately."
            ],
            "recommended_articles": [
                f"Beginner's roadmap for {topic}",
                f"10 practical use cases of {topic}",
                f"Best tools for {topic} in 2026",
                f"{topic}: common mistakes and solutions"
            ]
        }
    }

    return json.dumps(mock_report)


def run_agent(topic: str) -> dict:
    """
    Mock agent workflow.
    """

    print(f"[Agent] Running mock research for: '{topic}'")

    raw_report = call_claude("mock_system_prompt", topic)

    try:
        final_report = json.loads(raw_report)
    except json.JSONDecodeError:
        final_report = {
            "topic": topic,
            "summary": "Failed to generate mock report.",
            "seo_intelligence": {
                "keyword_clusters": [],
                "content_angles": [],
                "gap_analysis": [],
                "recommended_articles": []
            }
        }

    print("[Agent] Done ✓")
    return final_report


if __name__ == "__main__":
    result = run_agent("email marketing")
    print(json.dumps(result, indent=2))
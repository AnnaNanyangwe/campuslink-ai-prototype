from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


# Simple AI-assisted matching prototype
OPPORTUNITIES = [
    {
        "title": "Software Development Project",
        "description": "Work on a student software project involving programming and web development.",
        "skills": ["python", "java", "javascript", "programming", "software", "web development"]
    },
    {
        "title": "Database Assistant",
        "description": "Support database-related projects involving SQL and database management.",
        "skills": ["sql", "postgresql", "mysql", "database", "databases"]
    },
    {
        "title": "Student Research Assistant",
        "description": "Assist with university research projects involving technology and data.",
        "skills": ["research", "data", "python", "artificial intelligence", "ai"]
    },
    {
        "title": "Web Development Opportunity",
        "description": "Contribute to websites and web applications using modern web technologies.",
        "skills": ["html", "css", "javascript", "web", "web development"]
    },
    {
        "title": "AI and Technology Project",
        "description": "Explore artificial intelligence and technology solutions for real-world problems.",
        "skills": ["ai", "artificial intelligence", "python", "machine learning"]
    },
    {
        "title": "Student Technology Support",
        "description": "Help students or university projects with technology, networking, and computer systems.",
        "skills": ["networking", "linux", "computers", "technology", "it", "systems"]
    }
]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/match", methods=["POST"])
def match_opportunities():

    data = request.get_json()
    message = data.get("message", "").lower().strip()

    if not message:
        return jsonify({
            "error": "Please describe your skills or interests."
        }), 400

    matches = []

    for opportunity in OPPORTUNITIES:

        score = 0

        for skill in opportunity["skills"]:
            if skill in message:
                score += 1

        if score > 0:
            matches.append({
                "title": opportunity["title"],
                "description": opportunity["description"],
                "score": score
            })

    matches.sort(key=lambda x: x["score"], reverse=True)

    if not matches:
        matches = [
            {
                "title": "Explore Campus Opportunities",
                "description": "Your profile did not produce a direct match yet. Try adding skills such as Python, databases, web development, networking, research, or AI."
            }
        ]

    return jsonify({
        "matches": matches[:3]
    })


if __name__ == "__main__":
    app.run(debug=True)
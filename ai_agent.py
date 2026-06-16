def ask_agent(user_query, context):

    query = user_query.lower()

    if "about" in query or "foundation" in query:

        return """
NayePankh Foundation is a non-profit organization focused on:

• Education Support
• Community Development
• Awareness Campaigns
• Youth Empowerment
• Skill Development

The foundation works with volunteers and interns to create social impact through various community initiatives.
"""

    elif "volunteer" in query:

        return """
Available Volunteer Opportunities:

• Teaching & Mentoring
• Social Media Management
• Event Management
• Content Writing
• Graphic Design
"""

    elif "internship" in query:

        return """
Available Internship Domains:

• AI Development
• AI Agent Development
• Full Stack Development
• Web Development
• Data Analytics
• Machine Learning
"""

    else:

        return f"""
Sorry, I couldn't understand that.

You can ask me about:

• NayePankh Foundation
• Volunteer Opportunities
• Internship Programs

Question:
{user_query}
"""
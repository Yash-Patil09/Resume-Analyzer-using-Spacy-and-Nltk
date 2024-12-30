from skills import (
    data_science_skills, web_development_skills, aiml_skills,
    devops_skills, cybersecurity_skills, cloud_computing_skills, mobile_development_skills
)
from utils import extract_text_from_pdf, preprocess_text

# Combine all skills into one set for easy matching
all_skills = (
    data_science_skills.union(web_development_skills)
    .union(aiml_skills).union(devops_skills)
    .union(cybersecurity_skills).union(cloud_computing_skills)
    .union(mobile_development_skills)
)

def extract_skills(tokens):
    """Extract skills from the tokens based on predefined skill sets."""
    return set(tokens).intersection(all_skills)

def generate_suggestions(matched_skills, field):
    """Generate suggestions for missing skills based on the field."""
    missing_skills = []
    if field == "Data Science":
        missing_skills = data_science_skills.difference(matched_skills)
    elif field == "Web Development":
        missing_skills = web_development_skills.difference(matched_skills)
    elif field == "AIML":
        missing_skills = aiml_skills.difference(matched_skills)
    elif field == "DevOps":
        missing_skills = devops_skills.difference(matched_skills)
    elif field == "Cybersecurity":
        missing_skills = cybersecurity_skills.difference(matched_skills)
    elif field == "Cloud Computing":
        missing_skills = cloud_computing_skills.difference(matched_skills)
    elif field == "Mobile Development":
        missing_skills = mobile_development_skills.difference(matched_skills)

    suggestions = f"You could focus on improving these skills: {', '.join(missing_skills)}"
    return suggestions

def analyze_internships(resume_text):
    """Analyze internship sections in the resume."""
    internship_sections = [line for line in resume_text.split("\n") if "intern" in line.lower()]
    ds_keywords = {"data", "analysis", "machine learning", "regression", "forecast", "model"}
    wd_keywords = {"web", "frontend", "backend", "javascript", "react", "html", "css"}
    aiml_keywords = {"machine learning", "artificial intelligence", "deep learning"}
    devops_keywords = {"docker", "kubernetes", "aws", "azure", "terraform"}
    cybersecurity_keywords = {"security", "penetration", "firewall", "malware"}
    cloud_keywords = {"cloud", "aws", "azure", "gcp"}
    mobile_keywords = {"android", "ios", "flutter", "react native"}

    internships = []
    for section in internship_sections:
        if any(keyword in section.lower() for keyword in ds_keywords):
            internships.append({"type": "Data Science", "description": section.strip()})
        elif any(keyword in section.lower() for keyword in wd_keywords):
            internships.append({"type": "Web Development", "description": section.strip()})
        elif any(keyword in section.lower() for keyword in aiml_keywords):
            internships.append({"type": "AIML", "description": section.strip()})
        elif any(keyword in section.lower() for keyword in devops_keywords):
            internships.append({"type": "DevOps", "description": section.strip()})
        elif any(keyword in section.lower() for keyword in cybersecurity_keywords):
            internships.append({"type": "Cybersecurity", "description": section.strip()})
        elif any(keyword in section.lower() for keyword in cloud_keywords):
            internships.append({"type": "Cloud Computing", "description": section.strip()})
        elif any(keyword in section.lower() for keyword in mobile_keywords):
            internships.append({"type": "Mobile Development", "description": section.strip()})

    return internships

def analyze_projects(resume_text):
    """Analyze project sections in the resume."""
    project_sections = [line for line in resume_text.split("\n") if "project" in line.lower()]
    ds_project_keywords = {"data", "analysis", "machine learning", "predictive", "model", "regression", "forecast"}
    wd_project_keywords = {"web", "frontend", "backend", "javascript", "react", "html", "css", "node.js"}
    aiml_project_keywords = {"machine learning", "artificial intelligence", "deep learning"}
    devops_project_keywords = {"docker", "kubernetes", "aws", "azure"}
    cybersecurity_project_keywords = {"security", "penetration", "firewall"}
    cloud_project_keywords = {"cloud", "aws", "azure", "gcp"}
    mobile_project_keywords = {"android", "ios", "flutter", "react native"}

    projects = []
    for section in project_sections:
        if any(keyword in section.lower() for keyword in ds_project_keywords):
            projects.append({"type": "Data Science", "description": section.strip()})
        elif any(keyword in section.lower() for keyword in wd_project_keywords):
            projects.append({"type": "Web Development", "description": section.strip()})
        elif any(keyword in section.lower() for keyword in aiml_project_keywords):
            projects.append({"type": "AIML", "description": section.strip()})
        elif any(keyword in section.lower() for keyword in devops_project_keywords):
            projects.append({"type": "DevOps", "description": section.strip()})
        elif any(keyword in section.lower() for keyword in cybersecurity_project_keywords):
            projects.append({"type": "Cybersecurity", "description": section.strip()})
        elif any(keyword in section.lower() for keyword in cloud_project_keywords):
            projects.append({"type": "Cloud Computing", "description": section.strip()})
        elif any(keyword in section.lower() for keyword in mobile_project_keywords):
            projects.append({"type": "Mobile Development", "description": section.strip()})

    return projects

def analyze_resume(file_path):
    """Main function to analyze the resume."""
    resume_text = extract_text_from_pdf(file_path)
    if not resume_text:
        return {"error": "Failed to analyze resume text."}

    tokens = preprocess_text(resume_text)
    matched_skills = extract_skills(tokens)
    internships = analyze_internships(resume_text)
    project_counts = analyze_projects(resume_text)

    # Count skills for each field
    ds_skill_count = len(matched_skills.intersection(data_science_skills))
    wd_skill_count = len(matched_skills.intersection(web_development_skills))
    aiml_skill_count = len(matched_skills.intersection(aiml_skills))
    devops_skill_count = len(matched_skills.intersection(devops_skills))
    cybersecurity_skill_count = len(matched_skills.intersection(cybersecurity_skills))
    cloud_computing_skill_count = len(matched_skills.intersection(cloud_computing_skills))
    mobile_dev_skill_count = len(matched_skills.intersection(mobile_development_skills))

    # Create a dictionary to hold the totals
    field_totals = {
        "Data Science": ds_skill_count,
        "Web Development": wd_skill_count,
        "AIML": aiml_skill_count,
        "DevOps": devops_skill_count,
        "Cybersecurity": cybersecurity_skill_count,
        "Cloud Computing": cloud_computing_skill_count,
        "Mobile Development": mobile_dev_skill_count
    }

    # Determine the field with the highest total
    field = max(field_totals, key=field_totals.get)

    suggestions = generate_suggestions(matched_skills, field)

    return {
        "field": field,
        "matched_skills": matched_skills,
        "internships": internships,
        "projects": project_counts,
        "suggestions": suggestions,
    }
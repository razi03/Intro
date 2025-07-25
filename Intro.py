info = {
    "Name": "Razi Ur Rehman",
    "Role": "Automation & Web Developer",
    "Organization": "Upwork Freelancer",
    "Background": "BSCS (Final Year)",
    "Experience": "2+ years (Freelance & Internships)"
}

md_output = f"""# About Me

| Field          | Details                          |
|----------------|----------------------------------|
| **Name**       | {info['Name']}                   |
| **Role**       | {info['Role']}                   |
| **Org**        | {info['Organization']}           |
| **Background** | {info['Background']}             |
| **Experience** | {info['Experience']}             |
"""

print(md_output)

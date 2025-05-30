# Task 1
strings = ["apple", "banana", "cherry", "date"]
lengths = [(s, len(s)) for s in strings]

# Task 2
nums = range(-5, 6)
result = [x**2 if x % 2 == 0 else x**3 for x in nums]

# Task 3
nums = range(-5, 6)
even_squares = [(x, x**2) for x in nums if x % 2 == 0]

# Task 4
job_roles = [
    {'role': 'Data Analyst', 'skills': ['Python', 'SQL', 'Excel']},
    {'role': 'Data Scientist', 'skills': ['Python', 'R', 'Machine Learning', 'Deep Learning']},
    {'role': 'Machine Learning Engineer', 'skills': ['Python', 'TensorFlow', 'PyTorch', 'Scikit-Learn']},
    {'role': 'Data Engineer', 'skills': ['Python', 'Apache Spark', 'Hadoop', 'SQL']},
    {'role': 'Business Intelligence Analyst', 'skills': ['Python', 'SQL', 'Tableau', 'Power BI', 'Excel']},
    {'role': 'Quantitative Analyst', 'skills': ['R', 'Python', 'MATLAB', 'Statistics']},
    {'role': 'Operations Analyst', 'skills': ['Python', 'SQL', 'Data Visualization', 'Process Improvement']},
    {'role': 'Database Administrator', 'skills': ['SQL', 'Oracle', 'MySQL', 'Database Management']},
    {'role': 'AI Engineer', 'skills': ['Python', 'TensorFlow', 'PyTorch', 'Computer Vision']},
    {'role': 'Statistician', 'skills': ['R', 'SAS', 'Python', 'Statistical Modeling']}
]

my_skills = ['Python', 'SQL', 'Excel']

qualified_roles = []

for job in job_roles:
    for skill in job['skills']:
        if skill in my_skills:
            qualified_roles.append(job['role'])
            break

print("Qualified roles:", qualified_roles)

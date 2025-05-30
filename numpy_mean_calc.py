import numpy as np

web_development_jobs = [
    {'job_title': 'Frontend Developer', 'job_skills': "['HTML', 'CSS', 'JavaScript']", 'job_date': '2023-06-01', 'salary': 70000},
    {'job_title': 'Backend Developer', 'job_skills': "['Node.js', 'Express', 'MongoDB']", 'job_date': '2023-06-03', 'salary': None},
    {'job_title': 'Full Stack Developer', 'job_skills': "['React', 'Node.js', 'SQL']", 'job_date': '2023-06-05', 'salary': 85000},
    {'job_title': 'Web Designer', 'job_skills': "['Figma', 'CSS', 'UX/UI']", 'job_date': '2023-06-07', 'salary': 60000},
    {'job_title': 'DevOps Engineer', 'job_skills': "['Docker', 'AWS', 'CI/CD']", 'job_date': '2023-06-10', 'salary': 95000},
    {'job_title': 'Web Developer Intern', 'job_skills': "['HTML', 'Bootstrap', 'Git']", 'job_date': '2023-06-12', 'salary': None},
    {'job_title': 'React Developer', 'job_skills': "['React', 'Redux', 'JavaScript']", 'job_date': '2023-06-15', 'salary': 75000},
    {'job_title': 'UI/UX Designer', 'job_skills': "['Adobe XD', 'Figma', 'Prototyping']", 'job_date': '2023-06-18', 'salary': 65000},
    {'job_title': 'PHP Developer', 'job_skills': "['PHP', 'Laravel', 'MySQL']", 'job_date': '2023-06-20', 'salary': 70000},
    {'job_title': 'WordPress Developer', 'job_skills': "['WordPress', 'PHP', 'CSS']", 'job_date': '2023-06-22', 'salary': 60000},
    {'job_title': 'Angular Developer', 'job_skills': "['Angular', 'TypeScript', 'HTML']", 'job_date': '2023-06-25', 'salary': 77000},
    {'job_title': 'MERN Stack Developer', 'job_skills': "['MongoDB', 'Express', 'React', 'Node.js']", 'job_date': '2023-06-28', 'salary': 88000},
    {'job_title': 'Junior Frontend Developer', 'job_skills': "['HTML', 'CSS', 'JavaScript']", 'job_date': '2023-07-01', 'salary': 55000},
    {'job_title': 'Cloud Engineer', 'job_skills': "['AWS', 'Docker', 'Kubernetes']", 'job_date': '2023-07-04', 'salary': 98000},
    {'job_title': 'Mobile App Developer', 'job_skills': "['React Native', 'Flutter', 'iOS']", 'job_date': '2023-07-07', 'salary': 82000},
    {'job_title': 'Django Developer', 'job_skills': "['Python', 'Django', 'PostgreSQL']", 'job_date': '2023-07-10', 'salary': 81000},
]

salaries = [job['salary'] for job in web_development_jobs]
salaries_with_nan = np.array([np.nan if s is None else s for s in salaries], dtype=float)

mean_salary = np.nanmean(salaries_with_nan)

print("Salaries with NaN:", salaries_with_nan)
print("Mean salary ignoring None values:", mean_salary)

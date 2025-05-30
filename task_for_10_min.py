import numpy as np

web_dev_jobs = [
    "Frontend Developer",
    "Backend Developer",
    "Full Stack Developer",
    "Web Designer",
    "DevOps Engineer",
    "React Developer",
    "UI/UX Designer"
]

salaries = [70000, 80000, 85000, 60000, 95000, 75000, 65000]

mean_salary = np.mean(salaries)
max_salary = np.max(salaries)
print("Mean salary:", mean_salary)
print("Max salary:", max_salary)

salaries_with_none = [70000, None, 85000, 60000, None, 75000, 65000]

salaries_nan = np.array([np.nan if x is None else x for x in salaries_with_none], dtype=float)

mean_salary_with_nan = np.nanmean(salaries_nan)
print("Mean salary with some missing values:", mean_salary_with_nan)

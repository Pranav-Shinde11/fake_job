import requests
from bs4 import BeautifulSoup

url = 'https://internshala.com/job/detail/fresher-business-development-associate-job-in-hyderabad-at-globus1711609840'

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
title_elem = soup.find('span', attrs={'class': 'profile_on_detail_page'})
title = title_elem.get_text() if title_elem else "Title Not Found"

company_elem = soup.find('a', attrs={'class': 'link_display_like_text view_detail_button'})
company = company_elem.get_text() if company_elem else "Company Not Found"

details_companylinksrc = soup.find('div', attrs={'class': 'text-container website_link'})
details_companylink = details_companylinksrc.find('a').get('href') if details_companylinksrc else "Link Not Found"
details_companylinktext = details_companylinksrc.find('a').get_text() if details_companylinksrc else "Link Text Not Found"

location_elem = soup.find('p', attrs={'id': 'location_names'})
location = location_elem.get_text() if location_elem else "Location Not Found"

internshipdetails_elem = soup.find('div', attrs={'class': 'other_detail_item_row'})
internshipdetails = internshipdetails_elem.get_text() if internshipdetails_elem else "Details Not Found"

tags_elem = soup.find('div', attrs={'class': 'tags_container_outer'})
tags = tags_elem.get_text() if tags_elem else "Tags Not Found"

details_elem = soup.find('div', attrs={'class': 'internship_details'})
job_details = details_elem.get_text().strip() if details_elem else "Job Details Not Found"

skills_required_elem = soup.find('div', attrs={'class': 'round_tabs_container'})
skills_required = skills_required_elem.get_text() if skills_required_elem else "Skills Required Not Found"

salary_elem = soup.find('div', attrs={'class': 'text-container salary_container'})
salary = salary_elem.get_text() if salary_elem else "Salary Not Found"

print("Title:", title)
print("Company:", company)
print("Company Link:", details_companylink)
print("Company Link Text:", details_companylinktext)
print("Location:", location)
print("Internship Details:", internshipdetails)
print("Tags:", tags)
print("Job Details:", job_details)
print("Skills Required:", skills_required)
print("Salary:", salary)

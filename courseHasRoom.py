# Provide the course offerings registrar webpage for course in question
# example: EGR 494 S18: https://registrar.princeton.edu/course-offerings/course_details.xml?courseid=012448&term=1184
course_urls = [
'https://registrar.princeton.edu/course-offerings/course_details.xml?courseid=012448&term=1184',
]
course_names = [
'EGR 494', 
]
numbers = [
'+11234567890',
]

previous_enrollments = [(0,0) for _ in range(len(numbers))]

def get_availability(url):
	from bs4 import BeautifulSoup
	import urllib

	page = urllib.request.urlopen(url)
	soup = BeautifulSoup(page, 'html.parser')
	cap = soup.body.table.find_all('td')[5]

	current_enrollement = cap.contents[1].rstrip()
	max_capacity = cap.contents[3]

	return int(current_enrollement), int(max_capacity)

def send_text(phone, course, enrollment, capacity):
	from twilio.rest import Client
	account_sid = "SSID"
	auth_token  = "TOKEN"
	client = Client(account_sid, auth_token)
	message = client.messages.create(
	    to=phone, 
	    from_="",
	    body=f"Update: {course} at {enrollment}/{capacity} enrollment.")

# Makes sure that you've configured everything right...
assert(len(course_urls) == len(course_names) and len(course_names) == len(numbers))

import time
SECONDS_BETWEEN_CHECKS = 60 * 5 # 5 minutes
while True:
	for i, (url, course, phone) in enumerate(zip(course_urls, course_names, numbers)):
		enrollment, capacity = get_availability(url)
		if (enrollment, capacity) != previous_enrollments[i]:
			previous_enrollments[i] = enrollment, capacity
		
			if  True:
				send_text(phone, course, enrollment, capacity)
				print(f"Text sent to {phone} for class {course} at {enrollment}/{capacity}.")
	time.sleep(SECONDS_BETWEEN_CHECKS)


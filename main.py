import re
def find_emails(file_location):
    with open(file_location, 'r') as file:
        file_content = file.read()
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        found_emails = re.findall(pattern, file_content)
        return found_emails


file_location = 'C:/Users/User/PycharmProjects/pythonProject7/file.html'

extracted_emails = find_emails(file_location)

print("Found Email Addresses:", extracted_emails)
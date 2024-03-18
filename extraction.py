import requests
from bs4 import BeautifulSoup
import os
import urllib
import re

def extract_text_and_images(url):
    # Fetch the HTML content of the website
    response = requests.get(url)
    if response.status_code == 200:
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Extract text
        text = soup.get_text()
        
        # Shrink text removing extra spaces but keeping line breaks
        text = re.sub(r'\s+', ' ', text)
        
        # Save text to a text file
        with open('text_content.txt', 'w', encoding='utf-8') as text_file:
            text_file.write(text)
            print("Text content saved successfully.")
        
        # Extract images
        images = soup.find_all('img')
        image_urls = [img['src'] for img in images]
        
        # Create a folder to save images
        if not os.path.exists('images'):
            os.makedirs('images')
        
        # Download images
        for img_url in image_urls:
            try:
                # Construct full image URL
                if not img_url.startswith('http'):
                    img_url = urllib.parse.urljoin(url, img_url)
                    
                # Extract image name
                img_name = os.path.basename(img_url)
                
                # Download image
                img_path = os.path.join('images', img_name)
                with open(img_path, 'wb') as img_file:
                    img_response = requests.get(img_url)
                    img_file.write(img_response.content)
                    
                print(f"Image '{img_name}' downloaded successfully.")
            except Exception as e:
                print(f"Error downloading image '{img_url}': {str(e)}")
        
        return text
    else:
        print("Failed to fetch the website content.")
        return None

# Example usage
website_url = input("Enter the website URL: ")
text_content = extract_text_and_images(website_url)
if text_content:
    print("Text content extracted successfully.")
else:
    print("Failed to extract text content.")
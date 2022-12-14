from bs4 import BeautifulSoup

soup = BeautifulSoup

with open("udemycontents.html") as html_file:
    contents = html_file.read()

soup = BeautifulSoup(contents, "html.parser")


# Things I'm interested in scraping
# Top div: <div class="ct-sidebar-course-content">…</div>
#
# Within it, each day (or section) are separated like this: # <div data-purpose="section-panel-0" class="accordion-panel--panel--24beS section--section--BukKG">

# Each day's title is stored here: <span class="truncate-with-tooltip--ellipsis--2-jEx" style="-webkit-line-clamp: 2;">Section 1: Day 1 - Beginner - Working with Variables in Python to Manage Data</span>
#
#


# This finds the first instance of the required classes, then returns the string of the content.
tag = soup.find(attrs={"class":"ct-sidebar-course-content", "class":"truncate-with-tooltip--ellipsis--2-jEx"})
print(tag.string)


# This will find all the instances.
all_contents = soup.find_all(attrs={"class":"ct-sidebar-course-content", "class":"truncate-with-tooltip--ellipsis--2-jEx"})

for content in all_contents:
    print(content.string)

with open('course_content.txt', 'w') as file:
    for content in all_contents:
        file.write(content.string)
        file.write('\n')
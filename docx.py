from docx import Document

# Create a new document
doc = Document()
doc.add_heading("Web Development MCQs (Easy + Hard)", level=1)

# Full set of 60 MCQs (Easy + Hard) pasted by user
mcqs_text = """
Easy Level MCQs

1. What does the "C" in CSS stand for?
A. Colorful
B. Cascading
C. Central
D. Content
Correct Answer: B. Cascading

2. According to the provided material, which language provides the structure for a web page?
A. CSS
B. JavaScript
C. HTML
D. PHP
Correct Answer: C. HTML

3. In a CSS rule like h1 { color: blue; }, what is the h1 called?
A. Value
B. Property
C. Selector
D. Declaration
Correct Answer: C. Selector

4. What is the primary function of a web browser?
A. To host a website
B. To send and receive emails
C. To access and display web content
D. To write code for web pages
Correct Answer: C. To access and display web content

5. What is a collection of interconnected web pages called?
A. A website
B. An IP address
C. A server
D. A web browser
Correct Answer: A. A website

6. Which protocol is described as adding an extra layer of security with encryption?
A. HTTP
B. HTTPS
C. FTP
D. TCP
Correct Answer: B. HTTPS

7. Which of the following is an example of a search engine, according to the images?
A. Windows
B. Mozilla Firefox
C. Google
D. Microsoft Excel
Correct Answer: C. Google

8. In the CSS rule p { font-size: 16px; }, what is 16px?
A. The property
B. The value
C. The selector
D. The declaration block
Correct Answer: B. The value

9. What is the main role of JavaScript in web development?
A. To add styling
B. To provide functionality
C. To create structure
D. To manage databases
Correct Answer: B. To provide functionality

10. What is a "Declaration" in CSS?
A. A selector and a value
B. A property and a value
C. A selector and a property
D. A property and a declaration block
Correct Answer: B. A property and a value

11. What does the text-align CSS property do?
A. Adds an underline to text.
B. Changes the color of text.
C. Aligns the text in an element.
D. Capitalizes the text.
Correct Answer: C. Aligns the text in an element.

12. Which of the following is a key element of a website's structure, as mentioned in the images?
A. Keyboard
B. Server
C. Homepage
D. IP address
Correct Answer: C. Homepage

13. What is the main disadvantage of a fixed-width web page layout?
A. It uses percentages.
B. It does not adapt to screen size.
C. It is difficult to customize.
D. It always looks good on all devices.
Correct Answer: B. It does not adapt to screen size.

14. What is the process of a search engine bot scanning web pages by following links called?
A. Indexing
B. Ranking
C. Crawling
D. Surfing
Correct Answer: C. Crawling

15. What is the main purpose of padding in the CSS Box Model?
A. To add space outside the element’s border.
B. To add a line around the content.
C. To add space inside the element’s border.
D. To change the element’s color.
Correct Answer: C. To add space inside the element’s border.

16. Which CSS property would you use to change the font of the content?
A. font-size
B. font-weight
C. font-family
D. color
Correct Answer: C. font-family

17. What is a linear-gradient used for?
A. To create a gradual color change in a straight line.
B. To create a color change radiating from a center point.
C. To add a solid color to a background.
D. To change the text color.
Correct Answer: A. To create a gradual color change in a straight line.

18. What does a full stack developer work on?
A. Front-end only
B. Back-end only
C. Front-end and back-end
D. Databases only
Correct Answer: C. Front-end and back-end

19. Which CSS property is used to create rounded edges on a box?
A. border-style
B. border-color
C. border-width
D. border-radius
Correct Answer: D. border-radius

20. What is the transform: rotate() property used for?
A. To move an element
B. To change an element's size
C. To skew an element
D. To rotate an element
Correct Answer: D. To rotate an element

21. Where is Internal CSS written in an HTML document?
A. Inside the <body> tag
B. In a separate .css file
C. Inside a <style> tag in the <head> section
D. At the end of the document
Correct Answer: C. Inside a <style> tag in the <head> section

22. What is the main goal of responsive design?
A. To create a fixed layout
B. To make the page load faster
C. To make a page render well on different screen sizes
D. To add more images to a page
Correct Answer: C. To make a page render well on different screen sizes

23. Which component of a URL identifies the directory or file location on the server?
A. Scheme
B. Domain
C. Path
D. Query
Correct Answer: C. Path

24. What is the purpose of the <div> tag?
A. To display an image
B. To create a clickable link
C. To mark a logical division of content for styling
D. To add a heading to a page
Correct Answer: C. To mark a logical division of content for styling

25. How is an external CSS file linked to an HTML page?
A. With a <style> tag
B. With a <link> tag
C. With a <script> tag
D. With an <a> tag
Correct Answer: B. With a <link> tag

26. What does the H in HSL stand for?
A. Height
B. Hue
C. Horizontal
D. History
Correct Answer: B. Hue

27. Which of the following is a type of web page layout mentioned in the images?
A. Fast
B. Liquid
C. Static
D. Fixed
Correct Answer: B. Liquid

28. Which component of the CSS Box Model adds space outside an element’s border?
A. padding
B. border
C. margin
D. content
Correct Answer: C. margin

29. What is the primary function of a server in the internet's client-server model?
A. To request web content
B. To display web content
C. To store and serve web content
D. To browse the internet
Correct Answer: C. To store and serve web content

30. What does the A in RGBA specify?
A. Animate
B. Area
C. Alpha (opacity)
D. Angle
Correct Answer: C. Alpha (opacity)


Hard Level MCQs

31. What is the key difference between the purpose of the <header> and <footer> tags versus the generic <div> tag, according to the notes?
A. The <header> and <footer> tags add functionality to a page.
B. The <div> tag is used for semantic purposes, while <header> and <footer> are not.
C. The <header> and <footer> tags divide a page into more specific, meaningful areas.
D. The <div> tag is only used for styling, while the others are for structure.
Correct Answer: C. The <header> and <footer> tags divide a page into more specific, meaningful areas.

32. According to the provided material, which of the following is a key advantage of using HTTPS over HTTP that directly impacts user security?
A. HTTPS compresses data for faster transfer.
B. HTTPS requires a special browser to view pages.
C. HTTPS ensures data transmitted is encrypted and cannot be tampered with easily.
D. HTTPS allows for more complex web page designs.
Correct Answer: C. HTTPS ensures data transmitted is encrypted and cannot be tampered with easily.

33. The images describe the transform CSS property with various values. Which of these values would you use to change the size of an element?
A. transform: rotate()
B. transform: translate()
C. transform: scale()
D. transform: skew()
Correct Answer: C. transform: scale()

34. A designer wants to create a web page that adjusts its width to fill any browser window, but they are concerned about text readability on very large screens. Based on the notes, which layout type are they using and what is the specific issue?
A. Fixed-width, the issue is a horizontal scroll bar.
B. Responsive, the issue is difficulty in implementation.
C. Liquid, the issue is that lines of text can become too long.
D. Fixed-width, the issue is excessive white space.
Correct Answer: C. Liquid, the issue is that lines of text can become too long.

35. What is the primary role of the back-end in a full stack application, as described in the images?
A. To handle all user interaction and the visual interface.
B. To serve as a communication layer between front-end and database.
C. To provide the structure and content of a web page.
D. To run on the server and handle requests, application logic, and data.
Correct Answer: D. To run on the server and handle requests, application logic, and data.

36. Based on the images, what is the correct order of a search engine's operations?
A. Indexing, Ranking, Crawling
B. Ranking, Indexing, Crawling
C. Crawling, Indexing, Ranking
D. Crawling, Ranking, Indexing
Correct Answer: C. Crawling, Indexing, Ranking

37. A CSS declaration block contains multiple declarations. How are these declarations separated from each other?
A. With a comma (,)
B. With a semicolon (;)
C. With a colon (:)
D. With a hyphen (-)
Correct Answer: B. With a semicolon (;)

38. According to the information provided, what is the main reason a fixed-width layout is considered a less-than-ideal solution for modern web design?
A. It uses a separate stylesheet.
B. It is not supported by all browsers.
C. It does not adapt to the wide variety of devices and screen sizes.
D. It is much more difficult to customize than other layouts.
Correct Answer: C. It does not adapt to the wide variety of devices and screen sizes.

39. Which of the following describes the difference between padding and margin in the CSS Box Model?
A. padding is inside the border, while margin is outside.
B. padding is outside the border, while margin is inside.
C. padding sets the element's width, while margin sets its height.
D. padding is used for text, and margin is used for images.
Correct Answer: A. padding is inside the border, while margin is outside.

40. What is a "client," as described in the provided text about how the internet works?
A. A powerful computer that stores and serves web content.
B. A device that requests and displays web content.
C. A communication protocol used for secure data transfer.
D. A program that organizes web pages into categories.
Correct Answer: B. A device that requests and displays web content.

41. According to the images, which CSS property would be used to control the spacing between individual letters within a word?
A. text-indent
B. text-align
C. letter-spacing
D. word-spacing
Correct Answer: C. letter-spacing

42. The images show different ways to specify a color. How is the HSL color model different from RGB?
A. HSL uses a combination of Red, Green, and Blue.
B. HSL uses Hexadecimal codes.
C. HSL uses a combination of Hue, Saturation, and Lightness.
D. HSL is only used for gradients.
Correct Answer: C. HSL uses a combination of Hue, Saturation, and Lightness.

43. What is a potential drawback of a liquid web page that uses percentages for its layout?
A. It is often too narrow for desktop screens.
B. It may not work with modern CSS.
C. It is very complex to create and test.
D. Content can become too wide and difficult to read.
Correct Answer: D. Content can become too wide and difficult to read.

44. What is the main difference between a web page and a website as defined in the images?
A. A website is a single document, while a web page is a collection.
B. A web page is a single document or resource, while a website is a collection of related web pages.
C. A web page is a physical document, while a website is a virtual one.
D. There is no difference between the two terms.
Correct Answer: B. A web page is a single document or resource, while a website is a collection of related web pages.

45. Based on the provided images, what is the relationship between the front-end, back-end, and database in full stack development?
A. They are all separate and unrelated parts of a system.
B. The front-end and back-end are the same, while the database is different.
C. The front-end is what the user interacts with, the back-end handles the logic, and the database stores the data.
D. The back-end and database are the same, while the front-end is separate.
Correct Answer: C. The front-end is what the user interacts with, the back-end handles the logic, and the database stores the data.

46. Which part of a URL, as defined in the images, contains optional data or parameters?
A. Domain
B. Path
C. Scheme
D. Query
Correct Answer: D. Query

47. What is the difference between a linear-gradient and a radial-gradient?
A. A linear-gradient is a solid color, while a radial-gradient is a transition.
B. A linear-gradient transitions color from a center point, while a radial-gradient transitions in a straight line.
C. A linear-gradient transitions color in a straight line, while a radial-gradient transitions from a center point.
D. A linear-gradient is used for text color, while a radial-gradient is for backgrounds.
Correct Answer: C. A linear-gradient transitions color in a straight line, while a radial-gradient transitions from a center point.

48. What is the key drawback of a fixed-width layout on a small screen device like a phone?
A. It is too easy to customize.
B. It creates excessive white space.
C. It requires a horizontal scroll bar.
D. It stretches the content to fit the screen.
Correct Answer: C. It requires a horizontal scroll bar.

49. A developer wants to use the transform property to move a box 200 pixels to the right and 50 pixels down. Which function should they use?
A. transform: rotate(200px, 50px);
B. transform: translate(200px, 50px);
C. transform: scale(200px, 50px);
D. transform: skew(200px, 50px);
Correct Answer: B. transform: translate(200px, 50px);

50. According to the images, what is the main purpose of the <link> tag when used with an external stylesheet?
A. To embed the entire stylesheet code in the HTML.
B. To tell the browser to download a separate CSS file.
C. To apply inline styles to a specific element.
D. To define the styling for a web page in the head section.
Correct Answer: B. To tell the browser to download a separate CSS file.

51. What is the correct term for the entire section of a CSS rule enclosed in curly braces, as defined by the images?
A. Selector
B. Property
C. Value
D. Declaration Block
Correct Answer: D. Declaration Block

52. What is the main difference between text-decoration and text-transform?
A. text-decoration adds an indent, while text-transform changes alignment.
B. text-decoration adds or removes underlines, while text-transform changes case.
C. text-decoration changes font size, while text-transform changes color.
D. text-decoration changes the font, while text-transform changes letter spacing.
Correct Answer: B. text-decoration adds or removes underlines, while text-transform changes case.

53. A developer is considering a responsive design for a new website. What is a known disadvantage of this approach, according to the provided material?
A. It is very easy to create and test.
B. It does not look good on a variety of devices.
C. It requires a significant amount of savvy and testing.
D. It uses fixed pixel values for layout.
Correct Answer: C. It requires a significant amount of savvy and testing.

54. Based on the images, which of the following is an example of a front-end technology?
A. SQL
B. Node.js
C. Python
D. CSS
Correct Answer: D. CSS

55. What is the main purpose of the <style> tag, according to the notes?
A. To link an external stylesheet.
B. To add an image to a webpage.
C. To embed a block of CSS code directly into the HTML file.
D. To add JavaScript functionality.
Correct Answer: C. To embed a block of CSS code directly into the HTML file.

56. Based on the images, what is the key difference between CSS1 and CSS3?
A. CSS1 focused on separating content from presentation, while CSS3 introduced new features like transitions.
B. CSS1 introduced gradients, while CSS3 introduced the box model.
C. CSS1 was used for structure, while CSS3 was for styling.
D. CSS1 was created for mobile devices, while CSS3 was for desktop.
Correct Answer: A. CSS1 focused on separating content from presentation, while CSS3 introduced new features like transitions.

57. The images mention that text-transform: capitalize; changes the first letter of each word to uppercase. What would text-transform: uppercase; do?
A. Change the first letter of the first word to uppercase.
B. Change all letters in the element to uppercase.
C. Change all letters to lowercase.
D. Remove all capital letters.
Correct Answer: B. Change all letters in the element to uppercase.

58. According to the images, which of the following is a disadvantage of a fixed-width web page on a large screen?
A. It creates a horizontal scroll bar.
B. It adds excessive white space.
C. It is difficult to customize.
D. It stretches the content to fill the screen.
Correct Answer: B. It adds excessive white space.

59. What is the purpose of crawling in the search engine process?
A. To evaluate the quality of a web page.
B. To rank a web page in search results.
C. To scan and follow links to discover new web pages.
D. To create a database of all web content.
Correct Answer: C. To scan and follow links to discover new web pages."""
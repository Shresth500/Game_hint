# Treasure Hunt
A login system - A person with his mail id would be able to register it.
A set of question that lead you to the treasure with 5 minimum hints, 2 dead ends and 1 solution
For every question minimum of 5 hints should be provided and if he answers them wrongly for 2 times then game will end, he can choose an option to see the solution only one's.
Each question will lead you to the next point.
Since here we would be showing the user his position w.r.t to others so we will be using flask and data analytics tools
Steps Involved - 
1.) Signup Page
2.) Signin Page 
3.) Main Page
  3.1) Start Game
  3.2) Account
  3.3) Statistics
  3.4) Sign Out
1.) Signup - If the user is not registered then sign up with it's details using signup page
2.) Signin - If user is already their then we can sign in with our details, if details matches with the userthen the page will redirect you to the Main Page
3.) Main Page - Main Page is the page consisting of 4 options whether to play the game if yes then click on Start Game, else if you want to see your account details then click on Account tabs, else if he wants to see the leaderboard then click on Statistics
3.1) Start Game - After Clicking on the start game a page will appear consisting of questions, and clues for the question, answer and etc, If you click on answer, it will show you the answer, if you want clue then click on clues for the question and get the hint, but remember if you can take atmost 5 hints, 1 solution and 2 wrong answers
Tech Stack used here are - 
1.) HTML
2.) CSS
3.) JAVASCRIPT
4.) DJANGO
5.) PYTHON
HTML - 
Web browsers receive HTML documents from a web server or from local storage and render the documents into multimedia web pages. HTML describes the structure of a web page semantically and originally included cues for its appearance.

HTML elements are the building blocks of HTML pages. With HTML constructs, images and other objects such as interactive forms may be embedded into the rendered page. HTML provides a means to create structured documents by denoting structural semantics for text such as headings, paragraphs, lists, links, quotes, and other items. HTML elements are delineated by tags, written using angle brackets. Tags such as <img /> and <input /> directly introduce content into the page. Other tags such as <p> and </p> surround and provide information about document text and may include sub-element tags. Browsers do not display the HTML tags but use them to interpret the content of the page.

CSS - 
Cascading Style Sheets (CSS) is a stylesheet language used to describe the presentation of a document written in HTML or XML (including XML dialects such as SVG, MathML or XHTML). CSS describes how elements should be rendered on screen, on paper, in speech, or on other media.

Javascript - 
JavaScript, often abbreviated as JS, is a programming language that is one of the core technologies of the World Wide Web, alongside HTML and CSS. As of 2022, 98% of websites use JavaScript on the client side for webpage behavior, often incorporating third-party libraries. All major web browsers have a dedicated JavaScript engine to execute the code on users' devices.

JavaScript is a high-level, often just-in-time compiled language that conforms to the ECMAScript standard.[10] It has dynamic typing, prototype-based object-orientation, and first-class functions. It is multi-paradigm, supporting event-driven, functional, and imperative programming styles. It has application programming interfaces (APIs) for working with text, dates, regular expressions, standard data structures, and the Document Object Model (DOM).

PYTHON - 
Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation via the off-side rule.

Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming. It is often described as a "batteries included" language due to its comprehensive standard library.

Guido van Rossum began working on Python in the late 1980s as a successor to the ABC programming language and first released it in 1991 as Python 0.9.0.[36] Python 2.0 was released in 2000. Python 3.0, released in 2008, was a major revision not completely backward-compatible with earlier versions. Python 2.7.18, released in 2020, was the last release of Python 2.

Python consistently ranks as one of the most popular programming languages.

Django - 
Django is a free and open-source, Python-based web framework that follows the model–template–views (MTV) architectural pattern. It is maintained by the Django Software Foundation (DSF), an independent organization established in the US as a 501 non-profit.

Django's primary goal is to ease the creation of complex, database-driven websites. The framework emphasizes reusability and "pluggability" of components, less code, low coupling, rapid development, and the principle of don't repeat yourself.[9] Python is used throughout, even for settings, files, and data models. Django also provides an optional administrative create, read, update and delete interface that is generated dynamically through introspection and configured via admin models.

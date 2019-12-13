1. There are two programs available, one with, one without, Flask
2. To access the Flask program, run the flaskAssignment.py file. This will start the server at the localhost, port 80.
3. To access the server as a client, simply run the server program, then go to your web browser and type into the taskbar: “localhost”. The home page will be displayed
4. From here, you can navigate the system:

	Navbar
	1.	All books -> takes you to a page where all books are displayed
	2.	User Dashboard -> takes you to where you can get recommendations and edit your ratings. Only available once you have logged in
	3.	Log in -> enter your userID and password (for ease of access purposes, userIDs are 0 to 20, with password equal to the userID. Security-wise, this would be more secure in a deployed system

	User Dashboard
	1.	Get recommendations -> displays top 5 recommended books for you based on previous ratings
	2.	View your user profile
		User Profile
		1.	Add rating -> add new book rating
		2.	Edit rating -> change current rating
		3.	Delete rating -> delete current rating


5. Use generateDataset.py to generate new random ratings